---
id: security.access-control.access-control-models
name: Access Control Models (DAC, MAC, RBAC, ABAC)
version: 1.0.0
domain: security
subdomain: access-control
summary: Implementation principles for Discretionary, Mandatory, Role-Based, and Attribute-Based Access Control.
triggers:
- designing authorization systems or user permission schemas
- implementing multi-tenant role-based access in web applications
- auditing user privilege boundaries and privilege escalation risks
tags:
- security
- access-control
- rbac
- abac
- authorization
priority: high
dependencies: []
related_skills:
- security.fundamentals.zero-trust-architecture
- security.app-security.api-security-best-practices
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: 1-fundamentals/1.2.1.2-Access-control-mechanisms-DAC-MAC-RBAC.md
last_updated: '2026-09-14'
---

# Access Control Models (DAC, MAC, RBAC, ABAC)

> Implementation principles for Discretionary, Mandatory, Role-Based, and Attribute-Based Access Control.

## When to Use (Triggers)

- designing authorization systems or user permission schemas
- implementing multi-tenant role-based access in web applications
- auditing user privilege boundaries and privilege escalation risks

## Key Insights & Principles

- DAC (Discretionary): Data owner specifies permissions (e.g. Linux file chmod). Flexible but prone to privilege sprawl.
- MAC (Mandatory): Central authority labels data and subjects (e.g. SELinux, Military Clearance). Strict, tamper-proof.
- RBAC (Role-Based): Users belong to roles; roles have permissions. Clean and scalable for enterprise business apps.
- ABAC (Attribute-Based): Fine-grained policies based on subject, resource, action, and environment (time, IP, device).

## Do's and Don'ts

- **Do:** Default to deny: all access requests must be explicitly authorized.
- **Do:** Separate authentication (AuthN - who you are) from authorization (AuthZ - what you can do).
- **Do:** Use RBAC for standard roles and ABAC for context-aware or multi-tenant permission rules.
- **Don't:** Hardcode role checks in client-side code without enforcing authorization on every API endpoint.
- **Don't:** Rely solely on user IDs in URL parameters without validating tenant authorization (IDOR vulnerability).

## Practical Implementation & Architecture

Practical implementation of these concepts involves various tools and techniques depending on specific requirements, technology stacks, and organizational constraints. Security professionals should maintain familiarity with industry-standard tools while remaining adaptable to emerging technologies and methodologies.

## Related Skills

- `security.fundamentals.zero-trust-architecture`
- `security.app-security.api-security-best-practices`
