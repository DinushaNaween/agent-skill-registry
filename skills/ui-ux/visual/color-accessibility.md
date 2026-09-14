---
id: ui-ux.visual.color-accessibility
name: Color Accessibility
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: 'Same text, same color: one is invisible. The contrast ratio nobody checks.'
triggers:
- designing or building color accessibility components
- reviewing UX/UI for color accessibility
- implementing visual pattern for color accessibility
- 'same text, same color: one is invisible'
tags:
- ui
- ux
- visual
- color
- accessibility
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/color-accessibility
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-04-03'
---

# Color Accessibility

> Same text, same color: one is invisible. The contrast ratio nobody checks.

## When to Use (Triggers)

- designing or building color accessibility components
- reviewing UX/UI for color accessibility
- implementing visual pattern for color accessibility
- same text, same color: one is invisible

## Key Insights & Principles

- Contrast is aratio, not a color: the exact same off-white (#F0F0F0) reads crisp on a dark panel and disappears on a light one — the background decides legibility.
- Know theWCAG thresholds: aim for4.5:1on body text and3:1on large text. Below 3:1 the text degrades from 'large-only' to flat-out invisible.
- Most failures hide in 'decorative' muted grays — nav links, card labels, and secondary headings routinely sit at 1.5–2:1 and quietly fall below the line.
- Never encode meaning withcolor alone: for the ~8% of users with color vision deficiency, a red error and a green success collapse into the same muddy tone.
- Add asecond signalalongside every color cue — an icon on error text, trend arrows on stats, or textures/patterns in charts — so the message survives when the color doesn't.
- A full pass is cheap: darken or lighten muted text to clear the ratio, then bolt an icon onto each state. Same layout, dramatically more readable.

## Do's and Don'ts

- **Do:** Check every text-on-background pair against WCAG — 4.5:1 for body copy, 3:1 for large text
- **Do:** Pair color with an icon, label, or pattern so state survives color blindness
- **Do:** Lighten or darken 'muted' secondary text until it clears the contrast threshold
- **Don't:** Rely on red-vs-green alone to separate errors from success
- **Don't:** Ship low-contrast grays for nav links and card labels just because they look sleek
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/color-accessibility.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/color-accessibility.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/color-accessibility)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
