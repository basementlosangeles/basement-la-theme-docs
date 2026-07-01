# Basement LA Theme — Section Schema Inventory

> Source theme repo: `../dev/2025-Website` (the Basement.la 2025 Shopify storefront).
> This is a raw inventory of every **section that exposes a `{% schema %}` block**
> (i.e. is editable in the Shopify theme editor), plus the **global theme settings**
> (`config/settings_schema.json`). Generated for review before docs pages are written.
> No metaobject references were found anywhere; all dynamic data comes from product
> **metafields** in the `custom` namespace.

---

## How sections reach the page (usage model)

This theme does **not** use a single `theme.liquid`. Sections appear on a page through one of three routes:

1. **Template JSON** (`templates/*.json`) — assigns a section to a page type.
2. **Section groups** (`sections/header-group.json`, `sections/header-group-no-background.json`) — the header stack, pulled into layouts via `{% sections %}`.
3. **Layout-level renders** (`layout/*.liquid`) — global chrome rendered on every page that uses that layout (cart, radio, code-popup, footer).

Layout → which global sections it renders:

| Layout | header group | cart-sidebar | radio-sidebar | code-popup | footer |
|---|---|---|---|---|---|
| `theme` | header-group | ✓ | ✓ | ✓ | ✓ |
| `homepage-theme` | header-group-no-background | ✓ | ✓ | — (commented out) | — |
| `page-cover-theme` | header-group-no-background | ✓ | ✓ | ✓ | ✓ |
| `page-text-theme` | header-group | ✓ | ✓ | ✓ | ✓ |
| `page-text-theme-no-code-popup` | header-group | ✓ | ✓ | — | ✓ |
| `password-theme` | — | — | — | — | — |

---

## Section inventory

Each entry lists: **file path**, **where it's used**, **schema settings** (id / label / type / default), **block settings defined inline** (if any), **snippets it renders**, and **metafields it reads**. Settings of `type: header` are editor labels only (no value) and are shown as *group dividers* in italics.

---

### 404 — `sections/404.liquid`
- **Used in:** `templates/404.json` (layout `theme`). Preset category: Pages.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| `title-text` | Title Text | text | `Page Not Found` |
| *— Shop Button —* | | header | |
| `shop-btn-text` | Shop Button Text | text | `Shop All` |
| `shop-btn-text-color` | Shop Button Text Color | color | `rgba(255,255,255,1)` |
| `shop-btn-background-color` | Shop Button Background Color | color | `#ED1F24` |
| `shop-btn-link` | Shop Button Link | url | `/collections/all` |

---

### About — `sections/about-page.liquid`
- **Used in:** `templates/page.About.json` (layout `page-text-theme`).
- **Schema settings:** none (content built entirely from `about-page-*` theme blocks: section, text, logo, pic-container, pic, link-container, link).
- **Snippets rendered:** none. **Metafields:** none.

---

### Announcement Bar — `sections/announcement-bar.liquid`
- **Used in:** both section groups (`header-group.json`, `header-group-no-background.json`) → appears on every page whose layout includes a header group. Preset category: Header Group.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Announcement Block —* | | header | |
| `announcement_text` | Announcement Text | text | `FREE SHIPPING ON US ORDERS 175+` |
| `announcement_text_color` | Announcement Text Color | color | `#ffffff` |
| `announcement_background_color` | Announcement Background Color | color | `#3b3b3bff` |
| *— Countdown Settings —* | | header | |
| `is-countdown-enabled` | Is Countdown Enabled? | checkbox | `false` |
| `date-time-before-drop` | Date and Time Before Drop | text | `08/25/2025 15:50:00` (fmt mm/dd/yyyy hh:mm:ss) |
| *— Time Block —* | | header | |
| `time_text_color` | Time Block Text Color | color | `#3A3A3A` |
| `time_background_color` | Time Block Background Color | color | `#d9d9d9ff` |

---

### Archive — `sections/archive.liquid`
- **Used in:** `templates/page.Archive.json` (layout `page-cover-theme`). Content from `archive-item` / `archive-small-group` theme blocks.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Content —* | | header | |
| `background-color` | Background Color | color | `rgba(17,17,17,1)` |
| *— Scrollbar —* | | header | |
| `scrollbar-foreground-color` | Scrollbar Foreground Color | color | `#d9d9d9` |

---

