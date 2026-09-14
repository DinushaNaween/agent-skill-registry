# AI Agent Skill Registry

> Central capability index for autonomous AI agents and developers.
> **Total Skills:** 102 | **Last Updated:** 2026-09-14

## How Agents Use This Registry

1. **Analyze Task:** Identify relevant domain and action keywords.
2. **Match Triggers:** Scan the `Triggers` list below or query `registry.json`.
3. **Selective Load:** Read only the matched skill file path into working context.
4. **Execute:** Apply the specific insights, rules, and code patterns.

---

## Security Domain (`security`)

### Access Control (2)

#### Access Control Models (DAC, MAC, RBAC, ABAC)
- **Path:** [`skills/security/access-control/access-control-models.md`](skills/security/access-control/access-control-models.md)
- **Summary:** Implementation principles for Discretionary, Mandatory, Role-Based, and Attribute-Based Access Control.
- **Triggers:** designing authorization systems or user permission schemas; implementing multi-tenant role-based access in web applications; auditing user privilege boundaries and privilege escalation risks
- **Tags:** `security, access-control, rbac, abac, authorization`

#### Operating System Security & Privilege Management
- **Path:** [`skills/security/access-control/privilege-management.md`](skills/security/access-control/privilege-management.md)
- **Summary:** Hardening OS privilege boundaries, sudoers configuration, UAC, and mitigating privilege escalation.
- **Triggers:** configuring Linux sudoers or Windows User Account Control (UAC); running container processes or system daemons with restricted privileges; reviewing SUID/SGID binaries and Linux capability assignments
- **Tags:** `security, privilege-management, linux, windows, sudo, hardening`

### Ai Security (3)

#### AI in Threat Detection & Behavioral Analytics
- **Path:** [`skills/security/ai-security/ai-threat-detection.md`](skills/security/ai-security/ai-threat-detection.md)
- **Summary:** Machine learning for security telemetry, UEBA anomaly detection, and reducing alert fatigue.
- **Triggers:** evaluating or building AI/ML models for threat detection or SIEM; implementing User and Entity Behavior Analytics (UEBA); tuning security detection algorithms to reduce false positives
- **Tags:** `security, ai, machine-learning, threat-detection, ueba, siem`

#### AI-Powered Security Orchestration (SOAR)
- **Path:** [`skills/security/ai-security/ai-security-orchestration-soar.md`](skills/security/ai-security/ai-security-orchestration-soar.md)
- **Summary:** Automating incident triage, playbook execution, and threat containment with AI and SOAR platforms.
- **Triggers:** designing automated incident response playbooks (SOAR); integrating AI agents into SOC analyst workflows; automating threat containment actions (IP blocking, credential revocation)
- **Tags:** `security, soar, automation, ai, soc, playbooks`

#### Adversarial Machine Learning & LLM Security
- **Path:** [`skills/security/ai-security/adversarial-machine-learning.md`](skills/security/ai-security/adversarial-machine-learning.md)
- **Summary:** Defending AI systems against prompt injection, model evasion, training data poisoning, and model extraction.
- **Triggers:** building or deploying Large Language Model (LLM) applications or agents; hardening AI systems against prompt injection and jailbreaking; evaluating security risks in machine learning pipelines and training data
- **Tags:** `security, ai, adversarial-ml, llm-security, prompt-injection, owasp-llm`

### App Security (3)

#### API Security & Token Protection
- **Path:** [`skills/security/app-security/api-security-best-practices.md`](skills/security/app-security/api-security-best-practices.md)
- **Summary:** Securing REST and GraphQL APIs using JWT validation, rate limiting, CORS, and schema verification.
- **Triggers:** designing or implementing public or internal REST/GraphQL APIs; configuring JWT authentication, refresh tokens, and revocation; setting up API gateway rate limiting and CORS headers
- **Tags:** `security, api, jwt, cors, rest, tokens`

#### OWASP Top 10 Web Application Defenses
- **Path:** [`skills/security/app-security/owasp-top-10-defenses.md`](skills/security/app-security/owasp-top-10-defenses.md)
- **Summary:** Practical countermeasures against the most critical web application security risks.
- **Triggers:** performing code reviews for web applications and APIs; designing input validation, authentication, and session handling; preparing web services for application penetration tests
- **Tags:** `security, owasp, web-security, appsec, vulnerabilities`

#### SQL Injection (SQLi) Prevention
- **Path:** [`skills/security/app-security/sql-injection-prevention.md`](skills/security/app-security/sql-injection-prevention.md)
- **Summary:** Eliminating SQL injection vulnerabilities using parameterized queries, prepared statements, and ORMs.
- **Triggers:** writing database queries or data access layers; reviewing SQL query construction for untrusted inputs; auditing dynamic query builders and ORM raw query calls
- **Tags:** `security, sqli, database, injection, appsec`

### Cloud Security (1)

#### Cloud Security Posture & IAM Hardening
- **Path:** [`skills/security/cloud-security/cloud-security-fundamentals.md`](skills/security/cloud-security/cloud-security-fundamentals.md)
- **Summary:** Shared Responsibility Model, least-privilege IAM policies, cloud storage security, and CSPM baselines.
- **Triggers:** architecting cloud infrastructure (AWS, Azure, GCP); configuring cloud IAM roles, bucket policies, and security groups; auditing cloud misconfigurations and public asset exposures
- **Tags:** `security, cloud, aws, azure, iam, s3, cspm`

### Cryptography (3)

#### Cryptographic Hashing & Data Integrity
- **Path:** [`skills/security/cryptography/hashing-and-integrity.md`](skills/security/cryptography/hashing-and-integrity.md)
- **Summary:** Secure hashing with SHA-256/SHA-3, collision attack defenses, and salted password storage with Argon2/bcrypt.
- **Triggers:** storing user passwords or credentials in a database; verifying software download integrity or file tampering; implementing HMAC signatures for API authentication
- **Tags:** `security, cryptography, hashing, passwords, argon2, sha256`

