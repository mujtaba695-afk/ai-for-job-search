---
name: ats-checker
description: >
  Check resumes for ATS (Applicant Tracking System) compatibility and optimization for
  performance marketing, digital marketing, and paid media roles. Analyzes formatting, keyword
  density, section structure, and compatibility with major ATS platforms. Use when the user
  wants to verify their resume will pass ATS screening, check keyword optimization, or fix
  formatting issues that could cause parsing errors.
---

# ATS Checker — Marketing Resume Optimizer

## Checks Performed

### 1. Format Check
```
✅ PASS / ❌ FAIL

| Check | Status | Notes |
|---|---|---|
| Single column layout | ✅ | No multi-column detected |
| Standard fonts | ✅ | Arial, Calibri |
| No tables | ✅ | Clean text layout |
| No graphics/images | ✅ | Text-only |
| Standard headings | ✅ | "Work Experience", "Education" |
| No headers/footers | ❌ | Header contains contact info — move to body |
| File format | ✅ | .docx (ATS-friendly) |
| Section order | ✅ | Summary → Experience → Skills → Education |
```

### 2. Keyword Analysis
```
Target JD Keywords: [extracted from job description]

| Keyword | Found in Resume? | Location | Frequency |
|---|---|---|---|
| performance marketing | ✅ | Summary, Exp | 3x |
| ROAS optimization | ✅ | Experience | 1x |
| Google Ads | ✅ | Skills, Exp | 4x |
| Meta Ads | ⚠️ | Skills only | 1x |
| TikTok Ads | ❌ | Not found | 0x |
| A/B testing | ✅ | Experience | 2x |
| programmatic | ❌ | Not found | 0x |

Keyword Match Score: 70%
Missing: [list of missing keywords]
```

### 3. Content Quality
```
| Check | Status | Notes |
|---|---|---|
| Quantified achievements | ⚠️ | 3/5 roles have metrics |
| Action verbs | ✅ | Strong verb usage |
| Consistency | ✅ | Dates, formatting consistent |
| Length | ✅ | 2 pages |
| Summary present | ✅ | Keyword-rich |
| Skills section | ⚠️ | Missing some target tools |
```

### 4. ATS-Specific Compatibility

Test against major ATS parsers:
- **Greenhouse**: ✅ Should parse well
- **Lever**: ✅ Compatible
- **Workday**: ⚠️ May miss skills in non-standard format
- **Taleo**: ✅ Simple format works

## Output

```
## 📋 ATS Resume Check Report

### Overall Score: [X/100]

### Strengths
- [What's working well]

### Issues to Fix
1. 🔴 [Critical issue]
2. 🟡 [Important issue]
3. 🟢 [Nice to fix]

### Action Items
1. [Specific fix with instructions]
2. [Specific fix with instructions]
3. [Specific fix with instructions]
```

## Rules

- Always test against a specific JD when available
- Provide specific fix instructions, not just "improve keywords"
- Prioritize fixes by impact on ATS parsing
- Note that some modern ATS (Greenhouse, Lever) handle PDFs well, but .docx is safest
