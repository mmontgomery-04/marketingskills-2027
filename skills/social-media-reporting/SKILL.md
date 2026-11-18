---
name: social-media-reporting
description: "Measures and reports organic and paid social performance: KPI selection by goal, metric definitions, dashboards, weekly/monthly/quarterly reports, benchmarking, attribution of social to pipeline (including self-reported and dark social), and insight-led recommendations. Use when the user asks for a social media report, social KPIs, social dashboard, LinkedIn analytics review, or proof that social is working."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Social Media Reporting

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Tie KPIs to goals
| Goal | Primary KPIs | Supporting |
|---|---|---|
| Awareness | Impressions in ICP, reach, follower growth in ICP | Video views, share of voice |
| Engagement / authority | Engagement rate, comments, profile visits, saves/shares | Top posts by topic |
| Demand | Clicks, landing page conversions, demo requests, pipeline influenced | Cost per lead (paid) |
| Hiring | Career page traffic, applicants | Employer brand sentiment |

Definitions and formulas: [metrics-definitions.md](references/metrics-definitions.md).

### 2. Collect data
Native analytics (LinkedIn page and creator analytics, YouTube Studio, ad managers), a social tool (Sprout, Hootsuite, Shield for LinkedIn creators) if available, GA4 for social traffic and conversions, and CRM for pipeline.

### 3. Account for dark social
Much B2B social influence doesn't leave a click trail (someone sees posts for weeks, then searches your brand). Add "How did you hear about us?" as a required free-text field on demo forms and track mentions of social, LinkedIn, or specific people. Watch branded search and direct traffic trends alongside social activity.

### 4. Build the report
Use [report-template.md](references/report-template.md). Lead with insights and decisions, not screenshots.

### 5. Recommend
Every report ends with 3 actions: keep, stop, try.

## Rules
- Compare to your own trend (period over period, same period last year) before industry benchmarks.
- Report organic and paid separately, then together for total impact.
- Note sample size: one viral post skews a month.

## References

Load these only when the task needs the detail:

- [Social Metrics Definitions](references/metrics-definitions.md)
- [Social Report Template](references/report-template.md)

## Related Skills

- [analytics](../analytics/SKILL.md) — GA4 and tracking
- [revops](../revops/SKILL.md) — pipeline attribution
- [social-media-strategy](../social-media-strategy/SKILL.md) — acting on insights
- [paid-social](../paid-social/SKILL.md) — paid performance
- [social-media-targeting](../social-media-targeting/SKILL.md) — audience quality
