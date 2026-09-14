"""
Data models for the Agent Skill Registry.
"""
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict, Any


@dataclass
class Media:
    thumbnail: Optional[str] = None
    video: Optional[str] = None
    poster: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class SourceInfo:
    name: str = ""
    url: str = ""
    instagram_url: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        return {k: v for k, v in asdict(self).items() if v is not None}


@dataclass
class Skill:
    id: str
    name: str
    domain: str
    subdomain: str
    slug: str
    summary: str
    version: str = "1.0.0"
    priority: str = "medium"
    triggers: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    key_insights: List[str] = field(default_factory=list)
    dos: List[str] = field(default_factory=list)
    donts: List[str] = field(default_factory=list)
    code_snippets: List[str] = field(default_factory=list)
    media: Media = field(default_factory=Media)
    source: SourceInfo = field(default_factory=SourceInfo)
    dependencies: List[str] = field(default_factory=list)
    related_skills: List[str] = field(default_factory=list)
    last_updated: str = ""

    def to_frontmatter_dict(self) -> Dict[str, Any]:
        data = {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "domain": self.domain,
            "subdomain": self.subdomain,
            "summary": self.summary,
            "triggers": self.triggers,
            "tags": self.tags,
            "priority": self.priority,
            "dependencies": self.dependencies,
            "related_skills": self.related_skills,
            "source": self.source.to_dict(),
        }
        if self.last_updated:
            data["last_updated"] = self.last_updated
        return data

    def to_index_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "domain": self.domain,
            "subdomain": self.subdomain,
            "slug": self.slug,
            "path": f"skills/{self.domain}/{self.subdomain}/{self.slug}.md",
            "summary": self.summary,
            "triggers": self.triggers,
            "tags": self.tags,
            "priority": self.priority,
            "dependencies": self.dependencies,
            "related_skills": self.related_skills,
            "media": self.media.to_dict(),
            "source": self.source.to_dict(),
            "last_updated": self.last_updated,
        }
