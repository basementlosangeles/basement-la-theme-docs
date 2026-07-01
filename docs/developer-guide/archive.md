# Archive

`sections/archive.liquid`

## What it does

The "Archive" cover page — a horizontally/vertically scrolling gallery of past
drops built from `archive-item` and `archive-small-group` theme blocks. The section
itself only exposes background and scrollbar colors; the items themselves are blocks.

## Where it's used

Assigned in `templates/page.Archive.json`, using the `page-cover-theme` layout
(no-background header group + footer, no code-popup is rendered into `main`). The
template instantiates the `archive` section multiple times with many `archive-item`
and `archive-small-group` blocks. Preset name: **Archive**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `background-color` | Background Color | color | `rgba(17,17,17,1)` |
| `scrollbar-foreground-color` | Scrollbar Foreground Color | color | `#d9d9d9` |

Content blocks accepted: `"blocks": [{ "type": "@theme" }]`.

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- This is a dark section by default (`#111`), distinct from the light primary theme
  background — keep that in mind if restyling.
- Adding/removing archive entries is a block operation, not a settings change.
