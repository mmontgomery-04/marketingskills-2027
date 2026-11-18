---
name: revops
description: "Designs and fixes revenue operations across marketing, sales, and CS: lifecycle stages (lead → MQL → SQL → opportunity → customer), lead scoring and routing, SLAs, CRM/MAP data hygiene, attribution, funnel and pipeline reporting, forecasting inputs, and GTM tech stack. Use when the user mentions RevOps, lifecycle stages, MQL/SQL definitions, lead scoring, lead routing, HubSpot or Salesforce setup, attribution, pipeline reporting, or marketing–sales alignment."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# RevOps

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Agree on definitions first
Most "marketing vs sales" fights are definition fights. Lock lifecycle stages, entry/exit criteria, and owners with [lifecycle-and-scoring.md](references/lifecycle-and-scoring.md).

### 2. Scoring and routing
- **Fit score** (from icp-targeting) + **engagement score** (behavior) → MQL threshold.
- Route by territory, segment, or account owner; round-robin within teams; existing-account matches go to the owner.
- SLA example: SDR first touch on MQLs within 1 business hour for demo requests, 1 business day for others.

### 3. Data hygiene
Required fields, picklists over free text, dedupe rules, enrichment, and ownership. See [crm-hygiene.md](references/crm-hygiene.md).

### 4. Reporting
Build the funnel and pipeline dashboards in [funnel-metrics.md](references/funnel-metrics.md). Report by source, segment, and cohort, not just totals.

### 5. Attribution
Use multi-touch for marketing's internal optimization, self-reported attribution ("How did you hear about us?") for dark-social reality, and pipeline sourced/influenced for the board. No model is "true"; pick one and use it consistently.

## Output
Stage definitions table, scoring model, routing rules, SLA doc, dashboard spec, and a prioritized fix list.

## References

Load these only when the task needs the detail:

- [Lifecycle Stages & Lead Scoring](references/lifecycle-and-scoring.md)
- [Funnel & Pipeline Metrics](references/funnel-metrics.md)
- [CRM & MAP Hygiene](references/crm-hygiene.md)

## Related Skills

- [analytics](../analytics/SKILL.md) — tracking and attribution data
- [icp-targeting](../icp-targeting/SKILL.md) — fit scoring inputs
- [email-marketing](../email-marketing/SKILL.md) — lifecycle automations
- [gtm-strategy](../gtm-strategy/SKILL.md) — pipeline targets
- [prospecting](../prospecting/SKILL.md) — routing and SDR workflows
- [social-media-reporting](../social-media-reporting/SKILL.md) — channel reporting into the funnel
