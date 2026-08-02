---
name: naukri-jobs
description: >
  Search Naukri.com and Foundit (Monster India) for performance marketing, digital marketing,
  paid media, PPC, SEM, and related roles in India. Optimized for the Indian job market including
  salary benchmarks in INR, major cities (Bangalore, Mumbai, Delhi NCR, Hyderabad, Chennai, Pune),
  and Indian company hiring patterns. Use when the user wants to find marketing jobs in India.
---

# Naukri Jobs — India Market Specialist

## Search Strategy

### URL Construction (Naukri)
```
https://www.naukri.com/{role}-jobs-in-{city}
https://www.naukri.com/performance-marketing-jobs-in-bangalore
https://www.naukri.com/paid-media-jobs-in-mumbai
```

### Indian Job Market Context

**Major Marketing Hubs:**
- **Bangalore** — Tech companies, startups, highest volume
- **Mumbai** — Agencies, media, e-commerce, BFSI
- **Delhi NCR (Gurgaon/Noida)** — E-commerce, startups, agencies
- **Hyderabad** — Growing tech hub, Amazon, Google offices
- **Chennai** — SaaS companies
- **Pune** — IT services, mid-size companies

**Indian Market Specifics:**
- Notice period matters (30-90 days common)
- CTC (Cost to Company) = total comp including benefits
- Take-home ≠ CTC (typically 65-75% of CTC)
- Agency experience is highly valued for in-house roles
- Common platforms: Google Ads, Meta, YouTube, WhatsApp marketing

### Salary Benchmarks (INR, Annual)
| Role | Junior | Mid | Senior | Lead/Manager |
|---|---|---|---|---|
| Performance Marketing | 3-6L | 6-12L | 12-20L | 20-40L |
| Paid Media | 2.5-5L | 5-10L | 10-18L | 18-35L |
| PPC/SEM | 2-4L | 4-8L | 8-15L | 15-30L |
| Growth Marketing | 4-7L | 7-15L | 15-25L | 25-50L |

*L = Lakhs (1L = ₹1,00,000)*

### Search Method
1. Use `mimo_web_search` with `site:naukri.com` for listings
2. Use `web_fetch` for full job descriptions
3. Also search Foundit (formerly Monster India)

## Output

```
## 💼 Naukri Jobs: [Role] in [Location], India

### Results (X found)

#### 1. [Job Title] — [Company]
- 📍 [City] | 💰 [CTC range] | 🕐 [Posted]
- 🏢 [Company type: Startup/MNC/Agency/Enterprise]
- ⏰ Notice period: [if mentioned]
- 🔗 [Link]
- **Key Requirements**: [summary]
```

## Rules

- Always show CTC, not take-home
- Note notice period requirements
- Indian market values certifications highly — highlight if JD mentions them
- Remote roles are increasingly common in India — filter for this