### Buy Together Products — `sections/buy-together-products-section.liquid`
- **Used in:** `templates/product.json` (layout `theme`). Preset category: Product.
- **Schema settings:** only an editor note header (`"Go to Theme Settings on Side Tab"`) — **all real configuration lives in the global `Buy Together Products` theme settings** (see settings_schema section below).
- **Snippets rendered:** `processed-product-title`, `processed-product-title-pure`.
- **Metafields read:** `product.metafields.custom.buy_together_and_get_featured_products` (the featured products list driving the section), `custom.color_label`, `custom.color_value` (color swatch label + hex).

---

### Cart Sidebar — `sections/cart-sidebar.liquid`
- **Used in:** rendered globally by layouts (`theme`, `homepage-theme`, `page-cover-theme`, `page-text-theme`, `page-text-theme-no-code-popup`, and GemPages layouts). Preset category: Header Menu.
- **Snippets rendered:** `processed-product-title`, `processed-product-title-pure`.
- **Metafields read:** `custom.color_label`, `custom.color_value`.

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `show-cart-sidebar` | Show Cart Sidebar | checkbox | `false` *(leave off in prod)* |
| `show-products-view` | Show Cart with Products View | checkbox | `false` *(leave off in prod)* |
| `product-show-products-view` | Product for Show Products View | product | — |
| *— Product Title Trademark —* | | header | |
| `mobile--product-title-trademark-margin-left` | Mobile Trademark Margin Left | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop Trademark Margin Left | number | `4` |
| *— Cart Recommendations —* | | header | |
| `cart-recommendations-collection` | Recommendation Collection | collection | — |
| `max-cart-recommendations-amount` | Max Recommendation Amount | number | `3` (-1 = unlimited) |
| `recommendations-title-text` | Recommendations Title Text | text | `Recommendations` |
| `no-products-text` | No Recommendations Available Text | text | `No Recommendations Available` |
| *— Free Shipping Bar —* | | header | |
| `progress-bar-fill-color` | Free Shipping Bar Fill Color | color | `rgba(17,17,17,1)` |
| `progress-bar-background-color` | Free Shipping Bar Background Color | color | `rgba(217,217,217,1)` |
| `progress-bar-info-text-less` | Bar Less-Than Text | text | `Away From Free Shipping` |
| `progress-bar-info-text-achieved` | Bar Achieved Text | text | `You Get Free Shipping!` |
| `progress-bar-info-text-not-work` | No Free Shipping (discounts) Text | text | `Free Shipping does not apply with discounts` |
| *— Cart Item —* | | header | |
| `remove-btn-hover-color` | Remove Button Hover Color | color | `rgba(207,58,50,1)` |
| *— Checkout —* | | header | |
| `checkout-extra-text` | Checkout Extra Text | text | `Taxes and shipping calculated at checkout` |
| *— Discount Badge —* | | header | |
| `discount-badge-text-color` | Discount Badge Text Color | color | `rgba(17,17,17,1)` |
| `discount-badge-background-color` | Discount Badge Background Color | color (alpha) | `rgba(84,62,62,0.75)` |
| `discount-badge-background-blur` | Discount Badge Background Blur | number | `5` (px) |
| `discount-badge-border-color` | Discount Badge Border Color | color (alpha) | `rgba(170,170,170,1)` |
| `discount-badge-border-thickness` | Discount Badge Border Thickness | number | `1` (px) |
| *— Empty Cart —* | | header | |
| `empty-cart-text` | Empty Cart Text | text | `your cart is currently empty...` |
| `best-sellers-btn-link` | Best Sellers Button Link | url | — |
| `best-sellers-btn-text-color` | Best Sellers Button Text Color | color | `rgba(255,255,255,1)` |
| `best-sellers-btn-background-color` | Best Sellers Button Background Color | color | `rgba(237,31,36,1)` |
| `best-sellers-btn-hover-background-color` | Best Sellers Button Hover Background Color | color | `rgba(212,14,19,1)` |
| `shop-now-btn-link` | Shop Now Button Link | url | — |

---

### Code Popup — `sections/code-popup.liquid`
- **Used in:** rendered globally by layouts `theme`, `page-cover-theme`, `page-text-theme` (commented out in `homepage-theme`; absent from the `-no-code-popup` layout). Steps are `code-popup-*-view` theme blocks (email → phone → code → claim).
- **Snippets rendered:** none. **Metafields:** none.
- **Note:** primary/text colors come from the global `Code Popup Settings` theme settings.

