---
name: linkedin-jobs
description: >
  Search LinkedIn Jobs specifically for performance marketing, digital marketing, paid media, PPC,
  SEM, growth marketing, and related roles. Optimized for LinkedIn's structure including Easy Apply,
  company pages, and recruiter connections. Use when the user wants to search LinkedIn for marketing
  jobs, filter by LinkedIn-specific criteria (company size, remote policy, experience level), or
  get insights from LinkedIn job postings.
---

# LinkedIn Jobs — Performance & Digital Marketing Specialist

## Search Strategy

### URL Construction
```
https://www.linkedin.com/jobs/search/?keywords={keywords}&location={location}&f_WT={work_type}&f_E={experience}&f_JT={job_type}
```

Work types: `1` = On-site, `2` = Remote, `3` = Hybrid
Experience: `1` = Internship, `2` = Entry, `3` = Associate, `4` = Mid-Senior, `5` = Director, `6` = Executive
Job types: `F` = Full-time, `P` = Part-time, `C` = Contract, `T` = Temporary

### Keyword Rotations (search each separately for breadth)
```
Batch 1 (Core):
- "performance marketing"
- "paid media manager"
- "growth marketing"
- "PPC specialist"

Batch 2 (Platform):
- "Google Ads manager"
- "Meta ads specialist"
- "TikTok advertising"
- "paid social media"

Batch 3 (Seniority):
- "head of performance marketing"
- "director of paid media"
- "VP growth marketing"
- "paid media lead"
```

### Search Method
1. Use `mimo_web_search` with `site:linkedin.com/jobs` prefix
2. For individual listings, use `web_fetch` on the LinkedIn job URL
3. Extract: title, company, location, posted date, salary (if listed), description

### LinkedIn-Specific Extraction
- **Company size** — from LinkedIn company page
- **Connections** — if user has connections at the company
- **Recruiter** — identify the poster if visible
- **Easy Apply** — note if Easy Apply is available
- **Similar jobs** — note other roles at the same company

### Company Insights (from LinkedIn)
- Company page follower count
- Recent company posts (marketing maturity signal)
- Marketing team size (count marketing employees)
- Growth trajectory (hiring velocity)

## Output

```
## 💼 LinkedIn Jobs: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [Location] | 💰 [Salary] | 🕐 [Posted]
- 👥 Company size: [X] | 📊 [Y] marketing employees
- 🔗 [Link]
- ✅ Easy Apply: Yes/No
- 👤 Posted by: [Recruiter Name] (if visible)
- **Key Requirements**: [3-4 bullet summary]
```

## Rules

- Always verify the role is performance/paid media focused
- Note if Easy Apply is available (faster application)
- Flag if salary is not listed (common on LinkedIn)
- Identify the hiring manager or recruiter when possible
