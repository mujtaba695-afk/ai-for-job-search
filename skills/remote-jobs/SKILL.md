---
name: remote-jobs
description: >
  Search remote-specific job boards and platforms for performance marketing, digital marketing,
  paid media, PPC, SEM, growth marketing, and related remote roles worldwide. Covers remote-native
  platforms like We Work Remotely, Remotive, FlexJobs, Remote.co, Working Nomads, Himalayas, and
  remote filters on major boards. Use when the user wants to find remote-only marketing jobs,
  work-from-anywhere roles, digital nomad positions, or location-independent marketing work.
---

# Remote Jobs — Performance & Digital Marketing

## Remote-Specific Job Boards

### Tier 1 — Remote-Native Platforms

| Platform | URL | Notes |
|---|---|---|
| **We Work Remotely** | weworkremotely.com | Largest remote-only board |
| **Remotive** | remotive.com | Tech & marketing remote jobs |
| **FlexJobs** | flexjobs.com | Vetted, scam-free (paid) |
| **Remote.co** | remote.co | Curated remote listings |
| **JustRemote** | justremote.org | Clean interface, global |
| **Working Nomads** | workingnomads.com | Digital nomad focused |
| **Himalayas** | himalayas.app | Transparent company profiles |
| **Remote OK** | remoteok.com | Global, aggregator |
| **Authentic Jobs** | authenticjobs.com | Design & marketing |
| **Dynamite Jobs** | dynamitejobs.com | Remote-first companies |

### Tier 2 — Remote Filters on Major Boards

| Platform | Remote Search |
|---|---|
| **LinkedIn** | Filter: Remote → `f_WT=2` |
| **Indeed** | Add "remote" to search or use remote filter |
| **Glassdoor** | Filter by "Remote" in location |
| **Google Jobs** | Add "remote" to query |
| **AngelList/Wellfound** | Filter: "Remote OK" |
| **Otta** | Remote filter (tech-focused) |
| **Wellfound** | Startup remote roles |

### Tier 3 — Niche Remote Marketing

| Platform | Focus |
|---|---|
| **MarketingHire** | Marketing-specific, has remote filter |
| **The Muse** | Company profiles + remote marketing |
| **PowerToFly** | Diversity-focused, remote marketing |
| **Jobspresso** | Remote tech & marketing |
| **Virtual Vocations** | US remote jobs (paid) |
| **Remotely Talents** | European remote companies |

## Search Strategy

### Query Templates
```
site:weworkremotely.com "performance marketing"
site:remotive.com "paid media"
site:remoteok.com "growth marketing"
"remote" "performance marketing" "paid media" jobs
"work from anywhere" "digital marketing" "PPC"
"remote" "Google Ads" OR "Meta Ads" OR "paid social" jobs
```

### Remote Role Types

| Type | Description | Best For |
|---|---|---|
| **Fully Remote** | Work from anywhere, no office | Digital nomads, global talent |
| **Remote (same timezone)** | Remote but must overlap hours | Regional teams |
| **Remote (country-specific)** | Remote within a country | Tax/legal compliance |
| **Hybrid** | Mix of remote and office | Local candidates |

### Timezone Considerations

For "remote but overlap required":
- **US companies**: EST/PST overlap → Americas-friendly
- **UK companies**: GMT overlap → Europe/Africa-friendly
- **Australian companies**: AEST overlap → APAC-friendly
- **Global companies**: "4-hour overlap" → most flexible

## Salary Context — Remote Roles

Remote salaries often follow one of these models:
1. **Location-based pay** — Adjusted to your local cost of living
2. **Company HQ rate** — Paid at company's home market rate
3. **Global flat rate** — Same pay regardless of location (rare but growing)

**For marketing roles, expect:**
- US-based remote: $60K-$180K (varies by seniority)
- Europe-based remote: €40K-€120K
- Global remote (anywhere): $40K-$120K
- Agency/contract remote: $30-$100/hour

## Output Format

```
## 🌍 Remote Jobs: [Role] — Worldwide

### Remote-Native Platforms (X found)

#### 1. [Job Title] — [Company]
- 🌐 [Remote type: Fully / Timezone / Country]
- 💰 [Salary] | 🕐 [Posted]
- ⏰ [Timezone requirement if any]
- 🔗 [Link]
- **Key Requirements**: [summary]

### Major Boards — Remote Filter (X found)
...

### 💡 Notes
- [Timezone considerations]
- [Company remote culture info]
```

## Rules

- Always clarify remote type: fully remote vs. timezone-restricted vs. hybrid
- Note timezone requirements prominently
- Flag if salary is location-adjusted
- Remote-first companies > companies that "allow" remote
- Check company's remote culture (async communication, distributed team tools)