| id | label | type | default |
|---|---|---|---|
| `is-enabled` | Is Enabled? | checkbox | `true` |
| `popup-appear-delay` | Popup Appear Delay (S) | number | `5` |
| *— Cancel Button —* | | header | |
| `cancel-button-text` | Cancel Button Text | text | `I don't want my gift` |
| `cancel-button-text-color` | Cancel Button Text Color | color | `#060607` |
| `cancel-button-background-color` | Cancel Button Background Color | color | `#595344` |
| `cancel-button-border-color` | Cancel Button Border Color | color | `#060607` |

---

### Collection — `sections/collection.liquid`
- **Used in:** `templates/collection.json` **and** `templates/index.json` (layout `theme`) — i.e. this section also renders the homepage product grid.
- **Snippets rendered:** `product-banner`, `processed-product-title`.
- **Metafields read:** `product.metafields.custom.fitting` (product fit label).

**Section settings:**

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `show-product-item-full-title` | Show Full Product Title | checkbox | `true` |
| *— Product Configuration —* | | header | |
| `mobile--min-product-width` | Mobile Min Product Item Width (PX) | number | `165` |
| `desktop--min-product-width` | Desktop Min Product Item Width (PX) | number | `297` |
| `desktop--grid-columns` | Default Desktop Grid Columns | range (2–10, step 1) | `4` |
| *— Filter Bar —* | | header | |
| `filter-bar-collection-default` | Filter Bar Collection Default | collection | — |
| `filter-bar-collection-title-remove-character` | Title Remove Character | text | `*` |
| `filter-item-selected-background-color` | Filter Item Selected Background Color | color | `rgba(217,217,217,1)` |
| `show-restock-alert-tab` | Show Restock Alert tab | checkbox | `true` |
| `restock-alert-tab-label` | Restock Alert tab label | text | `GET UPDATES` |
| `restock-alert-page` | Restock Alert page | page | — |
| *— Product Item Title Trademark —* | | header | |
| `mobile--product-title-trademark-margin-left` | Mobile Trademark Margin Left | number | `1` |
| `desktop--product-title-trademark-margin-left` | Desktop Trademark Margin Left | number | `1` |
| *— Product Item Details —* | | header | |
| `product-item-sold-out-overlay-color` | Sold Out Overlay Color | color (alpha) | `rgba(217,217,217,0.7)` |
| `no-products-text` | No Products Found Text | text | `No Products Available` |
| *— New Badge —* | | header | |
| `product-item-new-badge-text-color` | New Badge Text Color | color | `rgba(17,17,17,1)` |
| `product-item-new-badge-background-color` | New Badge Background Color | color | `rgba(247,231,76,1)` |
| *— Sold Out —* | | header | |
| `product-item-sold-out-badge-text-color` | Sold Out Badge Text Color | color | `rgba(217,217,217,1)` |
| `product-item-sold-out-badge-background-color` | Sold Out Badge Background Color | color | `rgba(86,87,87,1)` |

**Inline block — `collection-grid-columns` (name: "Collection Grid Columns"):**

| id | label | type | default |
|---|---|---|---|
| `collection-type` | Collection | collection | — |
| `grid-columns` | Desktop Grid Columns | range (2–10, step 1) | `4` |

**Inline block — `product-banner` (name: "Product Banner"):** an in-grid promo banner. Key settings (mobile/desktop variants share the same shape):

| id | label | type | default |
|---|---|---|---|
| `collection-type` | Collection Type | collection | — |
| `insert_after_product` | Insert After Product # | number | `0` (10000 = end) |
| `visibility_preference` | Visibility Preference | select (mobile/desktop/both) | `both` |
| `image_preference` | Image Preference | select (same/different) | `same` |
| `image` | Banner Image (`same`) | image_picker | — |
| `image_width` | Image Width Across Columns | number | `-1` (-1 = full row) |
| `image_height` | Image Height (px) | number | `-1` |
| `image_x` / `image_y` | Image X / Y Position | range 0–100 %, step 5 | `50` / `50` |
| `image_zoom` | Image Zoom | range 100–200 %, step 5 | `100` |
| `mobile_image*` (`mobile_image`, `_width`, `_height`, `_x`, `_y`, `_zoom`) | Mobile variants (`different`) | same types as above | same defaults |
| `desktop_image*` (`desktop_image`, `_width`, `_height`, `_x`, `_y`, `_zoom`) | Desktop variants (`different`) | same types as above | same defaults |
| `title` | Title | text | — |
| `subtitle` | Subtitle | text | — |
| `text_color` | Text Color | color | `#ffffff` |
| `title_size` | Title Size | range 16–72 px | `36` |
| `subtitle_size` | Subtitle Size | range 10–32 px | `16` |

