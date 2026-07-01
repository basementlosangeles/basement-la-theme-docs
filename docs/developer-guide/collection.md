# Collection

`sections/collection.liquid`

## What it does

The product grid. Handles the filter bar, responsive column counts, "new" and
"sold out" badges, and inline promotional banners. Notably, this same section also
builds the **homepage** grid (`templates/index.json`), not just collection pages.

## Where it's used

Assigned in `templates/collection.json` **and** `templates/index.json`, both using
the `theme` layout. Preset name: **Collection**.

## Schema settings

### Section settings

| id | label | type | default |
|---|---|---|---|
| `show-product-item-full-title` | Show Full Product Title | checkbox | `true` |
| `mobile--min-product-width` | Mobile Min Product Item Width (PX) | number | `165` |
| `desktop--min-product-width` | Desktop Min Product Item Width (PX) | number | `297` |
| `desktop--grid-columns` | Default Desktop Grid Columns | range 2–10 | `4` |
| `filter-bar-collection-default` | Filter Bar Collection Default | collection | — |
| `filter-bar-collection-title-remove-character` | Title Remove Character | text | `*` |
| `filter-item-selected-background-color` | Filter Item Selected Background Color | color | `rgba(217,217,217,1)` |
| `show-restock-alert-tab` | Show Restock Alert tab | checkbox | `true` |
| `restock-alert-tab-label` | Restock Alert tab label | text | `GET UPDATES` |
| `restock-alert-page` | Restock Alert page | page | — |
| `mobile--product-title-trademark-margin-left` | Mobile ® margin | number | `1` |
| `desktop--product-title-trademark-margin-left` | Desktop ® margin | number | `1` |
| `product-item-sold-out-overlay-color` | Sold Out Overlay Color | color (alpha) | `rgba(217,217,217,0.7)` |
| `no-products-text` | No Products Found Text | text | `No Products Available` |
| `product-item-new-badge-text-color` | New Badge Text Color | color | `rgba(17,17,17,1)` |
| `product-item-new-badge-background-color` | New Badge Background Color | color | `rgba(247,231,76,1)` |
| `product-item-sold-out-badge-text-color` | Sold Out Badge Text Color | color | `rgba(217,217,217,1)` |
| `product-item-sold-out-badge-background-color` | Sold Out Badge Background Color | color | `rgba(86,87,87,1)` |

### Block: `collection-grid-columns`

Overrides the default desktop column count per collection.

| id | label | type | default |
|---|---|---|---|
| `collection-type` | Collection | collection | — |
| `grid-columns` | Desktop Grid Columns | range 2–10 | `4` |

### Block: `product-banner`

An in-grid promo banner inserted after the Nth product. Supports same-across-devices
or separate mobile/desktop images, each with focal point (`_x`/`_y`, 0–100%), zoom
(100–200%), width-in-columns (`-1` = full row), and pixel height. Plus title,
subtitle, text color, and title/subtitle sizes. The mobile/desktop fields are gated
by `visible_if` on `image_preference`. Rendered through the `product-banner` snippet.

Key fields: `collection-type`, `insert_after_product` (`10000` = end),
`visibility_preference` (mobile/desktop/both), `image_preference` (same/different),
`image` / `mobile_image` / `desktop_image`, and the `*_width/_height/_x/_y/_zoom`
groups. See `inventory.md` for the full field list.

## Metafields & metaobjects

Reads `product.metafields.custom.fitting` (product fit label) on grid items. No
metaobjects.

## Snippets rendered

- `product-banner` — renders the in-grid banner block.
- `processed-product-title` — product names with the styled ® trademark.

## Notes

- Column resolution order: a matching `collection-grid-columns` block wins;
  otherwise the section's `desktop--grid-columns` is the fallback (1024px and up).
- `filter-bar-collection-title-remove-character` (default `*`) hides a collection
  from the filter bar when its title contains that character — a content-side toggle.
- Because this section doubles as the homepage grid, test both templates when
  changing grid logic.
