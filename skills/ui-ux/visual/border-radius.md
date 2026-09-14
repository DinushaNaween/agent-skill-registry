---
id: ui-ux.visual.border-radius
name: Border Radius
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Same card. One looks off, one looks expensive. The gap is one CSS rule.
triggers:
- designing or building border radius components
- reviewing UX/UI for border radius
- implementing visual pattern for border radius
- same card
tags:
- ui
- ux
- visual
- border
- radius
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-03-24'
---

# Border Radius

> Same card. One looks off, one looks expensive. The gap is one CSS rule.

## When to Use (Triggers)

- designing or building border radius components
- reviewing UX/UI for border radius
- implementing visual pattern for border radius
- same card

## Key Insights & Principles

- Nested corners follow math:inner radius = outer radius − padding. When the concentric curves line up, a card reads as intentional instead of "off."
- Pull every value from oneradius scale(4 · 8 · 12 · 16 · 24) instead of picking numbers per component — consistency is what makes UI look expensive.
- Scale radius with element size: tooltips ~4px, inputs ~8px, cards ~12px, modals ~16px, panels ~24px. Bigger surfaces earn bigger corners.
- Radius carries personality —small/sharp reads corporate,large/round reads friendly. Pick the range that matches your brand's tone.
- The difference is subtle but felt: off-scale, mismatched corners are exactly what separates "something's wrong here" from polished.

## Do's and Don'ts

- **Do:** Derive the inner radius from the outer radius minus padding so nested corners stay concentric.
- **Do:** Commit to a single radius scale and reuse it across every component.
- **Do:** Scale radius with element size — larger surfaces get larger corners.
- **Don't:** Pick radius values at random for each component.
- **Don't:** Nest a rounded card inside another without adjusting the inner corner.
- **Don't:** Mix a playful, oversized radius into a brand meant to feel serious — or the reverse.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