*(Same-vs-different image fields are toggled with `visible_if` on `image_preference`.)*

---

### Community Side Panel — `sections/community-side-panel.liquid`
- **Used in:** `templates/product.json` (layout `theme`). Items from `community-item` theme blocks. Preset category: Product.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Content —* | | header | |
| `title` | Title | text | `Styled By The Community` |
| `no-items-text` | No Items Text | text | `No Items Available` |
| *— UX —* | | header | |
| `scroll-amount` | Arrow Nav Button Scroll Amount (PX) | number | `600` |

---

### Contact — `sections/contact.liquid`
- **Used in:** `templates/page.Contact.json` (layout `page-cover-theme`). `max_blocks: 1` (one `featured-cover-image` theme block).
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Content —* | | header | |
| `title-text` | Title Text | text | `Get in Touch` |
| `body-text` | Body Text | richtext | `<p>Please fill in the form below or email us at <strong>getbasement@gmail.com.</strong></p>` |
| *— Inputs —* | | header | |
| `name-input-placeholder-text` | Name Input Placeholder | text | `Name` |
| `subject-input-placeholder-text` | Subject Input Placeholder | text | `SUBJECT (ORDER NUMBER IF APPLICABLE)` |
| `message-input-placeholder-text` | Message Input Placeholder | text | `Message` |
| *— Email Input —* | | header | |
| `email-input-placeholder-text` | Email Input Placeholder | text | `Email` |
| `email-input-error-text` | Email Input Error Text | text | `Enter a valid email!` |
| *— Submit Section —* | | header | |
| `submit-text` | Submit Text | text | `All fields are required to submit.` |
| `submit-btn-text` | Submit Button Text | text | `Submit` |

---

### Default Page — `sections/default-page.liquid`
- **Used in:** `templates/page.json` (layout `page-text-theme`) — the generic/fallback page template. Preset category: Main.
- **Schema settings:** none. **Snippets rendered:** none. **Metafields:** none.

---

### FAQ Page — `sections/faq-page.liquid`
- **Used in:** `templates/page.FAQ.json` (layout `page-text-theme`). Q&A from `faq-dropdown-item` theme blocks.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| `title-text` | Title Text | text | `FAQ` |

---

### Footer — `sections/footer.liquid`
- **Used in:** rendered globally by layouts (`page-cover-theme`, `page-text-theme`, `page-text-theme-no-code-popup`, `theme`, `theme.gempages.footer`) and explicitly in `templates/password.json`. Preset category: Layout.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Menu Lists —* | | header | |
| `footer-main-menu` | Footer Main Menu | link_list | — |
| `footer-social-menu` | Footer Social Menu | link_list | — |
| *— Content —* | | header | |
| `text-color` | Text Color | color | `rgba(255,255,255,1)` |
| `text-hover-color` | Text Hover Color | color | `rgba(170,170,170,1)` |
| `background-color` | Background Color | color | `rgba(17,17,17,1)` |
| `border-color` | Border Color | color (alpha) | `rgba(255,255,255,0.1)` |
| *— Early Access —* | | header | |
| `is-early-access-enabled` | Enable Early Access? | checkbox | `true` |
| `label-text` | Early Access Label Text | text | `Get Early Access` |
| `placeholder-input-text` | Early Access Placeholder Input Text | text | `Email` |
| *— Logo —* | | header | |
| `basement-logo-link` | Basement Logo Link | url | `/` |
| `copyright-text` | Copyright Text | text | `@Basement 2025.` |

---

### Header Menu — `sections/header-menu.liquid`
- **Used in:** both section groups (`header-group.json`, `header-group-no-background.json`). Composed of `header-sidebar`, `header-sidebar-home-view`, `header-sidebar-shop-view`, `header-shop-item`, `desktop-header-shop-drawer` theme blocks. Preset category: Header Group.
- **Snippets rendered:** `desktop-currency-selector`.
- **Metafields:** none. (Menu link lists configured in global `Header Menu` / `Header Sidebar` theme settings.)

