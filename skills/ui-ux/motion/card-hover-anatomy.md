---
id: ui-ux.motion.card-hover-anatomy
name: Card Hover Anatomy
version: 1.0.0
domain: ui-ux
subdomain: motion
summary: Same card. One feels alive, three stay dead. Four rules separate them.
triggers:
- designing or building card hover anatomy components
- reviewing UX/UI for card hover anatomy
- implementing motion pattern for card hover anatomy
- same card
tags:
- ui
- ux
- motion
- card
- hover
- anatomy
priority: medium
dependencies: []
related_skills:
- ui-ux.motion.animation-timing
- ui-ux.motion.easing-curves
- ui-ux.motion.scroll-driven-animations
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/card-hover-anatomy
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-05-16'
---

# Card Hover Anatomy

> Same card. One feels alive, three stay dead. Four rules separate them.

## When to Use (Triggers)

- designing or building card hover anatomy components
- reviewing UX/UI for card hover anatomy
- implementing motion pattern for card hover anatomy
- same card

## Key Insights & Principles

- Lift with weight:raise the card ~8px on hover and stretch its shadow with it over ~200ms ease-out. Faster reads as twitchy, slower feels stuck.
- Claim the cursor:a pulsing accent border or a gradient sweep around the edge stops the card looking flat and signals it's interactive.
- Cascade the actions:reveal hidden buttons (favorite, cart, share) staggered ~60ms apart, anchored at the bottom. A reveal adds an affordance, not a new layout.
- Push against the glass:scale the image to ~1.05inside anoverflow-hiddenframe while the container stays fixed — the product presses outward instead of resizing the card.
- The trap — keep the geometry:never scale the whole card. That shifts neighbors and breaks the grid. Animate the content, hold the footprint.

## Do's and Don'ts

- **Do:** Lift the card ~8px and grow its shadow together, using ~200ms ease-out for a sense of weight.
- **Do:** Stagger revealed actions ~60ms apart and anchor them to the card's bottom edge.
- **Do:** Scale the image to ~1.05 inside an overflow-hidden frame while the container holds still.
- **Don't:** Scale the entire card — it shifts neighboring cards and breaks the grid layout.
- **Don't:** Stack action buttons over the title or let them spill outside the card boundary.
- **Don't:** Time the lift too fast (twitchy) or too slow (stuck) — 200ms is the sweet spot.

## Code & Selectors

```css
overflow-hidden
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/card-hover-anatomy.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/card-hover-anatomy.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/card-hover-anatomy)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.motion.animation-timing`
- `ui-ux.motion.easing-curves`
- `ui-ux.motion.scroll-driven-animations`
