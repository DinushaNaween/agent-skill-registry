---
id: security.fundamentals.zero-trust-architecture
name: Zero Trust Architecture
version: 1.0.0
domain: security
subdomain: fundamentals
summary: 'Never trust, always verify: identity-based micro-segmented security architecture.'
triggers:
- designing cloud or enterprise network architecture
- implementing identity and access management (IAM) or MFA
- evaluating perimeter vs identity-based access controls
- implementing network micro-segmentation
tags:
- security
- zero-trust
- architecture
- iam
- network
priority: high
dependencies: []
related_skills:
- security.fundamentals.defense-in-depth
- security.access-control.access-control-models
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Zero Trust Architecture.md
last_updated: '2026-09-14'
---

# Zero Trust Architecture

> Never trust, always verify: identity-based micro-segmented security architecture.

## When to Use (Triggers)

- designing cloud or enterprise network architecture
- implementing identity and access management (IAM) or MFA
- evaluating perimeter vs identity-based access controls
- implementing network micro-segmentation

## Key Insights & Principles

- Never Trust, Always Verify: eliminate the traditional trusted-inside-the-firewall assumption.
- Verify User Identity continuously using MFA, risk-based authentication, and behavioral analytics.
- Verify Device Health by enforcing endpoint compliance, patch levels, and EDR agents before granting access.
- Principle of Least Privilege: grant time-bound, just-in-time (JIT) access scoped strictly to role duties.
- Micro-segmentation: partition network zones to strictly prevent lateral adversary movement upon breach.

## Do's and Don'ts

- **Do:** Require continuous authentication and context verification on every API and service call.
- **Do:** Enforce strict device compliance checks prior to admitting connections to sensitive networks.
- **Do:** Adopt assume-breach mentality: minimize blast radius with micro-perimeters and encryption in transit.
- **Don't:** Rely on internal network firewalls or VPNs as the sole boundary of trust.
- **Don't:** Grant permanent standing administrative access to any user account.
- **Don't:** Trust internal network traffic by default without mutual TLS (mTLS) or per-request auth.

## Practical Implementation & Architecture

of Zero Trust

## Related Skills

- `security.fundamentals.defense-in-depth`
- `security.access-control.access-control-models`
