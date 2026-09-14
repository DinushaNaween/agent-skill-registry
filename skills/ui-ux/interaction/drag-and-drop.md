---
id: ui-ux.interaction.drag-and-drop
name: Drag and Drop
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: 'The board does the thinking: moving a card is moving state.'
triggers:
- designing or building drag and drop components
- reviewing UX/UI for drag and drop
- implementing interaction pattern for drag and drop
- 'the board does the thinking: moving a card is moving state'
tags:
- ui
- ux
- interaction
- drag
- and
- drop
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/drag-and-drop
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-08'
---

# Drag and Drop

> The board does the thinking: moving a card is moving state.

## When to Use (Triggers)

- designing or building drag and drop components
- reviewing UX/UI for drag and drop
- implementing interaction pattern for drag and drop
- the board does the thinking: moving a card is moving state

## Key Insights & Principles

- A grabbed item needs to feel like it left the surface. Confirm the lift withthree cues at once: a slight scale-up, a deeper shadow, and a small tilt.
- Drop zones speak first.Reveal where the item will landbeforerelease, not after — the drag should never feel like a guess.
- Match the drop-zone cue to its scope: aninsertion lineto slot between existing items, afilled highlightto land inside a whole column.
- On structured surfaces,snapthe item to the nearest valid slot; reserve free positioning for canvases where any coordinate is valid.
- While dragging on a snapping surface, expose the valid target slots (dashed outlines) so the destination is never ambiguous.
- A drag is easy to fumble. Pair every drop with a shortundo toast(~5 seconds) so a wrong move costs one click, not a redo.

## Do's and Don'ts

- **Do:** Confirm pickup with scale, shadow, and tilt together so the grab reads instantly
- **Do:** Highlight the exact drop target during the drag, before the user lets go
- **Do:** Offer a brief undo after a drop so a misdrop is one click to reverse
- **Don't:** Snap a released card into place with no lift or shadow — it feels like nothing happened
- **Don't:** Force pixel-precise placement when snapping to a valid slot would do the work
- **Don't:** Make a wrong drop permanent with no way to reverse it
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/drag-and-drop.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/drag-and-drop.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/drag-and-drop)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
