---
name: abm
description: "Plans and runs account-based marketing for B2B: selecting and tiering target accounts, 1:1, 1:few, and 1:many plays, buying-committee coverage, intent and engagement signals, coordinated ads, outbound, content, direct mail, and events, sales and marketing orchestration, and account-level measurement. Use when the user mentions ABM, account-based marketing, target account lists, named accounts, account plays, or coordinating marketing and sales on specific companies. For defining the ICP itself use icp-targeting."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Account-Based Marketing

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

ABM concentrates marketing and sales effort on a defined set of accounts and treats each account (or cluster) as a market of one. It works best when deals are large, buying committees are complex, and the total number of good-fit accounts is limited.

## Workflow

### 1. Confirm ABM fits
ABM is usually worth it when ACV is high enough to justify per-account effort (often $25K+), sales cycles involve several stakeholders, and sales leadership will commit reps to the same account list. If those aren't true, a segment-based demand program will usually perform better.

### 2. Build and tier the account list
Pull the ICP and fit scoring from [icp-targeting](../icp-targeting/SKILL.md), layer intent and engagement signals from [prospecting](../prospecting/SKILL.md), and agree on the final list with sales. Tiering and capacity rules are in [tiers-and-plays.md](references/tiers-and-plays.md).

### 3. Map the buying committee
For each Tier 1 account (and each Tier 2 cluster), identify the economic buyer, champion, technical evaluator, users, and likely blockers. Gaps in coverage are the first thing to fix, because single-threaded deals stall.

### 4. Design the plays
Choose plays by tier and stage from [tiers-and-plays.md](references/tiers-and-plays.md). A play specifies the audience, message, channels, sequence, owner, and the signal that moves the account to the next stage.

### 5. Orchestrate with sales
Use the operating rhythm in [orchestration.md](references/orchestration.md): shared account list in the CRM, weekly account standups, clear triggers for sales outreach, and one place to see every touch.

### 6. Measure at the account level
Track account coverage, engagement, opportunity creation, pipeline, win rate, deal size, and cycle length for target accounts compared with a control group of similar non-target accounts. Lead counts and MQLs are the wrong scoreboard for ABM.

## Output
An ABM plan with the tiered account list, buying-committee coverage, plays per tier, a 90-day orchestration calendar, budget, and the measurement framework.

## References

Load these only when the task needs the detail:

- [Tiers & Plays](references/tiers-and-plays.md)
- [Sales & Marketing Orchestration](references/orchestration.md)

## Related Skills

- [icp-targeting](../icp-targeting/SKILL.md): fit scoring and tiers
- [prospecting](../prospecting/SKILL.md): signals and outreach
- [social-media-targeting](../social-media-targeting/SKILL.md): account-based audiences
- [paid-social](../paid-social/SKILL.md): account-targeted ads
- [retargeting](../retargeting/SKILL.md): re-engaging target-account visitors
- [event-marketing](../event-marketing/SKILL.md): dinners and roundtables
- [revops](../revops/SKILL.md): account flags, routing, and reporting
- [customer-advocacy](../customer-advocacy/SKILL.md): references and peer proof
