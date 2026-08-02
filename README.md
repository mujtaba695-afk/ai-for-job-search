# 🎯 AI Job Search with 48 Career Agent Skills

An open-source, autonomous **AI Job Search Engine with 48 Career Agent Skills, Live ATS Verifier & Playwright Resume Exporter** designed for senior professionals, performance marketing leads, and growth marketers.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium-green.svg)](https://playwright.dev/)
[![Career Agent Skills](https://img.shields.io/badge/Career%20Agent%20Skills-48-purple.svg)](skills/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Key Features

### 1. 🤖 48 Career Agent Skill Modules (`skills/`)
Automates every stage of the executive job hunt, from keyword parsing to compensation negotiation:
*   **Job Discovery Skills**: `linkedin-jobs`, `indeed-jobs`, `glassdoor-jobs`, `bayt-jobs`, `seek-jobs`, `stepstone-jobs`, `naukri-jobs`, `jobsdb-jobs`, `boss-zhipin`, `google-jobs`, `remote-jobs`, `job-alert-monitor`.
*   **ATS & Resume Engineering**: `ats-checker`, `resume-parser`, `resume-keyword-extractor`, `resume-tailor`, `resume-reframer`, `executive-job-search-and-tailor`, `portfolio-builder`, `portfolio-website-generator`.
*   **Application & Outreach Skills**: `cover-letter-writer`, `referral-request-writer`, `recruiter-response-handler`, `interview-thank-you`, `company-researcher`, `networking-strategy`.
*   **Interview & Negotiation Skills**: `interview-prep`, `interview-presentation-builder`, `marketing-case-study`, `salary-negotiator`, `salary-research`, `offer-evaluator`, `resignation-letter`.

See [`skills/README.md`](skills/README.md) for the complete catalog of all 48 skills.

### 2. ⚡ Real-Time Live ATS Verification Engine
Bypasses stale third-party caches by querying official **Greenhouse, Ashby, Lever, SmartRecruiters, and Workday APIs** directly.
*   **Live HTTP 200 Checks**: Verifies every posting is open right now before you spend time applying.
*   **Location & Residency Auditing**: Scans raw ATS headers for `US-Only`, `EMEA Remote`, `Worldwide Remote`, or `Relocation Sponsorship`.
*   **Recency Thresholds**: Filters for jobs posted within the last 24 hours, 7 days, or 14 days.

### 3. 🎨 Playwright & DOCX Pixel-Perfect Resume Engine
Generates high-converting **PDF & Word (.docx) resumes** tailored to specific Job Descriptions (JDs).
*   **Typography & Styling**: Built using modern fonts (*Plus Jakarta Sans*, *Inter*), HSL gradient section accents, and badge elements.
*   **Page Budget Discipline**: Enforces strict single-page (specialist) or two-page (executive) fit without awkward trailing lines or orphaned headings.
*   **ATS Keyword Injection**: Seamlessly maps candidate achievements to exact JD requirements without buzzword stuffing.

### 4. ✉️ Tailored Executive Cover Letter Generator
Produces strategic, executive cover letters mapping candidate achievements to the company's specific strategic ownership pillars.

---

## 🚀 Quick Start Guide

```bash
# Clone the repository
git clone https://github.com/mujtaba695-afk/ai-for-job-search.git
cd ai-for-job-search

# Set up Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
playwright install chromium

# Run System Sanity Test
python3 tests/test_pipeline.py
```

The sanity test prints a per-check `PASS`/`FAIL` line and exits non-zero if
anything is missing, so it can also be wired into CI.

---

## 🧠 How the Skills Work

The skills in this repository are **Markdown instruction modules**, not
executable Python. Each `skills/<name>/SKILL.md` carries YAML frontmatter and a
workflow an AI coding agent follows. Point your agent at a skill directory (or
load it into a compatible agent runtime) and ask for the task in plain language.

See [USER_GUIDE.md](USER_GUIDE.md) for full usage instructions.

---

## 👤 Author & Maintainer

**Mujtaba Sajawal**
*   **Role**: Performance Marketing Lead | Paid Media & Growth Analytics
*   **LinkedIn**: [linkedin.com/in/mujtaba-sajawal](https://www.linkedin.com/in/mujtaba-sajawal)
*   **Portfolio**: [mujtaba695-afk.github.io/marketing-ai-analytics-resume](https://mujtaba695-afk.github.io/marketing-ai-analytics-resume/)

---

## 📄 License
This project is open-source under the [MIT License](LICENSE).
