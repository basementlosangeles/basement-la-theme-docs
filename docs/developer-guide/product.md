# Product

`sections/product.liquid`

## What it does

The product detail page — image gallery (with optional desktop fullscreen view),
title with the styled ® trademark, color swatches, size selection, price, preorder
handling, and the Sizing / Terms info tabs. This is the largest section in the theme
and the heaviest consumer of product metafields.

## Where it's used

Assigned in `templates/product.json`, using the `theme` layout. Uses both `@theme`
and `@app` blocks (e.g. `slogan-container`, `buy-together-products-block`). Preset
name: **Product**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `show-fullscreen-img` | Show Desktop Fullscreen Image View? | checkbox | `false` |
| `nav-btn-color` | Navigation Button Color | color (alpha) | `rgba(17,17,17,0.5)` |
| `nav-btn-hover-color` | Navigation Button Hover Color | color (alpha) | `rgba(17,17,17,0.65)` |
| `mobile--product-title-trademark-margin-left` | Mobile ® margin | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop ® margin | number | `4` |
| `thumbnail-btn-selected-border-thickness` | Thumbnail Btn Selected Border Thickness (px) | number | `1` |
| `preorder-text` | Preorder Text | text | `Preorder now. Ships in 4-8 weeks.` |
| `preorder-tag-title` | Preorder Tag Title | text | `Preorder` |
| `no-details-text` | No Details Text | text | `No Details Available` |
| `no-sizing-text` | No Size Chart Text | text | `No Size Chart Available` |
| `no-terms-text` | No Terms Text | text | `No Terms Available` |

Many product visuals (size buttons, color items, price slash, etc.) are styled via
the global `Product Color Settings` and `Product` theme settings, including
`product-title-trademark-font` and `product-preorder-text-format`.

## Metafields & metaobjects

Reads product metafields (all `custom` namespace — **no metaobjects**):

- `custom.color_label` / `custom.color_value` — color swatch label + hex.
- `custom.size_chart` — an image rendered in the **Sizing** tab (accessed via
  `| image_url`).

The **Terms** tab content is currently hardcoded in the section markup (a link to
`basement.la/pages/terms`), not a metafield. Preorder state is derived from the
product's **tags** matching `preorder-tag-title` / the global preorder format setting.

## Snippets rendered

- `processed-product-title` — title + styled ® trademark.

## Notes

- `show-fullscreen-img` is an **editor-preview toggle** ("[Leave Disabled in
  Production!]") — it forces the fullscreen image view open for styling.
- Per the theme's own notes, product shipping display moved between metafield keys
  historically (`ship-label` → `ship-date`) — confirm the live key in Liquid before
  touching shipping/slogan logic.
- Color swatch rendering here mirrors `cart-sidebar`, `related-products`, and
  `buy-together` — they all read the same `color_label`/`color_value` pair, so a
  change to that data model ripples across all four.
