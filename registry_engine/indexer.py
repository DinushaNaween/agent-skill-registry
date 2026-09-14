"""
Registry Indexer.
Scans the skills directory and generates registry.md and registry.json.
"""
import os
import json
import yaml
from pathlib import Path
from typing import List, Dict, Any
from datetime import datetime


class RegistryIndexer:
    """Compiles registry.md and registry.json from markdown skill files."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.skills_dir = self.base_dir / "skills"
        self.registry_md = self.base_dir / "registry.md"
        self.registry_json = self.base_dir / "registry.json"

    def parse_skill_file(self, file_path: Path) -> Dict[str, Any]:
        """Extract YAML frontmatter and file metadata from a skill markdown file."""
        content = file_path.read_text(encoding="utf-8")
        if not content.startswith("---"):
            return {}

        parts = content.split("---", 2)
        if len(parts) < 3:
            return {}

        try:
            frontmatter = yaml.safe_load(parts[1])
            if not isinstance(frontmatter, dict):
                return {}
            frontmatter["relative_path"] = str(file_path.relative_to(self.base_dir))
            return frontmatter
        except Exception:
            return {}

    def scan_all_skills(self) -> List[Dict[str, Any]]:
        """Find and parse all skills in the skills directory."""
        if not self.skills_dir.exists():
            return []

        skills = []
        for path in sorted(self.skills_dir.rglob("*.md")):
            data = self.parse_skill_file(path)
            if data and "id" in data:
                skills.append(data)

        return skills

    def generate_registry_json(self, skills: List[Dict[str, Any]]) -> None:
        """Write machine-readable index to registry.json."""
        index_data = {
            "version": "1.0.0",
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_skills": len(skills),
            "domains": list(sorted(set(s.get("domain", "") for s in skills if s.get("domain")))),
            "skills": skills,
        }
        self.registry_json.write_text(json.dumps(index_data, indent=2, ensure_ascii=False), encoding="utf-8")

    def generate_registry_md(self, skills: List[Dict[str, Any]]) -> None:
        """Write human/agent-readable capability map to registry.md."""
        now_str = datetime.now().strftime("%Y-%m-%d")
        lines = [
            "# AI Agent Skill Registry",
            "",
            "> Central capability index for autonomous AI agents and developers.",
            f"> **Total Skills:** {len(skills)} | **Last Updated:** {now_str}",
            "",
            "## How Agents Use This Registry",
            "",
            "1. **Analyze Task:** Identify relevant domain and action keywords.",
            "2. **Match Triggers:** Scan the `Triggers` list below or query `registry.json`.",
            "3. **Selective Load:** Read only the matched skill file path into working context.",
            "4. **Execute:** Apply the specific insights, rules, and code patterns.",
            "",
            "---",
            "",
        ]

        # Group by domain -> subdomain
        by_domain: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        for s in skills:
            domain = s.get("domain", "other")
            subdomain = s.get("subdomain", "general")
            by_domain.setdefault(domain, {}).setdefault(subdomain, []).append(s)

        for domain in sorted(by_domain.keys()):
            domain_name = domain.replace("-", " ").title()
            lines.append(f"## {domain_name} Domain (`{domain}`)")
            lines.append("")

            for subdomain in sorted(by_domain[domain].keys()):
                sub_name = subdomain.replace("-", " ").title()
                sub_skills = by_domain[domain][subdomain]
                lines.append(f"### {sub_name} ({len(sub_skills)})")
                lines.append("")

                for skill in sorted(sub_skills, key=lambda x: x.get("name", "")):
                    name = skill.get("name", skill.get("id"))
                    path = skill.get("relative_path", "")
                    summary = skill.get("summary", "")
                    triggers = skill.get("triggers", [])
                    tags = ", ".join(skill.get("tags", []))

                    lines.append(f"#### {name}")
                    lines.append(f"- **Path:** [`{path}`]({path})")
                    if summary:
                        lines.append(f"- **Summary:** {summary}")
                    if triggers:
                        trigger_str = "; ".join(triggers[:3])
                        lines.append(f"- **Triggers:** {trigger_str}")
                    if tags:
                        lines.append(f"- **Tags:** `{tags}`")
                    lines.append("")

            lines.append("---")
            lines.append("")

        self.registry_md.write_text("\n".join(lines), encoding="utf-8")

    def reindex(self) -> Dict[str, Any]:
        """Perform full scan and regenerate registry.md and registry.json."""
        skills = self.scan_all_skills()
        self.generate_registry_json(skills)
        self.generate_registry_md(skills)
        return {
            "total_skills": len(skills),
            "domains": list(sorted(set(s.get("domain", "") for s in skills if s.get("domain")))),
            "registry_md": str(self.registry_md),
            "registry_json": str(self.registry_json),
        }
