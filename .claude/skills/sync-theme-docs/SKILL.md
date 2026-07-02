---
name: sync-theme-docs
description: Detect drift between the Basement LA theme repo and this docs site, and report what needs updating. Use when the user says the theme changed and wants to check what's out of date in the docs, or explicitly runs /sync-theme-docs. Report-only by default — never edits docs pages unless the user explicitly asks for a specific change to be applied afterward.
---

# Sync Theme Docs

This skill detects drift between the theme repo (`sections/*.liquid` schema blocks,
templates, section groups, layouts, snippets, metafields, and
`config/settings_schema.json`) and this docs site's tracked inventory. It is
**report-only**: it never edits anything under `docs/` on its own. You act on the
report only when the user explicitly asks you to.

## What to run

From the docs repo root:

```
py -3 scripts/extract_theme_inventory.py
```

On this machine, bare `py` (no version flag) fails with a broken WindowsApps
`python3.exe` alias error — always use `py -3`. If `py` isn't available at all, try
`python` or `python3`. The script takes no required
arguments — it reads the theme repo path from `scripts/sync.config.json`. If the
user gives you a different theme repo path for this run, pass it with
`--theme-path "<path>"` instead of editing the config file.

The script is pure Python stdlib — no venv, no pip install needed.

## What it produces

- **`inventory.json`** (repo root) — the new machine-readable snapshot. This file
  gets overwritten every run; it's committed to git so the *next* run has something
  to diff against. Don't hand-edit it.
- **`sync-report.md`** (repo root) — the human-readable diff for *this* run only:
  new sections, removed sections, changed settings/blocks/usage/metafields, and
  changed global theme-settings groups.
- **`docs/inventory.md`** (the original hand-written inventory from the initial
  build) is never touched by this script — it's a separate, static file.

## Steps

1. Run the extraction script as above.
2. Read `sync-report.md`.
3. **First run** (no prior `inventory.json` existed): the report will say so and
   just capture a baseline. Tell the user a baseline was captured — there's nothing
   to review yet.
4. **Later runs**: summarize the report in chat — don't just dump the raw file.
   Give a short rundown grouped the same way the report is (new / removed / changed
   sections, changed global settings), and point out which items look like they'd
   actually affect what a merchant or developer sees (e.g. a new setting, a changed
   default) versus cosmetic (e.g. a re-sorted metafield list).
5. Tell the user the report is saved at `sync-report.md` and that **nothing in
   `docs/` has been changed**. Ask which items, if any, they'd like applied.
6. **Only when the user names specific items** (e.g. "update the cart-sidebar page"
   or "apply all the changed-setting ones"), edit those pages yourself:
   - Cross-reference `inventory.json` for the authoritative current values (don't
     trust your memory of the diff for exact defaults/labels).
   - Edit `docs/developer-guide/<section>.md` and/or `docs/merchant-guide/<section>.md`
     directly, matching each file's existing style — this is prose editing, not
     template stamping. Preserve everything not affected by the specific change
     (GIF embeds, warnings, notes, existing formatting).
   - For **new sections**: create `docs/developer-guide/<section>.md` (always) and
     `docs/merchant-guide/<section>.md` (only if the section has real editor
     settings) following the existing pages' structure, then register both in
     `mkdocs.yml`'s `nav:` block and add card entries to `docs/merchant-guide/index.md`
     (and `docs/index.md` only if it changes the top-level pitch).
   - For **removed sections**: don't delete pages unprompted — ask whether to
     remove them or mark them legacy (matching how `homepage.md`/`policy-page.md`
     were handled previously, i.e. an explicit warning admonition rather than
     deletion), since the user may still want the page for historical reference.
7. Never touch a page for a section the user didn't mention.

## What this skill must not do

- Never overwrite a docs page automatically just because drift was detected.
- Never edit `docs/inventory.md` (separate from the script-managed `inventory.json`).
- Never touch the theme repo — it's read-only from this repo's perspective.
