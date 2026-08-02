---
name: executive-job-search-and-tailor
description: >
  End-to-end executive job search: discover fresh roles directly from company ATS boards
  (Greenhouse, Lever, Ashby, Workday), filter out stale and ghost postings, track opportunities
  in a spreadsheet, and produce tailored two-page resume and cover letter packages.
  Use when the user wants to run a full job search cycle rather than a single task — scanning
  boards for new roles, maintaining a pipeline, and generating application packages for the
  roles worth pursuing. Specialized for senior performance marketing, digital marketing,
  paid media, and growth leadership roles.
---

# Executive Job Search & Tailor

Orchestrates a complete job search cycle: **discover → filter → track → tailor**. Use the
focused skills for individual steps; use this one to run the whole loop.

## Prerequisites

Ask the user for these before starting:

1. **Target titles** — e.g. "Performance Marketing Lead", "Growth Lead"
2. **Target locations** — cities, regions, or remote scope (e.g. "Remote EMEA")
3. **Recency window** — how old a posting may be, in days (14 is a sensible default)
4. **Candidate profile** — a filled-in `config/master_profile.json` (copy it from
   `config/master_profile.template.json`)

Never invent any of these. If the profile is missing, stop and ask for it.

---

## 1. Discover

Query company ATS boards directly rather than aggregators — aggregator listings go stale and
often outlive the posting itself.

| ATS | Public endpoint pattern |
| --- | --- |
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/{company}/jobs` |
| Lever | `https://api.lever.co/v0/postings/{company}?mode=json` |
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/{company}` |
| SmartRecruiters | `https://api.smartrecruiters.com/v1/companies/{company}/postings` |

Rate-limit to roughly **1 request per second** per host, and set a descriptive `User-Agent`.

For board-specific and regional searches, use the dedicated discovery skills instead:
`linkedin-jobs`, `indeed-jobs`, `glassdoor-jobs`, `remote-jobs`, `bayt-jobs`, `seek-jobs`,
`stepstone-jobs`, `naukri-jobs`, `jobsdb-jobs`, `boss-zhipin`, `google-jobs`.

## 2. Filter

Drop a posting when any of these is true:

- It is older than the recency window
- The endpoint no longer returns HTTP 200 (the role closed)
- Location or work-authorization requirements exclude the candidate
- The title matches but the seniority clearly does not

Record *why* each posting was dropped, so the user can audit the filter.

## 3. Track

Maintain one row per opportunity. A workable minimum:

| Field | Notes |
| --- | --- |
| Company | |
| Role | |
| Location | Include remote scope |
| Source | Which ATS or board |
| Posted | Date, for recency |
| Link | Canonical posting URL |
| Status | `new` → `applied` → `screen` → `onsite` → `offer` / `rejected` |
| Notes | The user's own remarks |

Use `job-tracker` or `application-tracker-spreadsheet` for the tracker itself. On each run,
read the user's existing remarks before adding rows, and never overwrite them.

## 4. Tailor

For each role the user marks as worth pursuing:

1. `job-posting-analyzer` — extract the real requirements
2. `resume-keyword-extractor` — pull the high-signal keywords
3. `resume-tailor` — align the resume to the posting
4. `ats-checker` — verify the result parses cleanly
5. `cover-letter-writer` — draft the letter

Name outputs after the candidate and target, for example
`{LastName}_{Company}_Resume.docx`. Ask the user for their preferred naming rather than
assuming one.

---

## Zero-Fabrication Boundary

Every claim in generated documents must trace back to `master_profile.json`. Do not invent
metrics, employers, dates, titles, or tools. If the profile lacks something the posting asks
for, say so plainly and let the user decide — a gap the user knows about is far better than a
fabrication they discover in an interview.

## Formatting Rules That Affect Parsing

1. Use **tab stops** for right-aligned dates. Tables, columns, and text boxes fragment text in
   most ATS parsers.
2. Put keywords in dated experience bullets, not only in a trailing skills list — parsers infer
   recency and duration from where a skill appears.
3. Keep to a two-page budget for senior roles, without orphaned headings or single trailing lines.
4. Treat application form knockout questions as the primary rejection trigger; the resume is
   mostly used for ranking after that gate.

## Common Mistakes

1. Trusting an aggregator's "posted" date instead of re-checking the ATS endpoint.
2. Editing metrics or titles by hand instead of updating `master_profile.json`.
3. Re-running a scan and clobbering the user's tracker notes.
4. Tailoring before confirming the posting is still open.
