#!/usr/bin/env python3
"""Extract a machine-readable inventory of theme sections and diff against the last run.

Reads the theme repo (path from scripts/sync.config.json, or --theme-path),
parses every sections/*.liquid schema block plus template/section-group/layout
usage, snippet renders, and metafield references, and writes:

  - inventory.json   canonical machine-readable state (committed; diffed against
                      on each run, then overwritten with the fresh snapshot)
  - sync-report.md   human-readable drift report for this run only

Nothing under docs/ is ever touched by this script. Stdlib only, no deps.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

DOCS_REPO_ROOT = Path(__file__).resolve().parent.parent
CONFIG_PATH = DOCS_REPO_ROOT / "scripts" / "sync.config.json"
INVENTORY_PATH = DOCS_REPO_ROOT / "inventory.json"
REPORT_PATH = DOCS_REPO_ROOT / "sync-report.md"

SCHEMA_RE = re.compile(r"\{%-?\s*schema\s*-?%\}(.*?)\{%-?\s*endschema\s*-?%\}", re.DOTALL)
RENDER_RE = re.compile(r"\{%-?\s*render\s+'([a-zA-Z0-9_\-]+)'")
SECTION_TAG_RE = re.compile(r"\{%-?\s*section\s+'([a-zA-Z0-9_\-]+)'")
SECTIONS_TAG_RE = re.compile(r"\{%-?\s*sections\s+'([a-zA-Z0-9_\-]+)'")
METAFIELD_RE = re.compile(r"metafields\.([a-zA-Z0-9_]+)\.([a-zA-Z0-9_]+)")
METAOBJECT_RE = re.compile(r"\bmetaobjects?\b", re.IGNORECASE)


# ---------------------------------------------------------------------------
# JSONC (theme files use // never, but do use /* */ comments and trailing commas)
# ---------------------------------------------------------------------------

def strip_jsonc(text):
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)
    text = re.sub(r",(\s*[}\]])", r"\1", text)
    return text


def parse_jsonc(text, source_label):
    try:
        return json.loads(strip_jsonc(text))
    except json.JSONDecodeError as e:
        print(f"  ! could not parse JSON in {source_label}: {e}", file=sys.stderr)
        return None


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def simplify_settings(settings):
    """settings array -> {id: {label, type, default, info}}, skipping header dividers."""
    out = {}
    for s in settings or []:
        if not isinstance(s, dict) or s.get("type") == "header" or "id" not in s:
            continue
        out[s["id"]] = {
            "label": s.get("label"),
            "type": s.get("type"),
            "default": s.get("default"),
            "info": s.get("info"),
        }
    return out


def simplify_blocks(blocks):
    out = {}
    for b in blocks or []:
        if not isinstance(b, dict):
            continue
        btype = b.get("type")
        if not btype or btype in ("@theme", "@app"):
            continue
        out[btype] = {"name": b.get("name"), "settings": simplify_settings(b.get("settings"))}
    return out


def extract_section_schema(liquid_path):
    text = liquid_path.read_text(encoding="utf-8")
    m = SCHEMA_RE.search(text)
    schema = parse_jsonc(m.group(1), str(liquid_path)) if m else None
    renders = sorted(set(RENDER_RE.findall(text)))
    metafields = sorted({f"{ns}.{key}" for ns, key in METAFIELD_RE.findall(text)})
    has_metaobject = bool(METAOBJECT_RE.search(text))
    return schema, renders, metafields, has_metaobject


def walk_templates(theme_root):
    """section_type -> [{"template": relpath, "layout": layout_or_None}, ...]"""
    usage = {}

    def record(section_type, template_rel, layout):
        entry = {"template": template_rel, "layout": layout}
        bucket = usage.setdefault(section_type, [])
        if entry not in bucket:
            bucket.append(entry)

    templates_dir = theme_root / "templates"
    if not templates_dir.exists():
        return usage

    for path in sorted(templates_dir.glob("*.json")):
        data = parse_jsonc(path.read_text(encoding="utf-8"), str(path))
        if not data:
            continue
        layout = data.get("layout")
        sections = data.get("sections", {})
        if isinstance(sections, dict):
            for sec in sections.values():
                if isinstance(sec, dict) and "type" in sec:
                    record(sec["type"], f"templates/{path.name}", layout)

    for path in sorted(templates_dir.glob("*.liquid")):
        text = path.read_text(encoding="utf-8")
        for stype in SECTION_TAG_RE.findall(text):
            record(stype, f"templates/{path.name}", None)

    return usage


def walk_section_groups(theme_root):
    """Section-group JSON files living in sections/ (header-group.json etc).
    Returns (section_type -> [group filename, ...], list of group filenames)."""
    usage = {}
    groups = []
    sections_dir = theme_root / "sections"
    if not sections_dir.exists():
        return usage, groups

    for path in sorted(sections_dir.glob("*.json")):
        data = parse_jsonc(path.read_text(encoding="utf-8"), str(path))
        if not data or "sections" not in data:
            continue
        groups.append(path.name)
        for sec in data.get("sections", {}).values():
            if isinstance(sec, dict) and "type" in sec:
                usage.setdefault(sec["type"], []).append(path.name)

    return usage, groups


def walk_layouts(theme_root):
    """section_type -> sorted [layout filenames rendering it directly via {% section %}]."""
    global_usage = {}
    layout_dir = theme_root / "layout"
    if not layout_dir.exists():
        return global_usage

    for path in sorted(layout_dir.glob("*.liquid")):
        text = path.read_text(encoding="utf-8")
        for stype in SECTION_TAG_RE.findall(text):
            global_usage.setdefault(stype, set()).add(path.name)

    return {k: sorted(v) for k, v in global_usage.items()}


def build_snippet_render_map(theme_root):
    """snippet_name -> [snippet names it itself renders] (one level; transitive closure done separately)."""
    m = {}
    snippets_dir = theme_root / "snippets"
    if not snippets_dir.exists():
        return m
    for path in sorted(snippets_dir.glob("*.liquid")):
        text = path.read_text(encoding="utf-8")
        m[path.stem] = sorted(set(RENDER_RE.findall(text)))
    return m


def _transitive_renders_set(start, snippet_render_map, seen):
    result = set()
    for r in start:
        if r in seen:
            continue
        seen.add(r)
        result.add(r)
        result |= _transitive_renders_set(snippet_render_map.get(r, []), snippet_render_map, seen)
    return result


def transitive_renders(start, snippet_render_map, seen=None):
    seen = seen if seen is not None else set()
    return sorted(_transitive_renders_set(start, snippet_render_map, seen))


def extract_global_settings(theme_root):
    path = theme_root / "config" / "settings_schema.json"
    if not path.exists():
        return []
    data = parse_jsonc(path.read_text(encoding="utf-8"), str(path))
    groups = []
    if isinstance(data, list):
        for g in data:
            if not isinstance(g, dict) or "settings" not in g:
                continue  # skip the theme_info block, has no "settings" key
            groups.append({"name": g.get("name"), "settings": simplify_settings(g.get("settings"))})
    return groups


def build_inventory(theme_root):
    theme_root = Path(theme_root)
    template_usage = walk_templates(theme_root)
    group_usage, group_files = walk_section_groups(theme_root)
    global_usage = walk_layouts(theme_root)
    snippet_render_map = build_snippet_render_map(theme_root)

    sections = {}
    sections_dir = theme_root / "sections"
    for path in sorted(sections_dir.glob("*.liquid")):
        section_id = path.stem
        schema, renders, metafields, has_metaobject = extract_section_schema(path)
        if schema is None:
            print(f"  - skipping {path.name}: no parseable schema block", file=sys.stderr)
            continue

        presets = schema.get("presets") or []
        preset_category = next(
            (p.get("category") for p in presets if isinstance(p, dict) and p.get("category")), None
        )

        sections[section_id] = {
            "file": f"sections/{path.name}",
            "name": schema.get("name"),
            "preset_category": preset_category,
            "settings": simplify_settings(schema.get("settings")),
            "blocks": simplify_blocks(schema.get("blocks")),
            "max_blocks": schema.get("max_blocks"),
            "used_in_templates": sorted(
                template_usage.get(section_id, []), key=lambda e: (e["template"], e["layout"] or "")
            ),
            "used_in_section_groups": sorted(set(group_usage.get(section_id, []))),
            "used_globally_by_layouts": global_usage.get(section_id, []),
            "snippets_rendered": renders,
            "snippets_rendered_transitive": transitive_renders(renders, snippet_render_map),
            "metafields": metafields,
            "references_metaobject": has_metaobject,
        }

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "theme_repo_path": str(theme_root),
        "section_groups": group_files,
        "sections": sections,
        "global_settings": extract_global_settings(theme_root),
    }


# ---------------------------------------------------------------------------
# Diffing
# ---------------------------------------------------------------------------

def _fmt_setting(s):
    bits = [f"type={s.get('type')}"]
    if s.get("label"):
        bits.append(f"label={s['label']!r}")
    if s.get("default") is not None:
        bits.append(f"default={s['default']!r}")
    return ", ".join(bits)


def diff_settings(old, new):
    old, new = old or {}, new or {}
    changes = []
    for sid in sorted(set(new) - set(old)):
        changes.append(f"added setting `{sid}`: {_fmt_setting(new[sid])}")
    for sid in sorted(set(old) - set(new)):
        changes.append(f"removed setting `{sid}` (was: {_fmt_setting(old[sid])})")
    for sid in sorted(set(old) & set(new)):
        o, n = old[sid], new[sid]
        for field in ("label", "type", "default", "info"):
            if o.get(field) != n.get(field):
                changes.append(f"setting `{sid}`.{field} changed: {o.get(field)!r} -> {n.get(field)!r}")
    return changes


def diff_blocks(old, new):
    old, new = old or {}, new or {}
    changes = []
    for bt in sorted(set(new) - set(old)):
        changes.append(f"added block `{bt}` ({new[bt].get('name')})")
    for bt in sorted(set(old) - set(new)):
        changes.append(f"removed block `{bt}`")
    for bt in sorted(set(old) & set(new)):
        for c in diff_settings(old[bt].get("settings"), new[bt].get("settings")):
            changes.append(f"block `{bt}`: {c}")
    return changes


def diff_list_field(old, new, label):
    old_set, new_set = set(old or []), set(new or [])
    changes = []
    for x in sorted(new_set - old_set):
        changes.append(f"{label} added: `{x}`")
    for x in sorted(old_set - new_set):
        changes.append(f"{label} removed: `{x}`")
    return changes


def diff_section(old, new):
    changes = []
    for field in ("name", "preset_category", "max_blocks"):
        if old.get(field) != new.get(field):
            changes.append(f"`{field}` changed: {old.get(field)!r} -> {new.get(field)!r}")

    changes += diff_settings(old.get("settings"), new.get("settings"))
    changes += diff_blocks(old.get("blocks"), new.get("blocks"))

    old_tpl = [f"{e['template']} ({e['layout']})" for e in old.get("used_in_templates", [])]
    new_tpl = [f"{e['template']} ({e['layout']})" for e in new.get("used_in_templates", [])]
    changes += diff_list_field(old_tpl, new_tpl, "template usage")
    changes += diff_list_field(old.get("used_in_section_groups"), new.get("used_in_section_groups"), "section-group usage")
    changes += diff_list_field(old.get("used_globally_by_layouts"), new.get("used_globally_by_layouts"), "global layout usage")
    changes += diff_list_field(old.get("snippets_rendered_transitive"), new.get("snippets_rendered_transitive"), "snippet")
    changes += diff_list_field(old.get("metafields"), new.get("metafields"), "metafield")

    if bool(old.get("references_metaobject")) != bool(new.get("references_metaobject")):
        changes.append(f"metaobject reference changed: {old.get('references_metaobject')} -> {new.get('references_metaobject')}")

    return changes


def diff_inventories(old, new):
    old_sections = (old or {}).get("sections", {})
    new_sections = new.get("sections", {})

    added = sorted(set(new_sections) - set(old_sections))
    removed = sorted(set(old_sections) - set(new_sections))
    changed = {}
    for sid in sorted(set(old_sections) & set(new_sections)):
        c = diff_section(old_sections[sid], new_sections[sid])
        if c:
            changed[sid] = c

    old_globals = {g["name"]: g for g in (old or {}).get("global_settings", []) if g.get("name")}
    new_globals = {g["name"]: g for g in new.get("global_settings", []) if g.get("name")}
    global_changes = {}
    for gname in sorted(set(new_globals) - set(old_globals)):
        global_changes[gname] = [f"new theme-settings group `{gname}`"]
    for gname in sorted(set(old_globals) - set(new_globals)):
        global_changes[gname] = [f"theme-settings group `{gname}` removed"]
    for gname in sorted(set(old_globals) & set(new_globals)):
        c = diff_settings(old_globals[gname].get("settings"), new_globals[gname].get("settings"))
        if c:
            global_changes[gname] = c

    return {
        "added_sections": added,
        "removed_sections": removed,
        "changed_sections": changed,
        "global_setting_changes": global_changes,
    }


# ---------------------------------------------------------------------------
# Report rendering
# ---------------------------------------------------------------------------

def render_report(diff, new_inventory, docs_dir):
    lines = [
        "# Theme Sync Report",
        "",
        f"Generated: {new_inventory['generated_at']}",
        f"Theme repo: `{new_inventory['theme_repo_path']}`",
        "",
        "This report only describes drift — nothing in `docs/` was changed by this run.",
        "Tell Claude which items you'd like applied and it will edit those specific pages.",
        "",
    ]

    total = (
        len(diff["added_sections"])
        + len(diff["removed_sections"])
        + len(diff["changed_sections"])
        + len(diff["global_setting_changes"])
    )
    if total == 0:
        lines.append("No drift detected since the last sync. Nothing to review.")
        return "\n".join(lines) + "\n"

    lines += [
        "## Summary",
        f"- New sections: {len(diff['added_sections'])}",
        f"- Removed sections: {len(diff['removed_sections'])}",
        f"- Changed sections: {len(diff['changed_sections'])}",
        f"- Changed global theme-settings groups: {len(diff['global_setting_changes'])}",
        "",
    ]

    dev_pages = {p.stem for p in (docs_dir / "developer-guide").glob("*.md")} if (docs_dir / "developer-guide").exists() else set()
    merchant_pages = {p.stem for p in (docs_dir / "merchant-guide").glob("*.md")} if (docs_dir / "merchant-guide").exists() else set()

    if diff["added_sections"]:
        lines.append("## New sections")
        for sid in diff["added_sections"]:
            sec = new_inventory["sections"][sid]
            has_dev = sid in dev_pages
            has_merchant = sid in merchant_pages
            lines.append(f"### `{sid}` — {sec.get('name') or '(unnamed)'}")
            lines.append(f"- File: `{sec['file']}`")
            lines.append(f"- Dev page exists: {'yes' if has_dev else 'NO — needs docs/developer-guide/' + sid + '.md'}")
            if sec["settings"]:
                lines.append(f"- Merchant page exists: {'yes' if has_merchant else 'NO — needs docs/merchant-guide/' + sid + '.md'}")
            else:
                lines.append("- Merchant page: likely not needed (no editor settings)")
            if sec["settings"]:
                lines.append("- Settings:")
                for setting_id, s in sec["settings"].items():
                    lines.append(f"  - `{setting_id}`: {_fmt_setting(s)}")
            lines.append("")

    if diff["removed_sections"]:
        lines.append("## Removed sections")
        lines.append("(file deleted, or its `{% schema %}` block was removed)")
        for sid in diff["removed_sections"]:
            lines.append(f"### `{sid}`")
            if sid in dev_pages:
                lines.append(f"- `docs/developer-guide/{sid}.md` may need to be removed or marked legacy.")
            if sid in merchant_pages:
                lines.append(f"- `docs/merchant-guide/{sid}.md` may need to be removed or marked legacy.")
            lines.append("")

    if diff["changed_sections"]:
        lines.append("## Changed sections")
        for sid, changes in diff["changed_sections"].items():
            lines.append(f"### `{sid}`")
            if sid in dev_pages:
                lines.append(f"- Dev page: `docs/developer-guide/{sid}.md`")
            if sid in merchant_pages:
                lines.append(f"- Merchant page: `docs/merchant-guide/{sid}.md`")
            for c in changes:
                lines.append(f"- {c}")
            lines.append("")

    if diff["global_setting_changes"]:
        lines.append("## Changed global theme settings")
        lines.append("(`config/settings_schema.json` — referenced from pages like `buy-together-products-section.md` and `code-popup.md`)")
        for gname, changes in diff["global_setting_changes"].items():
            lines.append(f"### {gname}")
            for c in changes:
                lines.append(f"- {c}")
            lines.append("")

    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def load_config():
    if CONFIG_PATH.exists():
        return json.loads(CONFIG_PATH.read_text(encoding="utf-8"))
    return {}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--theme-path", help="Path to the theme repo (overrides scripts/sync.config.json)")
    args = parser.parse_args()

    config = load_config()
    theme_path = args.theme_path or config.get("theme_repo_path")
    if not theme_path:
        print(
            "No theme repo path given. Pass --theme-path or set 'theme_repo_path' in scripts/sync.config.json.",
            file=sys.stderr,
        )
        sys.exit(1)

    theme_root = Path(theme_path)
    if not theme_root.exists():
        print(f"Theme repo path does not exist: {theme_root}", file=sys.stderr)
        sys.exit(1)

    old_inventory = None
    if INVENTORY_PATH.exists():
        try:
            old_inventory = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            print(f"Warning: could not parse existing {INVENTORY_PATH.name}, treating as first run.", file=sys.stderr)

    print(f"Extracting theme inventory from {theme_root} ...")
    new_inventory = build_inventory(theme_root)
    print(f"Found {len(new_inventory['sections'])} sections with schema blocks.")

    if old_inventory is None:
        INVENTORY_PATH.write_text(json.dumps(new_inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        report = (
            "# Theme Sync Report\n\n"
            f"Generated: {new_inventory['generated_at']}\n"
            f"Theme repo: `{new_inventory['theme_repo_path']}`\n\n"
            "This is the first run — no prior `inventory.json` existed to diff against.\n"
            f"Captured a baseline of {len(new_inventory['sections'])} sections. "
            "Future runs will report drift against this baseline.\n"
        )
        REPORT_PATH.write_text(report, encoding="utf-8")
        print(f"No prior inventory.json found — wrote baseline to {INVENTORY_PATH.name} and {REPORT_PATH.name}.")
        return

    diff = diff_inventories(old_inventory, new_inventory)
    report = render_report(diff, new_inventory, DOCS_REPO_ROOT / "docs")

    INVENTORY_PATH.write_text(json.dumps(new_inventory, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    REPORT_PATH.write_text(report, encoding="utf-8")

    total = (
        len(diff["added_sections"])
        + len(diff["removed_sections"])
        + len(diff["changed_sections"])
        + len(diff["global_setting_changes"])
    )
    print(f"Wrote {INVENTORY_PATH.name} and {REPORT_PATH.name}.")
    print(f"Drift detected in {total} area(s)." if total else "No drift detected.")


if __name__ == "__main__":
    main()
