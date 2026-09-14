---
id: ui-ux.visual.design-system-kit
name: Design System Kit
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Random hex and eyeballed pixels don't scale. A token system does.
triggers:
- designing or building design system kit components
- reviewing UX/UI for design system kit
- implementing visual pattern for design system kit
- random hex and eyeballed pixels don't scale
tags:
- ui
- ux
- visual
- design
- system
- kit
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/design-system-kit
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Design System Kit

> Random hex and eyeballed pixels don't scale. A token system does.

## When to Use (Triggers)

- designing or building design system kit components
- reviewing UX/UI for design system kit
- implementing visual pattern for design system kit
- random hex and eyeballed pixels don't scale

## Key Insights & Principles

- Swap hardcoded hex forsemantic tokenslikevar(--brand)orvar(--error). Intent survives every redesign, and a single rename updates the whole app.
- Build anumbered color scale(100–900) so every shade is systematic instead of a lucky guess, then map it to semantic names such as brand, success, and error.
- Define atype scalewith fixed sizes and weights. Same size and weight everywhere means no hierarchy; a real scale separates heading from body at a glance.
- Base spacing on a4px scale— space-1=4 up to space-16=64. Random gaps like 7px, 23px, or 11px read as sloppy, while scale-based gaps feel deliberate.
- Standardize components asvariants, sizes, and states: primary/secondary/ghost/destructive buttons, small/medium/large sizing, and default/focus/error/disabled inputs.
- Matchmotion to intent— ease-out to enter, ease-in-out to move, ease-in to exit — and keep a duration scale from 100ms micro-interactions to 500ms complex transitions.

## Do's and Don'ts

- **Do:** Store every value as a named token so color, type, and spacing stay consistent across the app
- **Do:** Build numbered scales (color 100–900, spacing 4→64) so choices are systematic, not improvised
- **Do:** Tie easing and duration to the interaction's intent — entering, moving, or leaving
- **Don't:** Hardcode raw hex or pixel values inline
- **Don't:** Pick spacing by eye, 7px here and 23px there
- **Don't:** Give every text the same size and weight, killing all hierarchy

## Code & Selectors

```css
var(--brand)
```

```css
var(--error)
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/design-system-kit.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/design-system-kit.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/design-system-kit)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
