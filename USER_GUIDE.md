# 🚀 User Guide: AI Job Search with Career Agent Skills

Welcome. This guide helps you set up the environment, use the 48 career agent
skills to search live job boards, audit residency/visa restrictions, and build
tailored PDF and Word application packages.

---

## 📋 Table of Contents
1. [Prerequisites](#️-prerequisites)
2. [Installation & Setup](#-installation--setup)
3. [Pre-Flight System Check](#-pre-flight-system-check)
4. [Configuring Your Profile](#-configuring-your-profile)
5. [Using the Skills](#-using-the-skills)
6. [Searching Live Job Boards](#-searching-live-job-boards)
7. [Analyzing Job Descriptions & ATS Match](#-analyzing-job-descriptions--ats-match)
8. [Generating Application Packages](#-generating-application-packages)

---

## 🛠️ Prerequisites
* **Python 3.10+**
* **Git**
* **An AI coding agent** that can read the `SKILL.md` instruction modules
* **Internet Connection** (for querying live Greenhouse, Lever, Ashby, and SmartRecruiters APIs)

---

## 📥 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mujtaba695-afk/ai-for-job-search.git
cd ai-for-job-search
```

That is enough to start using the skills — they are Markdown instruction
modules with no install step.

The packages in `requirements.txt` are optional and only needed once you start
generating `.docx` and `.pdf` documents:

```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

pip install -r requirements.txt
playwright install chromium  # only if you want HTML -> PDF rendering
```

---

## 🧪 Environment Check

Verify your Python version, the optional document libraries, and live ATS
connectivity:

```bash
python3 scripts/preflight_check.py
```

Each check prints its own status line. Missing optional packages are reported as
`OPTIONAL` and do not fail the run; only a too-old Python version does. Add
`--strict` to fail on optional checks too, or `--offline` to skip the network
probe.

---

## 👤 Configuring Your Profile

1. Copy the anonymized template:
   ```bash
   cp config/master_profile.template.json config/master_profile.json
   ```
2. Open `config/master_profile.json` in your editor and update your:
   * **Contact Information** (Name, Location, Email, Phone, LinkedIn, Portfolio)
   * **Executive Summary** (3–4 sentence value proposition)
   * **Work History** (Company, Title, Dates, Location, Bullet points with metrics)
   * **Skill Matrix** (Categorized tools, platforms, and methodologies)

`config/master_profile.json` is git-ignored, so your real details stay local.

---

## 🧠 Using the Skills

The 48 modules in `skills/` are **instruction sets for AI agents**, not
standalone command-line programs. Each `skills/<name>/SKILL.md` contains YAML
frontmatter (name, description, trigger conditions) followed by the workflow the
agent should follow.

To use one:

1. Open `skills/README.md` and find the skill matching your task.
2. Load that skill directory into your AI coding agent, or point the agent at
   the `SKILL.md` path.
3. Ask for the task in plain language — for example,
   *"Use the resume-tailor skill to align my resume to this job description."*

---

## 🔎 Searching Live Job Boards

Use the job discovery skills to search live company boards (Greenhouse, Lever,
Ashby, SmartRecruiters) and regional aggregators:

| Region / Source | Skill |
| --- | --- |
| Global / LinkedIn | `linkedin-jobs` |
| Global aggregator | `google-jobs`, `job-search` |
| Remote-first | `remote-jobs` |
| US / Global | `indeed-jobs`, `glassdoor-jobs` |
| MENA & Gulf | `bayt-jobs` |
| Australia & NZ | `seek-jobs` |
| DACH & Europe | `stepstone-jobs` |
| India | `naukri-jobs` |
| Southeast Asia | `jobsdb-jobs` |
| China | `boss-zhipin` |

For continuous coverage, combine `job-alert-monitor` with
`job-board-alert-aggregator` to deduplicate results across sources.

---

## 📊 Analyzing Job Descriptions & ATS Match

Before applying, run a posting through the analysis skills:

1. `job-posting-analyzer` — deep-analyze the posting for real requirements and red flags.
2. `resume-keyword-extractor` — pull the high-density keywords from the JD.
3. `ats-checker` — score your resume for ATS compatibility and formatting issues.
4. `skills-gap-analyzer` — identify gaps between your profile and the target role.
5. `competitor-candidate-analysis` — understand who else is likely applying.

---

## 📑 Generating Application Packages

Use the tailoring and outreach skills to build a complete application:

1. `resume-tailor` or `executive-job-search-and-tailor` — align your resume to the JD.
2. `resume-reframer` — reframe existing experience without fabricating anything.
3. `cover-letter-writer` — generate a tailored cover letter.
4. `interview-presentation-builder` — build a case study deck when one is requested.

Track everything with `job-tracker` and `application-tracker-spreadsheet`, then
use `salary-research`, `salary-negotiator`, and `offer-evaluator` once offers
arrive.

---

## 📄 License
Released under the [MIT License](LICENSE).
