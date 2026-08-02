---
name: google-jobs
description: >
  Search Google Jobs aggregator for performance marketing, digital marketing, paid media, and
  related roles. Leverages Google's job aggregation from multiple sources including company career
  pages, job boards, and staffing agencies. Use when the user wants a broad search across all
  sources, wants to find jobs on company career pages directly, or needs the widest possible
  coverage of available roles.
---

# Google Jobs — Performance & Digital Marketing Specialist

## Search Strategy

Google Jobs aggregates from hundreds of sources. Use `mimo_web_search` with targeted queries.

### Query Templates
```
Core:
- "{role} jobs in {location}"
- "{role} remote jobs"
- "{role} jobs near me"

With filters:
- "{role} jobs {location} site:jobs.lever.co OR site:boards.greenhouse.io"
- "{role} jobs {location} $salary"
- "{role} jobs {location} {company}"

Career pages:
- "site:careers.{company}.com {role}"
- "site:{company}.com/careers {role}"
```

### Source Discovery
Google Jobs pulls from:
- Company career pages (Lever, Greenhouse, Workday, iCIMS)
- Job boards (LinkedIn, Indeed, Glassdoor)
- Staffing agencies
- Niche job boards
- Government job banks

Use this to find roles **not posted on major boards**.

### Advanced Searches
```
# Find roles on ATS platforms directly
"site:boards.greenhouse.io performance marketing"
"site:jobs.lever.co paid media"
"site:apply.workable.com growth marketing"

# Find company career pages
"site:careers.*.com performance marketing"
```

## Output

```
## 💼 Google Jobs: [Role] in [Location]

### Aggregated Results (X found)

#### Sources Breakdown
- LinkedIn: X jobs
- Indeed: X jobs
- Company career pages: X jobs
- Other boards: X jobs

### Top Results

#### 1. [Job Title] — [Company]
- 📍 [Location] | 💰 [Salary] | 🕐 [Posted]
- 📌 Source: [LinkedIn / Company site / etc.]
- 🔗 [Direct link]
- **Key Requirements**: [summary]
```

## Rules

- Google Jobs has the widest coverage — use as primary discovery tool
- Always check the source URL — some redirect to expired listings
- Cross-reference with other board-specific skills to avoid duplicates
- Career page listings often have less competition than LinkedIn/Indeed
