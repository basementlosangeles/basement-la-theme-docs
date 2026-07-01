# About

`sections/about-page.liquid`

## What it does

The About page shell. The section itself holds **no settings** — all content is
composed from `about-page-*` theme blocks, so the entire page is built block-by-block
in the editor rather than from section fields.

## Where it's used

Assigned in `templates/page.About.json`, using the `page-text-theme` layout. Preset
name: **About**.

## Schema settings

None. The schema declares `"blocks": [{ "type": "@theme" }]`, accepting any theme
block. In practice the About template wires up these blocks:

- `about-page-section` — a layout container
- `about-page-text` — rich text content
- `about-page-logo` — logo mark
- `about-page-pic-container` / `about-page-pic` — image groupings
- `about-page-link-container` / `about-page-link` — link rows

## Metafields & metaobjects

None.

## Snippets rendered

None directly (block templates handle their own markup).

## Notes

- Because there are no section settings, "editing the About page" means editing its
  blocks — keep that in mind when documenting it for merchants.
- Block files live in the theme's `blocks/` directory; this page only documents the
  section that hosts them.
