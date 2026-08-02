---
name: salary-research
description: >
  Conduct real-time salary research for performance marketing, digital marketing, paid media,
  and related roles across global markets. Searches multiple salary databases, compares regions,
  and provides data-backed salary ranges. Use when the user wants to know market rate for a
  role, compare salaries across locations, prepare for salary discussions, or validate an
  offer against market data.
---

# Salary Research — Performance Marketing

## Research Workflow

### 1. Search Multiple Sources

Use `mimo_web_search` for each:
```
"{role} salary {location} site:glassdoor.com"
"{role} salary {location} site:levels.fyi"
"{role} salary {location} site:payScale.com"
"{role} salary {location} site:salary.com"
"{role} salary {location} site:linkedin.com/salary"
"digital marketing salary guide {year} {country}"
"performance marketing salary survey {year}"
```

### 2. Cross-Reference Data

Compare at least 3 sources. Average them with weights:
- Glassdoor (largest sample): 40%
- Levels.fyi (tech companies): 25%
- LinkedIn Salary: 20%
- Other sources: 15%

### 3. Output

```
## 💰 Salary Research: [Role] in [Location]

### Market Rate Summary
| Percentile | Annual Salary |
|---|---|
| 25th (Junior/Entry) | $X |
| 50th (Mid-level) | $Y |
| 75th (Senior) | $Z |
| 90th (Top/Lead) | $W |

### Sources Consulted
| Source | Range | Sample Size |
|---|---|---|
| Glassdoor | $X - $Y | N responses |
| Levels.fyi | $X - $Y | N data points |
| LinkedIn | $X - $Y | N profiles |

### Factors That Affect Pay
- **Company type**: Startup (+10-20% equity) vs. Enterprise (higher base)
- **Industry**: Tech/Finance > Agency > Retail
- **Remote**: May be location-adjusted (-10-20% for global remote)
- **Specialization**: Programmatic > Paid Social > PPC (typically)
- **Budget scale**: Managing $1M+/mo commands premium

### Regional Comparison
| Location | Range | vs. [Base Location] |
|---|---|---|
| New York | $X - $Y | Baseline |
| London | $X - $Y | -15% |
| Singapore | $X - $Y | -10% |
| Dubai | $X - $Y | -20% (but tax-free) |
| Remote (US) | $X - $Y | -5 to -15% |
```

## Rules
- Always search live data (salary data changes yearly)
- Note the year of data — don't use 2022 data in 2025
- Account for total comp, not just base
- Different currencies require conversion AND purchasing power comparison
- Flag when sample size is too small to be reliable
