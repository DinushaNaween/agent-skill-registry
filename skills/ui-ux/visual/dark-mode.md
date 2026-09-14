---
id: ui-ux.visual.dark-mode
name: Dark Mode
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: Same app, one inverts colors. The other feels premium.
triggers:
- designing or building dark mode components
- reviewing UX/UI for dark mode
- implementing visual pattern for dark mode
- same app, one inverts colors
tags:
- ui
- ux
- visual
- dark
- mode
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/dark-mode
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-03-24'
---

# Dark Mode

> Same app, one inverts colors. The other feels premium.

## When to Use (Triggers)

- designing or building dark mode components
- reviewing UX/UI for dark mode
- implementing visual pattern for dark mode
- same app, one inverts colors

## Key Insights & Principles

- Dark mode isnot black mode. Build on a near-black base like#121212, not pure #000000, so shadows and depth stay visible.
- Signal elevation withlayered surfaces: each step up gets a lighter grey (base → surface → elevated), the way shadows do the job in light mode.
- Desaturate accent colorsby roughly20%. Full-saturation buttons and highlights vibrate and strain the eye against a dark background.
- Never use pure white text.#FFFFFF glares on dark UI — calibrate it down to a soft off-white for comfortable reading.
- Buildtext hierarchy with opacity, not new colors: high-emphasis, medium, and disabled text simply step down in white opacity.

## Do's and Don'ts

- **Do:** Base your darkest layer on a near-black grey like #121212, then lighten each surface as it elevates.
- **Do:** Desaturate accent colors so buttons and highlights sit calmly against the background.
- **Do:** Dim body text to a soft off-white and use opacity tiers to separate emphasis levels.
- **Don't:** Use pure black (#000000) as the background — it flattens elevation and hides shadows.
- **Don't:** Ship fully saturated accent colors — they buzz and read as cheap on dark UI.
- **Don't:** Set text to pure white (#FFFFFF) — the glare fatigues the eyes over time.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/dark-mode.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/dark-mode.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/dark-mode)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
