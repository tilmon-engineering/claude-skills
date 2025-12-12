#!/usr/bin/env python3

"""
Script to analyze skill dependencies and generate a Mermaid diagram
- Sorts skills by dependency count (most dependencies first)
- Detects and highlights circular dependencies in red
Usage: python3 analyze-skill-dependencies.py
"""

import re
import subprocess
from pathlib import Path
from collections import defaultdict

# Configuration
SKILLS_DIR = Path(".claude/skills")
OUTPUT_FILE = SKILLS_DIR / "skill-dependencies.mermaid"

def get_skills():
    """Get list of skill directories."""
    skills = []
    for item in SKILLS_DIR.iterdir():
        # Skip files and hidden directories
        if item.is_dir() and not item.name.startswith('.'):
            skills.append(item.name)
    return sorted(skills)

def find_skill_references(skill_dir, skills):
    """
    Find all references to other skills in a skill directory.
    Returns a dict with 'all', 'prerequisites', and 'invocations'.
    """
    pattern = '|'.join(re.escape(s) for s in skills)

    # Patterns that indicate a prerequisite or informational reference (not an active invocation)
    prerequisite_patterns = [
        r'prerequisite.*?(`|skill[:\s])',  # "prerequisite" followed by skill reference
        r'(have|has)\s+completed.*?(`|skill)',  # "have completed"
        r'after.*?(`|skill)',  # "after X skill"
        r'before.*?using',  # "before using"
        r'must.*?(complete|have).*?(`|skill)',  # "must complete/have"
        r'requires?.*?(`|skill)',  # "requires"
        r'depends?\s+on.*?(`|skill)',  # "depends on"
        r'flow.*?through.*?(`|skill)',  # "flow through" (pipeline)
        r'MANDATORY.*?before',  # "MANDATORY before"
        r'see also.*?(`|skill)',  # "See also:" informational references
        r'related skills?.*?(`|skill)',  # "Related skills:" informational references
        r'\bsee\s+`[^`]+`\s+skill',  # "see `skill-name` skill"
    ]

    all_references = set()
    prerequisites = set()

    # Get all skill references with context (5 lines before and after)
    try:
        result = subprocess.run(
            ['grep', '-r', '-i', '-B', '5', '-A', '5', '-E', pattern, str(skill_dir)],
            capture_output=True,
            text=True
        )

        if result.returncode == 0:
            lines = result.stdout

            # Extract skill names from the output
            for skill in skills:
                if skill in lines:
                    all_references.add(skill)

                    # Check if this reference appears in a prerequisite context
                    for prereq_pattern in prerequisite_patterns:
                        # Look for the skill name near prerequisite keywords
                        context_pattern = f'({prereq_pattern}).*?{re.escape(skill)}|{re.escape(skill)}.*?({prereq_pattern})'
                        if re.search(context_pattern, lines, re.IGNORECASE | re.DOTALL):
                            prerequisites.add(skill)
                            break

    except Exception as e:
        print(f"Warning: Error searching {skill_dir}: {e}")

    # Invocations are references that aren't prerequisites
    invocations = all_references - prerequisites

    return {
        'all': all_references,
        'prerequisites': prerequisites,
        'invocations': invocations
    }

def build_dependency_graph(skills):
    """
    Build dependency graphs for all skills.
    Returns three graphs: all, prerequisites_only, invocations_only
    """
    graph_all = defaultdict(set)
    graph_prereq = defaultdict(set)
    graph_invoke = defaultdict(set)

    for skill in skills:
        skill_dir = SKILLS_DIR / skill
        print(f"Analyzing {skill}...")

        ref_data = find_skill_references(skill_dir, skills)

        # Build graphs, filtering out self-references
        for ref in ref_data['all']:
            if ref != skill and ref in skills:
                graph_all[skill].add(ref)

        for ref in ref_data['prerequisites']:
            if ref != skill and ref in skills:
                graph_prereq[skill].add(ref)

        for ref in ref_data['invocations']:
            if ref != skill and ref in skills:
                graph_invoke[skill].add(ref)

    return {
        'all': graph_all,
        'prerequisites': graph_prereq,
        'invocations': graph_invoke
    }

def count_dependencies(graph, skills):
    """Count dependencies for each skill."""
    counts = {}
    for skill in skills:
        counts[skill] = len(graph.get(skill, set()))
    return counts

