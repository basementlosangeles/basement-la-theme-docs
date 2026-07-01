# Editing the Cart (Slide-Out)

<span class="bla-badge">Cart</span>

**What it changes:** The slide-out cart panel — the free-shipping progress bar text
and colors, cart recommendations, discount badges, empty-cart message, and the
checkout helper text.

**Where to find it:** Shopify Admin → Online Store → Themes → Customize → click
**Cart Sidebar** in the left sidebar (it appears on every page).

## Quick preview

<!-- TODO: record a 5-10s GIF of this click-path, save to docs/assets/gifs/cart-sidebar.gif, then uncomment the line below -->
<!-- ![Editing the cart sidebar](../assets/gifs/cart-sidebar.gif) -->

## Steps

<div class="bla-step" markdown>
<span class="bla-step__num">01</span>
<span class="bla-step__body">Select the **Cart Sidebar** section. To see it while editing, temporarily tick **Show Cart Sidebar**.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">02</span>
<span class="bla-step__body">Choose a **Recommendation Collection** and set the **Max Recommendation Amount** (use `-1` for unlimited).</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">03</span>
<span class="bla-step__body">Edit the **Free Shipping Bar** text and colors, plus the **Empty Cart** message and buttons.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">04</span>
<span class="bla-step__body">**Untick Show Cart Sidebar** again, then click **Save**.</span>
</div>

!!! warning "Turn the preview toggles back off"
    **Show Cart Sidebar** and **Show Cart with Products View** are for previewing only.
    Leave both **disabled** before saving for production, or shoppers will see the cart
    forced open.

!!! note "Free shipping amount lives elsewhere"
    The dollar amount that unlocks free shipping is set in **Theme settings → Free
    Shipping**, and must match your actual free-shipping discount in Shopify.
