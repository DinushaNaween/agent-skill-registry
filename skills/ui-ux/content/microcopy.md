---
id: ui-ux.content.microcopy
name: Microcopy
version: 1.0.0
domain: ui-ux
subdomain: content
summary: Same form. Different words. One converts.
triggers:
- designing or building microcopy components
- reviewing UX/UI for microcopy
- implementing content pattern for microcopy
- same form
tags:
- ui
- ux
- content
- microcopy
priority: medium
dependencies: []
related_skills:
- ui-ux.content.empty-states
- ui-ux.content.serial-position
- ui-ux.content.landing-page-skeleton
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-26'
---

# Microcopy

> Same form. Different words. One converts.

## When to Use (Triggers)

- designing or building microcopy components
- reviewing UX/UI for microcopy
- implementing content pattern for microcopy
- same form

## Key Insights & Principles

- Buttonlabels should name the reward, not the mechanic. "Create my free account" feels like a gift; "Submit" feels like a chore — same action, different conversion.
- Turn errors into help. "Invalid input" tells the user nothing; "That email's taken — want to log in?" names the problem and offers the next move.
- Empty states are onboarding, not dead ends.Instead of a blank inbox, show the first step the user can take right now.
- Placeholder text is not a label.It vanishes the moment they start typing, leaving fields unidentified — keep a persistent label above the input.
- Write like a person. No real human says "operation failed" — match the tone a helpful colleague would use.
- Copy carries as much weight as layout: labels, errors, empty states, and tone shape whether the interface feels usable or hostile.

## Do's and Don'ts

- **Do:** Label actions with the reward the user gets ("Create my free account"), not the system verb
- **Do:** Turn error messages into a next step ("That email's taken — want to log in?")
- **Do:** Fill empty states with the first useful action, not a blank screen
- **Don't:** Rely on placeholder text as a stand-in for a persistent field label
- **Don't:** Ship system-speak like "Invalid input" or "operation failed"
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.content.empty-states`
- `ui-ux.content.serial-position`
- `ui-ux.content.landing-page-skeleton`
