---
name: job-posting-analyzer
description: >
  Deep-analyze job postings for performance marketing, digital marketing, paid media, and related
  roles. Decodes hidden requirements, identifies red flags, estimates real job scope, and predicts
  interview focus areas. Use when the user wants to understand what a job REALLY requires beyond
  the posted description, detect if a role is genuinely performance-focused or just relabeled,
  or get a strategic breakdown before applying.
---

# Job Posting Analyzer — Decode the JD

## Workflow

### 1. Input
Job posting URL or pasted text.

### 2. Deep Analysis

```
## 🔍 Job Posting Analysis: [Role] at [Company]

### Surface vs. Reality

| What They Say | What They Mean |
|---|---|
| "Wear many hats" | Understaffed, you'll do everything |
| "Fast-paced environment" | High pressure, long hours |
| "Self-starter" | No onboarding or training |
| "Own the channel" | You ARE the team |
| "Data-driven" | They want someone who can prove ROI |
| "Scale our growth" | Current results are underwhelming |
| "Join a growing team" | Team is tiny or newly created |

### Role Classification
- **Type**: [Specialist / Manager / Generalist / Hybrid]
- **Real Focus**: [60% execution, 40% strategy / vice versa]
- **Team Size**: [Solo / Small (2-5) / Medium (5-15) / Large (15+)]
- **Budget Scale**: [Startup ($1-10K/mo) / Mid ($10-100K/mo) / Enterprise ($100K+/mo)]
- **Growth Stage**: [Building from scratch / Optimizing existing / Scaling]

### Red Flags 🚩
- [List any concerning signals]
- Vague metrics ("improve performance")
- No budget mentioned
- "Marketing manager" but 90% non-paid tasks
- Agency listed as client-side role
- Unrealistic expectations (e.g., "10x ROAS in 30 days")

### Green Flags ✅
- [List positive signals]
- Specific platforms mentioned
- Budget range disclosed
- Clear reporting structure
- Defined success metrics
- Growth path mentioned

### Interview Prediction
Based on the JD, expect questions about:
1. [Topic 1 — based on emphasis in JD]
2. [Topic 2]
3. [Topic 3]

### Application Priority: [High / Medium / Low]
**Reason**: [Why this role is or isn't worth pursuing]
```

### 3. Red Flag Dictionary (Marketing-Specific)

| Red Flag | Translation |
|---|---|
| "Manage all digital marketing" | You'll be a one-person department |
| "Startup environment" | No processes, chaos, maybe no budget |
| "Competitive salary" (no number listed) | Below market rate |
| "Must have agency experience" | We want someone used to being overworked |
| "Immediate start" | Previous person quit or was fired |
| "Reports to CEO" | No marketing leadership, you're on your own |
| "Unlimited PTO" | Nobody takes vacation here |
| "Rockstar/ninja/guru" | Unprofessional, likely poor culture |
| "10+ channels" | Jack of all trades, master of none |

## Rules
- Be brutally honest — the user needs to know what they're walking into
- Distinguish between legitimate concerns and minor issues
- Always fetch the full JD with `web_fetch` for thorough analysis
- Flag if the role seems relabeled (e.g., "Growth Marketing" but it's really content marketing)
