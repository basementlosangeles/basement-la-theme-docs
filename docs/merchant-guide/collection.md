# Editing Collection Pages (Product Grid)

<span class="bla-badge">Collection</span>

**What it changes:** The product grid on collection pages (and the homepage grid) —
number of columns, the filter bar, "New"/"Sold Out" badges, and in-grid promo banners.

**Where to find it:** Shopify Admin → Online Store → Themes → Customize → switch the
template to a **Collection** page → click the **Collection** section.

## Quick preview

<!-- TODO: record a 5-10s GIF of this click-path, save to docs/assets/gifs/collection.gif, then uncomment the line below -->
<!-- ![Editing collection pages](../assets/gifs/collection.gif) -->

## Steps

<div class="bla-step" markdown>
<span class="bla-step__num">01</span>
<span class="bla-step__body">Select the **Collection** section and set **Default Desktop Grid Columns** (2–10).</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">02</span>
<span class="bla-step__body">To override columns for one specific collection, add a **Collection Grid Columns** block, pick the collection, and set its column count.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">03</span>
<span class="bla-step__body">To place a promo image in the grid, add a **Product Banner** block: choose the collection, set **Insert After Product #** (use `10000` for the end), pick the image, and adjust focal point/zoom.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">04</span>
<span class="bla-step__body">Adjust the **New Badge** and **Sold Out** colors as needed, then click **Save**.</span>
</div>

!!! note "This also controls the homepage grid"
    The same Collection section builds the product grid on the homepage. Changes to
    grid behavior can affect both — check the homepage after editing.
