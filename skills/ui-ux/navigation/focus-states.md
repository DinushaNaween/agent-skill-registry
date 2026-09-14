---
id: ui-ux.navigation.focus-states
name: Focus States
version: 1.0.0
domain: ui-ux
subdomain: navigation
summary: Press Tab. Where did the focus go?
triggers:
- designing or building focus states components
- reviewing UX/UI for focus states
- implementing navigation pattern for focus states
- press tab
tags:
- ui
- ux
- navigation
- focus
- states
priority: medium
dependencies: []
related_skills:
- ui-ux.navigation.navigation-patterns
- ui-ux.navigation.tabs-system
- ui-ux.navigation.pagination
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/focus-states
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-03'
---

# Focus States

> Press Tab. Where did the focus go?

## When to Use (Triggers)

- designing or building focus states components
- reviewing UX/UI for focus states
- implementing navigation pattern for focus states
- press tab

## Key Insights & Principles

- outline: noneisn't a style choice — remove the default focus ring and you've shipped an accessibility failure. If you kill it, replace it with something better.
- A proper focus ring needs three things:2pxthickness, a2px offset, and enough contrast to stay visible on both light and dark backgrounds.
- :focus-visibletells mouse and keyboard apart — a click gets no ring, a Tab press gets one — so keyboard users can navigate without cluttering the pointer experience.
- Focus follows theDOM order, not your visual layout. Reorder columns with CSS and Tab starts teleporting across the page — keep visual order and DOM order in sync.
- Inside a modal,trap the focus: Tab should cycle through the dialog and wrap around, andEscapeshould close it and hand focus back to the element that opened it.
- Askip linkjumps past dozens of nav links in a single keypress. Keep it invisible until focused, and make it the first element on the page.

## Do's and Don'ts

- **Do:** Replace a removed outline with a custom ring — 2px thick, offset, and contrasting on every background
- **Do:** Reach for:focus-visibleso keyboard users get a ring while mouse clicks stay clean
- **Do:** Place a skip link as the first focusable element, hidden until focused
- **Don't:** Setoutline: nonewithout shipping a visible replacement
- **Don't:** Reorder content with CSS and let the DOM order drift from the visual order
- **Don't:** Let a modal leak focus to the page behind it, or drop focus when it closes
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/focus-states.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/focus-states.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/focus-states)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.navigation.navigation-patterns`
- `ui-ux.navigation.tabs-system`
- `ui-ux.navigation.pagination`
