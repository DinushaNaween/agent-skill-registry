---
id: ui-ux.forms.otp-input
name: OTP Input
version: 1.0.0
domain: ui-ux
subdomain: forms
summary: Your OTP input is a system, not six boxes.
triggers:
- designing or building otp input components
- reviewing UX/UI for otp input
- implementing forms pattern for otp input
- your otp input is a system, not six boxes
tags:
- ui
- ux
- forms
- otp
- input
priority: medium
dependencies: []
related_skills:
- ui-ux.forms.settings-system
- ui-ux.forms.autosave-ux
- ui-ux.forms.date-pickers
source:
  name: web-ui-patterns
  category: design-pattern-library
last_updated: '2026-06-08'
---

# OTP Input

> Your OTP input is a system, not six boxes.

## When to Use (Triggers)

- designing or building otp input components
- reviewing UX/UI for otp input
- implementing forms pattern for otp input
- your otp input is a system, not six boxes

## Key Insights & Principles

- Treatpasteas the primary path: when a code is pasted into any box, strip spaces and non-digits (value.replace(/\D/g, "")) and distribute the digits across all six boxes at once.
- Auto-advancefocus as each digit lands, and make backspace on an empty box jump back to the previous one and clear it — so correcting a typo never traps the cursor.
- Model the field asone string, not six independent values.useState("847291")beatsuseState(["","","","","",""]); the boxes are just a view of a single source of truth.
- On mobile, wire upinputmode="numeric"andautocomplete="one-time-code"so the OS surfaces the SMS code as a one-tap autofill above the keypad.
- Throttle resendbehind a visible 30s countdown. Without it, impatient users spam the button, hit429 Too Many Requests, and get temporarily banned by the server.
- Giveinstant feedbackon submit: a wrong code shakes and clears back to focus, a correct code locks each box green with a check and a 'Verified' state.

## Do's and Don'ts

- **Do:** Store the full code as a single string and render the six boxes as a view of it
- **Do:** Strip non-digits from pasted input and spread the code across every box automatically
- **Do:** Gate the resend button behind a visible countdown timer to avoid rate-limit bans
- **Don't:** Rely on one wide input — pasted codes with spaces overflow and choke it
- **Don't:** Leave a wrong code sitting silently — shake, clear, and refocus instead

## Code & Selectors

```css
value.replace(/\D/g, "")
```

```css
useState("847291")
```

```css
useState(["","","","","",""])
```

```css
inputmode="numeric"
```

```css
autocomplete="one-time-code"
```

```css
429 Too Many Requests
```

## References

- Modern Web UI/UX Design Patterns & Standards

## Related Skills

- `ui-ux.forms.settings-system`
- `ui-ux.forms.autosave-ux`
- `ui-ux.forms.date-pickers`
