---
id: security.network-security.network-security-monitoring
name: Network Security & Traffic Monitoring
version: 1.0.0
domain: security
subdomain: network-security
summary: Network protocol analysis, IDS/IPS deployment (Suricata/Zeek), firewall architecture, and packet inspection.
triggers:
- investigating suspicious network traffic or packet captures (PCAP)
- configuring Network Intrusion Detection Systems (NIDS) or firewalls
- analyzing DNS, TCP/IP, or HTTP/TLS handshake anomalies
tags:
- security
- network-security
- ids
- ips
- wireshark
- zeek
- firewall
priority: high
dependencies: []
related_skills:
- security.network-security.ddos-mitigation-architecture
- security.fundamentals.cyber-kill-chain
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/2. Network Security & Monitoring/2. Network Security & Monitoring.md
last_updated: '2026-09-14'
---

# Network Security & Traffic Monitoring

> Network protocol analysis, IDS/IPS deployment (Suricata/Zeek), firewall architecture, and packet inspection.

## When to Use (Triggers)

- investigating suspicious network traffic or packet captures (PCAP)
- configuring Network Intrusion Detection Systems (NIDS) or firewalls
- analyzing DNS, TCP/IP, or HTTP/TLS handshake anomalies

## Key Insights & Principles

- Stateful vs Stateless Firewalls: Stateful firewalls track connection state tables, blocking unsolicited incoming packets.
- IDS vs IPS: Intrusion Detection Systems (IDS) alert on anomalous signatures; Intrusion Prevention Systems (IPS) inline-block packets.
- Network Telemetry: NetFlow/IPFIX metadata provides broad visibility; full packet inspection (PCAP) provides deep forensic detail.
- DNS Monitoring: DNS requests are the most frequent indicator of early malware command-and-control communication.

## Do's and Don'ts

- **Do:** Monitor internal east-west traffic between servers, not just north-south perimeter edge traffic.
- **Do:** Inspect DNS queries for DNS tunneling, high-entropy subdomain generation (DGA), and known malicious domains.
- **Do:** Capture PCAPs immediately upon detecting critical intrusion alerts before memory buffers overwrite.
- **Don't:** Leave management ports (SSH 22, RDP 3389) open to the public internet.
- **Don't:** Assume encrypted TLS traffic cannot be monitored: inspect SNI, certificate metadata, and connection volume.

## Related Skills

- `security.network-security.ddos-mitigation-architecture`
- `security.fundamentals.cyber-kill-chain`
