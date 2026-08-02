---
name: resume-tailor
description: >
  Tailor resumes to match job descriptions with near-100% alignment. Reads a job description
  (from URL, pasted text, or file) and rewrites/restructures a resume to perfectly match the
  requirements, keywords, and language of the target role.
  Use when the user wants to: tailor a resume for a specific job posting, optimize a resume for ATS
  (Applicant Tracking Systems), rewrite experience to match a JD, generate a targeted cover letter,
  or analyze how well a resume matches a job description. Specialized for performance marketing,
  digital marketing, paid media, PPC, SEM, and related marketing roles.
---

# Resume Tailor — Performance & Digital Marketing

## Workflow

### 1. Collect Inputs

Need two things:
1. **Job Description** — from URL (fetch with `web_fetch`), pasted text, or file
2. **Current Resume** — from file, pasted text, or user provides details verbally

If resume is not provided, ask user to share it or describe their experience.

### 2. Analyze the Job Description

Extract and categorize:

```
MUST-HAVE SKILLS:
- [List every required skill/technology/tool]

NICE-TO-HAVE SKILLS:
- [List preferred qualifications]

KEY RESPONSIBILITIES:
- [Core duties of the role]

TOOLS & PLATFORMS:
- [Specific ad platforms, analytics tools, software]

SOFT SKILLS:
- [Leadership, communication, etc.]

KEYWORD FREQUENCY:
- [Most repeated terms — these are ATS priorities]

COMPANY CONTEXT:
- [Industry, size, stage, culture signals]
```

### 3. Gap Analysis

Compare resume vs. JD:

```
✅ MATCH — Skills/experience that align directly
⚠️ PARTIAL — Related experience that can be reframed
❌ GAP — Missing skills/experience (flag to user)
🔄 WEAK MATCH — Mentioned but not prominent enough
```

### 4. Rewrite the Resume

#### Structure (for marketing roles)

```
[NAME]
[Contact: Email | Phone | LinkedIn | Portfolio if applicable]

PROFESSIONAL SUMMARY (3-4 lines)
- Mirror the JD's language for the role title and key skills
- Include top 3-5 must-have keywords naturally
- Quantify impact (revenue managed, ROAS achieved, budget scale)

CORE COMPETENCIES / SKILLS (keyword-rich grid)
- Match exact terminology from the JD
- Group by: Platforms, Analytics, Strategy, Leadership
- Include certifications (Google Ads, Meta Blueprint, etc.)

PROFESSIONAL EXPERIENCE (reverse chronological)
For each role:
  [Title] | [Company] | [Dates]
  - Bullet 1: Action verb + what you did + result (quantified)
  - Mirror JD keywords in bullet points
  - Emphasize responsibilities that match the target role
  - Use STAR format: Situation → Task → Action → Result
  - Scale numbers: budgets, ROAS, CPA, team size, channels managed

EDUCATION
- Degree, institution, year

CERTIFICATIONS & TRAINING
- Google Ads, Meta Blueprint, TikTok Ads, GA4, etc.

TOOLS & PLATFORMS
- List every tool mentioned in the JD that you know
```

#### Rewriting Rules

1. **Keyword Injection**: Every must-have keyword from the JD must appear in the resume at least once
2. **Mirror Language**: If JD says "ROAS optimization," don't write "ad efficiency" — use their exact words
3. **Quantify Everything**: Add numbers, percentages, dollar amounts, timeframes
4. **Reframe Experience**: Shift emphasis to match the target role (e.g., if JD emphasizes TikTok Ads but resume is Meta-heavy, rebalance)
5. **ATS Optimization**: No tables, no graphics, no fancy formatting — clean text with standard headings
6. **Summary First**: Professional summary must read like the JD's "ideal candidate" paragraph
7. **Skills Grid**: Exact-match the tools/platforms section to what the JD lists
8. **Action Verbs**: Match the JD's tone — if it says "own," "drive," "scale," use those verbs

### 5. Generate Match Report

```
## 📊 Resume-JD Match Report

**Target Role**: [Title] at [Company]

### Match Score: XX%

| Category | Match | Notes |
|---|---|---|
| Core Skills | ✅ 95% | All major platforms covered |
| Experience Level | ✅ 100% | 7+ years matches 5+ requirement |
| Tools/Platforms | ⚠️ 80% | Missing TikTok Ads experience |
| Education | ✅ 100% | Degree matches |
| Certifications | ⚠️ 70% | Add GA4 certification |

### Changes Made
1. ✅ Reframed Facebook Ads experience as "Meta Ads" to match JD terminology
2. ✅ Added ROAS metrics from campaign data
3. ✅ Restructured summary to mirror JD's "growth marketing" framing
4. ⚠️ Flagged: No TikTok Ads experience — consider adding or addressing in cover letter

### Keywords Added
[performance marketing, ROAS optimization, paid social, Google Ads, Meta Ads, campaign management, budget allocation, A/B testing, attribution modeling]
```

### 6. Output

Save tailored resume as a clean markdown file (can be converted to PDF/DOCX later).
Optionally generate a cover letter that addresses gaps and reinforces strengths.

## Important Rules

- **Never fabricate experience** — reframe and emphasize, but don't invent skills the user doesn't have
- **Flag gaps honestly** — tell the user what's missing so they can decide how to handle it
- **Preserve truth** — all claims must be things the user actually did (just better worded)
- **ATS-first** — optimize for machine parsing, not visual beauty
- **One resume per JD** — each job gets a uniquely tailored version

## Cover Letter (Optional)

When requested, generate a cover letter that:
1. Opens with the exact role title and company name
2. Mirrors the JD's top 3 requirements with matching experience
3. Addresses any gaps proactively (e.g., "While my direct TikTok experience is developing, my proven track record in Meta Ads scaling translates directly...")
4. Closes with enthusiasm specific to the company/role
5. Keeps it under 400 words
