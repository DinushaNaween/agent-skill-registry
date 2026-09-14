---
id: ui-ux.motion.animation-timing
name: Animation Timing
version: 1.0.0
domain: ui-ux
subdomain: motion
summary: 'Same modal, two timings: one feels premium, one feels broken. It''s all milliseconds.'
triggers:
- designing or building animation timing components
- reviewing UX/UI for animation timing
- implementing motion pattern for animation timing
- 'same modal, two timings: one feels premium, one feels broken'
tags:
- ui
- ux
- motion
- animation
- timing
priority: medium
dependencies: []
related_skills:
- ui-ux.motion.easing-curves
- ui-ux.motion.card-hover-anatomy
- ui-ux.motion.scroll-driven-animations
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/animation-timing
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Animation Timing

> Same modal, two timings: one feels premium, one feels broken. It's all milliseconds.

## When to Use (Triggers)

- designing or building animation timing components
- reviewing UX/UI for animation timing
- implementing motion pattern for animation timing
- same modal, two timings: one feels premium, one feels broken

## Key Insights & Principles

- Entrancesland best at 200–300ms with a cubic ease-out — fast enough to feel responsive, slow enough to read as deliberate.
- Exitsshould be faster than entrances: pair a 250ms entrance with a ~150ms exit so dismissals feel snappy instead of dragging.
- Feedbackon taps and button presses must fire in under 100ms — anything slower reads as lag, even when the action itself is instant.
- Attention-grabbing motion like notifications can run longer, 500–800ms, and use a bounce or overshoot to pull the eye.
- Staggerlist items about 50ms apart — 30ms blurs them into one blob, 100ms makes the whole list crawl in.
- Match the easing curve to intent: ease-out for entrances, and reserve springs and bounce for moments that genuinely need attention.

## Do's and Don'ts

- **Do:** Use ease-out curves for entrances so motion decelerates into place
- **Do:** Make exits roughly 40% faster than their entrance so dismissals feel instant
- **Do:** Keep tap and press feedback under 100ms so the interface feels alive
- **Don't:** Stretch entrances past ~300ms — they start to feel sluggish and in the way
- **Don't:** Use symmetric in/out timing — a matched-length exit feels like the UI is dragging
- **Don't:** Reach for linear easing on entrances — it reads mechanical and cheap
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/animation-timing.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/animation-timing.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/animation-timing)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.motion.easing-curves`
- `ui-ux.motion.card-hover-anatomy`
- `ui-ux.motion.scroll-driven-animations`
