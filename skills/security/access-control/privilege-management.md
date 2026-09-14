---
id: security.access-control.privilege-management
name: Operating System Security & Privilege Management
version: 1.0.0
domain: security
subdomain: access-control
summary: Hardening OS privilege boundaries, sudoers configuration, UAC, and mitigating privilege escalation.
triggers:
- configuring Linux sudoers or Windows User Account Control (UAC)
- running container processes or system daemons with restricted privileges
- reviewing SUID/SGID binaries and Linux capability assignments
tags:
- security
- privilege-management
- linux
- windows
- sudo
- hardening
priority: high
dependencies: []
related_skills:
- security.system-hardening.system-hardening-baseline
- security.access-control.access-control-models
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/5. Operating System Security & Privilege Management/5. Operating System Security
    & Privilege Management.md
last_updated: '2026-09-14'
---

# Operating System Security & Privilege Management

> Hardening OS privilege boundaries, sudoers configuration, UAC, and mitigating privilege escalation.

## When to Use (Triggers)

- configuring Linux sudoers or Windows User Account Control (UAC)
- running container processes or system daemons with restricted privileges
- reviewing SUID/SGID binaries and Linux capability assignments

## Key Insights & Principles

- Never run workloads as root: containers and services must execute under dedicated unprivileged service accounts.
- SUID/SGID Binaries: Binaries with SUID bits execute with file owner permissions—a primary local privilege escalation target.
- Linux Capabilities: Grant fine-grained capabilities (e.g. `CAP_NET_BIND_SERVICE`) instead of full root access.
- JIT & PAM: Use Privileged Access Management (PAM) with just-in-time elevation and session auditing.

## Do's and Don'ts

- **Do:** Audit `sudoers` configurations and require passwords for privileged operations; avoid `NOPASSWD: ALL`.
- **Do:** Strip unnecessary SUID/SGID bits (`find / -perm -4000`) across all server images.
- **Do:** Enforce SELinux or AppArmor profiles on Linux hosts to constrain daemon capabilities.
- **Don't:** Deploy production Docker containers running as root (`UID 0`).
- **Don't:** Grant generic developer accounts permanent administrative or root access on production servers.

## Related Skills

- `security.system-hardening.system-hardening-baseline`
- `security.access-control.access-control-models`
