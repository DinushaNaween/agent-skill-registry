---
id: ui-ux.visual.depth-layers
name: Depth Layers
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: 'Same layout, same colors: three properties turn flat cards into real depth.'
triggers:
- designing or building depth layers components
- reviewing UX/UI for depth layers
- implementing visual pattern for depth layers
- 'same layout, same colors: three properties turn flat cards into real depth'
tags:
- ui
- ux
- visual
- depth
- layers
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-03-10'
---

# Depth Layers

> Same layout, same colors: three properties turn flat cards into real depth.

## When to Use (Triggers)

- designing or building depth layers components
- reviewing UX/UI for depth layers
- implementing visual pattern for depth layers
- same layout, same colors: three properties turn flat cards into real depth

## Key Insights & Principles

- You don't need to redesign to add depth.Same layout, same colors— three CSS properties do the whole job.
- Layered shadowsbeat a single drop shadow: stack a tight one (~2px), a mid spread (~12px), and a large ambient one (~32px) to mimic how real light falls off.
- Parallax scrollsells distance by moving layers at different speeds — background slow, midground medium, foreground fastest (roughly 1x / 2.5x / 5x).
- Z-translation on hovermakes an element react to the cursor: lift it toward the viewer withtranslateZplus a slightscale(1.03)and a soft glow.
- Depth also lives in the border and shadowintensity, not just position — brightening the border on hover reinforces the lift.
- Stack all three techniques and the interface reads as fully dimensional while still feeling flat and clean.

## Do's and Don'ts

- **Do:** Stack multiple shadows at increasing blur and offset instead of one flat drop shadow
- **Do:** Keep hover lifts subtle — a few pixels plus ~3% scale reads as physical, not cartoonish
- **Do:** Vary scroll speed per layer so background, mid, and foreground imply real distance
- **Don't:** Redesign the layout or palette to fake depth when three properties already do it
- **Don't:** Push parallax offsets or hover scale so far they pull attention off the content

## Code & Selectors

```css
translateZ
```

```css
scale(1.03)
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
