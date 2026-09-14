---
id: ui-ux.interaction.inline-editing
name: Inline Editing
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Click the title. It's an input now, and nothing moved.
triggers:
- designing or building inline editing components
- reviewing UX/UI for inline editing
- implementing interaction pattern for inline editing
- click the title
tags:
- ui
- ux
- interaction
- inline
- editing
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/inline-editing
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-23'
---

# Inline Editing

> Click the title. It's an input now, and nothing moved.

## When to Use (Triggers)

- designing or building inline editing components
- reviewing UX/UI for inline editing
- implementing interaction pattern for inline editing
- click the title

## Key Insights & Principles

- Editable text has towhisperits affordance: a pencil on hover, a soft background tint. With no signal, people file support tickets just to rename a title.
- Keep every pixel in place during the swap. Same font, same size, same padding, with the border going from transparent to accent. One jump and the illusion collapses.
- Enter commits, Escape cancels, and everyone agrees on that. Blur is the contested one: some apps save on click-away, others discard. Pick one rule and never break it.
- Saveoptimistically: the text updates on screen while the request is still in flight. If the server fails, roll back, keep the draft, and say why.
- Match the editing mode to the cost of a typo. Make every cell editable when mistakes are cheap, or require an explicit Edit action when they are expensive.

## Do's and Don'ts

- **Do:** Signal editability on hover with a pencil icon or a soft background tint.
- **Do:** Update the UI immediately, then roll back and keep the draft if the save fails.
- **Do:** Keep font, size, and padding identical between the text and the input.
- **Don't:** Leave editable text with zero affordance, so users cannot tell it is editable.
- **Don't:** Change what blur does from one screen to the next (save here, discard there).
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/inline-editing.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/inline-editing.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/inline-editing)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
