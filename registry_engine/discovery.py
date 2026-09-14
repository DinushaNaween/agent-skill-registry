"""
Skill Discovery and Agent Retrieval utilities.
"""
import json
from pathlib import Path
from typing import List, Dict, Any, Optional


class SkillDiscovery:
    """Provides fast search and context retrieval for AI agents and CLI."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.registry_json = self.base_dir / "registry.json"

    def load_registry(self) -> List[Dict[str, Any]]:
        if not self.registry_json.exists():
            return []
        try:
            data = json.loads(self.registry_json.read_text(encoding="utf-8"))
            return data.get("skills", [])
        except Exception:
            return []

    def search(
        self, query: str, domain: Optional[str] = None, subdomain: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """Search skills by keywords in name, summary, triggers, and tags."""
        skills = self.load_registry()
        query_terms = query.lower().split()
        results = []

        for skill in skills:
            if domain and skill.get("domain") != domain:
                continue
            if subdomain and skill.get("subdomain") != subdomain:
                continue

            # Calculate match score
            score = 0
            name = skill.get("name", "").lower()
            summary = skill.get("summary", "").lower()
            triggers = " ".join(skill.get("triggers", [])).lower()
            tags = " ".join(skill.get("tags", [])).lower()
            skill_id = skill.get("id", "").lower()

            for term in query_terms:
                if term in skill_id:
                    score += 5
                if term in name:
                    score += 4
                if term in triggers:
                    score += 3
                if term in tags:
                    score += 2
                if term in summary:
                    score += 1

            if score > 0:
                results.append({"skill": skill, "score": score})

        results.sort(key=lambda x: x["score"], reverse=True)
        return [r["skill"] for r in results]

    def load_skill_content(self, skill_id_or_slug: str) -> Optional[str]:
        """Retrieve full markdown content for a skill by ID or slug."""
        skills = self.load_registry()
        target_path = None

        for s in skills:
            if s.get("id") == skill_id_or_slug or s.get("slug") == skill_id_or_slug:
                target_path = s.get("relative_path")
                break

        if not target_path:
            # Try direct file lookup
            for candidate in self.base_dir.rglob(f"{skill_id_or_slug}.md"):
                target_path = str(candidate.relative_to(self.base_dir))
                break

        if target_path:
            full_path = self.base_dir / target_path
            if full_path.exists():
                return full_path.read_text(encoding="utf-8")

        return None
