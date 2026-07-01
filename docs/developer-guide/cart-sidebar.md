# Cart Sidebar

`sections/cart-sidebar.liquid`

## What it does

The slide-out cart. Shows line items, a free-shipping progress bar, cart
recommendations, discount badges, and the checkout button. It re-renders itself via
the Section Rendering API: cart actions fetch `/?section_id=cart-sidebar` and swap
`#cart-sidebar-container`'s innerHTML, after which `addCartEventListeners()` must be
re-run (logic in `assets/cart.js`).

## Where it's used

Rendered **globally by layouts**, not assigned via a template — it appears in
`theme`, `homepage-theme`, `page-cover-theme`, `page-text-theme`,
`page-text-theme-no-code-popup`, and the GemPages layouts. Preset category:
**Header Menu**.

## Schema settings

| id | label | type | default |
|---|---|---|---|
| `show-cart-sidebar` | Show Cart Sidebar | checkbox | `false` |
| `show-products-view` | Show Cart with Products View | checkbox | `false` |
| `product-show-products-view` | Product for Show Products View | product | — |
| `mobile--product-title-trademark-margin-left` | Mobile ® margin | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop ® margin | number | `4` |
| `cart-recommendations-collection` | Recommendation Collection | collection | — |
| `max-cart-recommendations-amount` | Max Recommendation Amount | number | `3` (-1 = unlimited) |
| `recommendations-title-text` | Recommendations Title Text | text | `Recommendations` |
| `no-products-text` | No Recommendations Available Text | text | `No Recommendations Available` |
| `progress-bar-fill-color` | Free Shipping Bar Fill Color | color | `rgba(17,17,17,1)` |
| `progress-bar-background-color` | Free Shipping Bar Background Color | color | `rgba(217,217,217,1)` |
| `progress-bar-info-text-less` | Bar Less-Than Text | text | `Away From Free Shipping` |
| `progress-bar-info-text-achieved` | Bar Achieved Text | text | `You Get Free Shipping!` |
| `progress-bar-info-text-not-work` | No Free Shipping (discounts) Text | text | `Free Shipping does not apply with discounts` |
| `remove-btn-hover-color` | Remove Button Hover Color | color | `rgba(207,58,50,1)` |
| `checkout-extra-text` | Checkout Extra Text | text | `Taxes and shipping calculated at checkout` |
| `discount-badge-text-color` | Discount Badge Text Color | color | `rgba(17,17,17,1)` |
| `discount-badge-background-color` | Discount Badge Background Color | color (alpha) | `rgba(84,62,62,0.75)` |
| `discount-badge-background-blur` | Discount Badge Background Blur (px) | number | `5` |
| `discount-badge-border-color` | Discount Badge Border Color | color (alpha) | `rgba(170,170,170,1)` |
| `discount-badge-border-thickness` | Discount Badge Border Thickness (px) | number | `1` |
| `empty-cart-text` | Empty Cart Text | text | `your cart is currently empty...` |
| `best-sellers-btn-link` | Best Sellers Button Link | url | — |
| `best-sellers-btn-text-color` | Best Sellers Button Text Color | color | `rgba(255,255,255,1)` |
| `best-sellers-btn-background-color` | Best Sellers Button Background Color | color | `rgba(237,31,36,1)` |
| `best-sellers-btn-hover-background-color` | Best Sellers Button Hover Background Color | color | `rgba(212,14,19,1)` |
| `shop-now-btn-link` | Shop Now Button Link | url | — |

The free-shipping threshold itself is **not** here — it's the global
`free-shipping-amount-threshold` setting (in cents-style integer form, e.g. `17500`).

## Metafields & metaobjects

Reads `custom.color_label` and `custom.color_value` (color swatch label + hex) on
cart line items and recommendations. No metaobjects.

## Snippets rendered

- `processed-product-title`
- `processed-product-title-pure`

## Notes

- `show-cart-sidebar` and `show-products-view` are **editor-preview toggles** —
  marked "[Leave Disabled in Production!]". They force the cart open so it can be
  styled in the editor; leaving them on ships an always-open cart.
- After any innerHTML swap, event listeners are gone — always re-run
  `addCartEventListeners()`. This is the single biggest gotcha when modifying cart JS.
- Keep `free-shipping-amount-threshold` consistent with the actual free-shipping
  discount in Shopify.
