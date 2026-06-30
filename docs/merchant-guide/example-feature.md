# Changing the Homepage Banner

<span class="bla-badge">Homepage</span>

**What it changes:** The large image and headline at the top of the homepage.

**Where to find it:** Shopify Admin → Online Store → Themes → Customize →
Homepage → click the **Hero Banner** section in the left sidebar.

## Quick preview

Drop a short (5-10 second), compressed GIF at
`docs/assets/gifs/homepage-banner.gif` and reference it like this:

![Changing the homepage banner](../assets/gifs/homepage-banner.gif)

Keep GIFs under ~5MB — they're checked into the repo, so size adds up over time.
[ezgif.com](https://ezgif.com) or `gifski` work well for compressing screen recordings.

## Full walkthrough (longer video)

For anything that takes more than ~15 seconds to show, upload an **unlisted**
YouTube video (or a Loom link) instead of a GIF, and embed it:

```html
<iframe width="100%" height="400"
  src="https://www.youtube.com/embed/VIDEO_ID_HERE"
  title="Changing the Homepage Banner"
  frameborder="0" allowfullscreen>
</iframe>
```

## Steps

<div class="bla-step" markdown>
<span class="bla-step__num">01</span>
<span class="bla-step__body">Open the theme editor and select the **Hero Banner** section.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">02</span>
<span class="bla-step__body">Click **Image** to upload a new banner image (recommended size: 2400×1200px, &lt;500KB).</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">03</span>
<span class="bla-step__body">Edit the **Heading** and **Subheading** text fields.</span>
</div>

<div class="bla-step" markdown>
<span class="bla-step__num">04</span>
<span class="bla-step__body">Click **Save** in the top right.</span>
</div>

!!! warning "Image size"
    Oversized images here will slow down the homepage. Compress before uploading —
    see the [Developer Docs: Performance](../developer-guide/architecture.md) notes
    on image handling if you want the technical reason why.
