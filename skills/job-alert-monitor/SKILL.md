---
name: job-alert-monitor
description: >
  Set up automated job monitoring and alerts for performance marketing, digital marketing, paid
  media, and related roles. Creates recurring search schedules, tracks new postings, and notifies
  the user of relevant opportunities. Use when the user wants to set up job alerts, monitor
  specific companies for openings, track new roles daily/weekly, or get notified when dream
  companies post relevant positions.
---

# Job Alert Monitor — Performance & Digital Marketing

## Setup

### 1. Define Alert Criteria

```
Alert Name: [descriptive name]
Role Keywords: [performance marketing, paid media, etc.]
Locations: [cities, countries, or "remote"]
Seniority: [junior/mid/senior/lead/director]
Salary Min: [optional]
Companies to Watch: [specific companies, optional]
Exclude: [agencies, specific companies, industries]
Frequency: [daily / every 3 days / weekly]
```

### 2. Create Cron Jobs

Use the `cron` tool to schedule recurring searches:

```
Schedule: Daily at 9:00 AM user's timezone
Action: Run job-search skill with saved criteria
Output: Summary of new postings found since last check
```

### 3. Tracking New vs. Seen

Maintain a state file at `job-tracker/alert-state.json`:
```json
{
  "alerts": {
    "senior-paid-media-sg": {
      "lastRun": "2025-01-15T09:00:00",
      "seenJobs": ["company-role-123", "..."],
      "totalFound": 15,
      "newSinceLastRun": 3
    }
  }
}
```

### 4. Notification Format

```
🔔 Job Alert: [Alert Name]
[X] new positions found!

1. [Title] — [Company] | [Location] | [Salary]
   Posted: [date] | Source: [LinkedIn/Indeed/etc.]
   [Link]

2. [Title] — [Company] | [Location] | [Salary]
   ...

💡 Tip: [Highlight the most promising one based on user's profile]
```

## Alert Ideas

- **Dream Company Watch** — Monitor 5-10 specific companies for any paid media openings
- **Salary Upgrade** — Alert when roles above $X salary are posted
- **Remote Opportunities** — Weekly digest of remote performance marketing roles
- **New Market** — Monitor a new city/country the user is considering

## Rules

- Deduplicate across sources (same job on LinkedIn and Indeed = 1 listing)
- Prioritize by relevance to user's profile
- Don't spam — if no new jobs, skip the notification
- Highlight "easy apply" or direct application options
