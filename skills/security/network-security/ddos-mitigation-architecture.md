---
id: security.network-security.ddos-mitigation-architecture
name: DDoS Mitigation Strategies & Resilience
version: 1.0.0
domain: security
subdomain: network-security
summary: Architectural defenses against Volumetric, Protocol (SYN Flood), and Application-layer (HTTP Flood) DDoS attacks.
triggers:
- architecting internet-facing systems against denial-of-service attacks
- configuring edge rate limiting, Cloudflare, or AWS Shield
- responding to unexpected web service availability degradation
tags:
- security
- ddos
- rate-limiting
- cdn
- availability
priority: medium
dependencies: []
related_skills:
- security.network-security.network-security-monitoring
- security.app-security.api-security-best-practices
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: 1-fundamentals/1.2.3.2-DDoS-attack-mitigation-strategies.md
last_updated: '2026-09-14'
---

# DDoS Mitigation Strategies & Resilience

> Architectural defenses against Volumetric, Protocol (SYN Flood), and Application-layer (HTTP Flood) DDoS attacks.

## When to Use (Triggers)

- architecting internet-facing systems against denial-of-service attacks
- configuring edge rate limiting, Cloudflare, or AWS Shield
- responding to unexpected web service availability degradation

## Key Insights & Principles

- Attack Categories: Volumetric (NTP/DNS amplification saturated pipe), Protocol (SYN flood exhausting state tables), Application (Slowloris, complex query spam).
- Anycast Routing: Distributes incoming traffic across dozens of globally distributed edge PoPs to absorb volumetric spikes.
- SYN Cookies: Kernel defense enabling servers to acknowledge TCP connections without storing state until handshake completes.
- Edge Rate Limiting & WAF: Filters malicious HTTP flood bots before requests reach origin backend servers.

## Do's and Don'ts

- **Do:** Place internet-facing web apps behind Anycast CDN and DDoS scrubbing networks (Cloudflare, AWS CloudFront).
- **Do:** Enable SYN cookies (`net.ipv4.tcp_syncookies = 1`) on Linux servers.
- **Do:** Implement aggressive rate limiting and adaptive CAPTCHA challenges on expensive API routes (login, search, checkout).
- **Don't:** Expose the true origin IP address of web servers—attackers will bypass CDN/WAF defenses directly.
- **Don't:** Design database queries that execute unpaginated full-table scans easily triggered by malicious requests.

## Practical Implementation & Architecture

Practical implementation of these concepts involves various tools and techniques depending on specific requirements, technology stacks, and organizational constraints. Security professionals should maintain familiarity with industry-standard tools while remaining adaptable to emerging technologies and methodologies.

## Related Skills

- `security.network-security.network-security-monitoring`
- `security.app-security.api-security-best-practices`
