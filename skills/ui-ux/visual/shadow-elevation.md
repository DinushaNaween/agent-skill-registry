---
id: ui-ux.visual.shadow-elevation
name: Shadow Elevation
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Shadows aren't decoration. They encode hierarchy and depth.
triggers:
- designing or building shadow elevation components
- reviewing UX/UI for shadow elevation
- implementing visual pattern for shadow elevation
- shadows aren't decoration
tags:
- ui
- ux
- visual
- shadow
- elevation
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Shadow Elevation

> Shadows aren't decoration. They encode hierarchy and depth.

## When to Use (Triggers)

- designing or building shadow elevation components
- reviewing UX/UI for shadow elevation
- implementing visual pattern for shadow elevation
- shadows aren't decoration

## Key Insights & Principles

- Real depth comes fromstacking multiple shadows, not one blur: a tightcontact shadow, a mid-distance shadow, and a wide soft spread shadow layered together.
- The tight contact shadow (~0 1px 3px) anchors the element to the surface — it's what makes the card feel physically placed rather than floating.
- A subtlecolored glow(a low-opacity blur in an accent hue) adds a premium, branded feel that plain black shadows can't.
- Match the glow color to theproduct context— purple for creative tools, blue for fintech, green for health — so elevation reinforces brand identity.
- A3D lift(perspective + a small rotateX + translateZ) adds genuine depth beyond a flat drop shadow, making the surface read as tilted toward the viewer.
- Elevation is a hierarchy signal: the more elevated an element, the more important it reads — which is why a premium tier looks lifted while a basic one stays flat.

## Do's and Don'ts

- **Do:** Layer three shadows — tight contact, mid-distance, and wide soft spread — for believable depth.
- **Do:** Tint the glow to your brand accent so elevation reinforces identity.
- **Do:** Reserve the strongest elevation for the elements that matter most.
- **Don't:** Rely on a single flat drop shadow for every surface.
- **Don't:** Treat shadows as decoration — they communicate depth and hierarchy.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
