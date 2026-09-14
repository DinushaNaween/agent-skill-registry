---
id: ui-ux.interaction.tooltip-design
name: Tooltip Design
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Your tooltip is annoying. Five rules that make it feel premium.
triggers:
- designing or building tooltip design components
- reviewing UX/UI for tooltip design
- implementing interaction pattern for tooltip design
- your tooltip is annoying
tags:
- ui
- ux
- interaction
- tooltip
- design
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/tooltip-design
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Tooltip Design

> Your tooltip is annoying. Five rules that make it feel premium.

## When to Use (Triggers)

- designing or building tooltip design components
- reviewing UX/UI for tooltip design
- implementing interaction pattern for tooltip design
- your tooltip is annoying

## Key Insights & Principles

- Add a300ms delaybefore a hover tooltip appears, so it doesn't fire on every accidental cursor graze across the trigger.
- Anchor the tooltip to its trigger with anarrow. Without one, a floating label sitting above a row of icons leaves users guessing which element it actually describes.
- Flipthe tooltip to the opposite side when the trigger sits near a viewport edge — otherwise it gets clipped off-screen instead of staying readable.
- Make itdismissible everywhere: mouse leave, the Escape key, focus out (blur), and a tap outside should all close it. Every escape route matters.
- Keep the copytight— cap the width around300pxand hold it to one sentence. If you need a documentation paragraph, it's not a tooltip anymore.

## Do's and Don'ts

- **Do:** Wait ~300ms before revealing a hover tooltip
- **Do:** Point at the trigger with an arrow so the reference is unambiguous
- **Do:** Flip position near viewport edges to prevent clipping
- **Don't:** Fire instantly on every cursor graze
- **Don't:** Cram multi-line, documentation-length text into a single tooltip
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/tooltip-design.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/tooltip-design.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/tooltip-design)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
