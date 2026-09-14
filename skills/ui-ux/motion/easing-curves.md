---
id: ui-ux.motion.easing-curves
name: Easing Curves
version: 1.0.0
domain: ui-ux
subdomain: motion
summary: 'Same distance, different feel: the easing curve is what decides how motion reads.'
triggers:
- designing or building easing curves components
- reviewing UX/UI for easing curves
- implementing motion pattern for easing curves
tags:
- ui
- ux
- motion
- easing
- curves
priority: medium
dependencies: []
related_skills:
- ui-ux.motion.animation-timing
- ui-ux.motion.card-hover-anatomy
- ui-ux.motion.scroll-driven-animations
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/easing-curves
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Easing Curves

> Same distance, different feel: the easing curve is what decides how motion reads.

## When to Use (Triggers)

- designing or building easing curves components
- reviewing UX/UI for easing curves
- implementing motion pattern for easing curves

## Key Insights & Principles

- An easing curve maps how a value changes over time. Keep the same distance and duration but swap the curve, and the motionfeelscompletely different — that shape is what your eye actually reads.
- Linearmoves at a constant speed. It looks mechanical and cheap, so reserve it for continuous motion like spinners or marquees — never for UI that starts and stops.
- Ease-outstarts fast then decelerates into place. It's the safest default for elements entering the screen because it mirrors how real objects settle.
- Springovershoots slightly then settles, adding a bounce that reads as alive and premium — ideal for button presses, modals, and playful confirmations.
- Apply the same handful of curves everywhere: button press, card cascade, sheet open. Consistent easing is a big part of why an interface feels coherent instead of stitched together.
- Stagger list and card entrances a few frames apart so they cascade in, rather than snapping onto the screen as one rigid block.

## Do's and Don'ts

- **Do:** Default to ease-out for elements entering the screen so they decelerate naturally into place.
- **Do:** Add a subtle spring overshoot to presses, modals, and confirmations to make the UI feel alive.
- **Do:** Stagger card and list entrances a few frames apart for a cascade instead of a single hard snap.
- **Don't:** Reach for linear easing on UI that starts and stops — it reads as mechanical and cheap.
- **Don't:** Push spring stiffness or bounce so high the element wobbles; a little overshoot sells premium, too much feels broken.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/easing-curves.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/easing-curves.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/easing-curves)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.motion.animation-timing`
- `ui-ux.motion.card-hover-anatomy`
- `ui-ux.motion.scroll-driven-animations`
