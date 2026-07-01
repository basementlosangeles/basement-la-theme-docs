# Setting Up "Buy Together & Save"

<span class="bla-badge">Product</span>

**What it changes:** The "Buy Any and Get Additional X% Off" cross-sell row on product
pages — its title, the collection of products it pulls from, and the discount it
applies.

**Where to find it:** This section is controlled almost entirely from **Theme
Settings**, not the section itself. Shopify Admin → Online Store → Themes → Customize
→ click the **gear / Theme settings** icon at the bottom of the left sidebar →
**Buy Together Products**.

## Quick preview

<!-- TODO: record a 5-10s GIF of this click-path, save to docs/assets/gifs/buy-together.gif, then uncomment the line below -->
<!-- ![Setting up buy together and save](../assets/gifs/buy-together.gif) -->

## Steps

<div class="bla-step" markdown>
<span class="bla-step__num">01</span>
<span class="bla-step__body">Open **Theme settings → Buy Together Products**.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">02</span>
<span class="bla-step__body">Set the **Buy Together Title** and choose the **Buy Together Collection** (the pool of eligible products).</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">03</span>
<span class="bla-step__body">Enter the **Discount Code** and **Discount Amount (%)** so they match a real Shopify discount.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">04</span>
<span class="bla-step__body">Click **Save**.</span>
</div>

!!! warning "Match the actual discount"
    The **Discount Code** must equal the discount's **Title** in Shopify Admin →
    Discounts, and the **Discount Amount (%)** must equal its percentage. If they
    don't match, the cart total won't apply the savings the product page promises.

!!! note "Per-product featured items"
    Which specific products appear can also be driven by a product's
    *Buy together & get featured products* metafield. If a product shows the wrong
    items, check its metafields — see the
    [developer notes](../developer-guide/buy-together-products-section.md).
