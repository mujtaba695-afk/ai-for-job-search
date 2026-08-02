---
name: job-search
description: >
  Search for performance marketing, digital marketing, paid media, PPC, SEM, social media advertising,
  programmatic advertising, and related marketing roles across global job boards.
  Use when the user wants to find job listings, search job portals, discover open roles in
  digital/performance marketing, or research the job market for paid media positions.
  Covers LinkedIn, Indeed, Glassdoor, Google Jobs, and regional boards (Seek, StepStone, Bayt,
  Naukri, JobsDB, Boss直聘, 拉勾, etc.). Only for marketing/advertising roles — not general job search.
---

# Job Search — Performance & Digital Marketing Roles

## Scope

Only search for roles in these domains:
- Performance Marketing / Growth Marketing
- Paid Media / Paid Social / Paid Search
- PPC / SEM / Google Ads / Bing Ads
- Programmatic Advertising / DSP / DV360 / The Trade Desk
- Social Media Advertising (Meta Ads, TikTok Ads, LinkedIn Ads, Twitter/X Ads)
- Display & Video Advertising
- Affiliate Marketing
- Conversion Rate Optimization (CRO)
- Marketing Analytics (paid channel focus)
- E-commerce Marketing / DTC Marketing
- App Install / Mobile Marketing (UA)

Reject or skip any roles outside these domains.

## Workflow

### 1. Gather Requirements

Ask (or infer from context):
- **Location**: City, country, or "remote"
- **Seniority**: Junior / Mid / Senior / Lead / Director / VP / Head
- **Employment type**: Full-time, contract, freelance, agency
- **Salary range**: Optional, filter if provided
- **Keywords**: Specific platforms (Google Ads, Meta, TikTok), industries, or company names

### 2. Search Strategy

Search across multiple sources in parallel. For each source, use `web_fetch` or `mimo_web_search`.

#### Global Job Boards

| Board | Search Approach |
|---|---|
| **LinkedIn** | `mimo_web_search`: "site:linkedin.com/jobs {role} in {location}" |
| **Indeed** | `web_fetch`: `https://www.indeed.com/jobs?q={keywords}&l={location}` |
| **Glassdoor** | `mimo_web_search`: "site:glassdoor.com {role} jobs {location}" |
| **Google Jobs** | `mimo_web_search`: "{role} jobs in {location}" |
| **SimplyHired** | `mimo_web_search`: "site:simplyhired.com {role} {location}" |
| **ZipRecruiter** | `mimo_web_search`: "site:ziprecruiter.com {role} {location}" |

#### Regional Job Boards

| Region | Board | Approach |
|---|---|---|
| **UK** | Reed, TotalJobs | `mimo_web_search`: "site:reed.co.uk {role}" |
| **EU** | StepStone, EuroJobs | `mimo_web_search`: "{role} jobs {country}" |
| **Australia/NZ** | Seek | `mimo_web_search`: "site:seek.com.au {role}" |
| **India** | Naukri, Foundit | `mimo_web_search`: "site:naukri.com {role} {location}" |
| **Middle East** | Bayt, GulfTalent | `mimo_web_search`: "site:bayt.com {role}" |
| **Southeast Asia** | JobsDB, JobStreet | `mimo_web_search`: "site:jobsdb.com {role} {location}" |
| **China** | Boss直聘, 拉勾, 猎聘 | `mimo_web_search`: "{role} 招聘 {location}" |
| **Germany** | StepStone, Xing | `mimo_web_search`: "site:stepstone.de {role}" |
| **Canada** | Job Bank, Workopolis | `mimo_web_search`: "{role} jobs Canada {city}" |

#### Niche / Marketing-Specific Boards

- **MarketingHire** — marketing-specific roles
- **AngelList/Wellfound** — startup marketing roles
- **The Drum** — advertising/marketing industry jobs
- **PerformanceIN** — performance marketing specific
- **Remotive, We Work Remotely, FlexJobs** — remote marketing roles

### 3. Search Query Construction

Build search queries using these keyword combinations (rotate through them for breadth):

```
Primary:
- "performance marketing"
- "paid media"
- "paid digital marketing"
- "PPC manager"
- "SEM specialist"
- "growth marketing"

Platform-specific:
- "Google Ads specialist"
- "Meta ads manager"
- "TikTok ads"
- "programmatic media buyer"
- "paid social media manager"

Seniority variants:
- "performance marketing director"
- "head of paid media"
- "VP of growth"
- "paid media lead"
```

Combine with location and adjust keywords per user preference.

### 4. Extract & Present Results

For each job found, extract:
- **Job Title**
- **Company**
- **Location** (including remote/hybrid/onsite)
- **Salary** (if listed)
- **Posted Date**
- **Key Requirements** (brief summary)
- **Source/URL**

Present results in a clean table or grouped list. Sort by relevance (most recent first within each source).

### 5. Deep Dive (Optional)

When user wants more detail on a specific listing:
- Fetch the full job description with `web_fetch`
- Summarize key requirements, nice-to-haves, and company info
- Flag if the role is truly performance/paid media focused (vs. general marketing with paid as a small part)

## Output Format

```
## 🔍 Job Search Results: [Role] in [Location]

### LinkedIn (X results)
| # | Title | Company | Location | Salary | Posted | Link |
|---|-------|---------|----------|--------|--------|------|
| 1 | ...   | ...     | ...      | ...    | ...    | ...  |

### Indeed (X results)
...

### 💡 Tips
- [Any observations about the market, salary trends, or role patterns]
```

## Important Notes

- Always use `web_fetch` for individual job pages to get full descriptions
- Use `mimo_web_search` for broad discovery across Google Jobs and aggregated results
- Respect rate limits — don't hammer a single site with rapid requests
- If a job board blocks scraping, note it and suggest the user visit directly
- Always verify the role is actually in the performance/paid media domain before presenting
