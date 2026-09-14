"""
Skill Serializer.
Converts canonical Skill objects into standard Markdown documents with YAML frontmatter.
"""
import os
import hashlib
import yaml
from pathlib import Path
from typing import Tuple
from registry_engine.models import Skill


class SkillSerializer:
    """Serializes Skill objects to Markdown files with YAML frontmatter."""

    def __init__(self, base_dir: str = "."):
        self.base_dir = Path(base_dir)
        self.skills_dir = self.base_dir / "skills"

    def serialize_to_markdown(self, skill: Skill) -> str:
        """Produce clean Markdown string with YAML frontmatter."""
        frontmatter_data = skill.to_frontmatter_dict()
        fm_yaml = yaml.dump(frontmatter_data, sort_keys=False, allow_unicode=True, width=120)

        lines = [
            "---",
            fm_yaml.strip(),
            "---",
            "",
            f"# {skill.name}",
            "",
            f"> {skill.summary}" if skill.summary else "",
            "",
            "## When to Use (Triggers)",
            "",
        ]

        if skill.triggers:
            for trigger in skill.triggers:
                lines.append(f"- {trigger}")
        else:
            lines.append(f"- Use when working with {skill.name.lower()} in {skill.subdomain}.")

        lines.extend([
            "",
            "## Key Insights & Principles",
            "",
        ])

        if skill.key_insights:
            for insight in skill.key_insights:
                lines.append(f"- {insight}")
        else:
            lines.append("- Refer to design system documentation.")

        lines.extend([
            "",
            "## Do's and Don'ts",
            "",
        ])

        if skill.dos or skill.donts:
            for d in skill.dos:
                lines.append(f"- **Do:** {d}")
            for d in skill.donts:
                lines.append(f"- **Don't:** {d}")
        else:
            lines.append("- Follow established UX guidelines for this pattern.")

        if skill.code_snippets:
            lines.extend([
                "",
                "## Code & Selectors",
                "",
            ])
            for code in skill.code_snippets:
                lines.append(f"```css\n{code}\n```\n")

        # Media section
        has_media = skill.media.video or skill.media.thumbnail
        if has_media or skill.source.url:
            lines.extend([
                "## Media & References",
                "",
            ])
            if skill.media.video:
                lines.append(f"- **Demo Video:** [Watch MP4 Breakdown]({skill.media.video})")
            if skill.media.thumbnail:
                lines.append(f"- **Thumbnail:** [Visual Preview]({skill.media.thumbnail})")
            if skill.source.url:
                lines.append(f"- **Original Pattern:** [{skill.source.name}]({skill.source.url})")
            if skill.source.instagram_url:
                lines.append(f"- **Instagram Reel:** [Watch on Instagram]({skill.source.instagram_url})")

        if skill.related_skills:
            lines.extend([
                "",
                "## Related Skills",
                "",
            ])
            for rel in skill.related_skills:
                lines.append(f"- `{rel}`")

        lines.append("")
        return "\n".join(lines)

    def write_skill(self, skill: Skill, force: bool = False) -> Tuple[str, str]:
        """
        Write skill to disk at skills/<domain>/<subdomain>/<slug>.md.
        Returns (filepath, action) where action is 'created', 'updated', or 'skipped'.
        """
        target_dir = self.skills_dir / skill.domain / skill.subdomain
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / f"{skill.slug}.md"
        content = self.serialize_to_markdown(skill)

        if target_file.exists() and not force:
            existing_content = target_file.read_text(encoding="utf-8")
            if hashlib.sha256(existing_content.encode()).hexdigest() == hashlib.sha256(content.encode()).hexdigest():
                return str(target_file), "skipped"
            action = "updated"
        else:
            action = "updated" if target_file.exists() else "created"

        target_file.write_text(content, encoding="utf-8")
        return str(target_file), action
