---
id: ui-ux.interaction.accordion-disclosure
name: Accordion Disclosure
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: One accordion glides open, the other jumps. Four small rules separate them.
triggers:
- designing or building accordion disclosure components
- reviewing UX/UI for accordion disclosure
- implementing interaction pattern for accordion disclosure
- one accordion glides open, the other jumps
tags:
- ui
- ux
- interaction
- accordion
- disclosure
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.css-has-selector
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-02'
---

# Accordion Disclosure

> One accordion glides open, the other jumps. Four small rules separate them.

## When to Use (Triggers)

- designing or building accordion disclosure components
- reviewing UX/UI for accordion disclosure
- implementing interaction pattern for accordion disclosure
- one accordion glides open, the other jumps

## Key Insights & Principles

- Youcan't animateheight: auto— the transition just snaps. Usedisplay: gridwithgrid-template-rowsgoing from0frto1fr, or measurescrollHeightand animate to a pixel value.
- Drive thechevron rotation from the same timing curve as the panel. Even ~10 frames of lag between the two reads as broken, not smooth.
- Decidesingle vs multi open: an accordion lets one panel open at a time, a disclosure lets many stay open. Sequential steps stay single; FAQ lists let several breathe.
- The header is a<button>, not a<div>. Wirearia-expandedto reflect state andaria-controlsto point at the panel, so Enter/Space toggle it and the focus ring shows.
- When an item near the bottom expands,anchor the tapped headerso the list doesn't jump under the user, and stagger the revealed content in.

## Do's and Don'ts

- **Do:** Drive chevron rotation and panel height from one shared timing curve so they move as a unit
- **Do:** Render the header as a real<button>witharia-expandedandaria-controlswired to the panel
- **Do:** Match open behavior to content — one-at-a-time for steps, many-open for FAQ lists
- **Don't:** Animateheight: autoand expect a transition — use grid rows or a measured pixel height
- **Don't:** Let the chevron trail the panel; even a few frames of lag feels janky
- **Don't:** Let the list scroll-jump when a lower item expands — keep the tapped header anchored

## Code & Selectors

```css
height: auto
```

```css
display: grid
```

```css
grid-template-rows
```

```css
0fr
```

```css
1fr
```

```css
scrollHeight
```

```css
<button>
```

```css
<div>
```

```css
aria-expanded
```

```css
aria-controls
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.interaction.css-has-selector`
- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
