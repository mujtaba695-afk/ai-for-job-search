---
name: glassdoor-jobs
description: >
  Search Glassdoor for performance marketing, digital marketing, paid media, and related roles
  with integrated salary data, company reviews, and interview insights. Use when the user wants
  to find jobs with salary transparency, research company culture before applying, or access
  interview questions reported by other candidates.
---

# Glassdoor Jobs — Performance & Digital Marketing Specialist

## Search Strategy

### URL Construction
```
https://www.glassdoor.com/Job/jobs.htm?sc.keyword={keywords}&locT=C&locId={city_id}&jobType={type}&fromAge={days}
```

### Search Method
1. Use `mimo_web_search` with `site:glassdoor.com` for job discovery
2. Use `web_fetch` for individual listings (may require navigation past login walls)
3. Supplement with `mimo_web_search` for salary and review data

### Glassdoor-Specific Value
- **Salary ranges** — often more accurate than Indeed estimates
- **Company reviews** — detailed pros/cons from employees
- **Interview reviews** — reported questions, difficulty, process length
- **Benefits reviews** — detailed compensation package info

## Research Workflow (for each interesting role)

1. **Job listing** — extract requirements, responsibilities, salary
2. **Company reviews** — read recent reviews, focus on marketing department
3. **Salary data** — compare listed salary to Glassdoor range
4. **Interview intel** — check for reported interview questions and process

## Output

```
## 💼 Glassdoor Jobs: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [Location] | 💰 [Salary range] | 🕐 [Posted]
- ⭐ Overall: [X/5] | 📈 Recommend to friend: [X%]
- 🔗 [Link]

**Company Snapshot:**
- Pros (from reviews): [2-3 top pros]
- Cons (from reviews): [2-3 top cons]
- Interview process: [X rounds, Y weeks avg]
- Common questions: [if available]
```

## Rules

- Glassdoor salary data is self-reported — note sample size
- Focus on recent reviews (last 12 months)
- Filter reviews by department (Marketing) when possible
- Interview intel is gold for prep — always surface it
