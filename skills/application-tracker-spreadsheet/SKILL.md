---
name: application-tracker-spreadsheet
description: >
  Create and manage a detailed job application tracking spreadsheet for performance marketing,
  digital marketing, and paid media roles. Generates a formatted Excel/Google Sheets tracker
  with columns for all application data, status tracking, and analytics. Use when the user
  wants a structured spreadsheet to track applications, analyze their job search pipeline,
  or generate reports on their search progress.
---

# Application Tracker Spreadsheet

## Spreadsheet Structure

### Sheet 1: Applications

| Column | Description |
|---|---|
| Company | Company name |
| Role | Job title |
| Location | City / Remote |
| Source | LinkedIn / Indeed / Referral / etc. |
| Date Applied | YYYY-MM-DD |
| Status | Applied / Screening / Interview / Final / Offer / Rejected |
| Salary Listed | Range if available |
| Resume Version | Which tailored resume was used |
| Contact Name | Recruiter / Hiring Manager |
| Contact Email | Email address |
| Contact LinkedIn | Profile URL |
| JD Link | URL to job posting |
| Next Action | What to do next |
| Next Action Date | When to follow up |
| Notes | Any relevant notes |

### Sheet 2: Pipeline Summary

```
| Stage | Count | Conversion Rate |
|---|---|---|
| Applied | 25 | 100% |
| Screening | 8 | 32% |
| Interview | 4 | 16% |
| Final Round | 2 | 8% |
| Offer | 1 | 4% |
| Rejected | 5 | 20% |
```

### Sheet 3: Weekly Stats

```
| Week | Applied | Responses | Interviews | Offers |
|---|---|---|---|---|
| Week 1 | 10 | 2 | 1 | 0 |
| Week 2 | 8 | 3 | 2 | 0 |
```

## Output

Generate a formatted Excel file using the excel-xlsx skill with:
- Conditional formatting for status colors
- Dropdown for status options
- Auto-calculated pipeline stats
- Charts for visual progress

## Rules
- Update after every interaction
- Track which resume version was used (important for learning what works)
- Set reminders for follow-ups (7 days after application, 3 days after interview)
- Review weekly to identify patterns (which sources have best response rates)
