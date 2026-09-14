---
id: ui-ux.visual.reverse-engineered-linear
name: Reverse-Engineered Linear
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Why does Linear feel expensive? Five decisions. None need a designer.
triggers:
- designing or building reverse-engineered linear components
- reviewing UX/UI for reverse-engineered linear
- implementing visual pattern for reverse-engineered linear
- why does linear feel expensive? five decisions
tags:
- ui
- ux
- visual
- reverse
- engineered
- linear
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.charts-that-lie
- ui-ux.visual.design-system-kit
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/reverse-engineered-linear
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-09-07'
---

# Reverse-Engineered Linear

> Why does Linear feel expensive? Five decisions. None need a designer.

## When to Use (Triggers)

- designing or building reverse-engineered linear components
- reviewing UX/UI for reverse-engineered linear
- implementing visual pattern for reverse-engineered linear
- why does linear feel expensive? five decisions

## Key Insights & Principles

- Density reads as competence.13px text, 32px rows, letter spacing pulled in by 1%. The same viewport shows 14 issues instead of 8, with no scroll.
- Depth comes from value, not blur.Kill the shadows and stack three background values (base, surface, raised surface) separated by a 1px border at 8% white. Hover changes the surface value, not the elevation. Flat surfaces look engineered, shadows look decorated.
- One color, used twice.Indigo on the selected row and the primary button, nowhere else. Status is a grey icon, not a colored pill. Seven colors collapse to one and the UI instantly looks deliberate.
- Every action shows its shortcut.C creates, Cmd K searches. Hover feedback lands in about 80ms and transitions stay under 150ms, with no bounce or overshoot. The UI answers before you finish the gesture.
- A 4px grid does the rest.16px icons centered on the text line, labels left, numbers and dates right, nothing centered. Alignment is invisible when right and loud when wrong.

## Do's and Don'ts

- **Do:** Build depth from three stacked background values plus a hairline border (rgba white at 8%), and change the surface value on hover.
- **Do:** Print the keyboard shortcut next to every action, and keep hover feedback near 80ms with transitions under 150ms.
- **Do:** Left-align labels and ids, right-align numbers and dates, and center icons on the text line using a 4px grid.
- **Don't:** Use drop shadows to separate rows, panels, or the sidebar.
- **Don't:** Encode status or priority with colored pills when a grey icon says the same thing.
- **Don't:** Let transitions bounce, overshoot, or drag past 150ms.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/reverse-engineered-linear.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/reverse-engineered-linear.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/reverse-engineered-linear)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.charts-that-lie`
- `ui-ux.visual.design-system-kit`
