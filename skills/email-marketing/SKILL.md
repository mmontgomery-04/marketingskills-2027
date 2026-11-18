---
name: email-marketing
description: "Plans, writes, and optimizes opt-in email marketing: welcome and onboarding sequences, lead nurture, newsletters, product announcements, re-engagement, trial-to-paid, and customer lifecycle emails, plus segmentation, deliverability, and email metrics. Use when the user asks for an email sequence, drip campaign, newsletter, nurture flow, or help with open/click rates or deliverability for permission-based lists. For outbound to people who haven't opted in, use cold-email."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Email Marketing (Lifecycle & Nurture)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow
1. **Define the trigger and goal.** What event starts the flow (signup, download, trial start, inactivity) and what single action counts as success?
2. **Segment.** By lifecycle stage, persona, and behavior at minimum. Details: [lifecycle-sequences.md](references/lifecycle-sequences.md).
3. **Map the sequence.** For each email: day/trigger, goal, subject, preview text, core message, CTA, exit condition.
4. **Write.** Use copywriting rules: one idea and one CTA per email, plain-text style for B2B, subject ≤45 characters.
5. **Set exits and suppressions.** Stop nurture when someone books a meeting, becomes an opportunity, or unsubscribes from that stream.
6. **Protect deliverability.** See [deliverability.md](references/deliverability.md).
7. **Measure.** Clicks, replies, conversions, and pipeline influenced matter more than opens (Apple Mail Privacy Protection inflates opens).

## Output
A sequence table, then full copy for each email with 2 subject-line variants.

| # | Trigger/Day | Goal | Subject | Preview | CTA | Exit if… |
|---|---|---|---|---|---|---|

## References

Load these only when the task needs the detail:

- [Lifecycle Sequences](references/lifecycle-sequences.md)
- [Deliverability Essentials](references/deliverability.md)

## Related Skills

- [cold-email](../cold-email/SKILL.md) — outbound to non-opted-in prospects
- [copywriting](../copywriting/SKILL.md) — email copy craft
- [lead-magnets](../lead-magnets/SKILL.md) — assets that start nurture flows
- [revops](../revops/SKILL.md) — lifecycle stages and handoff
- [analytics](../analytics/SKILL.md) — tracking email-driven conversions
- [event-marketing](../event-marketing/SKILL.md) — event invite and follow-up flows
