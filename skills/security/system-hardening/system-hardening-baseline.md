---
id: security.system-hardening.system-hardening-baseline
name: System Hardening & Baseline Configuration
version: 1.0.0
domain: security
subdomain: system-hardening
summary: Applying CIS Benchmarks, disabling unnecessary services, configuring OSSEC/auditd, and host firewalling.
triggers:
- provisioning production virtual machines or golden OS images
- applying Center for Internet Security (CIS) hardening benchmarks
- configuring Linux auditd, systemd security, or Windows Group Policies
tags:
- security
- hardening
- cis-benchmarks
- auditd
- linux
- baseline
priority: high
dependencies: []
related_skills:
- security.access-control.privilege-management
- security.system-hardening.vulnerability-assessment-and-prioritization
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/7. System Hardening & Security Monitoring/7. System Hardening & Security Monitoring.md
last_updated: '2026-09-14'
---

# System Hardening & Baseline Configuration

> Applying CIS Benchmarks, disabling unnecessary services, configuring OSSEC/auditd, and host firewalling.

## When to Use (Triggers)

- provisioning production virtual machines or golden OS images
- applying Center for Internet Security (CIS) hardening benchmarks
- configuring Linux auditd, systemd security, or Windows Group Policies

## Key Insights & Principles

- Minimize Attack Surface: Remove or disable unused network protocols, background daemons, and software packages.
- CIS Benchmarks: Industry-standard consensus hardening baselines for Linux, Windows, Kubernetes, and cloud providers.
- Immutable Infrastructure: Deploy stateless immutable host images and replace rather than patch in-place.
- Audit Logging: Configure Linux `auditd` to capture system calls for privilege escalation, file modifications, and network connections.

## Do's and Don'ts

- **Do:** Automate baseline configuration via Ansible or Packer using official CIS Benchmark playbooks.
- **Do:** Disable legacy and insecure protocols (Telnet, FTP, SMBv1, TLS 1.0/1.1).
- **Do:** Forward all host system logs immediately to a centralized, tamper-resistant SIEM.
- **Don't:** Run services under default factory passwords or unconfigured default settings.
- **Don't:** Leave development tools (compilers, debuggers) installed on production application servers.

## Related Skills

- `security.access-control.privilege-management`
- `security.system-hardening.vulnerability-assessment-and-prioritization`
