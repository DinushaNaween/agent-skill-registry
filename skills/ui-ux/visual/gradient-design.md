---
id: ui-ux.visual.gradient-design
name: Gradient Design
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Why your gradients look cheap
triggers:
- designing or building gradient design components
- reviewing UX/UI for gradient design
- implementing visual pattern for gradient design
- why your gradients look cheap
tags:
- ui
- ux
- visual
- gradient
- design
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-22'
---

# Gradient Design

> Why your gradients look cheap

## When to Use (Triggers)

- designing or building gradient design components
- reviewing UX/UI for gradient design
- implementing visual pattern for gradient design
- why your gradients look cheap

## Key Insights & Principles

- Cheap-looking gradients usually travel too far across the hue wheel. Neighboring hues (teal → cyan) blend cleanly; opposites (orange → blue) create a muddy gray dead zone in the middle.
- Keep lightness moving in one direction. A gradient that gets darker, then lighter, then darker again reads as banding.
- Gradients work best as ambiance, not surface: a soft radial glow behind content beats a full-bleed linear wash on top of it.
- Subtle grain on top of a gradient hides banding on cheap displays and adds perceived texture.

## Do's and Don'ts

- **Do:** stay within 60° of hue travel, add 2–3% noise, and test on a low-quality screen.
- **Don't:** put body text directly on a gradient's mid-transition zone — contrast is unpredictable there.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
