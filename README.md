# 🎯 Open ATS Career Engine & Executive Resume Generator

An open-source, automated **job search, live ATS verification, and executive application package generator** designed for senior professionals, performance marketing leads, and growth marketers.

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Chromium-green.svg)](https://playwright.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## 🌟 Key Features

### 1. Real-Time Live ATS Verification Engine
Bypasses stale third-party caches by querying official **Greenhouse, Ashby, Lever, SmartRecruiters, and Workday APIs** directly.
*   **Live HTTP 200 Checks**: Verifies every posting is open right now before you spend time applying.
*   **Location & Residency Auditing**: Scans raw ATS headers for `US-Only`, `EMEA Remote`, `Worldwide Remote`, or `Relocation Sponsorship`.
*   **Recency Thresholds**: Filters for jobs posted within the last 24 hours, 7 days, or 14 days.

### 2. Playwright & DOCX Pixel-Perfect Resume Engine
Generates high-converting **PDF & Word (.docx) resumes** tailored to specific Job Descriptions (JDs).
*   **Typography & Styling**: Built using modern fonts (*Plus Jakarta Sans*, *Inter*), HSL gradient section accents, and badge elements.
*   **Page Budget Discipline**: Enforces strict single-page (specialist) or two-page (executive) fit without awkward trailing lines or orphaned headings.
*   **ATS Keyword Injection**: Seamlessly maps candidate achievements to exact JD requirements without buzzword stuffing.

### 3. Tailored Executive Cover Letter Generator
Produces strategic, executive cover letters mapping candidate achievements to the company's specific strategic ownership pillars.

---

## 🚀 Quick Start Guide

```bash
# Clone the repository
git clone https://github.com/mujtaba695-afk/open-ats-career-engine.git
cd open-ats-career-engine

# Set up Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

# Install Dependencies
pip install -r requirements.txt
playwright install chromium

# Run System Sanity Test
python3 tests/test_pipeline.py
```

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
