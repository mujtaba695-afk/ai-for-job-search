"""Structural checks for the skill library.

These run offline and require no third-party packages beyond pytest. They guard
the invariants that are easy to break by hand: frontmatter validity, the catalog
staying in sync with the directories, and personal data leaking into a skill.
"""

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = ROOT / "skills"
CATALOG = SKILLS_DIR / "README.md"

SKILL_DIRS = sorted(p for p in SKILLS_DIR.iterdir() if p.is_dir())


def frontmatter(skill_dir):
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    match = re.match(r"---\n(.*?)\n---", text, re.S)
    assert match, f"{skill_dir.name}: SKILL.md has no YAML frontmatter block"
    return match.group(1)


def test_skill_directories_exist():
    assert SKILL_DIRS, "no skill directories found"


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
def test_skill_has_skill_md(skill_dir):
    assert (skill_dir / "SKILL.md").is_file(), f"{skill_dir.name}: missing SKILL.md"


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
def test_frontmatter_name_matches_directory(skill_dir):
    match = re.search(r"^name:\s*(\S+)", frontmatter(skill_dir), re.M)
    assert match, f"{skill_dir.name}: frontmatter has no 'name' field"
    assert match.group(1) == skill_dir.name, (
        f"{skill_dir.name}: frontmatter name is '{match.group(1)}'"
    )


@pytest.mark.parametrize("skill_dir", SKILL_DIRS, ids=lambda p: p.name)
def test_frontmatter_has_description(skill_dir):
    assert re.search(r"^description:", frontmatter(skill_dir), re.M), (
        f"{skill_dir.name}: frontmatter has no 'description' field"
    )


def test_catalog_matches_directories():
    listed = set(re.findall(r"^\* `([a-z0-9-]+)`:", CATALOG.read_text(encoding="utf-8"), re.M))
    actual = {p.name for p in SKILL_DIRS}
    assert not listed - actual, f"catalog lists non-existent skills: {sorted(listed - actual)}"
    assert not actual - listed, f"skills missing from catalog: {sorted(actual - listed)}"


def test_catalog_section_counts_are_accurate():
    text = CATALOG.read_text(encoding="utf-8")
    sections = re.findall(r"^### \d+\. .+? \((\d+)\)$", text, re.M)
    assert sections, "catalog has no numbered sections"
    assert sum(int(n) for n in sections) == len(SKILL_DIRS)


def test_profile_template_is_valid_json():
    data = json.loads((ROOT / "config" / "master_profile.template.json").read_text())
    assert set(data) >= {"candidate", "work_experience", "skills"}


# Patterns that indicate someone's real details were committed by mistake.
LEAK_PATTERNS = [
    (r"/Users/[a-z]", "absolute macOS home path"),
    (r"/home/[a-z]", "absolute Linux home path"),
    (r"C:\\\\Users\\\\", "absolute Windows home path"),
    (r"docs\.google\.com/spreadsheets/d/[A-Za-z0-9_-]{20,}", "Google Sheet URL"),
    (r"\bsheet_id\s*=\s*[\"'][A-Za-z0-9_-]{20,}[\"']", "hardcoded Google Sheet ID"),
    (r"\b[A-Za-z0-9._%+-]+@(?!example\.com)[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", "email address"),
]

TRACKED = [
    p
    for p in ROOT.rglob("*")
    if p.is_file()
    and ".git" not in p.parts
    and "__pycache__" not in p.parts
    and p.suffix in {".md", ".py", ".json", ".yml", ".yaml"}
    and p.name != "test_skills.py"  # this file contains the patterns themselves
]


@pytest.mark.parametrize("path", TRACKED, ids=lambda p: str(p.relative_to(ROOT)))
def test_no_personal_data_committed(path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    for pattern, label in LEAK_PATTERNS:
        match = re.search(pattern, text)
        assert not match, (
            f"{path.relative_to(ROOT)}: possible {label} -> {match.group(0)!r}"
        )