#### Digital Signatures & Public Key Infrastructure (PKI)
- **Path:** [`skills/security/cryptography/digital-signatures-and-pki.md`](skills/security/cryptography/digital-signatures-and-pki.md)
- **Summary:** Non-repudiation, X.509 certificate validation, Certificate Authorities, and certificate pinning.
- **Triggers:** configuring TLS/SSL certificates and automated renewal (Let's Encrypt); implementing digital document or code signing; enforcing mutual TLS (mTLS) for microservices
- **Tags:** `security, pki, digital-signatures, certificates, tls, x509`

#### Symmetric vs Asymmetric Encryption
- **Path:** [`skills/security/cryptography/symmetric-vs-asymmetric-encryption.md`](skills/security/cryptography/symmetric-vs-asymmetric-encryption.md)
- **Summary:** Engineering guide for AES bulk encryption, RSA/ECC key exchange, and secure key management.
- **Triggers:** choosing encryption algorithms for data at rest or in transit; implementing hybrid cryptosystems or key exchange protocols; designing secure key rotation and Hardware Security Module (HSM) integrations
- **Tags:** `security, cryptography, encryption, aes, rsa, tls`

### Fundamentals (7)

#### CIA Triad Principles
- **Path:** [`skills/security/fundamentals/cia-triad.md`](skills/security/fundamentals/cia-triad.md)
- **Summary:** The cornerstone model balancing Confidentiality, Integrity, and Availability in software systems.
- **Triggers:** evaluating security requirements for a new system or feature; conducting security risk assessments and compliance reviews; architecting data protection and disaster recovery strategies
- **Tags:** `security, cia-triad, confidentiality, integrity, availability`

#### Cyber Kill Chain & Attack Lifecycle
- **Path:** [`skills/security/fundamentals/cyber-kill-chain.md`](skills/security/fundamentals/cyber-kill-chain.md)
- **Summary:** Lockheed Martin 7-phase cyberattack lifecycle model and defensive intervention techniques.
- **Triggers:** analyzing an ongoing or simulated security intrusion; designing detection rules and early warning alert triggers; modeling threat actor advancement through internal networks
- **Tags:** `security, kill-chain, threat-intelligence, incident-response`

#### Defense in Depth
- **Path:** [`skills/security/fundamentals/defense-in-depth.md`](skills/security/fundamentals/defense-in-depth.md)
- **Summary:** Multi-layered security strategy ensuring no single defensive failure leads to total system compromise.
- **Triggers:** designing system infrastructure or application security architecture; reviewing single points of failure in security controls; auditing multi-tier security layers (network, host, app, data)
- **Tags:** `security, defense-in-depth, layered-security, architecture`

#### MITRE ATT&CK Framework Mapping
- **Path:** [`skills/security/fundamentals/mitre-attck-framework.md`](skills/security/fundamentals/mitre-attck-framework.md)
- **Summary:** Curated knowledge base of cyber adversary tactics, techniques, and procedures (TTPs).
- **Triggers:** mapping defensive security monitoring to real adversary techniques; conducting threat modeling and red/blue team simulations; assessing security coverage gaps across SIEM detection rules
- **Tags:** `security, mitre, attck, threat-detection, siem`

#### Security Risk Assessment Methodology
- **Path:** [`skills/security/fundamentals/risk-assessment-methodology.md`](skills/security/fundamentals/risk-assessment-methodology.md)
- **Summary:** Quantitative and qualitative frameworks for identifying, evaluating, and prioritizing cybersecurity risks.
- **Triggers:** evaluating security vulnerabilities and calculating risk scores; presenting security risk trade-offs to engineering leadership; prioritizing vulnerability remediation schedules (CVSS vs business impact)
- **Tags:** `security, risk-assessment, cvss, governance`

#### Threat Modeling & Actor Profiling
- **Path:** [`skills/security/fundamentals/threat-modeling-and-actors.md`](skills/security/fundamentals/threat-modeling-and-actors.md)
- **Summary:** Systematic identification of threat actors, capabilities, attack vectors, and high-value targets.
- **Triggers:** conducting threat modeling for architecture design (STRIDE); evaluating adversary motivation (nation-state, cybercrime, insider); identifying critical digital assets and attack surface vectors
- **Tags:** `security, threat-modeling, stride, threat-actors`

#### Zero Trust Architecture
- **Path:** [`skills/security/fundamentals/zero-trust-architecture.md`](skills/security/fundamentals/zero-trust-architecture.md)
- **Summary:** Never trust, always verify: identity-based micro-segmented security architecture.
- **Triggers:** designing cloud or enterprise network architecture; implementing identity and access management (IAM) or MFA; evaluating perimeter vs identity-based access controls
- **Tags:** `security, zero-trust, architecture, iam, network`

### Incident Response (3)

#### Backup Strategies & Disaster Recovery (DR)
- **Path:** [`skills/security/incident-response/backup-and-disaster-recovery.md`](skills/security/incident-response/backup-and-disaster-recovery.md)
- **Summary:** The 3-2-1 backup rule, immutable backups against ransomware, and RPO/RTO engineering metrics.
- **Triggers:** designing enterprise backup and disaster recovery architecture; defending against ransomware data destruction scenarios; establishing Recovery Point Objective (RPO) and Recovery Time Objective (RTO)
- **Tags:** `security, backup, disaster-recovery, ransomware, rpo, rto`

#### Bug Bounty & Responsible Vulnerability Disclosure
- **Path:** [`skills/security/incident-response/bug-bounty-and-responsible-disclosure.md`](skills/security/incident-response/bug-bounty-and-responsible-disclosure.md)
- **Summary:** Authoring security.txt, defining safe harbor scopes, vulnerability triage, and coordinating patches.
- **Triggers:** establishing a Vulnerability Disclosure Policy (VDP) or bug bounty program; deploying a security.txt file (RFC 9116) for security researchers; triaging incoming external security vulnerability reports
- **Tags:** `security, bug-bounty, vdp, responsible-disclosure, security-txt`

#### Incident Response Lifecycle (NIST / SANS)
- **Path:** [`skills/security/incident-response/incident-response-lifecycle.md`](skills/security/incident-response/incident-response-lifecycle.md)
- **Summary:** 6-phase incident response methodology: Preparation, Identification, Containment, Eradication, Recovery, and Lessons Learned.
- **Triggers:** handling an active security incident or breach alert; authoring incident response runbooks and escalation trees; conducting post-incident reviews (blameless post-mortems)
- **Tags:** `security, incident-response, nist, sans, forensics`

### Network Security (2)

#### DDoS Mitigation Strategies & Resilience
- **Path:** [`skills/security/network-security/ddos-mitigation-architecture.md`](skills/security/network-security/ddos-mitigation-architecture.md)
- **Summary:** Architectural defenses against Volumetric, Protocol (SYN Flood), and Application-layer (HTTP Flood) DDoS attacks.
- **Triggers:** architecting internet-facing systems against denial-of-service attacks; configuring edge rate limiting, Cloudflare, or AWS Shield; responding to unexpected web service availability degradation
- **Tags:** `security, ddos, rate-limiting, cdn, availability`

#### Network Security & Traffic Monitoring
- **Path:** [`skills/security/network-security/network-security-monitoring.md`](skills/security/network-security/network-security-monitoring.md)
- **Summary:** Network protocol analysis, IDS/IPS deployment (Suricata/Zeek), firewall architecture, and packet inspection.
- **Triggers:** investigating suspicious network traffic or packet captures (PCAP); configuring Network Intrusion Detection Systems (NIDS) or firewalls; analyzing DNS, TCP/IP, or HTTP/TLS handshake anomalies
- **Tags:** `security, network-security, ids, ips, wireshark, zeek, firewall`

### System Hardening (2)

#### System Hardening & Baseline Configuration
- **Path:** [`skills/security/system-hardening/system-hardening-baseline.md`](skills/security/system-hardening/system-hardening-baseline.md)
- **Summary:** Applying CIS Benchmarks, disabling unnecessary services, configuring OSSEC/auditd, and host firewalling.
- **Triggers:** provisioning production virtual machines or golden OS images; applying Center for Internet Security (CIS) hardening benchmarks; configuring Linux auditd, systemd security, or Windows Group Policies
- **Tags:** `security, hardening, cis-benchmarks, auditd, linux, baseline`

#### Vulnerability Assessment & Prioritization
- **Path:** [`skills/security/system-hardening/vulnerability-assessment-and-prioritization.md`](skills/security/system-hardening/vulnerability-assessment-and-prioritization.md)
- **Summary:** Systematic scanning, CVSS 3.1/4.0 scoring, vulnerability validation, and SLA-driven remediation workflows.
- **Triggers:** running automated vulnerability scans (Nessus, OpenVAS, Trivy); triaging CVE alerts and dependency security warnings; establishing vulnerability remediation SLAs and patch policies
- **Tags:** `security, vulnerability-assessment, cve, cvss, patching`

---

## Ui Ux Domain (`ui-ux`)

### Content (4)

#### Empty States
- **Path:** [`skills/ui-ux/content/empty-states.md`](skills/ui-ux/content/empty-states.md)
- **Summary:** Your empty state is your first impression. Most apps waste it.
- **Triggers:** designing or building empty states components; reviewing UX/UI for empty states; implementing content pattern for empty states
- **Tags:** `ui, ux, content, empty, states`

#### Landing Page Skeleton
- **Path:** [`skills/ui-ux/content/landing-page-skeleton.md`](skills/ui-ux/content/landing-page-skeleton.md)
- **Summary:** Every landing page that converts follows the same 5-section skeleton.
- **Triggers:** designing or building landing page skeleton components; reviewing UX/UI for landing page skeleton; implementing content pattern for landing page skeleton
- **Tags:** `ui, ux, content, landing, page, skeleton`

#### Microcopy
- **Path:** [`skills/ui-ux/content/microcopy.md`](skills/ui-ux/content/microcopy.md)
- **Summary:** Same form. Different words. One converts.
- **Triggers:** designing or building microcopy components; reviewing UX/UI for microcopy; implementing content pattern for microcopy
- **Tags:** `ui, ux, content, microcopy`

#### Serial Position
- **Path:** [`skills/ui-ux/content/serial-position.md`](skills/ui-ux/content/serial-position.md)
- **Summary:** Strongest first, strongest last: people forget the middle
- **Triggers:** designing or building serial position components; reviewing UX/UI for serial position; implementing content pattern for serial position
- **Tags:** `ui, ux, content, serial, position`

### Feedback (9)

#### Doherty Threshold
- **Path:** [`skills/ui-ux/feedback/doherty-threshold.md`](skills/ui-ux/feedback/doherty-threshold.md)
- **Summary:** Cross 400ms and your user checks out. Perceived speed is a design choice.
- **Triggers:** designing or building doherty threshold components; reviewing UX/UI for doherty threshold; implementing feedback pattern for doherty threshold
- **Tags:** `ui, ux, feedback, doherty, threshold`

#### Error States
- **Path:** [`skills/ui-ux/feedback/error-states.md`](skills/ui-ux/feedback/error-states.md)
- **Summary:** Same error. Better recovery.
- **Triggers:** designing or building error states components; reviewing UX/UI for error states; implementing feedback pattern for error states
- **Tags:** `ui, ux, feedback, error, states`

#### Loading States System
- **Path:** [`skills/ui-ux/feedback/loading-states-system.md`](skills/ui-ux/feedback/loading-states-system.md)
- **Summary:** Stop using skeletons for everything. Loading is a system, not a default.
- **Triggers:** designing or building loading states system components; reviewing UX/UI for loading states system; implementing feedback pattern for loading states system
- **Tags:** `ui, ux, feedback, loading, states, system`

#### Notification System
- **Path:** [`skills/ui-ux/feedback/notification-system.md`](skills/ui-ux/feedback/notification-system.md)
- **Summary:** Notifications are a system. Pick the wrong surface and users tune out.
- **Triggers:** designing or building notification system components; reviewing UX/UI for notification system; implementing feedback pattern for notification system
- **Tags:** `ui, ux, feedback, notification, system`

#### Optimistic UI
- **Path:** [`skills/ui-ux/feedback/optimistic-ui.md`](skills/ui-ux/feedback/optimistic-ui.md)
- **Summary:** Click like. One waits. One feels instant.
- **Triggers:** designing or building optimistic ui components; reviewing UX/UI for optimistic ui; implementing feedback pattern for optimistic ui
- **Tags:** `ui, ux, feedback, optimistic`

#### Skeleton Loading
- **Path:** [`skills/ui-ux/feedback/skeleton-loading.md`](skills/ui-ux/feedback/skeleton-loading.md)
- **Summary:** Your loading spinner is making the wait feel longer
- **Triggers:** designing or building skeleton loading components; reviewing UX/UI for skeleton loading; implementing feedback pattern for skeleton loading
- **Tags:** `ui, ux, feedback, skeleton, loading`

#### Toast Notifications
- **Path:** [`skills/ui-ux/feedback/toast-notifications.md`](skills/ui-ux/feedback/toast-notifications.md)
- **Summary:** Toasts done right: five rules for notifications that inform without blocking.
- **Triggers:** designing or building toast notifications components; reviewing UX/UI for toast notifications; implementing feedback pattern for toast notifications
- **Tags:** `ui, ux, feedback, toast, notifications`

#### Undo UX
- **Path:** [`skills/ui-ux/feedback/undo-ux.md`](skills/ui-ux/feedback/undo-ux.md)
- **Summary:** Deleted. You have five seconds.
- **Triggers:** designing or building undo ux components; reviewing UX/UI for undo ux; implementing feedback pattern for undo ux
- **Tags:** `ui, ux, feedback, undo`

#### Zeigarnik Effect
- **Path:** [`skills/ui-ux/feedback/zeigarnik-effect.md`](skills/ui-ux/feedback/zeigarnik-effect.md)
- **Summary:** Your brain forgets what's finished, and won't stop nagging about what's not.
- **Triggers:** designing or building zeigarnik effect components; reviewing UX/UI for zeigarnik effect; implementing feedback pattern for zeigarnik effect
- **Tags:** `ui, ux, feedback, zeigarnik, effect`

### Forms (12)

#### Autosave
- **Path:** [`skills/ui-ux/forms/autosave-ux.md`](skills/ui-ux/forms/autosave-ux.md)
- **Summary:** Saved. It wasn't. Your wifi died mid-word.
- **Triggers:** designing or building autosave components; reviewing UX/UI for autosave; implementing forms pattern for autosave
- **Tags:** `ui, ux, forms, autosave`

#### Date Pickers
- **Path:** [`skills/ui-ux/forms/date-pickers.md`](skills/ui-ux/forms/date-pickers.md)
- **Summary:** Same date. Six clicks. Or one. The picker that respects your users' time.
- **Triggers:** designing or building date pickers components; reviewing UX/UI for date pickers; implementing forms pattern for date pickers
- **Tags:** `ui, ux, forms, date, pickers`

#### File Upload UX
- **Path:** [`skills/ui-ux/forms/file-upload-ux.md`](skills/ui-ux/forms/file-upload-ux.md)
- **Summary:** Same file. One upload feels broken. One feels safe.
- **Triggers:** designing or building file upload ux components; reviewing UX/UI for file upload ux; implementing forms pattern for file upload ux
- **Tags:** `ui, ux, forms, file, upload`

#### Form Field States
- **Path:** [`skills/ui-ux/forms/form-field-states.md`](skills/ui-ux/forms/form-field-states.md)
- **Summary:** Six field states, one system. Miss one and you ship a bug.
- **Triggers:** designing or building form field states components; reviewing UX/UI for form field states; implementing forms pattern for form field states
- **Tags:** `ui, ux, forms, form, field, states`

#### Form Validation Timing
- **Path:** [`skills/ui-ux/forms/form-validation-timing.md`](skills/ui-ux/forms/form-validation-timing.md)
- **Summary:** The error fires while you're still typing.
- **Triggers:** designing or building form validation timing components; reviewing UX/UI for form validation timing; implementing forms pattern for form validation timing
- **Tags:** `ui, ux, forms, form, validation, timing`

#### Input Masking
- **Path:** [`skills/ui-ux/forms/input-masking.md`](skills/ui-ux/forms/input-masking.md)
- **Summary:** Type 16 digits. Watch them become a card.
- **Triggers:** designing or building input masking components; reviewing UX/UI for input masking; implementing forms pattern for input masking
- **Tags:** `ui, ux, forms, input, masking`

#### OTP Input
- **Path:** [`skills/ui-ux/forms/otp-input.md`](skills/ui-ux/forms/otp-input.md)
- **Summary:** Your OTP input is a system, not six boxes.
- **Triggers:** designing or building otp input components; reviewing UX/UI for otp input; implementing forms pattern for otp input
- **Tags:** `ui, ux, forms, otp, input`

#### Password Field UX
- **Path:** [`skills/ui-ux/forms/password-field-ux.md`](skills/ui-ux/forms/password-field-ux.md)
- **Summary:** Eight characters, one symbol: still weak. Strength lives in real-time feedback.
- **Triggers:** designing or building password field ux components; reviewing UX/UI for password field ux; implementing forms pattern for password field ux
- **Tags:** `ui, ux, forms, password, field`

#### Range Sliders
- **Path:** [`skills/ui-ux/forms/range-sliders.md`](skills/ui-ux/forms/range-sliders.md)
- **Summary:** Drag to 47. Or 48? Your finger can't tell.
- **Triggers:** designing or building range sliders components; reviewing UX/UI for range sliders; implementing forms pattern for range sliders
- **Tags:** `ui, ux, forms, range, sliders`

#### Settings System
- **Path:** [`skills/ui-ux/forms/settings-system.md`](skills/ui-ux/forms/settings-system.md)
- **Summary:** Your settings page is harmless until the last section. Settings is a system.
- **Triggers:** designing or building settings system components; reviewing UX/UI for settings system; implementing forms pattern for settings system
- **Tags:** `ui, ux, forms, settings, system`

#### Stepper Wizard
- **Path:** [`skills/ui-ux/forms/stepper-wizard.md`](skills/ui-ux/forms/stepper-wizard.md)
- **Summary:** Twelve fields, one wall. Four steps, one path.
- **Triggers:** designing or building stepper wizard components; reviewing UX/UI for stepper wizard; implementing forms pattern for stepper wizard
- **Tags:** `ui, ux, forms, stepper, wizard`

#### Toggle Anatomy
- **Path:** [`skills/ui-ux/forms/toggle-anatomy.md`](skills/ui-ux/forms/toggle-anatomy.md)
- **Summary:** Two toggles. One snaps. One morphs, and the difference is everything.
- **Triggers:** designing or building toggle anatomy components; reviewing UX/UI for toggle anatomy; implementing forms pattern for toggle anatomy
- **Tags:** `ui, ux, forms, toggle, anatomy`

### Interaction (23)

#### Accordion Disclosure
- **Path:** [`skills/ui-ux/interaction/accordion-disclosure.md`](skills/ui-ux/interaction/accordion-disclosure.md)
- **Summary:** One accordion glides open, the other jumps. Four small rules separate them.
- **Triggers:** designing or building accordion disclosure components; reviewing UX/UI for accordion disclosure; implementing interaction pattern for accordion disclosure
- **Tags:** `ui, ux, interaction, accordion, disclosure`

#### Behind the Button
- **Path:** [`skills/ui-ux/interaction/behind-the-button.md`](skills/ui-ux/interaction/behind-the-button.md)
- **Summary:** Six things happen before the spinner stops.
- **Triggers:** designing or building behind the button components; reviewing UX/UI for behind the button; implementing interaction pattern for behind the button
- **Tags:** `ui, ux, interaction, behind, the, button`

#### Bottom Sheets
- **Path:** [`skills/ui-ux/interaction/bottom-sheets.md`](skills/ui-ux/interaction/bottom-sheets.md)
- **Summary:** Your thumb can't reach that menu.
- **Triggers:** designing or building bottom sheets components; reviewing UX/UI for bottom sheets; implementing interaction pattern for bottom sheets
- **Tags:** `ui, ux, interaction, bottom, sheets`

#### Bulk Actions
- **Path:** [`skills/ui-ux/interaction/bulk-actions.md`](skills/ui-ux/interaction/bulk-actions.md)
- **Summary:** Bulk actions are a system, not a lone checkbox.
- **Triggers:** designing or building bulk actions components; reviewing UX/UI for bulk actions; implementing interaction pattern for bulk actions
- **Tags:** `ui, ux, interaction, bulk, actions`

#### CSS Has Selector
- **Path:** [`skills/ui-ux/interaction/css-has-selector.md`](skills/ui-ux/interaction/css-has-selector.md)
- **Summary:** One line of CSS. The whole card reacts to its own checkbox.
- **Triggers:** designing or building css has selector components; reviewing UX/UI for css has selector; implementing interaction pattern for css has selector
- **Tags:** `ui, ux, interaction, css, has, selector`

#### Color Picker UX
- **Path:** [`skills/ui-ux/interaction/color-picker-ux.md`](skills/ui-ux/interaction/color-picker-ux.md)
- **Summary:** Pick a color. Your whole UI answers.
- **Triggers:** designing or building color picker ux components; reviewing UX/UI for color picker ux; implementing interaction pattern for color picker ux
- **Tags:** `ui, ux, interaction, color, picker`

#### Command Palette
- **Path:** [`skills/ui-ux/interaction/command-palette.md`](skills/ui-ux/interaction/command-palette.md)
- **Summary:** ⌘K is a system, not a search box.
- **Triggers:** designing or building command palette components; reviewing UX/UI for command palette; implementing interaction pattern for command palette
- **Tags:** `ui, ux, interaction, command, palette`

#### Context Menu
- **Path:** [`skills/ui-ux/interaction/context-menu.md`](skills/ui-ux/interaction/context-menu.md)
- **Summary:** A context menu is a system, not just a list of actions.
- **Triggers:** designing or building context menu components; reviewing UX/UI for context menu; implementing interaction pattern for context menu
- **Tags:** `ui, ux, interaction, context, menu`

#### Data Table
- **Path:** [`skills/ui-ux/interaction/data-table.md`](skills/ui-ux/interaction/data-table.md)
- **Summary:** Your data table feels cheap because it's a grid of divs, not a system.
- **Triggers:** designing or building data table components; reviewing UX/UI for data table; implementing interaction pattern for data table
- **Tags:** `ui, ux, interaction, data, table`

#### Destructive Actions
- **Path:** [`skills/ui-ux/interaction/destructive-actions.md`](skills/ui-ux/interaction/destructive-actions.md)
- **Summary:** Dangerous actions are a design language, not just a red button.
- **Triggers:** designing or building destructive actions components; reviewing UX/UI for destructive actions; implementing interaction pattern for destructive actions
- **Tags:** `ui, ux, interaction, destructive, actions`

#### Disabled Buttons
- **Path:** [`skills/ui-ux/interaction/disabled-buttons.md`](skills/ui-ux/interaction/disabled-buttons.md)
- **Summary:** The button is disabled, and nobody tells you why.
- **Triggers:** designing or building disabled buttons components; reviewing UX/UI for disabled buttons; implementing interaction pattern for disabled buttons
- **Tags:** `ui, ux, interaction, disabled, buttons`

#### Drag and Drop
- **Path:** [`skills/ui-ux/interaction/drag-and-drop.md`](skills/ui-ux/interaction/drag-and-drop.md)
- **Summary:** The board does the thinking: moving a card is moving state.
- **Triggers:** designing or building drag and drop components; reviewing UX/UI for drag and drop; implementing interaction pattern for drag and drop
- **Tags:** `ui, ux, interaction, drag, and, drop`

#### Dropdown Design
- **Path:** [`skills/ui-ux/interaction/dropdown-design.md`](skills/ui-ux/interaction/dropdown-design.md)
- **Summary:** Your dropdown is broken. Five rules separate cheap from premium.
- **Triggers:** designing or building dropdown design components; reviewing UX/UI for dropdown design; implementing interaction pattern for dropdown design
- **Tags:** `ui, ux, interaction, dropdown, design`

#### Filter Chips
- **Path:** [`skills/ui-ux/interaction/filter-chips.md`](skills/ui-ux/interaction/filter-chips.md)
- **Summary:** 200 results. Three taps. 12 left.
- **Triggers:** designing or building filter chips components; reviewing UX/UI for filter chips; implementing interaction pattern for filter chips
- **Tags:** `ui, ux, interaction, filter, chips`

#### Hover Trap
- **Path:** [`skills/ui-ux/interaction/hover-trap.md`](skills/ui-ux/interaction/hover-trap.md)
- **Summary:** Hover works on your laptop but is dead on mobile.
- **Triggers:** designing or building hover trap components; reviewing UX/UI for hover trap; implementing interaction pattern for hover trap
- **Tags:** `ui, ux, interaction, hover, trap`

#### Inline Editing
- **Path:** [`skills/ui-ux/interaction/inline-editing.md`](skills/ui-ux/interaction/inline-editing.md)
- **Summary:** Click the title. It's an input now, and nothing moved.
- **Triggers:** designing or building inline editing components; reviewing UX/UI for inline editing; implementing interaction pattern for inline editing
- **Tags:** `ui, ux, interaction, inline, editing`

#### Live Cursors
- **Path:** [`skills/ui-ux/interaction/live-cursors.md`](skills/ui-ux/interaction/live-cursors.md)
- **Summary:** Three cursors land on your canvas. None of them are yours.
- **Triggers:** designing or building live cursors components; reviewing UX/UI for live cursors; implementing interaction pattern for live cursors
- **Tags:** `ui, ux, interaction, live, cursors`

#### Modal Hierarchy
- **Path:** [`skills/ui-ux/interaction/modal-hierarchy.md`](skills/ui-ux/interaction/modal-hierarchy.md)
- **Summary:** 5 overlays. Most apps pick the wrong one.
- **Triggers:** designing or building modal hierarchy components; reviewing UX/UI for modal hierarchy; implementing interaction pattern for modal hierarchy
- **Tags:** `ui, ux, interaction, modal, hierarchy`

#### Peak-End Rule
- **Path:** [`skills/ui-ux/interaction/peak-end-rule.md`](skills/ui-ux/interaction/peak-end-rule.md)
- **Summary:** Users don't average an experience. They remember its peak and its end.
- **Triggers:** designing or building peak-end rule components; reviewing UX/UI for peak-end rule; implementing interaction pattern for peak-end rule
- **Tags:** `ui, ux, interaction, peak, end, rule`

#### Search Experience System
- **Path:** [`skills/ui-ux/interaction/search-experience-system.md`](skills/ui-ux/interaction/search-experience-system.md)
- **Summary:** Search is a system. Five parts. Most apps skip them.
- **Triggers:** designing or building search experience system components; reviewing UX/UI for search experience system; implementing interaction pattern for search experience system
- **Tags:** `ui, ux, interaction, search, experience, system`

#### Star Rating
- **Path:** [`skills/ui-ux/interaction/star-rating.md`](skills/ui-ux/interaction/star-rating.md)
- **Summary:** Five stars looks trivial. Hover, half-fills, and honest averages are where it breaks.
- **Triggers:** designing or building star rating components; reviewing UX/UI for star rating; implementing interaction pattern for star rating
- **Tags:** `ui, ux, interaction, star, rating`

#### Swipe Actions
- **Path:** [`skills/ui-ux/interaction/swipe-actions.md`](skills/ui-ux/interaction/swipe-actions.md)
- **Summary:** Your swipe actions are killing your UX
- **Triggers:** designing or building swipe actions components; reviewing UX/UI for swipe actions; implementing interaction pattern for swipe actions
- **Tags:** `ui, ux, interaction, swipe, actions`

#### Tooltip Design
- **Path:** [`skills/ui-ux/interaction/tooltip-design.md`](skills/ui-ux/interaction/tooltip-design.md)
- **Summary:** Your tooltip is annoying. Five rules that make it feel premium.
- **Triggers:** designing or building tooltip design components; reviewing UX/UI for tooltip design; implementing interaction pattern for tooltip design
- **Tags:** `ui, ux, interaction, tooltip, design`

### Motion (4)

#### Animation Timing
- **Path:** [`skills/ui-ux/motion/animation-timing.md`](skills/ui-ux/motion/animation-timing.md)
- **Summary:** Same modal, two timings: one feels premium, one feels broken. It's all milliseconds.
- **Triggers:** designing or building animation timing components; reviewing UX/UI for animation timing; implementing motion pattern for animation timing
- **Tags:** `ui, ux, motion, animation, timing`

#### Card Hover Anatomy
- **Path:** [`skills/ui-ux/motion/card-hover-anatomy.md`](skills/ui-ux/motion/card-hover-anatomy.md)
- **Summary:** Same card. One feels alive, three stay dead. Four rules separate them.
- **Triggers:** designing or building card hover anatomy components; reviewing UX/UI for card hover anatomy; implementing motion pattern for card hover anatomy
- **Tags:** `ui, ux, motion, card, hover, anatomy`

#### Easing Curves
- **Path:** [`skills/ui-ux/motion/easing-curves.md`](skills/ui-ux/motion/easing-curves.md)
- **Summary:** Same distance, different feel: the easing curve is what decides how motion reads.
- **Triggers:** designing or building easing curves components; reviewing UX/UI for easing curves; implementing motion pattern for easing curves
- **Tags:** `ui, ux, motion, easing, curves`

#### Scroll-Driven Animations
- **Path:** [`skills/ui-ux/motion/scroll-driven-animations.md`](skills/ui-ux/motion/scroll-driven-animations.md)
- **Summary:** Same scroll: one feels dead, the other comes alive. Pure CSS, zero JavaScript.
- **Triggers:** designing or building scroll-driven animations components; reviewing UX/UI for scroll-driven animations; implementing motion pattern for scroll-driven animations
- **Tags:** `ui, ux, motion, scroll, driven, animations`

### Navigation (4)

#### Focus States
- **Path:** [`skills/ui-ux/navigation/focus-states.md`](skills/ui-ux/navigation/focus-states.md)
- **Summary:** Press Tab. Where did the focus go?
- **Triggers:** designing or building focus states components; reviewing UX/UI for focus states; implementing navigation pattern for focus states
- **Tags:** `ui, ux, navigation, focus, states`

#### Navigation Patterns
- **Path:** [`skills/ui-ux/navigation/navigation-patterns.md`](skills/ui-ux/navigation/navigation-patterns.md)
- **Summary:** Five nav patterns, one system: mobile = tabs, desktop = sidebar.
- **Triggers:** designing or building navigation patterns components; reviewing UX/UI for navigation patterns; implementing navigation pattern for navigation patterns
- **Tags:** `ui, ux, navigation, patterns`

#### Pagination
- **Path:** [`skills/ui-ux/navigation/pagination.md`](skills/ui-ux/navigation/pagination.md)
- **Summary:** Add one row and your pagination breaks.
- **Triggers:** designing or building pagination components; reviewing UX/UI for pagination; implementing navigation pattern for pagination
- **Tags:** `ui, ux, navigation, pagination`

#### Tabs System
- **Path:** [`skills/ui-ux/navigation/tabs-system.md`](skills/ui-ux/navigation/tabs-system.md)
- **Summary:** Tabs aren't a widget. They're a system. Stop letting them jump.
- **Triggers:** designing or building tabs system components; reviewing UX/UI for tabs system; implementing navigation pattern for tabs system
- **Tags:** `ui, ux, navigation, tabs, system`

### Visual (20)

#### Border Radius
- **Path:** [`skills/ui-ux/visual/border-radius.md`](skills/ui-ux/visual/border-radius.md)
- **Summary:** Same card. One looks off, one looks expensive. The gap is one CSS rule.
- **Triggers:** designing or building border radius components; reviewing UX/UI for border radius; implementing visual pattern for border radius
- **Tags:** `ui, ux, visual, border, radius`

#### Charts That Lie
- **Path:** [`skills/ui-ux/visual/charts-that-lie.md`](skills/ui-ux/visual/charts-that-lie.md)
- **Summary:** Same data, opposite stories: how you draw a chart decides which truth people see.
- **Triggers:** designing or building charts that lie components; reviewing UX/UI for charts that lie; implementing visual pattern for charts that lie
- **Tags:** `ui, ux, visual, charts, that, lie`

#### Color Accessibility
- **Path:** [`skills/ui-ux/visual/color-accessibility.md`](skills/ui-ux/visual/color-accessibility.md)
- **Summary:** Same text, same color: one is invisible. The contrast ratio nobody checks.
- **Triggers:** designing or building color accessibility components; reviewing UX/UI for color accessibility; implementing visual pattern for color accessibility
- **Tags:** `ui, ux, visual, color, accessibility`

#### Dark Mode
- **Path:** [`skills/ui-ux/visual/dark-mode.md`](skills/ui-ux/visual/dark-mode.md)
- **Summary:** Same app, one inverts colors. The other feels premium.
- **Triggers:** designing or building dark mode components; reviewing UX/UI for dark mode; implementing visual pattern for dark mode
- **Tags:** `ui, ux, visual, dark, mode`

#### De-AI Landing Hero
- **Path:** [`skills/ui-ux/visual/de-ai-landing-hero.md`](skills/ui-ux/visual/de-ai-landing-hero.md)
- **Summary:** Your landing page looks AI-made. Five tells. Five fixes.
- **Triggers:** designing or building de-ai landing hero components; reviewing UX/UI for de-ai landing hero; implementing visual pattern for de-ai landing hero
- **Tags:** `ui, ux, visual, landing, hero`

#### Depth Layers
- **Path:** [`skills/ui-ux/visual/depth-layers.md`](skills/ui-ux/visual/depth-layers.md)
- **Summary:** Same layout, same colors: three properties turn flat cards into real depth.
- **Triggers:** designing or building depth layers components; reviewing UX/UI for depth layers; implementing visual pattern for depth layers
- **Tags:** `ui, ux, visual, depth, layers`

#### Design System Kit
- **Path:** [`skills/ui-ux/visual/design-system-kit.md`](skills/ui-ux/visual/design-system-kit.md)
- **Summary:** Random hex and eyeballed pixels don't scale. A token system does.
- **Triggers:** designing or building design system kit components; reviewing UX/UI for design system kit; implementing visual pattern for design system kit
- **Tags:** `ui, ux, visual, design, system, kit`

#### Design Tokens
- **Path:** [`skills/ui-ux/visual/design-tokens.md`](skills/ui-ux/visual/design-tokens.md)
- **Summary:** 47 changes, or just one. Design tokens change everything.
- **Triggers:** designing or building design tokens components; reviewing UX/UI for design tokens; implementing visual pattern for design tokens
- **Tags:** `ui, ux, visual, design, tokens`

#### Gestalt Laws
- **Path:** [`skills/ui-ux/visual/gestalt-laws.md`](skills/ui-ux/visual/gestalt-laws.md)
- **Summary:** Same elements. One is chaos. The other clicks instantly.
- **Triggers:** designing or building gestalt laws components; reviewing UX/UI for gestalt laws; implementing visual pattern for gestalt laws
- **Tags:** `ui, ux, visual, gestalt, laws`

#### Golden Ratio
- **Path:** [`skills/ui-ux/visual/golden-ratio.md`](skills/ui-ux/visual/golden-ratio.md)
- **Summary:** One layout looks cheap, the other expensive. The difference is 1.618.
- **Triggers:** designing or building golden ratio components; reviewing UX/UI for golden ratio; implementing visual pattern for golden ratio
- **Tags:** `ui, ux, visual, golden, ratio`

#### Gradient Design
- **Path:** [`skills/ui-ux/visual/gradient-design.md`](skills/ui-ux/visual/gradient-design.md)
- **Summary:** Why your gradients look cheap
- **Triggers:** designing or building gradient design components; reviewing UX/UI for gradient design; implementing visual pattern for gradient design
- **Tags:** `ui, ux, visual, gradient, design`

#### Grid System
- **Path:** [`skills/ui-ux/visual/grid-system.md`](skills/ui-ux/visual/grid-system.md)
- **Summary:** Align everything to a 12-column grid, then break it on purpose.
- **Triggers:** designing or building grid system components; reviewing UX/UI for grid system; implementing visual pattern for grid system
- **Tags:** `ui, ux, visual, grid, system`

#### Icon Design Rules
- **Path:** [`skills/ui-ux/visual/icon-design-rules.md`](skills/ui-ux/visual/icon-design-rules.md)
- **Summary:** Your icons look cheap. 5 rules turn them premium.
- **Triggers:** designing or building icon design rules components; reviewing UX/UI for icon design rules; implementing visual pattern for icon design rules
- **Tags:** `ui, ux, visual, icon, design, rules`

#### Perfect Card
- **Path:** [`skills/ui-ux/visual/perfect-card.md`](skills/ui-ux/visual/perfect-card.md)
- **Summary:** One card looks free. The other costs $1000. Four CSS changes.
- **Triggers:** designing or building perfect card components; reviewing UX/UI for perfect card; implementing visual pattern for perfect card
- **Tags:** `ui, ux, visual, perfect, card`

#### Proximity Rule
- **Path:** [`skills/ui-ux/visual/proximity-rule.md`](skills/ui-ux/visual/proximity-rule.md)
- **Summary:** Close = related, far = separate: spacing alone groups your UI, no borders needed.
- **Triggers:** designing or building proximity rule components; reviewing UX/UI for proximity rule; implementing visual pattern for proximity rule
- **Tags:** `ui, ux, visual, proximity, rule`

#### Reverse-Engineered Linear
- **Path:** [`skills/ui-ux/visual/reverse-engineered-linear.md`](skills/ui-ux/visual/reverse-engineered-linear.md)
- **Summary:** Why does Linear feel expensive? Five decisions. None need a designer.
- **Triggers:** designing or building reverse-engineered linear components; reviewing UX/UI for reverse-engineered linear; implementing visual pattern for reverse-engineered linear
- **Tags:** `ui, ux, visual, reverse, engineered, linear`

#### Shadow Elevation
- **Path:** [`skills/ui-ux/visual/shadow-elevation.md`](skills/ui-ux/visual/shadow-elevation.md)
- **Summary:** Shadows aren't decoration. They encode hierarchy and depth.
- **Triggers:** designing or building shadow elevation components; reviewing UX/UI for shadow elevation; implementing visual pattern for shadow elevation
- **Tags:** `ui, ux, visual, shadow, elevation`

#### Visual Hierarchy
- **Path:** [`skills/ui-ux/visual/visual-hierarchy.md`](skills/ui-ux/visual/visual-hierarchy.md)
- **Summary:** Five rules that decide what your users see first, and what they skip.
- **Triggers:** designing or building visual hierarchy components; reviewing UX/UI for visual hierarchy; implementing visual pattern for visual hierarchy
- **Tags:** `ui, ux, visual, hierarchy`

#### Von Restorff Effect
- **Path:** [`skills/ui-ux/visual/von-restorff.md`](skills/ui-ux/visual/von-restorff.md)
- **Summary:** Three identical pricing cards, nobody clicks. Isolate one: 3× more conversions.
- **Triggers:** designing or building von restorff effect components; reviewing UX/UI for von restorff effect; implementing visual pattern for von restorff effect
- **Tags:** `ui, ux, visual, von, restorff`

#### Z-Index Mastery
- **Path:** [`skills/ui-ux/visual/z-index-mastery.md`](skills/ui-ux/visual/z-index-mastery.md)
- **Summary:** z-index lies: a bigger number won't win if the element isn't positioned.
- **Triggers:** designing or building z-index mastery components; reviewing UX/UI for z-index mastery; implementing visual pattern for z-index mastery
- **Tags:** `ui, ux, visual, index, mastery`

---
