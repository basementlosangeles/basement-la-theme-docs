# Related Products

`sections/related-products.liquid`

## What it does

A "You may also like" horizontal carousel on the product page. Each card is rendered
by the `related-product-item` snippet (image, quick-add plus button with size
buttons, title, price). Includes a loading state and arrow navigation.

## Where it's used

Assigned in `templates/product.json` (the `theme` layout). Preset category:
**Product**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `title` | Title Text | text | `You may also like` |
| `no-products-text` | No Products Text | text | `No Products Found` |
| `loading-gif-background-color` | Loading Gif Background Color | color (alpha) | `rgba(17,17,17,0.5)` |
| `mobile--product-title-trademark-margin-left` | Mobile ® margin | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop ® margin | number | `4` |
| `scroll-amount` | Arrow Nav Button Scroll Amount (PX) | number | `600` |

## Metafields & metaobjects

The product list comes from `product.metafields.custom.related_products`
(list.product_reference, per the theme's metafield conventions). Each rendered card
reads `custom.color_label` / `custom.color_value` for its color swatch (via
`related-product-item`). No metaobjects.

## Snippets rendered

- `related-product-item` — a single product card. It in turn renders
  `processed-product-title` and `processed-product-title-pure`.

## Notes

- Curating which products appear is done by editing the product's
  `custom.related_products` metafield, not in the theme editor — only the surrounding
  copy/colors are section settings.
- Shares the `color_label`/`color_value` swatch model with `product`, `cart-sidebar`,
  and `buy-together`.
