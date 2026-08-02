---
name: company-researcher
description: >
  Research companies for job applications in performance marketing, digital marketing, and paid
  media. Provides deep insights into company culture, marketing maturity, tech stack, recent
  campaigns, growth trajectory, and interview process. Use when the user is preparing for an
  interview, evaluating a company before applying, comparing offers, or needs talking points
  for a networking conversation.
---

# Company Researcher — Marketing Focus

## Research Framework

### 1. Company Basics
- Industry, size, funding stage, revenue (if public)
- Headquarters, offices, remote policy
- Leadership team (especially CMO/VP Marketing)
- Glassdoor rating and reviews summary

### 2. Marketing Maturity Assessment
- Current ad presence (search Google, Meta Ad Library, TikTok Ad Library)
- Content marketing quality (blog, social, email)
- Tech stack (BuiltWith, Wappalyzer — what tools do they use?)
- Marketing team size (LinkedIn headcount in marketing)
- Agency vs. in-house

### 3. Recent Activity
- Recent campaigns or product launches
- Funding rounds or acquisitions
- News and press mentions
- Social media activity and engagement

### 4. Interview Intelligence (if available)
- Glassdoor interview reviews
- Common interview questions reported
- Interview process length and stages
- Salary data from reviews

### 5. Competitive Landscape
- Key competitors
- How they differentiate
- Market position

## Research Sources

- **Company website** (About, Careers, Blog, Press)
- **LinkedIn** (employees, recent posts, job listings)
- **Glassdoor** (reviews, salaries, interviews)
- **Meta Ad Library** (active ads: facebook.com/ads/library)
- **TikTok Ad Library** (ads.tiktok.com)
- **Google Ads Transparency** (adstransparency.google.com)
- **BuiltWith** (tech stack)
- **Crunchbase** (funding, acquisitions)
- **SimilarWeb** (traffic, channels)
- **G2/Trustpilot** (product reviews)

## Output Format

```
## 🏢 [Company Name] — Research Brief

### Overview
[2-3 sentence summary]

### Marketing Maturity: [High/Medium/Low]
- Active on: [platforms]
- Ad spend estimate: [if available]
- Marketing team: [X people]
- Tech stack: [tools]

### Recent Campaigns
- [Campaign 1 — channel, what they did]
- [Campaign 2 — channel, what they did]

### Interview Prep
- Process: [X rounds, Y weeks avg]
- Common questions: [from Glassdoor]
- Salary range: [from data]

### Talking Points
- [Insight 1 to mention in interview]
- [Insight 2 about their marketing approach]
- [Question to ask them]

### Red Flags / Green Flags
- 🟢 [Positive signal]
- 🔴 [Concern]
```

## Rules

- Always use live data (web_fetch, mimo_web_search) — don't rely on stale knowledge
- Focus on marketing-relevant insights (not generic company info)
- Provide actionable talking points for interviews
- Flag potential red flags honestly