| id | label | type | default |
|---|---|---|---|
| `does-header-have-background` | Does Header Have Background? | checkbox | `true` |
| *— Text —* | | header | |
| `text-color` | Text Color | color | `#111111` |
| `text-hover-color` | Text Hover Color | color (alpha) | `#111111` |
| `active-shop-drawer-inactive-text-color` | Inactive Text Color when Shop Drawer Active | color (alpha) | `rgba(17,17,17,0.5)` |
| *— Menu Item —* | | header | |
| `desktop--shop-menu-item-padding` | Desktop Shop Menu Item Padding | number | `8` |
| *— Restock Alert —* | | header | |
| `restock-alert-page` | Restock Alert page | page | — |
| `restock-alert-menu-label` | Restock Alert menu label | text | `GET UPDATES` |
| *(— Coming Soon —, header only)* | | header | |

---

### Homepage — `sections/homepage.liquid`
- **Used in:** ⚠️ **Not currently assigned to any template.** Preset "Homepage" exists, but `templates/index.json` builds the homepage from the `collection` section instead. Appears to be a legacy/alternate hero section. Worth confirming with the team before documenting.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| `media-type` | Media Type | select (image/video) | `image` |
| *— Background Image (visible if media-type=image) —* | | header | |
| `mobile--background-image` | Mobile Background Image | image_picker | — |
| `desktop--background-image` | Desktop Background Image | image_picker | — |
| `mobile--background-image-x-pos` | Mobile BG Image X Pos (%) | number | `0` |
| `mobile--background-image-y-pos` | Mobile BG Image Y Pos (%) | number | `0` |
| `mobile--background-image-zoom` | Mobile BG Image Zoom (%) | number | `100` |
| `desktop--background-image-x-pos` | Desktop BG Image X Pos (%) | number | `0` |
| `desktop--background-image-y-pos` | Desktop BG Image Y Pos (%) | number | `2` |
| `desktop--background-image-zoom` | Desktop BG Image Zoom (%) | number | `105` |
| *— Background Video (visible if media-type=video) —* | | header | |
| `mobile--background-video` | Mobile Background Video | video | — |
| `desktop--background-video` | Desktop Background Video | video | — |
| *— Background Overlay —* | | header | |
| `background-overlay-color` | Background Overlay Color | color (alpha) | `rgba(0,0,0,0.2)` |
| `background-graident-color` | Desktop Background Gradient Color | color | `#000000` |
| `desktop--background-graident-opacity` | Desktop Gradient Opacity (%) | range 0–100 | `30` |
| `desktop--background-graident-y-pos` | Desktop Gradient End Y Pos (%) | range 0–100, step 5 | `30` |
| *— Enter Button —* | | header | |
| `text-color` | Text Color | color | `#ffffff` |
| `text` | Text | text | `Enter Basement` |
| `btn-link` | Button Link | url | `/collections/all` |

---

### Join Waitlist Modal — `sections/join-waitlist-modal.liquid`
- **Used in:** `templates/product.json`, `templates/index.json`, `templates/collection.json`. Preset category: Pages.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `is-modal-for-product-page` | Is Modal for Product Page? | checkbox | `false` |
| `klaviyo-form-id` | Klaviyo Form ID | text | — |
| *— Content —* | | header | |
| `title-text` | Modal Title Text | text | `Notify Me When Available` |
| `background-color` | Background Color | color | `rgba(170,170,170,1)` |
| `backdrop-color` | Backdrop Color | color (alpha) | `rgba(17,17,17,0.2)` |

---

### Password — `sections/password.liquid`
- **Used in:** `templates/password.json` (layout `password-theme`). Uses `password-item` theme blocks + `@app` blocks. Carousel images come from blocks.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `show-password-page` | Show Password Page | checkbox | `false` *(leave off in prod)* |
| `klaviyo-form-id` | Klaviyo Form ID | text | — |
| *— Content —* | | header | |
| `title-text` | Title Text | text | `New Drop` |
| *— Countdown Text —* | | header | |
| `date-time-before-drop` | Date and Time Before Drop | text | `08/25/2025 15:50:00` |
| `countdown-done-text` | Countdown Done Text | text | `Please Wait A Moment` |
| *— Image Carousel —* | | header | |
| `is-scrolling-img-carousel` | Scroll Image Carousel? | checkbox | `true` |
| `img-carousel-scroll-speed` | Img Carousel Speed | number | `1` (no decimals — Safari) |
| *— Inputs —* | | header | |
| `password-input-placeholder-text` | Password Input Placeholder | text | `Password` |
| *— Buttons —* | | header | |
| `password-btn-text` | Password Button Text | text | `Password` |
| `enter-btn-text` | Enter Button Text | text | `Enter` |
| `subscribe-btn-text` | Subscribe Button Text | text | `Subscribe` |

