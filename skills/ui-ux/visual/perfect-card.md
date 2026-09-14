---
id: ui-ux.visual.perfect-card
name: Perfect Card
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: One card looks free. The other costs $1000. Four CSS changes.
triggers:
- designing or building perfect card components
- reviewing UX/UI for perfect card
- implementing visual pattern for perfect card
- one card looks free
tags:
- ui
- ux
- visual
- perfect
- card
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-03-15'
---

# Perfect Card

> One card looks free. The other costs $1000. Four CSS changes.

## When to Use (Triggers)

- designing or building perfect card components
- reviewing UX/UI for perfect card
- implementing visual pattern for perfect card
- one card looks free

## Key Insights & Principles

- Paddingis the biggest tell: going from a cramped 12px to40pxwith a24pxborder-radius instantly reads as intentional instead of cheap.
- Build a realtype hierarchy— push the title to 600 weight and ~38px, then shrink the body and drop it to55% opacityso the eye lands on the title first.
- Stacktwo shadowsfor believable depth: a tight, darker one for contrast plus a wide, soft one for ambient elevation.
- Add ahairline borderat roughly 12% opacity to define the card's edge against a dark background.
- Ahover state— lift the card ~8px, scale to 1.02, and deepen the shadow — signals it's clickable and adds the final layer of polish.
- Same content,four changes: spacing, typography, shadows, and hover are the entire gap between a card that looks free and one that looks premium.

## Do's and Don'ts

- **Do:** Layer a tight shadow for contrast with a soft ambient one for depth, plus a subtle border around 12% opacity.
- **Do:** Set the description to ~55% opacity so the title clearly wins the hierarchy.
- **Do:** Give the card a hover lift (~8px up, slight scale, deeper shadow) so it feels interactive.
- **Don't:** Cram content against the edges with tiny padding and near-zero border-radius — it reads as an unstyled default.
- **Don't:** Give the title and body the same weight and full opacity, so nothing guides the eye.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
