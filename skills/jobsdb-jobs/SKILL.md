---
name: jobsdb-jobs
description: >
  Search JobsDB, JobStreet, and regional job boards for performance marketing, digital marketing,
  paid media, and related roles in Southeast Asia (Singapore, Hong Kong, Thailand, Malaysia,
  Indonesia, Philippines, Vietnam). Use when the user wants to find marketing jobs in APAC
  outside of Australia, India, China, or Japan.
---

# JobsDB — Southeast Asia & APAC Specialist

## Search Strategy

### Platform URLs
- **JobsDB**: `https://www.jobsdb.com/{country}/jobs?keywords={role}`
- **JobStreet**: `https://www.jobstreet.com/{country}/{role}-jobs`
- **NodeFlair**: `https://www.nodeflair.com/` (Singapore, tech-focused)
- **Glints**: `https://glints.com/` (Southeast Asia startups)

### APAC Market Context

**Major Marketing Hubs:**
- **Singapore** — Regional HQs, highest salaries, English-speaking
- **Hong Kong** — Finance, agencies, international companies
- **Bangkok, Thailand** — Growing digital market, local + MNC
- **Kuala Lumpur, Malaysia** — Shared services, agencies
- **Jakarta, Indonesia** — Largest SEA market by population
- **Manila, Philippines** — BPO/shared services, growing digital
- **Ho Chi Minh, Vietnam** — Fast-growing, startup scene

**Market Specifics:**
- Singapore salary is benchmark for region
- EP (Employment Pass) required for foreigners in Singapore
- Regional roles often based in Singapore or Hong Kong
- Local platforms important: Shopee Ads, Lazada Ads, LINE Ads (Thailand), KakaoTalk (Korea)
- English is business language in Singapore, HK, Philippines

### Salary Benchmarks (Monthly, Local Currency)
**Singapore (SGD):**
| Role | Junior | Mid | Senior | Manager |
|---|---|---|---|---|
| Performance Marketing | 3.5-5K | 5-8K | 8-12K | 12-18K |
| Paid Media | 3-4.5K | 4.5-7K | 7-10K | 10-15K |
| Growth Marketing | 4-6K | 6-9K | 9-14K | 14-20K |

**Hong Kong (HKD):**
| Role | Junior | Mid | Senior | Manager |
|---|---|---|---|---|
| Performance Marketing | 18-25K | 25-40K | 40-60K | 60-90K |
| Paid Media | 15-22K | 22-35K | 35-50K | 50-75K |

### Search Method
1. Use `mimo_web_search` with `site:jobsdb.com` for listings
2. Also search `site:jobstreet.com`
3. Use `web_fetch` for full descriptions

## Output

```
## 💼 APAC Jobs: [Role] in [Location]

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City] | 💰 [Monthly salary] | 🕐 [Posted]
- 🏢 [Company type: MNC/Local/Startup/Agency]
- 🌐 [Language requirements]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Always quote salary in local currency, monthly
- Note visa/EP requirements for Singapore
- Regional roles (APAC-wide) are usually based in Singapore or HK
- Highlight English-friendly roles for non-local speakers
