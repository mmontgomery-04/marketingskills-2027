---
name: analytics
description: "Plans and implements marketing analytics and measurement: tracking plans, event taxonomies, GA4 setup, Google Tag Manager implementation, UTM governance, conversion tracking for ad platforms, dashboards, attribution, and turning data into decisions. Use when the user asks about tracking, GA4, GTM, events, conversions, UTMs, 'is this working', marketing dashboards, or measuring a campaign."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Analytics

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Start from decisions, not data
Ask: what decisions will this data drive? List 5–10 business questions ("Which channels create pipeline?", "Where do trial users drop off?"). Track what answers them; skip the rest.

### 2. Write a tracking plan
Use [event-library.md](references/event-library.md) for naming conventions and standard B2B events. Every event gets: name, trigger, parameters, owner, and which question it answers.

### 3. Implement
- GA4 configuration: [ga4-setup.md](references/ga4-setup.md)
- Tag Manager implementation: [gtm-setup.md](references/gtm-setup.md)
- Ad platform conversions: LinkedIn Insight Tag, Meta Pixel + Conversions API, Google Ads conversions (prefer server-side or offline conversion imports from the CRM for B2B).

### 4. Govern UTMs
Lowercase, hyphenated, one shared builder sheet. `utm_source` = platform, `utm_medium` = channel type (cpc, paid-social, email, organic-social), `utm_campaign` = `yyyy-mm_campaign-name`. Capture UTMs into hidden form fields → CRM (revops).

### 5. QA
GTM Preview + GA4 DebugView for every event before publishing. Re-QA after site changes.

### 6. Report and decide
Dashboards in Looker Studio or the BI tool, tied to the original questions. Every report ends with "so what / now what".

## Privacy
Respect consent: implement Consent Mode v2 for EEA/UK traffic, don't send PII (emails, names) to GA4, and document what's collected.

## References

Load these only when the task needs the detail:

- [Event Library (B2B)](references/event-library.md)
- [GA4 Setup Checklist](references/ga4-setup.md)
- [Google Tag Manager Implementation](references/gtm-setup.md)

## Related Skills

- [revops](../revops/SKILL.md) — CRM attribution and funnel reporting
- [cro](../cro/SKILL.md) — experiment measurement
- [paid-search](../paid-search/SKILL.md) — Google Ads conversions
- [paid-social](../paid-social/SKILL.md) — pixels and CAPI
- [social-media-reporting](../social-media-reporting/SKILL.md) — social analytics
- [ai-search](../ai-search/SKILL.md) — AI referral tracking
- [technical-seo](../technical-seo/SKILL.md) — organic measurement
