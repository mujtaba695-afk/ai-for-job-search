# 🚀 User Guide: Open ATS Career Engine & Resume Generator

Welcome to the **Open ATS Career Engine**. This guide will help you set up the environment, search live job boards, audit residency/visa restrictions, and build tailored PDF and Word application packages.

---

## 📋 Table of Contents
1. [Prerequisites](#-prerequisites)
2. [Installation & Setup](#-installation--setup)
3. [Pre-Flight System Check](#-pre-flight-system-check)
4. [Configuring Your Profile](#-configuring-your-profile)
5. [Searching Live Job Boards](#-searching-live-job-boards)
6. [Analyzing Job Descriptions & ATS Match](#-analyzing-job-descriptions--ats-match)
7. [Generating Application Packages](#-generating-application-packages)

---

## 🛠️ Prerequisites
* **Python 3.10+**
* **Git**
* **Internet Connection** (for querying live Greenhouse, Lever, Ashby, and SmartRecruiters APIs)

---

## 📥 Installation & Setup

```bash
# Clone the repository
git clone https://github.com/mujtaba695-afk/marketing-ai-analytics-resume.git
cd marketing-ai-analytics-resume

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
playwright install chromium
```

---

## 🧪 Pre-Flight System Check

Run the self-diagnostic test to verify Playwright Chromium, Python modules, and API connectors on your machine:

```bash
python3 tests/test_pipeline.py
```
*Expected Output: `✅ All Systems Operational: Playwright, ATS Connectors & Exporters ready.`*

---

## 👤 Configuring Your Profile

1. Copy the anonymized template:
   ```bash
   cp config/master_profile.template.json config/master_profile.json
   ```
2. Open `config/master_profile.json` in your favorite code editor and update your:
   * **Contact Information** (Name, Location, Email, Phone, LinkedIn, Portfolio)
   * **Executive Summary** (3–4 sentence value proposition)
   * **Work History** (Company, Title, Dates, Location, Bullet points with metrics)
   * **Skill Matrix** (Categorized tools, platforms, and methodologies)

---

## 🔎 Searching Live Job Boards

Search live company job boards (Greenhouse, Lever, Ashby, SmartRecruiters) directly to find 100% active roles:

```bash
python3 search_dubai_relocation_jobs.py
```
*This verifies `HTTP 200 OK` status and location suitability in real-time.*

---

## 📑 Generating Application Packages

To build a tailored 2-page PDF & Word resume plus executive cover letter:

```bash
python3 build_getyourguide_package.py
```

Generated outputs will be saved in your project folder as:
* 📄 `Candidate_Resume.pdf` (Pixel-perfect Playwright PDF)
* 📝 `Candidate_Resume.docx` (Matching Word Document)
* 📄 `Candidate_Cover_Letter.pdf` (Tailored Cover Letter PDF)
* 📝 `Candidate_Cover_Letter.docx` (Matching Cover Letter DOCX)

---

## 📄 License
Released under the [MIT License](LICENSE).