---

### Policy Page Section — `sections/policy-page-section.liquid`
- **Used in:** `templates/page.Privacy-Policy.json` (layout `page-text-theme`) — used multiple times. Content from `policy-page-header`, `policy-page-text`, `policy-page-bullet-parent`, `policy-page-bullet-item`, `policy-page-table*` theme blocks. Preset category: Main.
- **Schema settings:** none. **Snippets rendered:** none. **Metafields:** none.

---

### Policy Page — `sections/policy-page.liquid`
- **Used in:** ⚠️ **Not referenced by any template** (preset "Policy Page", category Main, exists). Likely superseded by `policy-page-section`. Confirm before documenting.
- **Schema settings:** none. **Snippets rendered:** none. **Metafields:** none.

---

### Product — `sections/product.liquid`
- **Used in:** `templates/product.json` (layout `theme`). Uses `@theme` + `@app` blocks (e.g. `slogan-container`, `buy-together-products-block`).
- **Snippets rendered:** `processed-product-title`.
- **Metafields read:** `custom.color_label`, `custom.color_value` (color swatches), `custom.size_chart` (image shown in the Sizing tab). Also reads product **tags** (preorder) and product description/terms. *(Note: the global `Product` theme setting `product-preorder-text-format` governs preorder detection too.)*

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `show-fullscreen-img` | Show Desktop Fullscreen Image View? | checkbox | `false` *(leave off in prod)* |
| *— Navigation Bar —* | | header | |
| `nav-btn-color` | Navigation Button Color | color (alpha) | `rgba(17,17,17,0.5)` |
| `nav-btn-hover-color` | Navigation Button Hover Color | color (alpha) | `rgba(17,17,17,0.65)` |
| *— Product Title Trademark —* | | header | |
| `mobile--product-title-trademark-margin-left` | Mobile Trademark Margin Left | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop Trademark Margin Left | number | `4` |
| *— Product Details —* | | header | |
| `thumbnail-btn-selected-border-thickness` | Thumbnail Btn Selected Border Thickness | number | `1` (px) |
| `preorder-text` | Preorder Text | text | `Preorder now. Ships in 4-8 weeks.` |
| `preorder-tag-title` | Preorder Tag Title | text | `Preorder` |
| *— Not Available Text —* | | header | |
| `no-details-text` | No Details Text | text | `No Details Available` |
| `no-sizing-text` | No Size Chart Text | text | `No Size Chart Available` |
| `no-terms-text` | No Terms Text | text | `No Terms Available` |

---

### Basement Radio Sidebar — `sections/radio-sidebar.liquid`
- **Used in:** rendered globally by layouts `theme`, `homepage-theme`, `page-cover-theme`, `page-text-theme`, `page-text-theme-no-code-popup`. Tracks from `radio-sidebar-track` theme blocks.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| `mobile--exit-arrow-text` | Mobile Exit Arrow Text | text | `Click Arrow to Exit` |
| *— Color —* | | header | |
| `primary-color` | Primary Color | color | `#3a3a3a` |
| `secondary-color` | Secondary Color | color | `#000000` |
| `background-color` | Background Color | color | `#d7d8d7` |
| `button-selected-color` | Button Selected Color | color | `#999999` |
| *— Images —* | | header | |
| `radio-default-img` | Radio Default Image | image_picker | — |

---

### Related Products — `sections/related-products.liquid`
- **Used in:** `templates/product.json` (layout `theme`). Preset category: Product.
- **Snippets rendered:** `related-product-item` (which in turn renders `processed-product-title` / `processed-product-title-pure`).
- **Metafields read (via `related-product-item`):** `custom.color_label`, `custom.color_value`. Related products themselves are sourced from `custom.related_products` per the theme CLAUDE.md.

| id | label | type | default |
|---|---|---|---|
| *— Content —* | | header | |
| `title` | Title Text | text | `You may also like` |
| `no-products-text` | No Products Text | text | `No Products Found` |
| `loading-gif-background-color` | Loading Gif Background Color | color (alpha) | `rgba(17,17,17,0.5)` |
| *— Product Item Title Trademark —* | | header | |
| `mobile--product-title-trademark-margin-left` | Mobile Trademark Margin Left | number | `2` |
| `desktop--product-title-trademark-margin-left` | Desktop Trademark Margin Left | number | `4` |
| *— UX —* | | header | |
| `scroll-amount` | Arrow Nav Button Scroll Amount (PX) | number | `600` |

