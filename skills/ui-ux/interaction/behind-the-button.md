---
id: ui-ux.interaction.behind-the-button
name: Behind the Button
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Six things happen before the spinner stops.
triggers:
- designing or building behind the button components
- reviewing UX/UI for behind the button
- implementing interaction pattern for behind the button
- six things happen before the spinner stops
tags:
- ui
- ux
- interaction
- behind
- the
- button
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/behind-the-button
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-07-31'
---

# Behind the Button

> Six things happen before the spinner stops.

## When to Use (Triggers)

- designing or building behind the button components
- reviewing UX/UI for behind the button
- implementing interaction pattern for behind the button
- six things happen before the spinner stops

## Key Insights & Principles

- Client-side validation exists for speed, not safety. Green checks and inline errors fire with0 network callsbecause catching mistakes instantly is a frontend job.
- The server re-runs every check the client already did, only stricter.Never trust the client: anyone can forge a request, so re-compute the total from your own catalog instead of believing the price the browser sent.
- Wrap the related writes (order, items, inventory, payment) in onetransaction. If a single row fails, every row rolls back, so an order never lands half-written. All of it, or none of it.
- When the response returns, repaint the UI withserver truth, the real order ID the server created, not a value you guessed locally.
- Optimistic UIfits cheap, reversible actions: a like, a favorite, a rename can repaint instantly and reconcile in the background. Money is different, so hold the spinner until the server actually confirms.

## Do's and Don'ts

- **Do:** Validate on the client for speed and on the server for trust, never one instead of the other.
- **Do:** Re-compute prices and totals server-side from your own source of truth.
- **Do:** Wrap multi-row writes in one transaction so any failure rolls back the whole thing.
- **Don't:** Trust values the client sends, including the price, since a request is trivial to forge.
- **Don't:** Reach for optimistic UI on payments or other irreversible actions; make them earn the spinner.
## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/behind-the-button.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/behind-the-button.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/behind-the-button)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
