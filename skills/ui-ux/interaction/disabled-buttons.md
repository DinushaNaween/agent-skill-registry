---
id: ui-ux.interaction.disabled-buttons
name: Disabled Buttons
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: The button is disabled, and nobody tells you why.
triggers:
- designing or building disabled buttons components
- reviewing UX/UI for disabled buttons
- implementing interaction pattern for disabled buttons
- the button is disabled, and nobody tells you why
tags:
- ui
- ux
- interaction
- disabled
- buttons
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.hover-trap
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/disabled-buttons
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-08-07'
---

# Disabled Buttons

> The button is disabled, and nobody tells you why.

## When to Use (Triggers)

- designing or building disabled buttons components
- reviewing UX/UI for disabled buttons
- implementing interaction pattern for disabled buttons
- the button is disabled, and nobody tells you why

## Key Insights & Principles

- A disabled button drops out of thetab order, so keyboard users skip right past it and screen readers stay silent. The block exists, but nothing announces it.
- Pointer events are deadon a disabled element, so a tooltip meant to explain the block never fires. The reason is unreachable by design.
- Greyed-out labels usually fail contrast. A disabled state can land near 1.9:1, well under the 4.5:1 threshold, so the text is hard to read on top of being blocked.
- Keep the button live andvalidate on clickinstead. Light up the fields that are blocking submit, then move focus to the first one so the path forward is visible.
- Disabled and loading are different states.During a request, hold focus, show a spinner, and reportaria-busy; greying the button out throws the user's place away.

## Do's and Don'ts

- **Do:** Keep the button enabled, validate on click, then flag the blocking fields and move focus to the first one.
- **Do:** For async actions, use a busy state that holds focus, spins, and sets aria-busy.
- **Do:** Name the blocker in reachable text, not a tooltip attached to a dead control.
- **Don't:** Disable submit and leave the user to guess what is missing.
- **Don't:** Rely on a tooltip to explain a disabled control, since pointer events never fire on it.
- **Don't:** Treat loading as disabled; greying out mid-request drops focus and the user's place.

## Code & Selectors

```css
aria-busy
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/disabled-buttons.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/disabled-buttons.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/disabled-buttons)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.hover-trap`
