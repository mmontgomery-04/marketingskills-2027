---
name: icp-targeting
description: "Defines and operationalizes the Ideal Customer Profile and buyer personas: firmographics, technographics, trigger events, buying committee mapping, account tiering and scoring, and negative ICP. Use when the user asks who to target, wants an ICP or personas, needs to tier accounts for ABM, asks why win rates are low, or needs targeting criteria for ads, outbound, or lists. Feeds marketing-context, prospecting, paid-social, and social-media-targeting."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# ICP Targeting

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Start from evidence, not aspiration
Pull the last 12–24 months of closed-won and closed-lost deals. Look for patterns in: industry, employee count, revenue, region, tech stack, deal size, sales cycle, win rate, retention/NRR, and expansion. The ICP is who you **win, keep, and grow** with, not who you wish bought.

### 2. Define the account ICP
Fill [icp-framework.md](references/icp-framework.md): firmographics, technographics, situational triggers, and the negative ICP (who to avoid).

### 3. Map the buying committee and personas
Use [persona-template.md](references/persona-template.md) for each role: economic buyer, champion, technical evaluator, end user, blocker.

### 4. Tier and score
Build Tier 1/2/3 with [tiering-and-scoring.md](references/tiering-and-scoring.md). Tier 1 gets 1:1 ABM, Tier 2 1:few, Tier 3 programmatic.

### 5. Operationalize
Turn the ICP into filters others can use:
- **Prospecting:** Apollo/ZoomInfo/LinkedIn Sales Navigator filters
- **Paid:** LinkedIn targeting facets and matched audiences
- **RevOps:** CRM fields and fit score
- Write the summary back to `.agents/marketing-context.md`.

## Output
ICP one-pager, persona cards, tiering rules, and a filters table per tool.

## References

Load these only when the task needs the detail:

- [ICP Framework](references/icp-framework.md)
- [Persona Template](references/persona-template.md)
- [Account Tiering & Fit Scoring](references/tiering-and-scoring.md)

## Related Skills

- [marketing-context](../marketing-context/SKILL.md) — stores the ICP summary
- [prospecting](../prospecting/SKILL.md) — turns ICP into lists
- [social-media-targeting](../social-media-targeting/SKILL.md) — turns ICP into audiences
- [paid-social](../paid-social/SKILL.md) — ICP-based ad targeting
- [revops](../revops/SKILL.md) — fit scoring in the CRM
- [gtm-strategy](../gtm-strategy/SKILL.md) — segment selection
