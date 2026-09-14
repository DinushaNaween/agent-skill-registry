---
id: ui-ux.interaction.color-picker-ux
name: Color Picker UX
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Pick a color. Your whole UI answers.
triggers:
- designing or building color picker ux components
- reviewing UX/UI for color picker ux
- implementing interaction pattern for color picker ux
- pick a color
tags:
- ui
- ux
- interaction
- color
- picker
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/color-picker-ux
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-06-10'
---

# Color Picker UX

> Pick a color. Your whole UI answers.

## When to Use (Triggers)

- designing or building color picker ux components
- reviewing UX/UI for color picker ux
- implementing interaction pattern for color picker ux
- pick a color

## Key Insights & Principles

- Treat the picker as a decision tool, not a gradient with a slider — every choice cascades into the rest of the UI.
- OfferOKLCHnext to hex. Hex is for machines; OKLCH's lightness, chroma, and hue let you change one number and get a predictable shade.
- Give the pickermemory: recent swatches and saved palettes put your last five picks one tap away instead of re-hunting each time.
- Show alive contrast ratioat pick time, not in review — a badge that flips red to green kills failing pairs before they ship.
- Previewalpha over a checkerboardon both light and dark backgrounds. Transparency lies on a white canvas, so check it before you commit.
- Turn one pick into a system:generate tints and shadesfrom a single hue to produce ten tokens from one decision.

## Do's and Don'ts

- **Do:** Expose human-readable formats like OKLCH so one value maps to a predictable shade
- **Do:** Surface recent swatches and saved palettes so past picks stay one tap away
- **Do:** Validate contrast live while picking, with a badge that reads red or green
- **Don't:** Preview alpha only on white — a checkerboard reveals the true transparency
- **Don't:** Ship a bare gradient-and-slider picker with no memory, contrast check, or palette output
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/color-picker-ux.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/color-picker-ux.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/color-picker-ux)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
