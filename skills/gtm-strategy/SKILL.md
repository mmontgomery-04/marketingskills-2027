---
name: gtm-strategy
description: "Builds go-to-market strategy and plans: market and segment selection, motion choice (product-led, sales-led, partner-led, ABM, hybrid), channel strategy, pricing go-to-market, launch plans, pipeline targets and funnel math, and GTM team alignment. Use when the user asks for a GTM plan, how to enter a new market or segment, which channels to prioritize, how much pipeline is needed, or how to launch a new product to market."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# GTM Strategy

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Where to play
Pick segments by attractiveness (size, pain intensity, ability to pay, reachability) × ability to win (fit, proof, competition). Pull the ICP from icp-targeting.

### 2. How to win
Positioning from product-marketing. Choose the motion with [gtm-motions.md](references/gtm-motions.md); ACV and buyer behavior usually decide it.

### 3. Pipeline math
Work backwards from the revenue target with [pipeline-math.md](references/pipeline-math.md). This turns strategy into a lead/meeting/opportunity budget per channel.

### 4. Channel plan
Choose 2–3 primary channels you can realistically win in and resource properly. For each: owner, budget, expected pipeline, leading indicators.

### 5. Launch plan
Phased: **Prepare** (enablement, assets, tracking) → **Launch** (announce, campaigns) → **Sustain** (always-on programs, optimization). Use product-marketing's launch tiers.

### 6. Alignment and cadence
Shared definitions (revops), SLAs between marketing and sales, a weekly pipeline review, and quarterly strategy reviews.

## Output
A one-page GTM plan: segment → ICP → positioning → motion → channels → pipeline targets → 90-day milestones → metrics → risks.

## References

Load these only when the task needs the detail:

- [GTM Motions](references/gtm-motions.md)
- [Pipeline Math](references/pipeline-math.md)

## Related Skills

- [abm](../abm/SKILL.md): account-based motions
- [marketing-project-management](../marketing-project-management/SKILL.md): executing the plan on time
- [product-marketing](../product-marketing/SKILL.md): positioning and launch tiers
- [icp-targeting](../icp-targeting/SKILL.md): segment definition
- [revops](../revops/SKILL.md): funnel definitions and reporting
- [analytics](../analytics/SKILL.md): measurement
- [paid-search](../paid-search/SKILL.md): demand capture channel
- [paid-social](../paid-social/SKILL.md): demand creation channel
- [event-marketing](../event-marketing/SKILL.md): field and virtual programs
- [prospecting](../prospecting/SKILL.md): outbound engine
