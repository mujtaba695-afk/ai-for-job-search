# Contributing

Contributions are welcome — new skills, corrections to existing ones, and better guidance for
regions or roles that are thinly covered.

## Skill format

Every skill is one directory under `skills/` containing a single `SKILL.md`:

```
skills/your-skill-name/SKILL.md
```

`SKILL.md` opens with YAML frontmatter:

```markdown
---
name: your-skill-name
description: >
  What the skill does, in one or two sentences.
  Use when the user wants to: <concrete triggers, comma separated>.
---

# Your Skill Name

## Workflow
...
```

Rules the test suite enforces:

- `name` must match the directory name exactly
- `description` must be present
- The skill must be listed in `skills/README.md` under a section whose heading count is accurate

Keep skills as instructions for an agent, not as executable scripts. The library is deliberately
Markdown-only apart from `scripts/preflight_check.py`.

## Never commit personal data

This repository is public and the skills operate on real career data. The test suite fails if it
finds any of the following in a tracked file:

- Absolute home paths (`/Users/...`, `/home/...`, `C:\Users\...`)
- Google Sheet IDs or spreadsheet URLs
- Email addresses other than `@example.com`

Put your own details in `config/master_profile.json`, which is git-ignored. Generated `.pdf` and
`.docx` files are ignored too.

## Running the checks locally

```bash
pip install pytest
python -m pytest tests/ -q
python scripts/preflight_check.py --offline
```

Both run offline and take a couple of seconds.

## Pull requests

1. One skill or one focused fix per pull request
2. Update `skills/README.md` when adding or removing a skill, including the section count
3. Make sure the checks pass before opening the PR
