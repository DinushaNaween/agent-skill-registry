---
id: security.app-security.api-security-best-practices
name: API Security & Token Protection
version: 1.0.0
domain: security
subdomain: app-security
summary: Securing REST and GraphQL APIs using JWT validation, rate limiting, CORS, and schema verification.
triggers:
- designing or implementing public or internal REST/GraphQL APIs
- configuring JWT authentication, refresh tokens, and revocation
- setting up API gateway rate limiting and CORS headers
tags:
- security
- api
- jwt
- cors
- rest
- tokens
priority: high
dependencies: []
related_skills:
- security.app-security.owasp-top-10-defenses
- security.access-control.access-control-models
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md
last_updated: '2026-09-14'
---

# API Security & Token Protection

> Securing REST and GraphQL APIs using JWT validation, rate limiting, CORS, and schema verification.

## When to Use (Triggers)

- designing or implementing public or internal REST/GraphQL APIs
- configuring JWT authentication, refresh tokens, and revocation
- setting up API gateway rate limiting and CORS headers

## Key Insights & Principles

- JWT Validation: Always verify signature, expiration (`exp`), issuer (`iss`), and algorithm (reject `alg: none`).
- BOLA / IDOR: Broken Object Level Authorization is the #1 API vulnerability—verify user ownership of requested resource IDs.
- Rate Limiting: Token-bucket or sliding-window rate limiting prevents credential stuffing and denial of service.
- CORS: Cross-Origin Resource Sharing is a browser mechanism; it does not protect against non-browser clients (curl, Postman).

## Do's and Don'ts

- **Do:** Validate incoming JSON payloads against strict schemas (Pydantic, Zod, JSON Schema).
- **Do:** Store sensitive session tokens in `HttpOnly`, `Secure`, `SameSite=Strict` cookies rather than `localStorage`.
- **Do:** Implement granular rate limiting tied to API keys, authenticated user IDs, and client IP addresses.
- **Don't:** Return raw database entities in API responses—filter out internal IDs, passwords, and sensitive fields.
- **Don't:** Use wildcard `Access-Control-Allow-Origin: *` alongside `Access-Control-Allow-Credentials: true`.

## Related Skills

- `security.app-security.owasp-top-10-defenses`
- `security.access-control.access-control-models`