def detect_circular_dependencies(graph, label=""):
    """Detect bidirectional (circular) dependencies."""
    circular = set()

    for source, targets in graph.items():
        for target in targets:
            # Check if reverse edge exists
            if source in graph.get(target, set()):
                # Store as sorted tuple to avoid duplicates
                edge = tuple(sorted([source, target]))
                circular.add(edge)

    return circular

def generate_mermaid_diagram(graph, dep_counts, circular_deps):
    """Generate Mermaid diagram with sorted dependencies and styling."""
    # Sort skills by dependency count (descending)
    sorted_skills = sorted(dep_counts.keys(), key=lambda s: dep_counts[s], reverse=True)

    lines = ["graph TD", ""]

    # Track edge indices for styling
    edge_styles = []
    edge_index = 0

    # Generate edges sorted by source skill
    for skill in sorted_skills:
        targets = sorted(graph.get(skill, set()))
        for target in targets:
            # Check if this is a circular dependency
            edge_tuple = tuple(sorted([skill, target]))
            if edge_tuple in circular_deps:
                lines.append(f"    {skill} -->|⚠️| {target}")
                edge_styles.append(f"    linkStyle {edge_index} stroke:#ff0000,stroke-width:3px")
            else:
                lines.append(f"    {skill} --> {target}")
            edge_index += 1

    # Add styling for circular dependencies
    if edge_styles:
        lines.append("")
        lines.append("    %% Style circular dependencies")
        lines.extend(edge_styles)

    return '\n'.join(lines)

def main():
    print("=" * 60)
    print("Skill Dependency Analysis")
    print("=" * 60)
    print()

    # Get all skills
    skills = get_skills()
    print(f"Found {len(skills)} skills:")
    print(f"  {', '.join(skills)}")
    print()

    # Build dependency graphs
    print("Building dependency graph...")
    graphs = build_dependency_graph(skills)
    graph_all = graphs['all']
    graph_prereq = graphs['prerequisites']
    graph_invoke = graphs['invocations']
    print()

    # Count dependencies
    print("Counting dependencies...")
    dep_counts = count_dependencies(graph_all, skills)

    # Sort and display
    sorted_skills = sorted(dep_counts.keys(), key=lambda s: dep_counts[s], reverse=True)
    print("\nSkills sorted by dependency count:")
    for skill in sorted_skills:
        count = dep_counts[skill]
        print(f"  {skill}: {count} dependencies")
    print()

    # Detect circular dependencies
    print("Detecting circular dependencies...")

    # Check all relationships
    all_circular = detect_circular_dependencies(graph_all)
    print(f"  Total bidirectional relationships: {len(all_circular)}")

    # Check only prerequisite relationships
    prereq_circular = detect_circular_dependencies(graph_prereq)
    print(f"  Prerequisite cycles (expected/harmless): {len(prereq_circular)}")

    # Check invocation relationships (these are potential problems)
    invoke_circular = detect_circular_dependencies(graph_invoke)

    if invoke_circular:
        print(f"\n⚠️  Found {len(invoke_circular)} problematic circular invocations:")
        for pair in sorted(invoke_circular):
            print(f"     {pair[0]} ↔ {pair[1]}")
    else:
        print("\n✓ No problematic circular invocations found.")

    print("\nPrerequisite cycles (harmless workflow sequences):")
    for pair in sorted(prereq_circular):
        print(f"  ✓ {pair[0]} ↔ {pair[1]}")
    print()

    # Generate Mermaid diagram - only highlight problematic invocation cycles
    print("Generating Mermaid diagram...")
    mermaid = generate_mermaid_diagram(graph_all, dep_counts, invoke_circular)

    # Write to file
    OUTPUT_FILE.write_text(mermaid)

    # Calculate statistics
    total_edges = sum(len(targets) for targets in graph_all.values())
    total_prereq = sum(len(targets) for targets in graph_prereq.values())
    total_invoke = sum(len(targets) for targets in graph_invoke.values())

    print()
    print("=" * 60)
    print("Analysis complete!")
    print("=" * 60)
    print(f"Output file: {OUTPUT_FILE}")
    print()
    print("Statistics:")
    print(f"  Total skills: {len(skills)}")
    print(f"  Total references: {total_edges}")
    print(f"    Prerequisites: {total_prereq}")
    print(f"    Invocations: {total_invoke}")
    print(f"  Bidirectional relationships: {len(all_circular)}")
    print(f"    Prerequisite cycles (harmless): {len(prereq_circular)}")
    print(f"    Invocation cycles (problematic): {len(invoke_circular)}")
    print()
    print("Preview:")
    print("-" * 60)
    print(mermaid)
    print("-" * 60)

if __name__ == "__main__":
    main()
