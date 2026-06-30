# Project Context: Basement LA Theme Docs

## What this is

A documentation site for the **Basement LA** Shopify theme (a fully custom theme —
no Dawn, no base theme — built in Liquid, SCSS, and vanilla JS). This repo is
**only the docs site**, not the theme itself. The theme codebase lives in a
separate repo.

The docs site has two audiences sharing one MkDocs deployment:

1. **Merchant Guide** — non-technical, visual walkthroughs (GIFs/short videos) for
   making changes via the Shopify admin theme editor. No code shown.
2. **Developer Docs** — technical reference on theme architecture, conventions,
   and the reasoning behind implementation decisions. Assumes Shopify/Liquid
   familiarity.

## Stack

- **Static site generator:** MkDocs + Material for MkDocs theme
- **Hosting:** GitHub Pages, deployed via GitHub Actions on every push to `main`
- **Repo:** `basementlosangeles/basement-la-docs` (GitHub org, not personal account)
- **Local dev:** Python venv (`.venv`) + `pip install -r requirements.txt` + `mkdocs serve`
- No JS framework, no build step beyond MkDocs itself — keep it that way.

## Repo structure

```
basement-la-docs/
├── mkdocs.yml                  # nav structure, theme config, palette
├── requirements.txt            # just mkdocs-material
├── .github/workflows/deploy.yml  # auto-deploys to gh-pages on push to main
├── docs/
│   ├── index.md                 # homepage — branded hero + entry cards
│   ├── assets/
│   │   ├── css/extra.css        # Basement LA brand system (see below)
│   │   ├── gifs/                # short UI-confirmation GIFs, <5MB each
│   │   └── img/                 # logos, screenshots
│   ├── merchant-guide/
│   │   ├── index.md             # card grid linking to feature pages
│   │   └── example-feature.md   # template page — copy this pattern for new pages
│   └── developer-guide/
│       ├── index.md
│       └── architecture.md      # theme structure, conventions, metafield patterns
```

## Design system — IMPORTANT, read before touching CSS

`docs/assets/css/extra.css` contains a scoped brand system under the `.bla-*`
class prefix (hero, ticker, card grid, numbered steps, badges). This is
**intentionally scoped** — it does NOT override Material's default theme
variables (`--md-default-*`, `--md-primary-*`, etc.), so the Developer Docs
pages stay in plain default Material styling. Do not change that — it's
deliberate, so technical readers get a utilitarian reference experience while
merchants get the polished, on-brand one.

**Current status: the color/font tokens in `:root` are PLACEHOLDERS**, not the
real Basement LA brand values:

```css
--bla-bg: #0b0b0c;
--bla-surface: #161618;
--bla-ink: #f2f1ec;
--bla-accent: #e2402f;
--bla-font-display: 'Archivo Black', sans-serif;
--bla-font-body: 'Inter', sans-serif;
--bla-font-mono: 'IBM Plex Mono', monospace;
```

**TODO:** Replace these with the real values from the theme's SCSS variables
file (color + font definitions) and the real logo asset. Everything else
(hero, cards, steps) inherits from these tokens, so it should be a single
find-and-replace in the `:root` block — no other files need to change for a
brand-token update.

## Conventions for adding pages

- **Merchant guide pages:** copy `merchant-guide/example-feature.md`'s
  structure — badge, what-it-changes, where-to-find-it, GIF/video, numbered
  `.bla-step` blocks, a `!!! warning` callout if relevant. Add an entry to the
  `.bla-grid` card list in `merchant-guide/index.md`.
- **Every new page must be registered in `mkdocs.yml`'s `nav:` block** or it
  won't appear in the sidebar even though the file exists.
- **GIFs:** short (5-10s), compressed, under ~5MB, committed to
  `docs/assets/gifs/`. Longer recordings go to an **unlisted** YouTube/Loom
  link, embedded via `<iframe>` (pattern is in `example-feature.md`).

## Known gaps / next steps

- [ ] Swap placeholder brand tokens in `extra.css` for real values
- [ ] Add logo asset and reference it in `mkdocs.yml` (`theme.logo` /
      `theme.favicon`, currently commented out)
- [ ] Populate developer-guide stub pages: Sections & Snippets, Metafields &
      Metaobjects, JS Modules, Build & Deploy (listed but not yet written in
      `developer-guide/index.md`)
- [ ] Write out the full merchant-guide page list once real theme section
      names are confirmed (currently only one example page exists)
- [ ] Once the theme repo's `audit.md` (codebase audit, severity-ranked) is
      generated, fold relevant findings into the developer docs

## Things NOT to do

- Don't add a JS framework or build step (React, Vue, bundlers) — this is
  meant to stay a simple, fast-deploying static site.
- Don't change global Material theme variables to "fix" the merchant guide
  styling — extend the `.bla-*` classes instead, to keep developer docs
  unaffected.
- Don't commit large video files — link out instead (see GIF/video convention
  above).
