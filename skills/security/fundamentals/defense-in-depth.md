---
id: security.fundamentals.defense-in-depth
name: Defense in Depth
version: 1.0.0
domain: security
subdomain: fundamentals
summary: Multi-layered security strategy ensuring no single defensive failure leads to total system compromise.
triggers:
- designing system infrastructure or application security architecture
- reviewing single points of failure in security controls
- auditing multi-tier security layers (network, host, app, data)
tags:
- security
- defense-in-depth
- layered-security
- architecture
priority: high
dependencies: []
related_skills:
- security.fundamentals.zero-trust-architecture
- security.system-hardening.system-hardening-baseline
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Defense in Depth.md
last_updated: '2026-09-14'
---

# Defense in Depth

> Multi-layered security strategy ensuring no single defensive failure leads to total system compromise.

## When to Use (Triggers)

- designing system infrastructure or application security architecture
- reviewing single points of failure in security controls
- auditing multi-tier security layers (network, host, app, data)

## Key Insights & Principles

- Layered Redundancy: multiple independent security controls must fail before an asset is compromised.
- Diverse Defenses: avoid relying on a single vendor, tool, or detection mechanism across all layers.
- Full-Spectrum Coverage: secure all layers—Physical, Perimeter, Network, Host, Application, and Data.
- Containment & Delay: outer layers detect and delay attackers, giving incident responders time to react.

## Do's and Don'ts

- **Do:** Implement security controls across all 5 concentric layers: Perimeter, Network, Endpoint, App, and Data.
- **Do:** Pair preventive controls (firewalls, RBAC) with detective controls (SIEM, IDS) and responsive controls.
- **Do:** Ensure that if an outer layer is bypassed, inner layers still require independent authentication.
- **Don't:** Rely entirely on perimeter firewalls or edge WAFs to protect unhardened internal servers.
- **Don't:** Assume internal microservices communicate in a safe zone without transport encryption and auth tokens.
- **Don't:** Deploy identical security tools across all layers, creating a common-mode vulnerability.

## Related Skills

- `security.fundamentals.zero-trust-architecture`
- `security.system-hardening.system-hardening-baseline`
