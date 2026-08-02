# 🎯 AI Job Search — 48 Career Agent Skills

An open-source library of **48 agent skills** covering the full job search: discovering roles on
live ATS boards, auditing resumes for ATS compatibility, tailoring applications, preparing for
interviews, and negotiating offers.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Career Agent Skills](https://img.shields.io/badge/Career%20Agent%20Skills-48-purple.svg)](skills/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## What this is

Each skill is a **Markdown instruction module** — a `SKILL.md` with YAML frontmatter and a
workflow an AI coding agent follows. Point your agent at a skill and describe your task in plain
language.

This is a prompt/skill library, not an application. The repository ships instruction modules, a
profile template, and an environment check; it does not ship a job scraper or a resume renderer.
The skills tell an agent how to build those against your own profile.

---

## 🌟 Skill Coverage

**Job discovery (12)** — Live company boards and regional aggregators:
`linkedin-jobs`, `indeed-jobs`, `glassdoor-jobs`, `google-jobs`, `remote-jobs`, `job-search`,
`bayt-jobs` (MENA), `seek-jobs` (ANZ), `stepstone-jobs` (DACH), `naukri-jobs` (India),
`jobsdb-jobs` (SEA), `boss-zhipin` (China).

**ATS & resume engineering (8)** — `ats-checker`, `resume-parser`, `resume-keyword-extractor`,
`resume-tailor`, `resume-reframer`, `executive-job-search-and-tailor`, `portfolio-builder`,
`portfolio-website-generator`.

**Job analysis & market intelligence (6)** — `job-posting-analyzer`, `job-market-intelligence`,
`skills-gap-analyzer`, `competitor-candidate-analysis`, `job-alert-monitor`,
`job-board-alert-aggregator`.

**Application & outreach (5)** — `cover-letter-writer`, `referral-request-writer`,
`recruiter-response-handler`, `company-researcher`, `networking-strategy`.

**Interview prep (4)** — `interview-prep`, `interview-presentation-builder`,
`interview-thank-you`, `marketing-case-study`.

**Compensation & offers (5)** — `salary-research`, `salary-negotiator`, `offer-evaluator`,
`freelance-rate-calculator`, `resignation-letter`.

**Tracking (3)** — `job-tracker`, `application-tracker-spreadsheet`, `job-search-accountability`.

**Personal brand (5)** — `linkedin-optimizer`, `linkedin-content-strategy`,
`personal-brand-auditor`, `career-coach`, `marketing-certification-guide`.

See [`skills/README.md`](skills/README.md) for the full catalog with descriptions.

---

## 🎯 Focus

The skills are written for **performance marketing, paid media, growth, and digital marketing**
roles — search queries, salary bands, and keyword guidance assume that domain. They adapt to
adjacent fields, but you will get the most out of them in marketing and growth.

---

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/mujtaba695-afk/ai-for-job-search.git
cd ai-for-job-search

# Verify your environment (standard library only, no install needed)
python3 scripts/preflight_check.py
```

Set up your profile:

```bash
cp config/master_profile.template.json config/master_profile.json
```

Fill it in with your real details. That file is git-ignored, so it stays on your machine.

Once you start generating documents, install the libraries the skills recommend:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

See [USER_GUIDE.md](USER_GUIDE.md) for full usage instructions.

---

## 🔒 Privacy

These skills operate on your own data. A few habits worth keeping:

- Keep real details in `config/master_profile.json`, never inside a skill file
- `.gitignore` already excludes that file plus generated `*.pdf` and `*.docx` output
- Review anything an agent writes before committing it to a public repository

---

## 🤝 Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md) for the skill format
and the checks to run before opening one.

---

## 📄 License

[MIT](LICENSE).
