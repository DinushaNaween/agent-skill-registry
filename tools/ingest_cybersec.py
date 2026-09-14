"""
Ingestion script: Extracts cybersecurity knowledge from cyber-sec repository
and normalizes it into canonical Schema v1.0 skills under skills/security/.
"""
import re
import os
import yaml
from pathlib import Path

SOURCE_DIR = Path("/Users/dinusha/Github-Clones/cyber-sec")
SKILLS_DIR = Path("skills/security")

SECURITY_SKILLS = [
    # 1. Fundamentals
    {
        "subdomain": "fundamentals",
        "slug": "zero-trust-architecture",
        "name": "Zero Trust Architecture",
        "summary": "Never trust, always verify: identity-based micro-segmented security architecture.",
        "priority": "high",
        "triggers": [
            "designing cloud or enterprise network architecture",
            "implementing identity and access management (IAM) or MFA",
            "evaluating perimeter vs identity-based access controls",
            "implementing network micro-segmentation",
        ],
        "tags": ["security", "zero-trust", "architecture", "iam", "network"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Zero Trust Architecture.md",
        "key_insights": [
            "Never Trust, Always Verify: eliminate the traditional trusted-inside-the-firewall assumption.",
            "Verify User Identity continuously using MFA, risk-based authentication, and behavioral analytics.",
            "Verify Device Health by enforcing endpoint compliance, patch levels, and EDR agents before granting access.",
            "Principle of Least Privilege: grant time-bound, just-in-time (JIT) access scoped strictly to role duties.",
            "Micro-segmentation: partition network zones to strictly prevent lateral adversary movement upon breach.",
        ],
        "dos": [
            "Require continuous authentication and context verification on every API and service call.",
            "Enforce strict device compliance checks prior to admitting connections to sensitive networks.",
            "Adopt assume-breach mentality: minimize blast radius with micro-perimeters and encryption in transit.",
        ],
        "donts": [
            "Rely on internal network firewalls or VPNs as the sole boundary of trust.",
            "Grant permanent standing administrative access to any user account.",
            "Trust internal network traffic by default without mutual TLS (mTLS) or per-request auth.",
        ],
        "related": ["security.fundamentals.defense-in-depth", "security.access-control.access-control-models"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "defense-in-depth",
        "name": "Defense in Depth",
        "summary": "Multi-layered security strategy ensuring no single defensive failure leads to total system compromise.",
        "priority": "high",
        "triggers": [
            "designing system infrastructure or application security architecture",
            "reviewing single points of failure in security controls",
            "auditing multi-tier security layers (network, host, app, data)",
        ],
        "tags": ["security", "defense-in-depth", "layered-security", "architecture"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Defense in Depth.md",
        "key_insights": [
            "Layered Redundancy: multiple independent security controls must fail before an asset is compromised.",
            "Diverse Defenses: avoid relying on a single vendor, tool, or detection mechanism across all layers.",
            "Full-Spectrum Coverage: secure all layers—Physical, Perimeter, Network, Host, Application, and Data.",
            "Containment & Delay: outer layers detect and delay attackers, giving incident responders time to react.",
        ],
        "dos": [
            "Implement security controls across all 5 concentric layers: Perimeter, Network, Endpoint, App, and Data.",
            "Pair preventive controls (firewalls, RBAC) with detective controls (SIEM, IDS) and responsive controls.",
            "Ensure that if an outer layer is bypassed, inner layers still require independent authentication.",
        ],
        "donts": [
            "Rely entirely on perimeter firewalls or edge WAFs to protect unhardened internal servers.",
            "Assume internal microservices communicate in a safe zone without transport encryption and auth tokens.",
            "Deploy identical security tools across all layers, creating a common-mode vulnerability.",
        ],
        "related": ["security.fundamentals.zero-trust-architecture", "security.system-hardening.system-hardening-baseline"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "cia-triad",
        "name": "CIA Triad Principles",
        "summary": "The cornerstone model balancing Confidentiality, Integrity, and Availability in software systems.",
        "priority": "high",
        "triggers": [
            "evaluating security requirements for a new system or feature",
            "conducting security risk assessments and compliance reviews",
            "architecting data protection and disaster recovery strategies",
        ],
        "tags": ["security", "cia-triad", "confidentiality", "integrity", "availability"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/CIA Triad.md",
        "key_insights": [
            "Confidentiality ensures only authorized users and processes access protected information.",
            "Integrity guarantees that data and code are accurate, trustworthy, and safeguarded against unauthorized modification.",
            "Availability guarantees that systems, networks, and applications are accessible when authorized users need them.",
            "Trade-offs must be consciously engineered: aggressive security controls must not cripple system availability.",
        ],
        "dos": [
            "Classify every data entity by confidentiality level (public, internal, confidential, restricted).",
            "Enforce cryptographic hashing (SHA-256) and digital signatures to guarantee data integrity.",
            "Design for high availability using redundant clusters, automated failovers, and resilient backups.",
        ],
        "donts": [
            "Prioritize confidentiality so heavily that users cannot access services during routine operations.",
            "Store sensitive credentials, secrets, or API keys in plaintext or version control.",
            "Treat backups as reliable without regularly running automated restore simulations.",
        ],
        "related": ["security.cryptography.symmetric-vs-asymmetric-encryption", "security.incident-response.backup-and-disaster-recovery"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "cyber-kill-chain",
        "name": "Cyber Kill Chain & Attack Lifecycle",
        "summary": "Lockheed Martin 7-phase cyberattack lifecycle model and defensive intervention techniques.",
        "priority": "medium",
        "triggers": [
            "analyzing an ongoing or simulated security intrusion",
            "designing detection rules and early warning alert triggers",
            "modeling threat actor advancement through internal networks",
        ],
        "tags": ["security", "kill-chain", "threat-intelligence", "incident-response"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Cyber Kill Chain.md",
        "key_insights": [
            "The 7 Phases: Reconnaissance → Weaponization → Delivery → Exploitation → Installation → Command & Control (C2) → Actions on Objectives.",
            "Early Interruption: Breaking any single link in the kill chain halts the entire attack progression.",
            "Dwell Time Reduction: Detecting attackers during delivery or exploitation prevents destructive impact on objectives.",
        ],
        "dos": [
            "Deploy threat intelligence feeds and DNS filtering to detect weaponized C2 infrastructure early.",
            "Implement email filtering and endpoint execution restrictions to neutralize Delivery and Exploitation.",
            "Monitor egress traffic for beaconing patterns to catch Command & Control communication.",
        ],
        "donts": [
            "Wait until the 'Actions on Objectives' phase (e.g. data exfiltration or ransomware) before triggering alerts.",
            "Ignore external reconnaissance indicators such as aggressive port scanning and OSINT scraping.",
        ],
        "related": ["security.fundamentals.mitre-attck-framework", "security.incident-response.incident-response-lifecycle"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "mitre-attck-framework",
        "name": "MITRE ATT&CK Framework Mapping",
        "summary": "Curated knowledge base of cyber adversary tactics, techniques, and procedures (TTPs).",
        "priority": "high",
        "triggers": [
            "mapping defensive security monitoring to real adversary techniques",
            "conducting threat modeling and red/blue team simulations",
            "assessing security coverage gaps across SIEM detection rules",
        ],
        "tags": ["security", "mitre", "attck", "threat-detection", "siem"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/MITRE ATT&CK Framework.md",
        "key_insights": [
            "Tactics represent the 'why' (e.g. Initial Access, Privilege Escalation, Lateral Movement, Exfiltration).",
            "Techniques describe 'how' adversaries accomplish the tactic (e.g. T1059 Command and Scripting Interpreter).",
            "Sub-techniques provide granular specifics (e.g. T1059.001 PowerShell).",
            "Matrix coverage mapping reveals blind spots where log telemetry is insufficient.",
        ],
        "dos": [
            "Map your SIEM correlation rules and detection alerts directly to ATT&CK Technique IDs.",
            "Prioritize detection rules for techniques commonly used by threat actors targeting your industry.",
            "Simulate adversary techniques using tools like Atomic Red Team to validate alert coverage.",
        ],
        "donts": [
            "Assume high logging volume equals security visibility without verified detection rules mapped to TTPs.",
            "Treat ATT&CK as a checklist to 'score 100%' rather than an adversary-grounded risk model.",
        ],
        "related": ["security.fundamentals.cyber-kill-chain", "security.system-hardening.vulnerability-assessment-and-prioritization"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "threat-modeling-and-actors",
        "name": "Threat Modeling & Actor Profiling",
        "summary": "Systematic identification of threat actors, capabilities, attack vectors, and high-value targets.",
        "priority": "medium",
        "triggers": [
            "conducting threat modeling for architecture design (STRIDE)",
            "evaluating adversary motivation (nation-state, cybercrime, insider)",
            "identifying critical digital assets and attack surface vectors",
        ],
        "tags": ["security", "threat-modeling", "stride", "threat-actors"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Threat Actors.md",
        "key_insights": [
            "Actor Archetypes: Nation-state APTs (persistence/espionage), Cybercrime Syndicates (financial/ransomware), Hacktivists (reputation), Insider Threats (privileged access).",
            "STRIDE Model: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege.",
            "Crown Jewels Analysis: Protect core databases, key vaults, and intellectual property with disproportionate rigor.",
        ],
        "dos": [
            "Apply STRIDE threat modeling at the design phase before writing application code.",
            "Differentiate defenses based on realistic threat actor capabilities rather than generic checklists.",
            "Include insider threat detection (e.g. unusual data downloads, off-hours access) in monitoring.",
        ],
        "donts": [
            "Treat all assets as equally valuable—prioritize defense around identified critical data.",
            "Assume external hackers are the only threat; unmonitored privileged insiders cause devastating leaks.",
        ],
        "related": ["security.fundamentals.risk-assessment-methodology", "security.fundamentals.zero-trust-architecture"],
    },
    {
        "subdomain": "fundamentals",
        "slug": "risk-assessment-methodology",
        "name": "Security Risk Assessment Methodology",
        "summary": "Quantitative and qualitative frameworks for identifying, evaluating, and prioritizing cybersecurity risks.",
        "priority": "medium",
        "triggers": [
            "evaluating security vulnerabilities and calculating risk scores",
            "presenting security risk trade-offs to engineering leadership",
            "prioritizing vulnerability remediation schedules (CVSS vs business impact)",
        ],
        "tags": ["security", "risk-assessment", "cvss", "governance"],
        "source_file": "content/cyber-security/1. Cybersecurity Fundamentals/Concepts/Risk Assessment.md",
        "key_insights": [
            "Risk Formula: Risk = Threat × Vulnerability × Asset Impact.",
            "Qualitative vs. Quantitative: Qualitative matrices (Low/Med/High) provide rapid triage; quantitative metrics (SLE, ALE) quantify financial exposure.",
            "Treatment Options: Mitigate (remediate), Transfer (cyber insurance), Accept (business decision), Avoid (decommission).",
        ],
        "dos": [
            "Pair CVSS technical vulnerability scores with business asset criticality to calculate true risk.",
            "Document every accepted risk with executive sign-off and an expiration review date.",
            "Continuously update risk assessments when system architectures or threat landscapes change.",
        ],
        "donts": [
            "Treat CVSS base score in isolation without considering network exposure and compensating controls.",
            "Leave identified vulnerabilities unaddressed without an explicit documented treatment decision.",
        ],
        "related": ["security.system-hardening.vulnerability-assessment-and-prioritization"],
    },

    # 2. Cryptography
    {
        "subdomain": "cryptography",
        "slug": "symmetric-vs-asymmetric-encryption",
        "name": "Symmetric vs Asymmetric Encryption",
        "summary": "Engineering guide for AES bulk encryption, RSA/ECC key exchange, and secure key management.",
        "priority": "high",
        "triggers": [
            "choosing encryption algorithms for data at rest or in transit",
            "implementing hybrid cryptosystems or key exchange protocols",
            "designing secure key rotation and Hardware Security Module (HSM) integrations",
        ],
        "tags": ["security", "cryptography", "encryption", "aes", "rsa", "tls"],
        "source_file": "1-fundamentals/1.2.1.1-Encryption-methods-Symmetric-vs-asymmetric-encryption.md",
        "key_insights": [
            "Symmetric (AES-256-GCM): High throughput, ideal for bulk data and storage encryption. Requires pre-shared key.",
            "Asymmetric (RSA-4096 / ECC secp256r1): Public/private key pairs solve key exchange; computationally intensive.",
            "Hybrid Cryptography: Use asymmetric encryption (e.g. ECDHE) to exchange an ephemeral symmetric session key (e.g. AES-GCM) — used in TLS 1.3.",
            "Key Management: Keys must be generated using cryptographically secure PRNGs (`/dev/urandom`), rotated regularly, and stored in HSMs or KMS.",
        ],
        "dos": [
            "Use AES in authenticated encryption modes (AES-GCM or ChaCha20-Poly1305) to guarantee both confidentiality and authenticity.",
            "Use Elliptic Curve Cryptography (ECDSA/Ed25519) instead of legacy RSA for smaller keys and faster handshakes.",
            "Isolate master keys in cloud KMS (AWS KMS, Azure Key Vault, HashiCorp Vault) with envelope encryption.",
        ],
        "donts": [
            "Never use ECB mode (Electronic Codebook) for AES—it leaks plaintext structural patterns.",
            "Never invent custom encryption algorithms or roll your own cryptographic primitives.",
            "Never hardcode encryption keys, passphrases, or IVs in source code.",
        ],
        "related": ["security.cryptography.hashing-and-integrity", "security.cryptography.digital-signatures-and-pki"],
    },
    {
        "subdomain": "cryptography",
        "slug": "hashing-and-integrity",
        "name": "Cryptographic Hashing & Data Integrity",
        "summary": "Secure hashing with SHA-256/SHA-3, collision attack defenses, and salted password storage with Argon2/bcrypt.",
        "priority": "high",
        "triggers": [
            "storing user passwords or credentials in a database",
            "verifying software download integrity or file tampering",
            "implementing HMAC signatures for API authentication",
        ],
        "tags": ["security", "cryptography", "hashing", "passwords", "argon2", "sha256"],
        "source_file": "1-fundamentals/1.2.2.1-Hashing-algorithms-MD5-SHA-256-and-collision-attacks.md",
        "key_insights": [
            "One-Way Function: Deterministic, pre-image resistant, second pre-image resistant, and collision resistant.",
            "General Hashing (SHA-256, SHA-3, BLAKE3): Designed to be fast; ideal for checksums, HMACs, and digital signatures.",
            "Password Hashing (Argon2id, bcrypt, PBKDF2): Deliberately slow and memory-hard to neutralize GPU/ASIC brute force attacks.",
            "Salting: Unique cryptographically random salt per user prevents rainbow table attacks.",
        ],
        "dos": [
            "Use Argon2id (or bcrypt) with an appropriate work factor for all password storage.",
            "Use HMAC-SHA256 for authenticating API webhooks and tamper-proofing tokens.",
            "Validate file and firmware checksums against published SHA-256 digests before execution.",
        ],
        "donts": [
            "Never use MD5 or SHA-1 for security purposes—practical collision attacks exist.",
            "Never use fast hashing algorithms (SHA-256, MD5) for password storage without slow key derivation.",
            "Never reuse salts across multiple password entries.",
        ],
        "related": ["security.cryptography.symmetric-vs-asymmetric-encryption", "security.access-control.access-control-models"],
    },
    {
        "subdomain": "cryptography",
        "slug": "digital-signatures-and-pki",
        "name": "Digital Signatures & Public Key Infrastructure (PKI)",
        "summary": "Non-repudiation, X.509 certificate validation, Certificate Authorities, and certificate pinning.",
        "priority": "medium",
        "triggers": [
            "configuring TLS/SSL certificates and automated renewal (Let's Encrypt)",
            "implementing digital document or code signing",
            "enforcing mutual TLS (mTLS) for microservices",
        ],
        "tags": ["security", "pki", "digital-signatures", "certificates", "tls", "x509"],
        "source_file": "1-fundamentals/1.2.2.2-Digital-signatures-and-certificate-authorities.md",
        "key_insights": [
            "Digital Signatures provide authentication, data integrity, and non-repudiation (sender cannot deny creating message).",
            "PKI Hierarchy: Root CAs sign Intermediate CAs, which sign End-Entity (server/client) certificates.",
            "Certificate Revocation: CRLs (Certificate Revocation Lists) and OCSP (Online Certificate Status Protocol) monitor revoked certs.",
            "mTLS: Both client and server present X.509 certificates, authenticating identity in both directions.",
        ],
        "dos": [
            "Automate certificate provisioning and renewals using ACME (Let's Encrypt, Cert-Manager) to prevent expiry outages.",
            "Use ECDSA or Ed25519 for modern digital signatures.",
            "Implement mTLS for all inter-service communications in containerized and Kubernetes environments.",
        ],
        "donts": [
            "Disable certificate chain verification (`verify=False` or insecure flags) in production code.",
            "Expose internal root CA private keys on internet-facing servers.",
        ],
        "related": ["security.cryptography.symmetric-vs-asymmetric-encryption", "security.network-security.network-security-monitoring"],
    },

    # 3. Access Control
    {
        "subdomain": "access-control",
        "slug": "access-control-models",
        "name": "Access Control Models (DAC, MAC, RBAC, ABAC)",
        "summary": "Implementation principles for Discretionary, Mandatory, Role-Based, and Attribute-Based Access Control.",
        "priority": "high",
        "triggers": [
            "designing authorization systems or user permission schemas",
            "implementing multi-tenant role-based access in web applications",
            "auditing user privilege boundaries and privilege escalation risks",
        ],
        "tags": ["security", "access-control", "rbac", "abac", "authorization"],
        "source_file": "1-fundamentals/1.2.1.2-Access-control-mechanisms-DAC-MAC-RBAC.md",
        "key_insights": [
            "DAC (Discretionary): Data owner specifies permissions (e.g. Linux file chmod). Flexible but prone to privilege sprawl.",
            "MAC (Mandatory): Central authority labels data and subjects (e.g. SELinux, Military Clearance). Strict, tamper-proof.",
            "RBAC (Role-Based): Users belong to roles; roles have permissions. Clean and scalable for enterprise business apps.",
            "ABAC (Attribute-Based): Fine-grained policies based on subject, resource, action, and environment (time, IP, device).",
        ],
        "dos": [
            "Default to deny: all access requests must be explicitly authorized.",
            "Separate authentication (AuthN - who you are) from authorization (AuthZ - what you can do).",
            "Use RBAC for standard roles and ABAC for context-aware or multi-tenant permission rules.",
        ],
        "donts": [
            "Hardcode role checks in client-side code without enforcing authorization on every API endpoint.",
            "Rely solely on user IDs in URL parameters without validating tenant authorization (IDOR vulnerability).",
        ],
        "related": ["security.fundamentals.zero-trust-architecture", "security.app-security.api-security-best-practices"],
    },
    {
        "subdomain": "access-control",
        "slug": "privilege-management",
        "name": "Operating System Security & Privilege Management",
        "summary": "Hardening OS privilege boundaries, sudoers configuration, UAC, and mitigating privilege escalation.",
        "priority": "high",
        "triggers": [
            "configuring Linux sudoers or Windows User Account Control (UAC)",
            "running container processes or system daemons with restricted privileges",
            "reviewing SUID/SGID binaries and Linux capability assignments",
        ],
        "tags": ["security", "privilege-management", "linux", "windows", "sudo", "hardening"],
        "source_file": "content/cyber-security/5. Operating System Security & Privilege Management/5. Operating System Security & Privilege Management.md",
        "key_insights": [
            "Never run workloads as root: containers and services must execute under dedicated unprivileged service accounts.",
            "SUID/SGID Binaries: Binaries with SUID bits execute with file owner permissions—a primary local privilege escalation target.",
            "Linux Capabilities: Grant fine-grained capabilities (e.g. `CAP_NET_BIND_SERVICE`) instead of full root access.",
            "JIT & PAM: Use Privileged Access Management (PAM) with just-in-time elevation and session auditing.",
        ],
        "dos": [
            "Audit `sudoers` configurations and require passwords for privileged operations; avoid `NOPASSWD: ALL`.",
            "Strip unnecessary SUID/SGID bits (`find / -perm -4000`) across all server images.",
            "Enforce SELinux or AppArmor profiles on Linux hosts to constrain daemon capabilities.",
        ],
        "donts": [
            "Deploy production Docker containers running as root (`UID 0`).",
            "Grant generic developer accounts permanent administrative or root access on production servers.",
        ],
        "related": ["security.system-hardening.system-hardening-baseline", "security.access-control.access-control-models"],
    },

    # 4. Network Security
    {
        "subdomain": "network-security",
        "slug": "network-security-monitoring",
        "name": "Network Security & Traffic Monitoring",
        "summary": "Network protocol analysis, IDS/IPS deployment (Suricata/Zeek), firewall architecture, and packet inspection.",
        "priority": "high",
        "triggers": [
            "investigating suspicious network traffic or packet captures (PCAP)",
            "configuring Network Intrusion Detection Systems (NIDS) or firewalls",
            "analyzing DNS, TCP/IP, or HTTP/TLS handshake anomalies",
        ],
        "tags": ["security", "network-security", "ids", "ips", "wireshark", "zeek", "firewall"],
        "source_file": "content/cyber-security/2. Network Security & Monitoring/2. Network Security & Monitoring.md",
        "key_insights": [
            "Stateful vs Stateless Firewalls: Stateful firewalls track connection state tables, blocking unsolicited incoming packets.",
            "IDS vs IPS: Intrusion Detection Systems (IDS) alert on anomalous signatures; Intrusion Prevention Systems (IPS) inline-block packets.",
            "Network Telemetry: NetFlow/IPFIX metadata provides broad visibility; full packet inspection (PCAP) provides deep forensic detail.",
            "DNS Monitoring: DNS requests are the most frequent indicator of early malware command-and-control communication.",
        ],
        "dos": [
            "Monitor internal east-west traffic between servers, not just north-south perimeter edge traffic.",
            "Inspect DNS queries for DNS tunneling, high-entropy subdomain generation (DGA), and known malicious domains.",
            "Capture PCAPs immediately upon detecting critical intrusion alerts before memory buffers overwrite.",
        ],
        "donts": [
            "Leave management ports (SSH 22, RDP 3389) open to the public internet.",
            "Assume encrypted TLS traffic cannot be monitored: inspect SNI, certificate metadata, and connection volume.",
        ],
        "related": ["security.network-security.ddos-mitigation-architecture", "security.fundamentals.cyber-kill-chain"],
    },
    {
        "subdomain": "network-security",
        "slug": "ddos-mitigation-architecture",
        "name": "DDoS Mitigation Strategies & Resilience",
        "summary": "Architectural defenses against Volumetric, Protocol (SYN Flood), and Application-layer (HTTP Flood) DDoS attacks.",
        "priority": "medium",
        "triggers": [
            "architecting internet-facing systems against denial-of-service attacks",
            "configuring edge rate limiting, Cloudflare, or AWS Shield",
            "responding to unexpected web service availability degradation",
        ],
        "tags": ["security", "ddos", "rate-limiting", "cdn", "availability"],
        "source_file": "1-fundamentals/1.2.3.2-DDoS-attack-mitigation-strategies.md",
        "key_insights": [
            "Attack Categories: Volumetric (NTP/DNS amplification saturated pipe), Protocol (SYN flood exhausting state tables), Application (Slowloris, complex query spam).",
            "Anycast Routing: Distributes incoming traffic across dozens of globally distributed edge PoPs to absorb volumetric spikes.",
            "SYN Cookies: Kernel defense enabling servers to acknowledge TCP connections without storing state until handshake completes.",
            "Edge Rate Limiting & WAF: Filters malicious HTTP flood bots before requests reach origin backend servers.",
        ],
        "dos": [
            "Place internet-facing web apps behind Anycast CDN and DDoS scrubbing networks (Cloudflare, AWS CloudFront).",
            "Enable SYN cookies (`net.ipv4.tcp_syncookies = 1`) on Linux servers.",
            "Implement aggressive rate limiting and adaptive CAPTCHA challenges on expensive API routes (login, search, checkout).",
        ],
        "donts": [
            "Expose the true origin IP address of web servers—attackers will bypass CDN/WAF defenses directly.",
            "Design database queries that execute unpaginated full-table scans easily triggered by malicious requests.",
        ],
        "related": ["security.network-security.network-security-monitoring", "security.app-security.api-security-best-practices"],
    },

    # 5. Application Security
    {
        "subdomain": "app-security",
        "slug": "owasp-top-10-defenses",
        "name": "OWASP Top 10 Web Application Defenses",
        "summary": "Practical countermeasures against the most critical web application security risks.",
        "priority": "high",
        "triggers": [
            "performing code reviews for web applications and APIs",
            "designing input validation, authentication, and session handling",
            "preparing web services for application penetration tests",
        ],
        "tags": ["security", "owasp", "web-security", "appsec", "vulnerabilities"],
        "source_file": "content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md",
        "key_insights": [
            "A01 Broken Access Control: Failure to enforce least privilege on endpoints and resources (IDOR, missing function-level auth).",
            "A02 Cryptographic Failures: Transmitting data in plaintext, using weak algorithms, hardcoding secrets.",
            "A03 Injection: SQL, Command, NoSQL, and LDAP injection from untrusted input.",
            "A05 Security Misconfiguration: Default accounts, unpatched components, verbose error stack traces.",
            "A07 Identification & Authentication Failures: Credential stuffing, missing MFA, session hijacking.",
        ],
        "dos": [
            "Validate and sanitize all user input using strict allowlists (type, length, format).",
            "Enforce authorization checks on every single API route at the business logic layer.",
            "Disable debug mode and verbose stack traces in production environments.",
        ],
        "donts": [
            "Rely on client-side validation (HTML attributes, JS checks) for security enforcement.",
            "Trust user-supplied IDs or roles directly from request payloads or query parameters.",
        ],
        "related": ["security.app-security.sql-injection-prevention", "security.app-security.api-security-best-practices"],
    },
    {
        "subdomain": "app-security",
        "slug": "sql-injection-prevention",
        "name": "SQL Injection (SQLi) Prevention",
        "summary": "Eliminating SQL injection vulnerabilities using parameterized queries, prepared statements, and ORMs.",
        "priority": "high",
        "triggers": [
            "writing database queries or data access layers",
            "reviewing SQL query construction for untrusted inputs",
            "auditing dynamic query builders and ORM raw query calls",
        ],
        "tags": ["security", "sqli", "database", "injection", "appsec"],
        "source_file": "content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md",
        "key_insights": [
            "Root Cause: Mixing untrusted user data with SQL code commands, altering query syntax.",
            "Parameterized Queries: The database engine compiles SQL structure first, then binds parameters strictly as literal data.",
            "Stored Procedures: Safe only when using parameters, not when dynamically concatenating strings inside the procedure.",
            "Least Privilege Database Accounts: Web applications must connect using restricted database users, not `sa` or `root`.",
        ],
        "dos": [
            "Always use parameterized queries or prepared statements across all database interactions.",
            "Use ORMs (Entity Framework, Prisma, SQLAlchemy) properly and avoid raw unparameterized SQL helpers.",
            "Apply principle of least privilege to database credentials (e.g. read-only where modification isn't required).",
        ],
        "donts": [
            "Never concatenate or format user input directly into SQL query strings (e.g. `f\"SELECT * FROM users WHERE id = '{user_id}'\"`).",
            "Never rely on custom character escaping or blacklisting quotes as primary injection defense.",
        ],
        "related": ["security.app-security.owasp-top-10-defenses", "security.app-security.api-security-best-practices"],
    },
    {
        "subdomain": "app-security",
        "slug": "api-security-best-practices",
        "name": "API Security & Token Protection",
        "summary": "Securing REST and GraphQL APIs using JWT validation, rate limiting, CORS, and schema verification.",
        "priority": "high",
        "triggers": [
            "designing or implementing public or internal REST/GraphQL APIs",
            "configuring JWT authentication, refresh tokens, and revocation",
            "setting up API gateway rate limiting and CORS headers",
        ],
        "tags": ["security", "api", "jwt", "cors", "rest", "tokens"],
        "source_file": "content/cyber-security/6. Web & Application Security Essentials/6. Web & Application Security Essentials.md",
        "key_insights": [
            "JWT Validation: Always verify signature, expiration (`exp`), issuer (`iss`), and algorithm (reject `alg: none`).",
            "BOLA / IDOR: Broken Object Level Authorization is the #1 API vulnerability—verify user ownership of requested resource IDs.",
            "Rate Limiting: Token-bucket or sliding-window rate limiting prevents credential stuffing and denial of service.",
            "CORS: Cross-Origin Resource Sharing is a browser mechanism; it does not protect against non-browser clients (curl, Postman).",
        ],
        "dos": [
            "Validate incoming JSON payloads against strict schemas (Pydantic, Zod, JSON Schema).",
            "Store sensitive session tokens in `HttpOnly`, `Secure`, `SameSite=Strict` cookies rather than `localStorage`.",
            "Implement granular rate limiting tied to API keys, authenticated user IDs, and client IP addresses.",
        ],
        "donts": [
            "Return raw database entities in API responses—filter out internal IDs, passwords, and sensitive fields.",
            "Use wildcard `Access-Control-Allow-Origin: *` alongside `Access-Control-Allow-Credentials: true`.",
        ],
        "related": ["security.app-security.owasp-top-10-defenses", "security.access-control.access-control-models"],
    },

    # 6. Cloud Security
    {
        "subdomain": "cloud-security",
        "slug": "cloud-security-fundamentals",
        "name": "Cloud Security Posture & IAM Hardening",
        "summary": "Shared Responsibility Model, least-privilege IAM policies, cloud storage security, and CSPM baselines.",
        "priority": "high",
        "triggers": [
            "architecting cloud infrastructure (AWS, Azure, GCP)",
            "configuring cloud IAM roles, bucket policies, and security groups",
            "auditing cloud misconfigurations and public asset exposures",
        ],
        "tags": ["security", "cloud", "aws", "azure", "iam", "s3", "cspm"],
        "source_file": "content/cyber-security/8. Cloud Security Fundamentals/8. Cloud Security Fundamentals.md",
        "key_insights": [
            "Shared Responsibility: Cloud provider secures the cloud (hardware, facilities); customer secures what's in the cloud (data, IAM, network).",
            "IAM Principle: Never use root accounts for workloads; use temporary STS role credentials instead of long-lived access keys.",
            "Storage Bucket Security: S3 buckets and Azure blobs must block public access by default, with encryption at rest enabled.",
            "Cloud Security Posture Management (CSPM): Continuous automated auditing for compliance drift and open security groups.",
        ],
        "dos": [
            "Enforce multi-factor authentication (MFA) on all cloud management console accounts.",
            "Enable cloud audit logging (AWS CloudTrail, Azure Activity Log) with log integrity validation and centralized forwarding.",
            "Use infrastructure-as-code (Terraform, CloudFormation) with automated security linting (Checkov, tfsec).",
        ],
        "donts": [
            "Commit cloud access keys (`AKIA...`) or service account JSON files to Git repositories.",
            "Allow `0.0.0.0/0` inbound rules on security groups for sensitive administrative ports (SSH, RDP, databases).",
        ],
        "related": ["security.fundamentals.zero-trust-architecture", "security.system-hardening.system-hardening-baseline"],
    },

    # 7. System Hardening & Vulnerability Management
    {
        "subdomain": "system-hardening",
        "slug": "system-hardening-baseline",
        "name": "System Hardening & Baseline Configuration",
        "summary": "Applying CIS Benchmarks, disabling unnecessary services, configuring OSSEC/auditd, and host firewalling.",
        "priority": "high",
        "triggers": [
            "provisioning production virtual machines or golden OS images",
            "applying Center for Internet Security (CIS) hardening benchmarks",
            "configuring Linux auditd, systemd security, or Windows Group Policies",
        ],
        "tags": ["security", "hardening", "cis-benchmarks", "auditd", "linux", "baseline"],
        "source_file": "content/cyber-security/7. System Hardening & Security Monitoring/7. System Hardening & Security Monitoring.md",
        "key_insights": [
            "Minimize Attack Surface: Remove or disable unused network protocols, background daemons, and software packages.",
            "CIS Benchmarks: Industry-standard consensus hardening baselines for Linux, Windows, Kubernetes, and cloud providers.",
            "Immutable Infrastructure: Deploy stateless immutable host images and replace rather than patch in-place.",
            "Audit Logging: Configure Linux `auditd` to capture system calls for privilege escalation, file modifications, and network connections.",
        ],
        "dos": [
            "Automate baseline configuration via Ansible or Packer using official CIS Benchmark playbooks.",
            "Disable legacy and insecure protocols (Telnet, FTP, SMBv1, TLS 1.0/1.1).",
            "Forward all host system logs immediately to a centralized, tamper-resistant SIEM.",
        ],
        "donts": [
            "Run services under default factory passwords or unconfigured default settings.",
            "Leave development tools (compilers, debuggers) installed on production application servers.",
        ],
        "related": ["security.access-control.privilege-management", "security.system-hardening.vulnerability-assessment-and-prioritization"],
    },
    {
        "subdomain": "system-hardening",
        "slug": "vulnerability-assessment-and-prioritization",
        "name": "Vulnerability Assessment & Prioritization",
        "summary": "Systematic scanning, CVSS 3.1/4.0 scoring, vulnerability validation, and SLA-driven remediation workflows.",
        "priority": "medium",
        "triggers": [
            "running automated vulnerability scans (Nessus, OpenVAS, Trivy)",
            "triaging CVE alerts and dependency security warnings",
            "establishing vulnerability remediation SLAs and patch policies",
        ],
        "tags": ["security", "vulnerability-assessment", "cve", "cvss", "patching"],
        "source_file": "content/cyber-security/4. Vulnerability Assessment & Risk Prioritization/4. Vulnerability Assessment & Risk Prioritization.md",
        "key_insights": [
            "Scanning Cadence: Run automated non-intrusive scans weekly and full credentialed scans monthly or post-deployment.",
            "Contextual Prioritization: A Critical CVSS (9.8) on an isolated internal server without public access may be lower real risk than a Medium CVSS on an internet-facing API.",
            "Remediation SLAs: Critical (remediate within 24-48h), High (within 7-14 days), Medium (within 30 days).",
        ],
        "dos": [
            "Integrate Software Composition Analysis (SCA) scanners (Trivy, Snyk) into CI/CD build pipelines.",
            "Verify exploitability before panicking: check whether known public exploits (EPSS score, CISA KEV catalog) exist.",
            "Enforce strict automated patching for base operating systems and container base images.",
        ],
        "donts": [
            "Rely exclusively on unauthenticated external scans—credentialed scans reveal deep internal package vulnerabilities.",
            "Ignore low or medium severity findings that can be chained together by an attacker to achieve full compromise.",
        ],
        "related": ["security.fundamentals.risk-assessment-methodology", "security.app-security.owasp-top-10-defenses"],
    },

    # 8. Incident Response
    {
        "subdomain": "incident-response",
        "slug": "incident-response-lifecycle",
        "name": "Incident Response Lifecycle (NIST / SANS)",
        "summary": "6-phase incident response methodology: Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned.",
        "priority": "high",
        "triggers": [
            "handling an active security incident or breach alert",
            "authoring incident response runbooks and escalation trees",
            "conducting post-incident reviews (blameless post-mortems)",
        ],
        "tags": ["security", "incident-response", "nist", "sans", "forensics"],
        "source_file": "content/cyber-security/9. Incident Response & Reporting/9. Incident Response & Reporting.md",
        "key_insights": [
            "Phase 1: Preparation (tools, jumpboxes, communications out-of-band, access policies).",
            "Phase 2: Identification (triage alerts, confirm true positive, establish scope of breach).",
            "Phase 3: Containment (short-term network isolation vs long-term system segmentation while preserving forensic evidence).",
            "Phase 4: Eradication (clean malware, rotate compromised credentials, patch root-cause vulnerabilities).",
            "Phase 5: Recovery (re-introduce systems with heightened monitoring, test business functions).",
            "Phase 6: Lessons Learned (document timeline, identify defensive gaps, update runbooks within 2 weeks).",
        ],
        "dos": [
            "Isolate compromised machines from the network without powering off immediately to preserve volatile RAM evidence.",
            "Establish out-of-band communication channels (Signal, phone) in case email/Slack is compromised.",
            "Conduct blameless post-mortems and track remediation action items to completion.",
        ],
        "donts": [
            "Power off or reboot an infected machine immediately—this destroys critical volatile memory forensic artifacts.",
            "Declare an incident resolved before verifying eradication and rotating all potentially exposed secrets.",
        ],
        "related": ["security.incident-response.backup-and-disaster-recovery", "security.fundamentals.cyber-kill-chain"],
    },
    {
        "subdomain": "incident-response",
        "slug": "backup-and-disaster-recovery",
        "name": "Backup Strategies & Disaster Recovery (DR)",
        "summary": "The 3-2-1 backup rule, immutable backups against ransomware, and RPO/RTO engineering metrics.",
        "priority": "high",
        "triggers": [
            "designing enterprise backup and disaster recovery architecture",
            "defending against ransomware data destruction scenarios",
            "establishing Recovery Point Objective (RPO) and Recovery Time Objective (RTO)",
        ],
        "tags": ["security", "backup", "disaster-recovery", "ransomware", "rpo", "rto"],
        "source_file": "1-fundamentals/1.2.3.3-Backup-and-disaster-recovery-planning.md",
        "key_insights": [
            "3-2-1 Rule: 3 copies of data, across 2 different media types, with 1 copy stored offsite/offline.",
            "Immutable Backups: Write-Once-Read-Many (WORM) storage prevents ransomware operators from deleting backups even with compromised admin credentials.",
            "RPO (Recovery Point Objective): Maximum acceptable data loss duration (e.g. 15 minutes of transactions).",
            "RTO (Recovery Time Objective): Maximum acceptable downtime before service restoration (e.g. 2 hours).",
        ],
        "dos": [
            "Enforce air-gapped or immutable cloud backup policies (e.g. AWS S3 Object Lock in Compliance Mode).",
            "Separate backup infrastructure credentials from general production administrative domains.",
            "Schedule automated disaster recovery drill simulations at least quarterly.",
        ],
        "donts": [
            "Store backup storage credentials on the same servers being backed up.",
            "Assume backups are working without regular test restores and checksum validations.",
        ],
        "related": ["security.fundamentals.cia-triad", "security.incident-response.incident-response-lifecycle"],
    },
    {
        "subdomain": "incident-response",
        "slug": "bug-bounty-and-responsible-disclosure",
        "name": "Bug Bounty & Responsible Vulnerability Disclosure",
        "summary": "Authoring security.txt, defining safe harbor scopes, vulnerability triage, and coordinating patches.",
        "priority": "medium",
        "triggers": [
            "establishing a Vulnerability Disclosure Policy (VDP) or bug bounty program",
            "deploying a security.txt file (RFC 9116) for security researchers",
            "triaging incoming external security vulnerability reports",
        ],
        "tags": ["security", "bug-bounty", "vdp", "responsible-disclosure", "security-txt"],
        "source_file": "content/cyber-security/11. Bug Bounty & Responsible Disclosure/11. Bug Bounty & Responsible Disclosure.md",
        "key_insights": [
            "RFC 9116 security.txt: Standardized machine-readable file located at `/.well-known/security.txt` defining security contact info.",
            "Safe Harbor: Legal commitment that good-faith security researchers will not face legal action when following policy guidelines.",
            "Clear Scope: Explicitly specify which domains, APIs, and techniques (e.g. no DoS, no social engineering) are in-scope.",
            "Triage & SLA: Acknowledge researcher reports within 24-48 hours and coordinate embargoed public disclosure post-patch.",
        ],
        "dos": [
            "Publish a `/.well-known/security.txt` on all public domains containing contact emails and encryption keys.",
            "Include explicit legal Safe Harbor terms protecting good-faith researchers.",
            "Validate and triage incoming reports with reproducing proof-of-concept steps before prioritizing fixes.",
        ],
        "donts": [
            "Threaten legal action against researchers who responsibly report vulnerabilities without accessing user data.",
            "Ignore reports received via security contacts, which risks uncoordinated zero-day public disclosure.",
        ],
        "related": ["security.system-hardening.vulnerability-assessment-and-prioritization"],
    },

    # 9. AI & Modern Threat Landscape
    {
        "subdomain": "ai-security",
        "slug": "ai-threat-detection",
        "name": "AI in Threat Detection & Behavioral Analytics",
        "summary": "Machine learning for security telemetry, UEBA anomaly detection, and reducing alert fatigue.",
        "priority": "medium",
        "triggers": [
            "evaluating or building AI/ML models for threat detection or SIEM",
            "implementing User and Entity Behavior Analytics (UEBA)",
            "tuning security detection algorithms to reduce false positives",
        ],
        "tags": ["security", "ai", "machine-learning", "threat-detection", "ueba", "siem"],
        "source_file": "content/cyber-security/12. Cybersecurity and AI/12. Cybersecurity and AI.md",
        "key_insights": [
            "Behavioral Baselining: ML models learn normal user/network patterns and flag statistical anomalies (unusual data volume, abnormal login geography).",
            "Alert Correlation: AI correlates hundreds of low-fidelity alerts into a single contextual attack story.",
            "False Positive Reduction: Supervised models learn from analyst feedback to suppress recurring benign alerts.",
        ],
        "dos": [
            "Establish clean baseline training data to avoid poisoning model perception of normal activity.",
            "Combine ML anomaly scores with deterministic rule-based triggers for high-confidence alerting.",
            "Maintain human-in-the-loop validation for critical automated isolation actions.",
        ],
        "donts": [
            "Rely entirely on black-box ML models without explainable feature attribution for security analysts.",
            "Train security models on static historical datasets without periodic re-training against emerging attack vectors.",
        ],
        "related": ["security.ai-security.ai-security-orchestration-soar", "security.ai-security.adversarial-machine-learning"],
    },
    {
        "subdomain": "ai-security",
        "slug": "ai-security-orchestration-soar",
        "name": "AI-Powered Security Orchestration (SOAR)",
        "summary": "Automating incident triage, playbook execution, and threat containment with AI and SOAR platforms.",
        "priority": "medium",
        "triggers": [
            "designing automated incident response playbooks (SOAR)",
            "integrating AI agents into SOC analyst workflows",
            "automating threat containment actions (IP blocking, credential revocation)",
        ],
        "tags": ["security", "soar", "automation", "ai", "soc", "playbooks"],
        "source_file": "content/cyber-security/12. Cybersecurity and AI/Concepts/AI-Powered Security Orchestration (SOAR).md",
        "key_insights": [
            "SOAR Core: Security Orchestration, Automation, and Response connects disparate security tools into unified automated workflows.",
            "Triage Acceleration: AI parses threat intelligence, enriches IP/file indicators, and prioritizes incidents in seconds.",
            "Automated Playbooks: Standardized response sequences executed without delay (e.g. isolate infected host, revoke session tokens).",
        ],
        "dos": [
            "Automate repetitive low-risk enrichment tasks first before enabling automated destructive containment.",
            "Include rollback mechanisms in every automated playbook.",
            "Audit all automated SOAR actions with detailed execution logs.",
        ],
        "donts": [
            "Enable autonomous blocking without confidence score thresholds that could disrupt critical production services.",
        ],
        "related": ["security.incident-response.incident-response-lifecycle", "security.ai-security.ai-threat-detection"],
    },
    {
        "subdomain": "ai-security",
        "slug": "adversarial-machine-learning",
        "name": "Adversarial Machine Learning & LLM Security",
        "summary": "Defending AI systems against prompt injection, model evasion, training data poisoning, and model extraction.",
        "priority": "high",
        "triggers": [
            "building or deploying Large Language Model (LLM) applications or agents",
            "hardening AI systems against prompt injection and jailbreaking",
            "evaluating security risks in machine learning pipelines and training data",
        ],
        "tags": ["security", "ai", "adversarial-ml", "llm-security", "prompt-injection", "owasp-llm"],
        "source_file": "content/cyber-security/12. Cybersecurity and AI/Concepts/Adversarial Machine Learning.md",
        "key_insights": [
            "Prompt Injection: Attackers craft untrusted user input that overrides system prompts, tricking the LLM into unauthorized actions.",
            "Indirect Prompt Injection: Malicious instructions embedded in external retrieved content (web pages, PDFs, emails).",
            "Data Poisoning: Injecting compromised samples into training or fine-tuning datasets to create backdoors.",
            "Model Evasion: Perturbing input features imperceptibly to cause ML classifiers to misclassify malicious payloads.",
        ],
        "dos": [
            "Treat all LLM output as untrusted before feeding it into backend systems, databases, or shell execution tools.",
            "Implement dual LLM validation architectures (guardrail models) to inspect inputs and outputs for prompt injection.",
            "Enforce strict tool authorization and human approval gates for sensitive actions executed by AI agents.",
        ],
        "donts": [
            "Grant autonomous AI agents direct, unconstrained access to write databases, delete files, or send external emails.",
            "Assume system instructions in prompts are secret—LLM prompt extraction techniques are widely effective.",
        ],
        "related": ["security.ai-security.ai-threat-detection", "security.app-security.owasp-top-10-defenses"],
    },
]


def generate_markdown(skill_def):
    """Generate Markdown with Schema v1.0 YAML frontmatter."""
    fm = {
        "id": f"security.{skill_def['subdomain']}.{skill_def['slug']}",
        "name": skill_def["name"],
        "version": "1.0.0",
        "domain": "security",
        "subdomain": skill_def["subdomain"],
        "summary": skill_def["summary"],
        "triggers": skill_def["triggers"],
        "tags": skill_def["tags"],
        "priority": skill_def["priority"],
        "dependencies": [],
        "related_skills": skill_def.get("related", []),
        "source": {
            "name": "cyber-security-vault",
            "url": "https://github.com/DinushaNaween/cyber-sec",
            "reference_file": skill_def.get("source_file", ""),
        },
        "last_updated": "2026-09-14",
    }

    fm_yaml = yaml.dump(fm, sort_keys=False, allow_unicode=True, width=120)

    lines = [
        "---",
        fm_yaml.strip(),
        "---",
        "",
        f"# {skill_def['name']}",
        "",
        f"> {skill_def['summary']}",
        "",
        "## When to Use (Triggers)",
        "",
    ]
    for trigger in skill_def["triggers"]:
        lines.append(f"- {trigger}")

    lines.extend(["", "## Key Insights & Principles", ""])
    for insight in skill_def["key_insights"]:
        lines.append(f"- {insight}")

    lines.extend(["", "## Do's and Don'ts", ""])
    for d in skill_def["dos"]:
        lines.append(f"- **Do:** {d}")
    for d in skill_def["donts"]:
        lines.append(f"- **Don't:** {d}")

    # Check if there is extra practical content from source file
    source_rel = skill_def.get("source_file")
    extra_content = ""
    if source_rel:
        src_path = SOURCE_DIR / source_rel
        if src_path.exists():
            content = src_path.read_text(encoding="utf-8")
            # Extract sections like Practical Applications or Tools
            tools_match = re.search(r"## (?:Tools & Techniques|Implementation Components|Core Pillars.*?)(.*?)(?:##|\Z)", content, re.DOTALL)
            if tools_match:
                extra_content = tools_match.group(1).strip()

    if extra_content:
        lines.extend(["", "## Practical Implementation & Architecture", "", extra_content])

    if skill_def.get("related"):
        lines.extend(["", "## Related Skills", ""])
        for rel in skill_def["related"]:
            lines.append(f"- `{rel}`")

    lines.append("")
    return "\n".join(lines)


def main():
    created = 0
    for s in SECURITY_SKILLS:
        sub_dir = SKILLS_DIR / s["subdomain"]
        sub_dir.mkdir(parents=True, exist_ok=True)
        target_file = sub_dir / f"{s['slug']}.md"
        content = generate_markdown(s)
        target_file.write_text(content, encoding="utf-8")
        created += 1
        print(f"Created: {target_file}")

    print(f"\nSuccessfully generated {created} security skills under {SKILLS_DIR}/")


if __name__ == "__main__":
    main()