---

### Signup — `sections/signup.liquid`
- **Used in:** `templates/page.Signup.json` **and** `templates/page.restock-alert.json` (both layout `page-text-theme-no-code-popup`).
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| *— Editor —* | | header | |
| `klaviyo-form-id` | Klaviyo Form ID | text | `X4vx3V` |
| *— Content —* | | header | |
| `title-text` | Title Text | text | `NEW DROP COMING SOON` |
| `subtitle-text` | Subtitle Text | text | `SIGN UP TO BE THE FIRST TO KNOW` |
| *— Image —* | | header | |
| `show-image` | Show Image | checkbox | `true` |
| `image` | Image | image_picker | — |
| *— Countdown —* | | header | |
| `show-countdown` | Show Countdown | checkbox | `false` |
| `date-time-before-drop` | Date and Time Before Drop | text | `12/31/2025 15:00:00` |
| `countdown-done-text` | Countdown Done Text | text | `DROP IS LIVE` |

---

### Spacer — `sections/spacer.liquid`
- **Used in:** ⚠️ **Not currently placed in a template** — a utility preset ("Spacer") that can be inserted anywhere via the editor.
- **Snippets rendered:** none. **Metafields:** none.

| id | label | type | default |
|---|---|---|---|
| `has-mobile-and-desktop-variants` | Has Mobile and Desktop Variants? | checkbox | `false` |
| `spacing` | Spacing (PX) | number | `0` (visible if variants = false) |
| `mobile--spacing` | Mobile Spacing (PX) | number | `0` (visible if variants = true) |
| `desktop--spacing` | Desktop Spacing (PX) | number | `0` (visible if variants = true) |

---

## Global theme settings — `config/settings_schema.json`

These are **site-wide**, edited under Theme Settings (the side tab), not per-section. Several sections delegate their real config here (notably Buy Together, Code Popup, Product, and all color tokens).

**theme_info:** name `JUST BASEMENT V.1`, version `1.0.0`, authors Julian, Nash, Kartik.

### Header Menu
| id | label | type | default |
|---|---|---|---|
| `header-left-menu` | Header Left Menu | link_list | — |
| `header-right-menu` | Header Right Menu | link_list | — |
| `header-menu-item-title-for-shop-drawer` | Menu Item Title for Shop Drawer | text | `Shop All` |
| `header-menu-item-title-for-radio` | Menu Item Title for Basement Radio | text | `Basement Radio` |
| `header-background-color` | Header Background Color | color | `rgba(255,255,255,1)` |

### Header Sidebar
| id | label | type | default |
|---|---|---|---|
| `header-sidebar-main-menu` | Header Sidebar Main Menu | link_list | — |
| `header-sidebar-soon-menu` | Header Sidebar Soon Menu | link_list | — |
| `header-sidebar-menu-item-title-for-shop-view` | Menu Item Title for Shop View | text | `Shop` |

### Product
| id | label | type | default |
|---|---|---|---|
| `product-title-trademark-font` | Product Title Trademark Font | font_picker | `arial_n7` |
| `product-preorder-text-format` | Product Preorder Text Format | text | `Preorder` |

### Free Shipping
| id | label | type | default |
|---|---|---|---|
| `free-shipping-amount-threshold` | Free Shipping Threshold | number | `17500` ($1.23 → 123) |

### Buy Together Products
| id | label | type | default |
|---|---|---|---|
| `buy-together-title` | Buy Together Title | text | `Buy Any and Get Additional 10% Off` |
| `buy-together-no-products-text` | Buy Together No Products Text | text | `No Products Found` |
| `buy-together-background-color` | Buy Together Background Color | color | `rgba(243,243,243,1)` |
| `mobile--buy-together-product-title-trademark-margin-left` | Mobile Trademark Margin Left (PX) | number | `2` |
| `desktop--buy-together-product-title-trademark-margin-left` | Desktop Trademark Margin Left (PX) | number | `4` |
| `buy-together-collection` | Buy Together Collection | collection | — |
| `buy-together-max-items-amount` | Buy Together Max Product Items Amount | number | `3` (-1 = unlimited) |
| `buy-together-discount-code` | Buy Together Discount Code | text | `BUYANYGET10OFF` |
| `buy-together-discount-amount` | Buy Together Discount Amount (%) | number | `10` |

