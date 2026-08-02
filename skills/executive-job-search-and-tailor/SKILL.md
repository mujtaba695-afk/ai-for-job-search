---
name: executive-job-search-and-tailor
description: >-
  Automates end-to-end ATS job discovery (Greenhouse, Lever, Ashby, Workday), recency filtering (<14 days), Google Sheet tracking, and tailored 2-page Word (.docx) & PDF application package generation for Mujtaba Sajawal.
---

# Executive Job Search & Tailor Skill

## Overview
This skill orchestrates your complete executive job search workflow. It scans top ATS job boards for fresh Performance Marketing Lead and Growth Lead roles in Dubai and Remote EMEA, filters out stale/ghost postings, syncs opportunities with your Google Sheet tracker (**`Mujtaba - Job Shortlist v5`**), and generates tailored 2-page executive Word (`.docx`) and print-ready (`.pdf`) application packages.

## Dependencies
- Python 3.10+
- Node.js (for Puppeteer PDF generation)
- `python-docx`
- `career-ops` and `performance-marketing-job-search` modules

## Quick Start

```bash
# 1. Scan ATS boards for fresh roles (<14 days old) in Dubai & Remote
python3 ~/.gemini/config/skills/executive-job-search-and-tailor/scripts/run_job_pipeline.py scan --since 14

# 2. Sync job matches to your Google Sheet tracker
python3 ~/.gemini/config/skills/executive-job-search-and-tailor/scripts/run_job_pipeline.py sync

# 3. Build tailored resume & cover letter package for a job URL or role
python3 ~/.gemini/config/skills/executive-job-search-and-tailor/scripts/run_job_pipeline.py tailor --url "https://to.indeed.com/aakychpd8fph"
```

## Utility Commands

### `scan`
Scans Greenhouse, Lever, Ashby, and Workday for roles matching target titles and locations.
- Options: `--since <days>` (default 14), `--limit <count>`, `--dry-run`

### `sync`
Syncs newly discovered postings with your live Google Sheet tracker and checks for your recent remarks (*applied*, *need resume for this*, *not interested*).

### `tailor`
Tailors candidate accomplishments from `master_profile.json` to the target job description. Outputs:
- `Mujtaba_Sajawal_Resume.docx`
- `Mujtaba_Sajawal_Resume.pdf`
- `Mujtaba_Sajawal_CoverLetter.docx`
- `Mujtaba_Sajawal_CoverLetter.pdf`

## Rate Limiting & Safety
- Respects ATS rate limits (1 req/sec).
- Enforces strict zero-fabrication boundary (pulls exclusively from `master_profile.json`).

## Common Mistakes
1. Running from outside the `Downloads/Resume` directory without providing relative paths.
2. Manually editing candidate metrics or company titles — always use `master_profile.json` as the single source of truth.
3. Placing target keywords only in the bottom skills list — modern parsers evaluate skill duration/recency from dated work experience bullets.
4. Using tables, columns, or text boxes for right-aligned date formatting — always use **tab stops** to prevent text fragmentation.
5. Disregarding online application form fields (knockout questions) — these are the primary triggers for auto-rejection, while the resume is used for ranking.

