# Developer Docs

Technical reference for the Basement LA Shopify theme. This theme is built from
scratch — no Dawn or other base theme — using Liquid, SCSS, and vanilla JS.

This section assumes familiarity with Shopify theme development. It documents
**how things are built and why**, not how to use the admin (see the
[Merchant Guide](../merchant-guide/index.md) for that).

## Pages

| Page | Covers |
|---|---|
| [Theme Architecture](architecture.md) | Folder structure, section/snippet conventions, schema patterns |
| _Sections & Snippets_ | *(add)* Full inventory of sections, what each renders, `include` vs `render` usage |
| _Metafields & Metaobjects_ | *(add)* Namespace/key reference, metaobject reference pattern, Storefront access notes |
| _JS Modules_ | *(add)* How JS is organized, what's modularized vs not |
| _Build & Deploy_ | *(add)* Shopify CLI workflow, theme environments, deploy process |

!!! note "Source of truth"
    Code is the source of truth — this page explains intent and reasoning, but if
    it ever conflicts with the actual codebase, the codebase wins. Update this page
    in the same PR that changes the relevant code.

## Refactor / audit tracking

Findings from codebase audits (severity-ranked technical debt, dead code, etc.)
should live here once generated, so the reasoning behind structural changes is
documented alongside the architecture itself.