### Code Popup Settings
| id | label | type | default |
|---|---|---|---|
| `code-popup-primary-color` | Code Popup Primary Color | color | `#ffce00` |
| `code-popup-text-color` | Code Popup Text Color | color | `#ffffff` |

### Primary Color Settings
Text/background/border/button/input color tokens used theme-wide. ids: `primary-text-color` (`rgba(17,17,17,1)`), `secondary-text-color` (`#454545`), `primary-background-color` (`#ECECEC`), `primary-backdrop-color` (`rgba(17,17,17,0.3)`), `primary-border-shadow-color` (`rgba(73,73,73,0.5)`), `primary-border-color` (`rgba(17,17,17,0.1)`), `primary-border-thickness` (`1`), `primary-btn-text-color` (`rgba(255,255,255,1)`), `primary-btn-background-color` (`rgba(17,17,17,1)`), `primary-btn-animation-time` (`0.15s`), `primary-btn-hover-background-color` (`rgba(51,51,51,1)`), `primary-btn-disabled-text-color` (`rgba(17,17,17,0.5)`), `primary-btn-disabled-background-color` (`rgba(170,170,170,1)`), `primary-input-border-color` (`rgba(170,170,170,1)`), `primary-input-selected-border-color` (`rgba(17,17,17,1)`), `primary-input-invalid-border-color` (`rgba(237,31,36,1)`), `primary-input-border-thickness` (`1`), `primary-input-placeholder-color` (`rgba(17,17,17,0.5)`), `primary-input-placeholder-disabled-color` (`rgba(17,17,17,0.3)`), `primary-input-disabled-background-color` (`rgba(217,217,217,1)`), `loading-gif-background-color` (`rgba(17,17,17,0.5)`).

### Product Color Settings
Product-specific color/size-selector tokens. ids: `product-background-color` (`rgba(217,217,217,1)`), `item-hover-border-color` (`rgba(170,170,170,1)`), `item-selected-border-color` (`#111111`), `product-color-item-border-thickness` (`1`), `product-size-dropdown-border-color` (`rgba(170,170,170,1)`), `product-size-dropdown-selected-border-color` (`rgba(17,17,17,1)`), `product-size-dropdown-text-color-sold-out` (`rgba(17,17,17,0.5)`), `product-size-option-text-color-sold-out` (`rgba(17,17,17,0.3)`), `product-size-btn-backdrop-color` (`rgba(58,58,58,0.01)`), `product-size-btn-backdrop-blur` (`6`), `product-size-btn-text-color` (`rgba(17,17,17,1)`), `product-size-btn-text-color-disabled` (`rgba(17,17,17,0.3)`), `product-size-btn-background-color` (`rgba(236,236,236,1)`), `product-size-btn-border-thickness` (`1`), `product-default-color-title` (`Default`), `product-default-size-title` (`Standard`), `product-slash-price-text-color` (`rgba(17,17,17,0.5)`).

### Other Color Settings
Arrow-nav button colors. ids: `arrow-nav-btn-background-color` (`rgba(170,170,170,1)`), `active-arrow-nav-btn-color` (`#111111`), `inactive-arrow-nav-btn-color` (`rgba(17,17,17,0.5)`).

---

## Cross-cutting notes (for the docs phase)

- **Metafields used by sections (all `custom` namespace, product-level):**
  `buy_together_and_get_featured_products` (buy-together), `related_products` (related-products, per theme docs), `color_label` + `color_value` (color swatches — product, cart-sidebar, buy-together, related-product-item), `size_chart` (product Sizing tab, image), `fitting` (collection grid). **No metaobjects referenced.**
- **Shared title snippets:** `processed-product-title` (adds the styled ® trademark using the global trademark font, optional color label) and `processed-product-title-pure` (plain base title, no markup) are used across product, cart, buy-together, collection, and related-products — central to how product names render everywhere.
- **"Leave Disabled in Production" toggles** exist on cart-sidebar (`show-cart-sidebar`, `show-products-view`), product (`show-fullscreen-img`), and password (`show-password-page`) — editor-only preview switches.
- **Sections to verify before documenting:** `homepage` (preset exists but unused — index uses `collection`), `policy-page` (superseded by `policy-page-section`), `spacer` (utility, not placed). 
- **Klaviyo form IDs** are merchant-entered on signup, password, and join-waitlist-modal.
