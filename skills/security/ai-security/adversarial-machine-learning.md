---
id: security.ai-security.adversarial-machine-learning
name: Adversarial Machine Learning & LLM Security
version: 1.0.0
domain: security
subdomain: ai-security
summary: Defending AI systems against prompt injection, model evasion, training data poisoning, and model extraction.
triggers:
- building or deploying Large Language Model (LLM) applications or agents
- hardening AI systems against prompt injection and jailbreaking
- evaluating security risks in machine learning pipelines and training data
tags:
- security
- ai
- adversarial-ml
- llm-security
- prompt-injection
- owasp-llm
priority: high
dependencies: []
related_skills:
- security.ai-security.ai-threat-detection
- security.app-security.owasp-top-10-defenses
source:
  name: cyber-security-vault
  url: https://github.com/DinushaNaween/cyber-sec
  reference_file: content/cyber-security/12. Cybersecurity and AI/Concepts/Adversarial Machine Learning.md
last_updated: '2026-09-14'
---

# Adversarial Machine Learning & LLM Security

> Defending AI systems against prompt injection, model evasion, training data poisoning, and model extraction.

## When to Use (Triggers)

- building or deploying Large Language Model (LLM) applications or agents
- hardening AI systems against prompt injection and jailbreaking
- evaluating security risks in machine learning pipelines and training data

## Key Insights & Principles

- Prompt Injection: Attackers craft untrusted user input that overrides system prompts, tricking the LLM into unauthorized actions.
- Indirect Prompt Injection: Malicious instructions embedded in external retrieved content (web pages, PDFs, emails).
- Data Poisoning: Injecting compromised samples into training or fine-tuning datasets to create backdoors.
- Model Evasion: Perturbing input features imperceptibly to cause ML classifiers to misclassify malicious payloads.

## Do's and Don'ts

- **Do:** Treat all LLM output as untrusted before feeding it into backend systems, databases, or shell execution tools.
- **Do:** Implement dual LLM validation architectures (guardrail models) to inspect inputs and outputs for prompt injection.
- **Do:** Enforce strict tool authorization and human approval gates for sensitive actions executed by AI agents.
- **Don't:** Grant autonomous AI agents direct, unconstrained access to write databases, delete files, or send external emails.
- **Don't:** Assume system instructions in prompts are secret—LLM prompt extraction techniques are widely effective.

## Related Skills

- `security.ai-security.ai-threat-detection`
- `security.app-security.owasp-top-10-defenses`
