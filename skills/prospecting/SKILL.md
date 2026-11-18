---
name: prospecting
description: "Finds, researches, and prioritizes prospects for outbound: building target account and contact lists, buying signals and intent data, account research briefs, multi-threading the buying committee, and multichannel outreach cadences (email, LinkedIn, phone). Use when the user asks to build a prospect list, research an account, find decision makers, use intent or trigger signals, or plan an SDR/BDR outreach cadence. Writing the emails themselves belongs to cold-email."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# Prospecting

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Build the account list
Translate the ICP (icp-targeting) into filters in Apollo, ZoomInfo, Clay, or LinkedIn Sales Navigator. See [list-building.md](references/list-building.md).

### 2. Prioritize with signals
Rank accounts by fit × timing. Signals in [signals.md](references/signals.md): hiring, funding, leadership changes, tech changes, intent topics, website visits, content engagement.

### 3. Research the account
Produce a 5-minute brief per Tier 1 account with [account-research.md](references/account-research.md). Tier 2/3 get trigger-level research only.

### 4. Multi-thread
Identify 3–5 contacts across the buying committee: economic buyer, champion, evaluator, user. Different message per role.

### 5. Cadence
A typical 3-week multichannel cadence:

| Day | Touch |
|---|---|
| 1 | LinkedIn profile view + email 1 |
| 2 | LinkedIn connection request (no pitch) |
| 4 | Call + voicemail |
| 6 | Email 2 (new angle) |
| 9 | LinkedIn engagement on their post / DM if connected |
| 12 | Email 3 (case study) + call |
| 16 | Email 4 (insight/resource) |
| 21 | Breakup email |

Hand copy to cold-email. Log everything in the CRM (revops).

## Output
Prioritized account table (`account | tier | fit score | top signal | contacts | angle | next step`) and research briefs.

## References

Load these only when the task needs the detail:

- [Buying Signals](references/signals.md)
- [Account Research Brief](references/account-research.md)
- [List Building](references/list-building.md)

## Related Skills

- [abm](../abm/SKILL.md): coordinated account plays
- [icp-targeting](../icp-targeting/SKILL.md): who to prospect
- [cold-email](../cold-email/SKILL.md): outreach copy
- [revops](../revops/SKILL.md): CRM hygiene and routing
- [competitor-research](../competitor-research/SKILL.md): displacement angles
- [social-media-targeting](../social-media-targeting/SKILL.md): LinkedIn audience overlap for air cover
