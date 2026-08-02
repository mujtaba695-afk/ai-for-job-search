# 🧠 48 Career Agent Skill Modules

This directory contains **48 skill modules** for AI coding agents, covering every
stage of the job search: discovery, ATS auditing, resume tailoring, outreach,
interview prep, and offer negotiation.

Every skill listed below exists as a directory in this folder. Each contains a
`SKILL.md` with YAML frontmatter and the workflow the agent should follow.

---

## 📋 Skill Catalog

### 1. ATS & Resume Engineering (8)
* `ats-checker`: Check resumes for ATS compatibility and optimization.
* `resume-parser`: Parse, analyze, and structure resumes/CVs.
* `resume-keyword-extractor`: Extract and analyze keywords from job descriptions for resume optimization.
* `resume-tailor`: Tailor resumes to match job descriptions with near-100% alignment.
* `resume-reframer`: Reframe existing experience for target roles without fabricating anything.
* `executive-job-search-and-tailor`: End-to-end ATS discovery (Greenhouse, Lever, Ashby, Workday), recency filtering, tracking, and tailored 2-page output.
* `portfolio-builder`: Build marketing portfolios and campaign case studies.
* `portfolio-website-generator`: Generate a professional portfolio website.

### 2. Job Discovery & Regional Job Boards (12)
* `job-search`: Broad search across performance marketing, paid media, PPC, SEM, programmatic, and related roles.
* `linkedin-jobs`: Optimized LinkedIn Jobs search.
* `indeed-jobs`: Search filters and salary insights for Indeed postings.
* `glassdoor-jobs`: Job search with integrated salary data, reviews, and interview insight.
* `google-jobs`: Broad aggregator search across direct company career pages.
* `remote-jobs`: Remote-specific job boards and platforms.
* `bayt-jobs`: Bayt.com and GulfTalent — Middle East & North Africa (MENA).
* `seek-jobs`: Seek.com.au — Australia & New Zealand.
* `stepstone-jobs`: StepStone, Xing Jobs, and European boards — Germany, Austria, Switzerland.
* `naukri-jobs`: Naukri.com and Foundit — India.
* `jobsdb-jobs`: JobsDB and JobStreet — Southeast Asia.
* `boss-zhipin`: BOSS 直聘, 拉勾, and 猎聘 — China.

### 3. Job Analysis & Market Intelligence (6)
* `job-posting-analyzer`: Deep-analyze postings for real requirements and red flags.
* `job-market-intelligence`: Real-time job market intelligence.
* `skills-gap-analyzer`: Analyze gaps between current skills and target roles.
* `competitor-candidate-analysis`: Analyze what competing candidates likely look like.
* `job-alert-monitor`: Set up automated job monitoring and alerts.
* `job-board-alert-aggregator`: Aggregate and deduplicate listings across multiple alerts.

### 4. Application & Recruiter Outreach (5)
* `cover-letter-writer`: Generate tailored cover letters.
* `referral-request-writer`: Craft personalized employee referral requests.
* `recruiter-response-handler`: Draft professional responses to recruiter outreach.
* `company-researcher`: Research companies for job applications.
* `networking-strategy`: Develop networking strategies and outreach messages.

### 5. Interview Prep (4)
* `interview-prep`: Role-specific questions, STAR answers, and mock scenarios.
* `interview-presentation-builder`: Build interview presentations and case study decks.
* `interview-thank-you`: Personalized post-interview thank-you emails.
* `marketing-case-study`: Detailed marketing and paid media campaign case studies.

### 6. Compensation & Offers (5)
* `salary-research`: Real-time salary benchmarks across global markets.
* `salary-negotiator`: Salary range research and negotiation strategies.
* `offer-evaluator`: Evaluate and compare total compensation.
* `freelance-rate-calculator`: Calculate freelance and contract rates.
* `resignation-letter`: Professional resignation letter templates.

### 7. Tracking & Accountability (3)
* `job-tracker`: Track applications, interview stages, follow-ups, and outcomes.
* `application-tracker-spreadsheet`: Create and manage a detailed application tracking spreadsheet.
* `job-search-accountability`: Accountability and progress tracking for job seekers.

### 8. Personal Brand & Career Growth (5)
* `linkedin-optimizer`: Optimize LinkedIn profiles for target roles.
* `linkedin-content-strategy`: Build thought leadership and visibility on LinkedIn.
* `personal-brand-auditor`: Audit and improve online presence and personal brand.
* `career-coach`: Career coaching and strategic guidance.
* `marketing-certification-guide`: Guide to relevant marketing certifications.

---

## 🛠️ How to Load a Skill

Each skill directory contains a `SKILL.md` with detailed instructions, prompt
rules, and workflow steps. To use a skill, point your AI agent at its `SKILL.md`
path or load the directory into a compatible agent runtime, then describe your
task in plain language.

These are instruction modules, not executable scripts — there is nothing to
`python3` here.
