---
name: resume-parser
description: >
  Parse, analyze, and structure resumes/CVs for performance marketing, digital marketing, and
  paid media professionals. Extracts skills, experience, metrics, and qualifications into a
  structured format. Use when the user shares a resume (PDF, DOCX, image, or text), wants to
  extract their experience into a structured profile, needs to verify resume data, or wants
  to convert a resume between formats.
---

# Resume Parser — Marketing Professional

## Workflow

### 1. Input Handling

Accept resume in any format:
- **PDF/DOCX file** — read and extract text
- **Image** — use mimo-omni for OCR
- **Pasted text** — parse directly
- **LinkedIn profile URL** — fetch and extract

### 2. Extract Structured Data

```
## Parsed Profile

### Contact
- Name:
- Email:
- Phone:
- LinkedIn:
- Location:

### Professional Summary
[2-3 sentence summary]

### Experience
#### [Title] — [Company] ([Dates])
- Channels: [Google Ads, Meta, etc.]
- Budget managed: [amount]
- Key metrics: [ROAS, CPA, revenue, etc.]
- Team size: [if mentioned]
- Key achievements: [bullet points]

#### [Title] — [Company] ([Dates])
...

### Skills
- Platforms: [Google Ads, Meta Ads, TikTok Ads, etc.]
- Analytics: [GA4, Looker Studio, etc.]
- Tools: [list]
- Soft skills: [list]

### Education
- [Degree] — [Institution] ([Year])

### Certifications
- [Google Ads Certified, Meta Blueprint, etc.]

### Gaps & Observations
- ⚠️ [Missing certifications or skills]
- 💡 [Suggestions for improvement]
```

### 3. Quality Checks

- Are metrics quantified? (ROAS, CPA, revenue, budget)
- Are platforms/tools explicitly listed?
- Is the summary keyword-rich for ATS?
- Are dates consistent and complete?
- Are there typos or formatting issues?

## Output

Structured profile ready to be used by resume-tailor, linkedin-optimizer, or portfolio-builder skills.

## Rules

- Extract every metric mentioned — numbers are gold
- Identify both explicit and implicit skills
- Flag inconsistencies (e.g., dates don't match, conflicting claims)
- Preserve the user's voice — don't rewrite, just structure
