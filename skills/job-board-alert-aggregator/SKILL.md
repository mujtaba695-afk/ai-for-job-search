---
name: job-board-alert-aggregator
description: >
  Aggregate and deduplicate job listings from multiple job board alerts and searches for
  performance marketing, digital marketing, paid media, and related roles. Combines results
  from LinkedIn, Indeed, Glassdoor, remote boards, and regional platforms into a single
  deduplicated feed. Use when the user receives alerts from multiple platforms and wants
  a single consolidated view, needs to avoid applying to the same job twice, or wants
  to prioritize the best opportunities across all sources.
---

# Job Board Alert Aggregator

## Workflow

### 1. Collect Alerts

Gather listings from all sources:
- LinkedIn job alerts
- Indeed email alerts
- Glassdoor alerts
- Google Jobs notifications
- Remote board alerts (We Work Remotely, Remotive, etc.)
- Regional board alerts
- Company career page alerts

### 2. Deduplicate

Same job posted on multiple platforms = 1 listing. Match by:
- Company name + Role title (fuzzy match)
- Company name + Location
- Job description similarity

### 3. Prioritize

Score each listing:
```
| Factor | Weight | Score (1-10) |
|---|---|---|
| Role match (to user's target) | 30% | ? |
| Company attractiveness | 20% | ? |
| Salary (if listed) | 15% | ? |
| Recency (newer = higher) | 15% | ? |
| Remote flexibility | 10% | ? |
| Application ease (Easy Apply?) | 10% | ? |
```

### 4. Output

```
## 📋 Aggregated Job Feed — Week of [Date]

### New Listings (X unique, Y total across boards)

| # | Role | Company | Location | Salary | Source | Priority |
|---|---|---|---|---|---|---|
| 1 | Senior Paid Media Mgr | Spotify | Remote | $120-150K | LinkedIn, Indeed | ⭐⭐⭐⭐⭐ |
| 2 | Performance Marketing Lead | Shopify | Toronto | $130-160K | LinkedIn, Glassdoor | ⭐⭐⭐⭐ |
| 3 | PPC Specialist | Startup X | London | £50-65K | Indeed | ⭐⭐⭐ |

### Duplicates Removed: [X] listings appeared on multiple boards

### Quick Actions
- Apply to #1 (Easy Apply available)
- Research #3 (startup, check funding)
- Skip #4 (agency role, not what you want)
```

## Rules
- Deduplicate aggressively — same job on 3 boards = 1 entry
- Prioritize based on user's stated preferences
- Flag "Easy Apply" roles (faster to apply)
- Note when salary is missing (common on LinkedIn)
- Group by company if multiple roles at same company
