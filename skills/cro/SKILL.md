---
name: cro
description: "Improves conversion rates on landing pages, homepages, pricing pages, forms, signup and demo flows, and in-product upgrade paths through audits, prioritized recommendations, and A/B testing. Use when the user asks why a page isn't converting, wants a CRO audit, landing page review, form optimization, more demo requests or signups, or help designing and reading an A/B test."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Conversion Rate Optimization

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Get the numbers
Traffic by source, conversion rate by source and device, funnel step drop-off, and the primary conversion. Without a baseline, recommendations are guesses.

### 2. Understand intent
Where do visitors come from and what did they expect? An ad promising a free template that lands on a demo page will fail no matter how good the page is.

### 3. Audit the page
Run [page-audit.md](references/page-audit.md), scoring each area. Add qualitative evidence: session recordings, heatmaps, on-page polls, sales call objections.

### 4. Prioritize
Score each idea with ICE (Impact, Confidence, Ease: 1–10 each). Ship obvious fixes (broken forms, slow load, mismatched message) immediately; **test** the uncertain ones.

### 5. Test properly
Use [ab-testing.md](references/ab-testing.md): hypothesis, sample size, duration, and one primary metric.

### 6. Forms
Forms are the highest-leverage element on most B2B pages: [form-optimization.md](references/form-optimization.md).

## Output
| # | Issue | Evidence | Recommendation | ICE | Test or ship? |
|---|---|---|---|---|---|

Include rewritten copy (via copywriting) for the top recommendations, not just "improve the headline".

## References

Load these only when the task needs the detail:

- [Landing Page Audit](references/page-audit.md)
- [A/B Testing](references/ab-testing.md)
- [Form Optimization](references/form-optimization.md)

## Related Skills

- [copywriting](../copywriting/SKILL.md) — rewriting page copy
- [ux-ui](../ux-ui/SKILL.md) — design and usability fixes
- [analytics](../analytics/SKILL.md) — measurement and experiments
- [lead-magnets](../lead-magnets/SKILL.md) — offer design
- [paid-search](../paid-search/SKILL.md) — landing page message match
- [paid-social](../paid-social/SKILL.md) — landing page message match
