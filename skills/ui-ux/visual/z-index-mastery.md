---
id: ui-ux.visual.z-index-mastery
name: Z-Index Mastery
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: 'z-index lies: a bigger number won''t win if the element isn''t positioned.'
triggers:
- designing or building z-index mastery components
- reviewing UX/UI for z-index mastery
- implementing visual pattern for z-index mastery
- 'z-index lies: a bigger number won''t win if the element isn''t positioned'
tags:
- ui
- ux
- visual
- index
- mastery
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

# Z-Index Mastery

> z-index lies: a bigger number won't win if the element isn't positioned.

## When to Use (Triggers)

- designing or building z-index mastery components
- reviewing UX/UI for z-index mastery
- implementing visual pattern for z-index mastery
- z-index lies: a bigger number won't win if the element isn't positioned

## Key Insights & Principles

- z-index needs position.Settingz-index: 9999on aposition: staticelement does nothing — give itposition: relative(or absolute/fixed/sticky) and the layering finally works.
- Every stacking context is its own universe.A child atz-index: 9999can never climb above its parent's siblings — if the parent sits below, the child sits below too, no matter how huge the number.
- Az-index arms race(9999, then 99999) is a symptom, not a fix — the real culprit is almost always an unexpected stacking context somewhere up the tree.
- isolation: isolatespins up a fresh stacking context in one line, so a component's internal layers stop leaking out and z-fighting with the rest of the page.
- Stop guessing at the order —Chrome DevTools' Layers panelrenders the page in 3D so you can see which element actually sits on top.

## Do's and Don'ts

- **Do:** Give an elementposition: relativebefore expectingz-indexto do anything.
- **Do:** Reach forisolation: isolateto contain a component's stacking in one clean line.
- **Do:** Open DevTools' Layers panel to inspect the real 3D stack instead of trial-and-error.
- **Don't:** Escalate toz-index: 9999to force a child above another branch — it can't beat what its parent already lost to.
- **Don't:** Assume a bigger z-index always wins; it only ranks siblings inside the same stacking context.

## Code & Selectors

```css
z-index: 9999
```

```css
position: static
```

```css
position: relative
```

```css
isolation: isolate
```

```css
z-index
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
