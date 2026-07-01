# Buy Together Products

`sections/buy-together-products-section.liquid`

## What it does

Renders the "Buy Any and Get Additional X% Off" cross-sell module on the product
page — a row of products that, when purchased together, trigger a discount code.

## Where it's used

Assigned in `templates/product.json` (the `theme` layout). Preset category:
**Product**.

## Schema settings

The section's own schema contains **only an editor note** (`type: header` →
"Go to Theme Settings on Side Tab"). All real configuration lives in the **global
theme settings** under `Buy Together Products` (see
[Theme Architecture](architecture.md) and `config/settings_schema.json`):

| global id | label | type | default |
|---|---|---|---|
| `buy-together-title` | Buy Together Title | text | `Buy Any and Get Additional 10% Off` |
| `buy-together-no-products-text` | No Products Text | text | `No Products Found` |
| `buy-together-background-color` | Background Color | color | `rgba(243,243,243,1)` |
| `buy-together-collection` | Buy Together Collection | collection | — |
| `buy-together-max-items-amount` | Max Product Items | number | `3` (-1 = unlimited) |
| `buy-together-discount-code` | Discount Code | text | `BUYANYGET10OFF` |
| `buy-together-discount-amount` | Discount Amount (%) | number | `10` |
| `mobile--buy-together-product-title-trademark-margin-left` | Mobile ® margin | number | `2` |
| `desktop--buy-together-product-title-trademark-margin-left` | Desktop ® margin | number | `4` |

!!! warning "Keep code + amount in sync with the actual Shopify discount"
    `buy-together-discount-code` must match the discount's **Title** and
    `buy-together-discount-amount` must match its **percentage** in Shopify Discounts,
    or the cart total won't reflect what the UI promises.

## Metafields & metaobjects

Reads product metafields (all `custom` namespace — **no metaobjects**):

- `custom.buy_together_and_get_featured_products` — the featured products list that
  populates this section.
- `custom.color_label` / `custom.color_value` — color swatch label + hex for each
  rendered product item.

## Snippets rendered

- `processed-product-title` — product name with the styled ® trademark.
- `processed-product-title-pure` — plain (markup-free) product name.

## Notes

- This is the most "configuration lives elsewhere" section in the theme: editing the
  section in the editor does almost nothing; the merchant works in Theme Settings.
- The discount is enforced by Shopify's discount engine, not by this section — the
  theme only displays it and applies the code.
