---
id: ui-ux.interaction.destructive-actions
name: Destructive Actions
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: Dangerous actions are a design language, not just a red button.
triggers:
- designing or building destructive actions components
- reviewing UX/UI for destructive actions
- implementing interaction pattern for destructive actions
- dangerous actions are a design language, not just a red button
tags:
- ui
- ux
- interaction
- destructive
- actions
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-17'
---

# Destructive Actions

> Dangerous actions are a design language, not just a red button.

## When to Use (Triggers)

- designing or building destructive actions components
- reviewing UX/UI for destructive actions
- implementing interaction pattern for destructive actions
- dangerous actions are a design language, not just a red button

## Key Insights & Principles

- Hold-to-confirmturns the gesture into the safeguard: a ring fills over roughly 300ms of a held press, replacing a modal, and releasing early cancels the action entirely.
- Name the action on the button itself.Delete project/Keep projectbeats a generic Yes / No, because the verb is the warning and nobody reads 'Are you sure?'.
- Never place a destructive button where confirm usually lives. Muscle memory clicks primary spots blind, so moving delete elsewhere keeps autopilot from reaching it.
- Red is a budget: spend it on destruction only. A red logout button cries wolf, and then the real delete looks routine.
- Bury deletion in a bordered, labeleddanger zoneat the bottom of the page. Geography itself becomes friction that slows the hand.
- Give irreversible deletions acooldown: schedule it with a grace period (for example 14 days to cancel). Time is the last line of defense.

## Do's and Don'ts

- **Do:** Name the destructive action on the button so the verb itself does the warning.
- **Do:** Reserve red for destructive actions only, and add friction like a hold gesture or a danger zone.
- **Do:** Give irreversible deletions a cancelable cooldown before they take effect.
- **Don't:** Place destructive buttons where the confirm button usually sits.
- **Don't:** Rely on a generic 'Are you sure?' dialog that nobody actually reads.
- **Don't:** Spread red across logout, badges, and alerts until delete looks routine.
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
