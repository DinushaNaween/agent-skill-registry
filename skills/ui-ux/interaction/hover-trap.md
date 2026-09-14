---
id: ui-ux.interaction.hover-trap
name: Hover Trap
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Hover works on your laptop but is dead on mobile.
triggers:
- designing or building hover trap components
- reviewing UX/UI for hover trap
- implementing interaction pattern for hover trap
- hover works on your laptop but is dead on mobile
tags:
- ui
- ux
- interaction
- hover
- trap
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/hover-trap
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-08-05'
---

# Hover Trap

> Hover works on your laptop but is dead on mobile.

## When to Use (Triggers)

- designing or building hover trap components
- reviewing UX/UI for hover trap
- implementing interaction pattern for hover trap
- hover works on your laptop but is dead on mobile

## Key Insights & Principles

- Touch has no hover, so the browser fakes one: the first tap is spent becoming asticky hoverthat freezes the revealed actions in place until the user taps somewhere else.
- Never bury aprimary actionbehind hover. Hover should surface extras only, never something the user cannot otherwise reach.
- Give hover-only actions a touch-reachable home: put themin the card, behind aswipe, or inside abottom sheet.
- Gate hover styles with@media (hover: hover)instead of sniffing the user agent, so a tablet with a mouse still gets the full treatment.
- Pair it withpointer: coarseto grow controls when the pointer is a thumb rather than a mouse.
- A 20px icon passes design review but misses the thumb. Pad the hit area to44pxand keep the glyph small.

## Do's and Don'ts

- **Do:** Reveal only secondary extras on hover, keeping every primary action reachable by tap
- **Do:** Gate hover effects behind@media (hover: hover)so pointer capability decides, not device type
- **Do:** Pad tap targets to 44px while keeping the visible icon around 20px
- **Don't:** Hide primary actions behind a hover state that touch users can never trigger
- **Don't:** Detect touch by sniffing the user agent instead of querying the pointer
- **Don't:** Size the tap target to the 20px icon and leave the thumb missing

## Code & Selectors

```css
@media (hover: hover)
```

```css
pointer: coarse
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/hover-trap.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/hover-trap.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/hover-trap)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
