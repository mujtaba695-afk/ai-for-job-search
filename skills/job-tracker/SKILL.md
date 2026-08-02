---
name: job-tracker
description: >
  Track job applications, interview stages, follow-ups, and outcomes for performance marketing
  and digital marketing roles. Maintains a structured log of all applications with statuses,
  deadlines, and action items. Use when the user wants to track their job search progress, log
  a new application, update application status, get follow-up reminders, or review their pipeline.
---

# Job Application Tracker

## Data Structure

Maintain a tracking file at `job-tracker/applications.md` (or user-specified location).

### Application Entry Format

```
## [Company] — [Role Title]
- **Status**: Applied | Screening | Interview | Final | Offer | Rejected | Withdrawn
- **Applied**: YYYY-MM-DD
- **Source**: LinkedIn | Indeed | Referral | Company Site
- **Salary Range**: $X - $Y (if listed)
- **Location**: Remote / Hybrid / Onsite (City)
- **Contact**: Recruiter name, email, LinkedIn
- **JD Link**: [URL]
- **Resume Version**: v1 (tailored for this role)

### Timeline
- [YYYY-MM-DD] Applied via [source]
- [YYYY-MM-DD] Recruiter responded, scheduled phone screen
- [YYYY-MM-DD] Phone screen completed — [notes]
- [YYYY-MM-DD] Technical interview — [notes]
- [YYYY-MM-DD] Final round — [notes]
- [YYYY-MM-DD] Offer received — $X base, $Y bonus, Z equity

### Notes
- [Any relevant notes about the role, company, or process]
```

## Commands (via conversation)

- **"Add [Company] [Role]"** — Create new entry
- **"Update [Company] to [status]"** — Update status
- **"Show my pipeline"** — Summary of all applications by stage
- **"What needs follow-up?"** — List applications with overdue actions
- **"Stats"** — Application-to-interview ratio, response rates, etc.

## Pipeline View

```
📊 Job Search Pipeline

| Stage | Count | Companies |
|---|---|---|
| Applied | 12 | Google, Meta, TikTok, ... |
| Screening | 4 | Amazon, Spotify, ... |
| Interview | 2 | Shopify, HubSpot |
| Final | 1 | Stripe |
| Offer | 0 | — |
| Rejected | 3 | Netflix, Uber, Lyft |

Response Rate: 42% | Interview Rate: 25% | Offer Rate: 0%
```

## Rules

- Update the tracker file after every interaction
- Remind user to follow up if no response after 7 days
- Track which resume version was used for each application
- Suggest follow-up templates when appropriate
