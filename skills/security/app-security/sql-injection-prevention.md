---
id: security.app-security.sql-injection-prevention
name: SQL Injection (SQLi) Prevention
version: 1.0.0
domain: security
subdomain: app-security
summary: Eliminating SQL injection vulnerabilities using parameterized queries, prepared statements, and ORMs.
triggers:
- writing database queries or data access layers
- reviewing SQL query construction for untrusted inputs
- auditing dynamic query builders and ORM raw query calls
tags:
- security
- sqli
- database
- injection
- appsec
priority: high
dependencies: []
related_skills:
- security.app-security.owasp-top-10-defenses
- security.app-security.api-security-best-practices
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md
last_updated: '2026-09-14'
---

# SQL Injection (SQLi) Prevention

> Eliminating SQL injection vulnerabilities using parameterized queries, prepared statements, and ORMs.

## When to Use (Triggers)

- writing database queries or data access layers
- reviewing SQL query construction for untrusted inputs
- auditing dynamic query builders and ORM raw query calls

## Key Insights & Principles

- Root Cause: Mixing untrusted user data with SQL code commands, altering query syntax.
- Parameterized Queries: The database engine compiles SQL structure first, then binds parameters strictly as literal data.
- Stored Procedures: Safe only when using parameters, not when dynamically concatenating strings inside the procedure.
- Least Privilege Database Accounts: Web applications must connect using restricted database users, not `sa` or `root`.

## Do's and Don'ts

- **Do:** Always use parameterized queries or prepared statements across all database interactions.
- **Do:** Use ORMs (Entity Framework, Prisma, SQLAlchemy) properly and avoid raw unparameterized SQL helpers.
- **Do:** Apply principle of least privilege to database credentials (e.g. read-only where modification isn't required).
- **Don't:** Never concatenate or format user input directly into SQL query strings (e.g. `f"SELECT * FROM users WHERE id = '{user_id}'"`).
- **Don't:** Never rely on custom character escaping or blacklisting quotes as primary injection defense.

## Related Skills

- `security.app-security.owasp-top-10-defenses`
- `security.app-security.api-security-best-practices`
