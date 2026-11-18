---
name: product-marketing
description: "Owns positioning, messaging, and product launches: positioning statements, messaging houses, value propositions, competitive differentiation, launch tiering and plans, sales enablement (pitch narratives, battlecards, one-pagers), pricing and packaging messaging, and customer research. Use when the user asks about positioning, messaging, value props, a product or feature launch, sales enablement, or 'how should we talk about this product'."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Product Marketing

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## What PMM owns
1. **Positioning:** what we are, for whom, against what alternative, and why we win.
2. **Messaging:** how that positioning is said, per persona and per channel.
3. **Launches:** getting new things to market with the right weight.
4. **Enablement:** making sales and CS effective with the story.
5. **Market intelligence:** customer, competitor, and win/loss insight (with competitor-research).

## Positioning workflow
Use [positioning.md](references/positioning.md):
1. Competitive alternatives (including "do nothing" and spreadsheets)
2. Unique attributes
3. Value those attributes enable (with proof)
4. Best-fit customers (from icp-targeting)
5. Market category / frame of reference
6. Positioning statement + one-liner

## Messaging workflow
Build a messaging house with [messaging-house.md](references/messaging-house.md), then tailor by persona.

## Launch workflow
Tier the launch with [launch-tiers.md](references/launch-tiers.md), then hand off the GTM plan to gtm-strategy, copy to copywriting, assets to lead-magnets, and measurement to analytics.

## Rules
- Test messaging with real buyers (5+ interviews or message tests) before scaling it.
- Write positioning back into `.agents/marketing-context.md`.

## References

Load these only when the task needs the detail:

- [Positioning](references/positioning.md)
- [Messaging House](references/messaging-house.md)
- [Launch Tiers](references/launch-tiers.md)

## Related Skills

- [marketing-context](../marketing-context/SKILL.md) — stores positioning
- [gtm-strategy](../gtm-strategy/SKILL.md) — market entry and launch execution
- [competitor-research](../competitor-research/SKILL.md) — battlecards and differentiation
- [copywriting](../copywriting/SKILL.md) — message execution
- [icp-targeting](../icp-targeting/SKILL.md) — best-fit customers
- [lead-magnets](../lead-magnets/SKILL.md) — enablement collateral
