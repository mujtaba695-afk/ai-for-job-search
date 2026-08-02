---
name: bayt-jobs
description: >
  Search Bayt.com and GulfTalent for performance marketing, digital marketing, paid media, and
  related roles in the Middle East and North Africa (MENA) region. Covers UAE, Saudi Arabia,
  Qatar, Bahrain, Kuwait, Oman, Egypt, Jordan, and other MENA countries. Use when the user wants
  to find marketing jobs in the Middle East/GCC region.
---

# Bayt Jobs — Middle East & MENA Specialist

## Search Strategy

### URL Construction
```
https://www.bayt.com/en/international/{role}-jobs/
https://www.bayt.com/en/uae/{role}-jobs/
https://www.bayt.com/en/saudi-arabia/{role}-jobs/
```

### MENA Market Context

**Major Marketing Hubs:**
- **Dubai, UAE** — Largest market, regional HQs, agencies, e-commerce
- **Abu Dhabi, UAE** — Government, finance, sovereign wealth
- **Riyadh, Saudi Arabia** — Growing fast (Vision 2030), huge budgets
- **Jeddah, Saudi Arabia** — Retail, e-commerce
- **Doha, Qatar** — Government, sports, events
- **Cairo, Egypt** — Agency hub, growing startup scene
- **Amman, Jordan** — Tech startups, regional offices

**Market Specifics:**
- Salary often quoted as monthly (not annual)
- Tax-free in GCC (UAE, Saudi, Qatar, Bahrain, Kuwait, Oman)
- Benefits often include: housing allowance, transportation, annual flights home
- "Package" = base salary + housing + transport + benefits
- Arabic is often preferred but English-only roles exist
- Saudi Vision 2030 driving massive marketing investment

### Salary Benchmarks (Monthly, AED/SAR)
| Role | Junior | Mid | Senior | Manager |
|---|---|---|---|---|
| Performance Marketing | 8-15K | 15-25K | 25-40K | 40-65K |
| Paid Media | 7-12K | 12-22K | 22-35K | 35-55K |
| PPC/SEM | 6-10K | 10-18K | 18-30K | 30-50K |
| Growth Marketing | 10-18K | 18-30K | 30-50K | 50-80K |

*AED (UAE) ≈ SAR (Saudi) ≈ 0.27 USD*

### Search Method
1. Use `mimo_web_search` with `site:bayt.com` for listings
2. Also search GulfTalent: `site:gulftalent.com`
3. Use `web_fetch` for full descriptions

## Output

```
## 💼 Bayt Jobs: [Role] in [Location], MENA

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City, Country] | 💰 [Monthly salary AED/SAR] | 🕐 [Posted]
- 🏢 [Company type: MNC/Local/Government/Agency]
- 🌐 [Arabic required? Bilingual?]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Note if Arabic is required
- Mention if housing/transport allowance is included
- Saudi market is booming — flag opportunities there
- Dubai is competitive but highest volume
