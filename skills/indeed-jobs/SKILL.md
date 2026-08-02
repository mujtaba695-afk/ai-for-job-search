---
name: indeed-jobs
description: >
  Search Indeed specifically for performance marketing, digital marketing, paid media, PPC, SEM,
  and related roles. Optimized for Indeed's search filters, salary insights, and company reviews.
  Use when the user wants to search Indeed for marketing jobs, compare Indeed salary data, or
  find roles not posted on LinkedIn.
---

# Indeed Jobs — Performance & Digital Marketing Specialist

## Search Strategy

### URL Construction
```
https://www.indeed.com/jobs?q={keywords}&l={location}&fromage={days}&salary={salary}&jt={job_type}
```

Parameters:
- `fromage`: 1, 3, 7, 14 (days posted)
- `jt`: fulltime, parttime, contract, internship
- `salary`: e.g., 60000, 80000
- `remotejob`: 032b3046-06a3-4876-8dfd-474eb5e7ed11 (remote only)

### Keyword Strategy
Indeed matches broadly, so be specific:
```
- "performance marketing manager" (exact match with quotes)
- "paid media specialist"
- "PPC manager Google Ads"
- "SEM specialist"
- "paid social media manager"
- "growth marketing manager"
- "programmatic media buyer"
```

### Search Method
1. Use `web_fetch` on Indeed URL to get listing results
2. Use `mimo_web_search` with `site:indeed.com` for broader discovery
3. For full descriptions, `web_fetch` individual job pages

### Indeed-Specific Features
- **Salary estimates** — Indeed provides estimated salaries for many roles
- **Company reviews** — Indeed has employee reviews (like Glassdoor)
- **Indeed Assessments** — note if skill assessments are required
- **Apply directly** — some jobs allow Indeed-native applications

## Output

```
## 💼 Indeed Jobs: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [Location] | 💰 [Salary (Indeed estimate)] | 🕐 [Posted]
- ⭐ Company rating: [X/5] ([Y] reviews)
- 🔗 [Link]
- 📝 Apply: Indeed / Company site
- **Key Requirements**: [summary]
```

## Rules

- Leverage Indeed's salary estimates as baseline data
- Note company review scores (below 3.5 is a flag)
- Indeed often has roles not posted on LinkedIn — highlight these
- Filter by posted date to avoid stale listings
