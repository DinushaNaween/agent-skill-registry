---
id: ui-ux.visual.proximity-rule
name: Proximity Rule
version: 1.0.0
domain: ui-ux
subdomain: visual
summary: 'Close = related, far = separate: spacing alone groups your UI, no borders needed.'
triggers:
- designing or building proximity rule components
- reviewing UX/UI for proximity rule
- implementing visual pattern for proximity rule
tags:
- ui
- ux
- visual
- proximity
- rule
priority: medium
dependencies: []
related_skills:
- ui-ux.visual.de-ai-landing-hero
- ui-ux.visual.reverse-engineered-linear
- ui-ux.visual.charts-that-lie
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-07-08'
---

# Proximity Rule

> Close = related, far = separate: spacing alone groups your UI, no borders needed.

## When to Use (Triggers)

- designing or building proximity rule components
- reviewing UX/UI for proximity rule
- implementing visual pattern for proximity rule

## Key Insights & Principles

- Proximity is a Gestalt principle: elements placedclose togetherread as one group, elements spaced apart read as separate. The eye infers relationships from distance alone.
- You rarely need borders, boxes, or dividers to create structure —spacing does the groupingby itself.
- The trick is contrast: make the gapwithina group smaller than the gapbetweengroups. Equal spacing everywhere flattens the hierarchy and everything reads as one undifferentiated block.
- In forms, tighten related fields (~12px) and open up section breaks (~40px) so 'Personal Info' and 'Payment' visibly separate without a single line.
- In toolbars and nav, group controls by function — navigate, actions, system — instead of laying them out in one evenly-spaced row.
- Same content, more clarity: a flat list of eight sidebar links becomes scannable the moment it's split into labeled groups like Dashboard, Management, and Account.

## Do's and Don'ts

- **Do:** Keep spacing within a group tighter than the spacing between groups
- **Do:** Group form fields and nav items by function or meaning
- **Do:** Let whitespace carry the grouping before reaching for borders or dividers
- **Don't:** Space every element equally — it erases hierarchy and forces users to parse everything at once
- **Don't:** Reach for boxes and dividers when a larger gap would communicate the same grouping
## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.visual.de-ai-landing-hero`
- `ui-ux.visual.reverse-engineered-linear`
- `ui-ux.visual.charts-that-lie`
