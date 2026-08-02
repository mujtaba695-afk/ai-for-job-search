---
name: salary-negotiator
description: >
  Research salary ranges and provide negotiation strategies for performance marketing, digital
  marketing, paid media, and related roles. Uses market data, benchmarks, and proven negotiation
  tactics. Use when the user wants to know market rate for a role, prepare for salary negotiation,
  evaluate a job offer, or understand compensation structures (base, bonus, equity) in marketing.
---

# Salary Negotiator — Performance & Digital Marketing

## Workflow

### 1. Research Market Rate

Search for salary data using `mimo_web_search`:
- Glassdoor salary ranges for the role/title
- Levels.fyi (for tech companies)
- Payscale, Salary.com, LinkedIn Salary
- Robert Half, Hays, Michael Page salary guides (marketing-specific)
- Regional salary surveys

Variables that affect compensation:
- Location (city/country)
- Company size and stage (startup vs. enterprise)
- Industry (tech, e-commerce, agency, etc.)
- Remote vs. onsite
- Years of experience
- Platform specialization (Google Ads specialists often earn more than generalists)

### 2. Compensation Breakdown

Help user understand total comp:

```
BASE SALARY
- Fixed annual amount
- Varies by location and seniority

BONUS
- Performance bonus (typically 10-20% of base)
- Company performance bonus
- Sign-on bonus (one-time)

EQUITY
- RSUs (Restricted Stock Units) — vesting schedule
- Stock options — strike price, FMV
- ESPP (Employee Stock Purchase Plan)

BENEFITS
- Health insurance value
- 401(k) match
- Learning budget
- Remote work stipend
- PTO policy
```

### 3. Offer Evaluation

When user receives an offer, calculate:
- **Total Year 1 comp** = base + sign-on + first-year equity vest
- **Annualized comp** = base + annual bonus + annual equity vest
- **Benefits value** = insurance + 401k match + perks monetary value
- **Compare to market** = percentile ranking (25th, 50th, 75th, 90th)

### 4. Negotiation Strategy

#### Before Negotiating
- Research exact market range for this role, location, company
- Identify your leverage (competing offers, unique skills, urgency)
- Determine your walk-away number

#### Negotiation Scripts

**Counter-offer email template:**
```
Thank you for the offer. I'm excited about [Company] and the [Role].
Based on my research and the value I'd bring — [specific qualifications] —
I'd like to discuss the base salary. The market range for this role in
[location] is [range]. Given my [specific experience], I believe a base of
[$X] would better reflect the value I'll deliver.
```

**If they say "this is our best offer":**
- Ask about sign-on bonus, equity refresh, earlier review cycle, title upgrade
- Negotiate non-salary items: remote days, learning budget, PTO

#### What to Negotiate (in order of flexibility)
1. Sign-on bonus (often easiest to increase)
2. Base salary
3. Equity
4. Start date (later = more vesting if close to vest date)
5. Title (affects future earning)
6. PTO / remote days
7. Learning/conference budget

### 5. Output

Provide a structured negotiation plan with:
- Market rate research (data-backed)
- Recommended ask amount
- Counter-offer scripts
- Backup positions if they push back

## Rules

- **Always use data** — never guess at numbers
- **Be location-specific** — London ≠ Manchester, NYC ≠ Austin
- **Consider total comp** — a lower base with great equity might be better
- **Don't negotiate against yourself** — make them go first when possible
- **Be positive** — negotiation is collaboration, not confrontation
