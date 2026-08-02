---
name: portfolio-website-generator
description: >
  Generate a professional portfolio website for performance marketing, digital marketing, and
  paid media professionals. Creates a single-page HTML site showcasing case studies, skills,
  certifications, and contact information. Use when the user needs a personal website to
  complement their resume, wants to showcase marketing campaigns visually, or needs a
  professional online presence for recruiters.
---

# Portfolio Website Generator

## Website Structure

### Single-Page HTML Portfolio

Generate a clean, professional single-page site with these sections:

```
1. HERO — Name, title, tagline, CTA
2. ABOUT — Brief professional summary
3. CASE STUDIES — 3-5 campaign showcases with metrics
4. SKILLS — Platforms, tools, certifications
5. EXPERIENCE — Timeline (condensed resume)
6. CONTACT — Email, LinkedIn, Calendly
```

### Case Study Cards (Key Section)

Each case study should display:
```
┌─────────────────────────────────┐
│ [Channel Icon] [Industry]       │
│                                  │
│ Campaign: [Name]                 │
│                                  │
│ ┌──────┐ ┌──────┐ ┌──────┐     │
│ │ +105%│ │ -51% │ │4.3x  │     │
│ │ ROAS │ │ CPA  │ │ ROAS │     │
│ └──────┘ └──────┘ └──────┘     │
│                                  │
│ [Brief description - 2 lines]    │
│                                  │
│ Tools: Google Ads, GA4, Looker   │
└─────────────────────────────────┘
```

### Design Requirements
- Clean, minimal design (no clutter)
- Mobile-responsive
- Fast loading (no heavy images)
- Dark mode option
- Professional color scheme (navy, white, accent color)
- Google Fonts (Inter, Poppins, or similar)

### Technical
- Single HTML file with embedded CSS (no dependencies)
- Can be hosted on GitHub Pages, Netlify, or Vercel for free
- No JavaScript required (keep it simple)
- Print-friendly (recruiters may print it)

## Output

Generate a complete HTML file that:
1. Works when opened directly in a browser
2. Is self-contained (no external dependencies except fonts)
3. Is ready to deploy to any free hosting
4. Includes placeholder content that user can customize

## Rules
- Metrics are the centerpiece — make numbers big and visible
- Keep it to one page (recruiters spend <30 seconds)
- Include a clear CTA (contact/hire me)
- Make it easy to update (clean HTML structure)
- Test on mobile before finalizing
