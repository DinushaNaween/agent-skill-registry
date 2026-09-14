"""
AI Agent Skill Registry CLI.
Discovery, search, context retrieval, and validation for software engineering skills.
"""
import sys
import argparse
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from registry_engine.indexer import RegistryIndexer
from registry_engine.discovery import SkillDiscovery

console = Console()


def run_search(args):
    """Search the skill registry."""
    discovery = SkillDiscovery(base_dir=".")
    results = discovery.search(args.query, domain=args.domain, subdomain=args.subdomain)

    if not results:
        console.print(f"[yellow]No skills matched query: '{args.query}'[/yellow]")
        return

    table = Table(title=f"Search Results for '{args.query}' ({len(results)} matches)", border_style="cyan")
    table.add_column("Skill ID", style="bold cyan")
    table.add_column("Name", style="bold white")
    table.add_column("Domain / Subdomain", style="magenta")
    table.add_column("Key Triggers", style="dim")
    table.add_column("Path", style="blue")

    for skill in results[:args.max_results]:
        triggers = "; ".join(skill.get("triggers", [])[:2])
        table.add_row(
            skill.get("id", ""),
            skill.get("name", ""),
            f"{skill.get('domain')}/{skill.get('subdomain')}",
            triggers,
            skill.get("relative_path", ""),
        )

    console.print(table)


def run_load(args):
    """Print the markdown content of a skill for agent context injection."""
    discovery = SkillDiscovery(base_dir=".")
    content = discovery.load_skill_content(args.skill_id)

    if not content:
        console.print(f"[red]Error: Skill '{args.skill_id}' not found.[/red]", file=sys.stderr)
        sys.exit(1)

    print(content)


def run_list(args):
    """List all registered skills grouped by domain and subdomain."""
    discovery = SkillDiscovery(base_dir=".")
    skills = discovery.load_registry()

    if not skills:
        console.print("[yellow]Registry is empty. Populate skills/ directory and run 'python main.py reindex'.[/yellow]")
        return

    by_domain = {}
    for s in skills:
        d = s.get("domain", "other")
        sub = s.get("subdomain", "general")
        by_domain.setdefault(d, {}).setdefault(sub, []).append(s)

    table = Table(title=f"Registered Skills Catalog ({len(skills)} Total)", border_style="cyan")
    table.add_column("Domain", style="bold cyan")
    table.add_column("Subdomain", style="magenta")
    table.add_column("Count", justify="right", style="bold green")
    table.add_column("Sample Skills", style="dim")

    for domain in sorted(by_domain.keys()):
        for subdomain in sorted(by_domain[domain].keys()):
            items = by_domain[domain][subdomain]
            sample = ", ".join(i.get("name", "") for i in items[:3])
            if len(items) > 3:
                sample += f" (+{len(items)-3} more)"
            table.add_row(domain, subdomain, str(len(items)), sample)

    console.print(table)


def run_reindex(args):
    """Regenerate registry.md and registry.json."""
    indexer = RegistryIndexer(base_dir=".")
    stats = indexer.reindex()
    console.print(Panel.fit(
        f"[bold green]Registry Successfully Reindexed[/bold green]\n"
        f"Total Skills: [bold cyan]{stats['total_skills']}[/bold cyan]\n"
        f"Domains: [bold white]{', '.join(stats['domains'])}[/bold white]\n"
        f"Updated: [white]registry.md[/white] and [white]registry.json[/white]",
        border_style="green"
    ))


def run_validate(args):
    """Validate all skill markdown files against Schema v1.0."""
    indexer = RegistryIndexer(base_dir=".")
    skills_dir = Path("skills")

    if not skills_dir.exists():
        console.print("[red]skills/ directory not found.[/red]")
        return

    required_fields = ["id", "name", "domain", "subdomain", "version", "summary", "triggers", "tags"]
    errors = []
    validated = 0

    for path in sorted(skills_dir.rglob("*.md")):
        validated += 1
        data = indexer.parse_skill_file(path)
        if not data:
            errors.append(f"{path}: Missing or invalid YAML frontmatter")
            continue

        for field in required_fields:
            if field not in data or not data[field]:
                errors.append(f"{path}: Missing required field '{field}'")

    if errors:
        console.print(f"[bold red]Validation Failed with {len(errors)} error(s):[/bold red]")
        for err in errors[:15]:
            console.print(f"  - {err}")
    else:
        console.print(Panel.fit(
            f"[bold green]Validation Passed![/bold green]\n"
            f"All [bold cyan]{validated}[/bold cyan] skills conform to Schema v1.0.",
            border_style="green"
        ))


def main():
    parser = argparse.ArgumentParser(
        description="AI Agent Skill Registry CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # search
    search_p = subparsers.add_parser("search", help="Search skills by keyword or trigger")
    search_p.add_argument("query", help="Search term or phrase")
    search_p.add_argument("--domain", help="Filter by domain")
    search_p.add_argument("--subdomain", help="Filter by subdomain")
    search_p.add_argument("--max-results", type=int, default=15, help="Maximum results to display")
    search_p.set_defaults(func=run_search)

    # load
    load_p = subparsers.add_parser("load", help="Output raw markdown skill for agent context")
    load_p.add_argument("skill_id", help="Skill ID (e.g. ui-ux.interaction.modal-hierarchy) or slug")
    load_p.set_defaults(func=run_load)

    # list
    list_p = subparsers.add_parser("list", help="List all indexed skills by domain and subdomain")
    list_p.set_defaults(func=run_list)

    # reindex
    reindex_p = subparsers.add_parser("reindex", help="Rebuild registry.md and registry.json")
    reindex_p.set_defaults(func=run_reindex)

    # validate
    validate_p = subparsers.add_parser("validate", help="Validate all skill files against Schema v1.0")
    validate_p.set_defaults(func=run_validate)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
