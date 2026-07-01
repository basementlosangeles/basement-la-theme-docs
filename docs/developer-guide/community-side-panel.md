# Community Side Panel

`sections/community-side-panel.liquid`

## What it does

A "Styled By The Community" horizontal scroller on the product page, populated by
`community-item` theme blocks (UGC / lookbook imagery). Includes arrow navigation
with a configurable scroll distance.

## Where it's used

Assigned in `templates/product.json` (the `theme` layout), with many
`community-item` blocks. Preset category: **Product**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `title` | Title | text | `Styled By The Community` |
| `no-items-text` | No Items Text | text | `No Items Available` |
| `scroll-amount` | Arrow Nav Button Scroll Amount (PX) | number | `600` |

Content blocks accepted: `"blocks": [{ "type": "@theme" }]`.

## Metafields & metaobjects

None.

## Snippets rendered

None directly.

## Notes

- Individual community tiles are blocks, not settings — adding/removing items is a
  block operation.
- `scroll-amount` is the per-click distance for the arrow nav, mirroring the same
  setting on `related-products`.
