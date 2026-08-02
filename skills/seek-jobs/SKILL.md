---
name: seek-jobs
description: >
  Search Seek.com.au for performance marketing, digital marketing, paid media, and related roles
  in Australia and New Zealand. Optimized for ANZ market including salary in AUD, major cities,
  and regional job market patterns. Use when the user wants to find marketing jobs in Australia
  or New Zealand.
---

# Seek Jobs — Australia & New Zealand Specialist

## Search Strategy

### URL Construction
```
https://www.seek.com.au/{role}-jobs/in-{location}
https://www.seek.com.au/performance-marketing-jobs/in-Sydney
https://www.seek.com.au/paid-media-jobs/in-Melbourne
```

### ANZ Market Context

**Major Marketing Hubs:**
- **Sydney** — Largest market, agencies, tech, finance
- **Melbourne** — Strong creative/agency scene, e-commerce
- **Brisbane** — Growing tech sector
- **Perth** — Mining/resources marketing
- **Auckland, NZ** — Smaller but active market

**Market Specifics:**
- Salary typically quoted as AUD + super (9.5% on top)
- "Package" = base + super + bonus
- Contract roles are very common in marketing (daily rate)
- Working rights/visa status often asked upfront
- Hybrid is the dominant model (2-3 days office)

### Salary Benchmarks (AUD, Annual Package)
| Role | Junior | Mid | Senior | Lead/Manager |
|---|---|---|---|---|
| Performance Marketing | $60-80K | $80-110K | $110-140K | $140-180K |
| Paid Media | $55-75K | $75-100K | $100-130K | $130-170K |
| PPC/SEM | $50-70K | $70-95K | $95-125K | $125-160K |
| Growth Marketing | $70-90K | $90-120K | $120-160K | $160-200K+ |

### Search Method
1. Use `mimo_web_search` with `site:seek.com.au` for listings
2. Use `web_fetch` for full descriptions
3. Note: Seek also powers JobStreet in some regions

## Output

```
## 💼 Seek Jobs: [Role] in [Location], Australia/NZ

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City] | 💰 [Salary range AUD] | 🕐 [Posted]
- 🏢 [Company type] | 📋 [Contract/Permanent]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Always quote salary in AUD (or NZD for NZ roles)
- Note superannuation on top of base salary
- Contract daily rates are common — convert to annual for comparison (daily rate × 220 days)
- Visa/working rights requirements should be flagged
