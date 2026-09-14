---
id: ui-ux.interaction.css-has-selector
name: CSS Has Selector
version: 1.0.0
domain: ui-ux
subdomain: interaction
summary: One line of CSS. The whole card reacts to its own checkbox.
triggers:
- designing or building css has selector components
- reviewing UX/UI for css has selector
- implementing interaction pattern for css has selector
- one line of css
tags:
- ui
- ux
- interaction
- css
- has
- selector
priority: medium
dependencies: []
related_skills:
- ui-ux.interaction.bulk-actions
- ui-ux.interaction.disabled-buttons
- ui-ux.interaction.hover-trap
source:
  name: designmotionhq
  url: https://www.designmotionhq.com/patterns/css-has-selector
  instagram_url: https://www.instagram.com/designmotionhq/
last_updated: '2026-09-07'
---

# CSS Has Selector

> One line of CSS. The whole card reacts to its own checkbox.

## When to Use (Triggers)

- designing or building css has selector components
- reviewing UX/UI for css has selector
- implementing interaction pattern for css has selector
- one line of css

## Key Insights & Principles

- :has()is theparent selector..plan:has(:checked)styles the whole card when its own radio is checked. For twenty years CSS only looked down and forward; now it looks up. Every major browser supports it since 2023.
- Validation without a handler:.field:has(:user-invalid)turns the border, label and icon at once. No onChange, no error state in React. The browser already knows the email is wrong, so let it drive the styling.
- Escalate to the form:form:has(:user-invalid) button { opacity: .4 }greys out the submit button while any field is invalid. One rule, zero derived state.
- Layout follows the DOM:.app:has(aside) { grid-template-columns: 280px 1fr }grows a column when a sidebar renders and collapses when it is removed. No showSidebar prop to thread through.
- Quantity querieslive in CSS:.grid:has(> :nth-child(n + 5))tightens gap, padding and font size across all cards the moment a fifth one arrives. No counting items in JavaScript.
- The document reacts to a modal:body:has(dialog[open]) { overflow: hidden }locks scroll and a second rule dims the app behind it. Close the dialog and everything reverts on its own. No cleanup effect.

## Do's and Don'ts

- **Do:** Reach for:has()when the state already lives in the DOM: checked, open, invalid, child count.
- **Do:** Use:user-invalidinstead of:invalidso errors show after the user leaves the field, not on first render.
- **Do:** Put the rule on the container so border, label and icon all update from one selector.
- **Don't:** Mirror DOM state into React state just to toggle a class the browser can already compute.
- **Don't:** Write a cleanup effect for scroll lock or dimming that abody:has(dialog[open])rule undoes by itself.
- **Don't:** Count children in JavaScript to pick a layout when a quantity query does it in one rule.

## Code & Selectors

```css
:has()
```

```css
.plan:has(:checked)
```

```css
.field:has(:user-invalid)
```

```css
form:has(:user-invalid) button { opacity: .4 }
```

```css
.app:has(aside) { grid-template-columns: 280px 1fr }
```

```css
.grid:has(> :nth-child(n + 5))
```

```css
body:has(dialog[open]) { overflow: hidden }
```

```css
:user-invalid
```

```css
:invalid
```

```css
body:has(dialog[open])
```

## Media & References

- **Demo Video:** [Watch MP4 Breakdown](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/videos/css-has-selector.mp4)
- **Thumbnail:** [Visual Preview](https://pub-8b35602514014e9aa3363da6c7b5416c.r2.dev/thumbs/css-has-selector.jpg)
- **Original Pattern:** [designmotionhq](https://www.designmotionhq.com/patterns/css-has-selector)
- **Instagram Reel:** [Watch on Instagram](https://www.instagram.com/designmotionhq/)

## Related Skills

- `ui-ux.interaction.bulk-actions`
- `ui-ux.interaction.disabled-buttons`
- `ui-ux.interaction.hover-trap`
