# Developer Docs

Technical reference for the Basement LA Shopify theme. This theme is built from
scratch — no Dawn or other base theme — using Liquid, CSS, and vanilla JS.

This section assumes familiarity with Shopify theme development. It documents
**how things are built and why**, not how to use the admin (see the
[Merchant Guide](../merchant-guide/index.md) for that).

## Pages

| Page | Covers |
|---|---|
| [Theme Architecture](architecture.md) | Folder structure, section/snippet conventions, schema patterns |
| **Sections** (nav group) | One page per section — schema settings, metafield dependencies, snippets rendered, and where each is used |
| _Metafields & Metaobjects_ | *(add)* Namespace/key reference, Storefront access notes. **Note:** the current theme uses product **metafields** only (`custom` namespace); no metaobjects are referenced — see individual section pages |
| _JS Modules_ | *(add)* How JS is organized, what's modularized vs not |
| _Build & Deploy_ | *(add)* Shopify CLI workflow, theme environments, deploy process |

The **Sections** group in the left nav has a page for every section that ships a
`{% schema %}` block. Start points worth knowing:

- [Collection](collection.md) — also powers the homepage grid; has the in-grid `product-banner` block.
- [Product](product.md) — the heaviest metafield consumer (`color_label`, `color_value`, `size_chart`).
- [Cart Sidebar](cart-sidebar.md) — global, re-renders via the Section Rendering API.
- Flagged as legacy/unassigned: [Homepage](homepage.md), [Policy Page](policy-page.md).

!!! note "Source of truth"
    Code is the source of truth — this page explains intent and reasoning, but if
    it ever conflicts with the actual codebase, the codebase wins. Update this page
    in the same PR that changes the relevant code.

## Refactor / audit tracking

Findings from codebase audits (severity-ranked technical debt, dead code, etc.)
should live here once generated, so the reasoning behind structural changes is
documented alongside the architecture itself.
