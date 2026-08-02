---
name: resume-keyword-extractor
description: >
  Extract and analyze keywords from job descriptions for resume optimization in performance
  marketing, digital marketing, paid media, and related roles. Identifies ATS-critical keywords,
  their frequency, and optimal placement in resumes. Use when the user wants to extract keywords
  from a JD, optimize keyword density in their resume, or understand which terms ATS systems
  prioritize for a specific role.
---

# Resume Keyword Extractor — ATS Optimization

## Workflow

### 1. Extract Keywords from JD

```
## 🔑 Keyword Extraction: [Role] at [Company]

### Priority 1 — Must Appear (3+ times in JD)
| Keyword | Frequency | Best Placement |
|---|---|---|
| performance marketing | 5x | Summary, Title, Skills |
| Google Ads | 4x | Skills, Experience bullets |
| ROAS | 3x | Summary, Experience metrics |

### Priority 2 — Should Appear (2 times in JD)
| Keyword | Frequency | Best Placement |
|---|---|---|
| A/B testing | 2x | Experience bullets |
| budget management | 2x | Experience bullets |

### Priority 3 — Include If Applicable (1 time in JD)
| Keyword | Frequency | Best Placement |
|---|---|---|
| TikTok Ads | 1x | Skills section |
| attribution modeling | 1x | Experience bullets |

### Synonyms & Variants
| JD Term | Acceptable Alternatives |
|---|---|
| ROAS | Return on Ad Spend |
| paid media | paid advertising, paid channels |
| campaign management | campaign execution, campaign operations |

### Skills/Tools Checklist
- [ ] Google Ads
- [ ] Meta Ads Manager
- [ ] Google Analytics / GA4
- [ ] Looker Studio / Data Studio
- [ ] [Other tools from JD]
```

### 2. Keyword Placement Map

Show exactly where each keyword should go:
- **Professional Summary**: Top 3-5 keywords
- **Skills Section**: All tools/platforms
- **Experience Bullets**: Keywords embedded in achievements
- **Job Titles**: If user's past titles can be adjusted to match

### 3. Density Check

After placement, verify:
- Primary keywords appear 2-3 times
- Secondary keywords appear at least once
- No keyword stuffing (reads naturally)
- Both abbreviations and full forms used

## Rules
- Extract EXACT terms from the JD, not synonyms
- Frequency matters — most repeated = highest priority
- Don't stuff keywords unnaturally — readability > density
- Always cross-reference with ATS-checker skill
