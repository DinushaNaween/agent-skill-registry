---
id: ui-ux.motion.scroll-driven-animations
name: Scroll-Driven Animations
version: 1.0.0
domain: ui-ux
subdomain: motion
summary: 'Same scroll: one feels dead, the other comes alive. Pure CSS, zero JavaScript.'
triggers:
- designing or building scroll-driven animations components
- reviewing UX/UI for scroll-driven animations
- implementing motion pattern for scroll-driven animations
- 'same scroll: one feels dead, the other comes alive'
tags:
- ui
- ux
- motion
- scroll
- driven
- animations
priority: medium
dependencies: []
related_skills:
- ui-ux.motion.animation-timing
- ui-ux.motion.easing-curves
- ui-ux.motion.card-hover-anatomy
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-04-12'
---

# Scroll-Driven Animations

> Same scroll: one feels dead, the other comes alive. Pure CSS, zero JavaScript.

## When to Use (Triggers)

- designing or building scroll-driven animations components
- reviewing UX/UI for scroll-driven animations
- implementing motion pattern for scroll-driven animations
- same scroll: one feels dead, the other comes alive

## Key Insights & Principles

- animation-timeline: scroll()turns the scrollbar itself into an animation controller — no JavaScript, no IntersectionObserver, just two lines of CSS.
- animation-rangesets the exact trigger point, so an animation can fire on entry, on exit, or anywhere in between the scroll.
- view()targets individual elements — each card or image animates the moment it enters the viewport, entirely on autopilot.
- Parallax that once took ~30 lines of JS and a scroll-event listener is now pure CSS: give layersdifferent speedswith zero dependencies.
- Layer these on top ofposition: stickyto build shrinking headers, reading-progress bars, and sidebars that transform as you scroll.

## Do's and Don'ts

- **Do:** Reach foranimation-timeline: scroll()andview()to tie motion to scroll position natively.
- **Do:** Combine sticky positioning with a scroll timeline for shrinking headers and reading-progress bars.
- **Don't:** Hand-roll parallax or reveals with a scroll listener andgetBoundingClientRect()that CSS now drives on its own.
- **Don't:** Pull in a JS animation library for effects the browser handles in a couple of CSS lines.

## Code & Selectors

```css
animation-timeline: scroll()
```

```css
animation-range
```

```css
view()
```

```css
position: sticky
```

```css
getBoundingClientRect()
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.motion.animation-timing`
- `ui-ux.motion.easing-curves`
- `ui-ux.motion.card-hover-anatomy`
