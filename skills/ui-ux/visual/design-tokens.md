---
id: ui-ux.visual.design-tokens
name: Design Tokens
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: 47 changes, or just one. Design tokens change everything.
triggers:
- designing or building design tokens components
- reviewing UX/UI for design tokens
- implementing visual pattern for design tokens
- 47 changes, or just one
tags:
- ui
- ux
- visual
- design
- tokens
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/design-tokens
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-04-07'
---

# Design Tokens

> 47 changes, or just one. Design tokens change everything.

## When to Use (Triggers)

- designing or building design tokens components
- reviewing UX/UI for design tokens
- implementing visual pattern for design tokens
- 47 changes, or just one

## Key Insights & Principles

- Name tokens bymeaning, not value.color-primarysurvives a rebrand, whilecolor-blue-500becomes a lie the moment blue turns teal.
- Structure tokens inthree layers— primitives (raw values), semantic (meaning), and component (usage) — each referencing the layer above.
- Change one primitive and itcascadesthrough every component that points to it: one edit instead of 47 hunted-down values.
- Define ascaleand snap everything to it. A stray 13px padding or 17px gap collapses to 12 and 16, so consistency stops being a guess.
- Dark mode isn't inverting colors — it'sswapping one token set for another. Same components, alias tokens, a completely different feel.
- Tokens are yoursingle source of truthfor color, spacing, and type — the design system is only as strong as they are.

## Do's and Don'ts

- **Do:** Name tokens by role —color-primary,spacing-md,font-body— so they hold through a rebrand
- **Do:** Layer tokens primitives → semantic → component so a single change cascades
- **Do:** Snap arbitrary spacing and font sizes onto a fixed scale
- **Don't:** Bake literal values into names likecolor-blue-500orspacing-16
- **Don't:** Treat dark mode as inverting colors instead of swapping token sets
- **Don't:** Hardcode raw values across components instead of referencing tokens

## Code & Selectors

```css
color-primary
```

```css
color-blue-500
```

```css
spacing-md
```

```css
font-body
```

```css
spacing-16
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/design-tokens.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/design-tokens.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/design-tokens)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
