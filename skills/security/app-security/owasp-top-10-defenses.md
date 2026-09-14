---
id: security.app-security.owasp-top-10-defenses
name: OWASP Top 10 Web Application Defenses
version: 1.0.0
domain: security
subdomain: app-security
summary: Practical countermeasures against the most critical web application security risks.
triggers:
- performing code reviews for web applications and APIs
- designing input validation, authentication, and session handling
- preparing web services for application penetration tests
tags:
- security
- owasp
- web-security
- appsec
- vulnerabilities
priority: high
dependencies: []
related_skills:
- security.app-security.sql-injection-prevention
- security.app-security.api-security-best-practices
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md
last_updated: '2026-09-14'
---

# OWASP Top 10 Web Application Defenses

> Practical countermeasures against the most critical web application security risks.

## When to Use (Triggers)

- performing code reviews for web applications and APIs
- designing input validation, authentication, and session handling
- preparing web services for application penetration tests

## Key Insights & Principles

- A01 Broken Access Control: Failure to enforce least privilege on endpoints and resources (IDOR, missing function-level auth).
- A02 Cryptographic Failures: Transmitting data in plaintext, using weak algorithms, hardcoding secrets.
- A03 Injection: SQL, Command, NoSQL, and LDAP injection from untrusted input.
- A05 Security Misconfiguration: Default accounts, unpatched components, verbose error stack traces.
- A07 Identification & Authentication Failures: Credential stuffing, missing MFA, session hijacking.

## Do's and Don'ts

- **Do:** Validate and sanitize all user input using strict allowlists (type, length, format).
- **Do:** Enforce authorization checks on every single API route at the business logic layer.
- **Do:** Disable debug mode and verbose stack traces in production environments.
- **Don't:** Rely on client-side validation (HTML attributes, JS checks) for security enforcement.
- **Don't:** Trust user-supplied IDs or roles directly from request payloads or query parameters.

## Related Skills

- `security.app-security.sql-injection-prevention`
- `security.app-security.api-security-best-practices`
