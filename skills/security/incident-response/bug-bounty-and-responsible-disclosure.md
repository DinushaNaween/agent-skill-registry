---
id: security.incident-response.bug-bounty-and-responsible-disclosure
name: Bug Bounty & Responsible Vulnerability Disclosure
version: 1.0.0
domain: security
subdomain: incident-response
summary: Authoring security.txt, defining safe harbor scopes, vulnerability triage, and coordinating patches.
triggers:
- establishing a Vulnerability Disclosure Policy (VDP) or bug bounty program
- deploying a security.txt file (RFC 9116) for security researchers
- triaging incoming external security vulnerability reports
tags:
- security
- bug-bounty
- vdp
- responsible-disclosure
- security-txt
priority: medium
dependencies: []
related_skills:
- security.system-hardening.vulnerability-assessment-and-prioritization
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/11. Bug Bounty & Responsible Disclosure/11. Bug Bounty & Responsible Disclosure.md
last_updated: '2026-09-14'
---

# Bug Bounty & Responsible Vulnerability Disclosure

> Authoring security.txt, defining safe harbor scopes, vulnerability triage, and coordinating patches.

## When to Use (Triggers)

- establishing a Vulnerability Disclosure Policy (VDP) or bug bounty program
- deploying a security.txt file (RFC 9116) for security researchers
- triaging incoming external security vulnerability reports

## Key Insights & Principles

- RFC 9116 security.txt: Standardized machine-readable file located at `/.well-known/security.txt` defining security contact info.
- Safe Harbor: Legal commitment that good-faith security researchers will not face legal action when following policy guidelines.
- Clear Scope: Explicitly specify which domains, APIs, and techniques (e.g. no DoS, no social engineering) are in-scope.
- Triage & SLA: Acknowledge researcher reports within 24-48 hours and coordinate embargoed public disclosure post-patch.

## Do's and Don'ts

- **Do:** Publish a `/.well-known/security.txt` on all public domains containing contact emails and encryption keys.
- **Do:** Include explicit legal Safe Harbor terms protecting good-faith researchers.
- **Do:** Validate and triage incoming reports with reproducing proof-of-concept steps before prioritizing fixes.
- **Don't:** Threaten legal action against researchers who responsibly report vulnerabilities without accessing user data.
- **Don't:** Ignore reports received via security contacts, which risks uncoordinated zero-day public disclosure.

## Related Skills

- `security.system-hardening.vulnerability-assessment-and-prioritization`
