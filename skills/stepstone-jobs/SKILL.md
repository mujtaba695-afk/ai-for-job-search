---
name: stepstone-jobs
description: >
  Search StepStone, Xing Jobs, and other European job boards for performance marketing, digital
  marketing, paid media, and related roles in Germany, Austria, Switzerland (DACH), and broader
  Europe. Use when the user wants to find marketing jobs in Europe, particularly DACH region,
  or needs European market salary and hiring context.
---

# StepStone & European Jobs — Specialist

## Search Strategy

### Platform URLs
- **StepStone DE**: `https://www.stepstone.de/jobs/{role}/in-{location}`
- **Xing Jobs**: `https://www.xing.com/jobs`
- **Indeed DE**: `https://de.indeed.com/jobs?q={role}&l={location}`
- **EuroJobs**: `https://www.eurojobs.com/`
- **Welcome to the Jungle**: `https://www.welcometothejungle.com/` (France, EU)
- **Arbeitnow**: `https://www.arbeitnow.com/` (Germany, English-friendly)

### European Market Context

**Major Marketing Hubs:**
- **Berlin** — Startups, tech, English-friendly
- **London** — Largest market, agencies, finance (post-Brexit: visa required)
- **Amsterdam** — Tech companies, English-friendly
- **Paris** — Luxury, fashion, tech (Welcome to the Jungle)
- **Munich** — Enterprise tech (SAP, Siemens), agencies
- **Barcelona** — Agencies, startups, lower cost
- **Dublin** — EU HQs of US tech companies (Google, Meta, LinkedIn)
- **Stockholm/Copenhagen** — Tech startups, high salaries

**Market Specifics:**
- Germany: Arbeitszeugnis (work certificate) is standard
- Notice periods: 1-3 months common in Europe
- Salary usually quoted gross (Brutto) annually
- English-only roles exist in Berlin, Amsterdam, Dublin, London
- EU work permit requirements vary by country
- Xing is the German LinkedIn (important for DACH market)

### Salary Benchmarks (EUR, Annual Gross)
| Role | Junior | Mid | Senior | Manager |
|---|---|---|---|---|
| Performance Marketing | €35-50K | €50-70K | €70-90K | €90-120K |
| Paid Media | €30-45K | €45-65K | €65-85K | €85-110K |
| PPC/SEM | €30-42K | €42-60K | €60-80K | €80-105K |
| Growth Marketing | €40-55K | €55-80K | €80-110K | €110-140K |

*London (GBP): typically 10-20% higher than EUR equivalents*

### Search Method
1. Use `mimo_web_search` with `site:stepstone.de` or `site:xing.com`
2. For English roles: add "English" to search
3. Use `web_fetch` for full descriptions

## Output

```
## 💼 European Jobs: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City, Country] | 💰 [Annual gross EUR/GBP] | 🕐 [Posted]
- 🌐 [Language: English/German/mixed]
- 📋 [Permanent/Contract]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Note language requirements (German is often required in DACH)
- Flag visa/work permit requirements
- London is post-Brexit — separate from EU job market
- English-friendly cities: Berlin, Amsterdam, Dublin, Barcelona
