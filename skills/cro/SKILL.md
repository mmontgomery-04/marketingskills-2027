---
name: cro
description: "Improves conversion rates on landing pages, homepages, pricing pages, forms, signup and demo flows, and in-product upgrade paths through audits, prioritized recommendations, and A/B testing. Use when the user asks why visitors aren't converting, wants a CRO audit, landing page review, form optimization, more demo requests or signups, or help designing and reading an A/B test."
metadata:
  version: 1.1.0
  author: William Montgomery
---

# Conversion Rate Optimization

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Get the numbers and the backstory
Ask for whatever the context file doesn't already answer:
- **Page type** and the **one conversion that counts** (demo request, trial, signup, download, contact).
- **Baseline:** traffic by source, conversion rate by source and device, funnel step drop-off.
- **What happens after the conversion:** thank-you page, scheduler, onboarding. A page that converts into a dead end isn't converting.
- **Research on hand:** session recordings, heatmaps, on-page polls, sales call notes, support tickets.
- **What's been tried:** past changes and tests and how they turned out, so you don't re-suggest a loser.

Without a baseline, recommendations are guesses.

### 2. Understand intent
Where do visitors come from and what did they expect? An ad promising a free template that lands on a demo page will fail no matter how good the page is.

### 3. Audit the page
Run [page-audit.md](references/page-audit.md) top to bottom. Its areas are ordered by typical impact: if visitors can't tell what the product is, button wording won't rescue the page. Back each finding with evidence (data, recordings, polls, sales objections). For what matters most on homepages, landing, pricing, product, demo, and blog pages, use [page-types.md](references/page-types.md).

### 4. Prioritize
Score each idea with ICE (Impact, Confidence, Ease: 1–10 each). Ship obvious fixes (broken forms, slow load, mismatched message) immediately; **test** the uncertain ones.

### 5. Test properly
Use [ab-testing.md](references/ab-testing.md): hypothesis, sample size, duration, and one primary metric.

### 6. Forms
Forms are the highest-leverage element on most B2B pages: [form-optimization.md](references/form-optimization.md).

## Output
Sort recommendations into three groups:
1. **Fix now:** clear problems that are cheap to fix (broken form, message mismatch, no proof near the CTA).
2. **Bigger bets:** changes that need design, development, or new assets but go after the biggest issues.
3. **Test first:** ideas where the evidence is mixed. Write each as a hypothesis ([ab-testing.md](references/ab-testing.md)).

Then the detail table:

| # | Issue | Evidence | Recommendation | ICE | Group |
|---|---|---|---|---|---|

For the headline, subhead, and primary CTA, write 2–3 options with a one-line reason each, using copywriting's rules and Don'ts. "Improve the headline" is not a recommendation; a rewritten headline is.

## Rules
- **Real proof only.** Any proof you suggest adding (stats, logos, testimonials) must exist. Mark gaps `[PROOF NEEDED]`; never fill them in.
- **No dark patterns:** fake countdowns or scarcity, pre-checked consent boxes, guilt-trip decline links, prices revealed only at the last step. They can lift one number while costing trust, refunds, and compliance.

## References

Load these only when the task needs the detail:

- [Landing Page Audit](references/page-audit.md)
- [CRO by Page Type](references/page-types.md)
- [A/B Testing](references/ab-testing.md)
- [Form Optimization](references/form-optimization.md)

## Related Skills

- [copywriting](../copywriting/SKILL.md) — rewriting page copy
- [ux-ui](../ux-ui/SKILL.md) — design and usability fixes
- [analytics](../analytics/SKILL.md) — measurement and experiments
- [lead-magnets](../lead-magnets/SKILL.md) — offer design
- [paid-search](../paid-search/SKILL.md) — landing page message match
- [paid-social](../paid-social/SKILL.md) — landing page message match
