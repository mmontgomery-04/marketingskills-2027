---
name: content-strategy
description: "Plans what content to create and why: topic clusters, pillar/spoke architecture, keyword-to-funnel mapping (TOFU/MOFU/BOFU), editorial calendars, content audits, refresh/prune decisions, and distribution. Use when the user asks for a content strategy, content plan, editorial calendar, topic ideas, content audit, or 'what should we blog about'. Writing the actual piece belongs to copywriting; optimizing it belongs to on-page-seo."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Content Strategy (B2B)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. Ask the user if they have any internal resources that can help, specifically transcripts (i.e. Otter) from SMEs, one-pagers, product pages, blogs, or VoC research from industry forums or Reddit

## Workflow

### 1. Anchor to business goals
Every content program should map to a pipeline goal: organic demo requests, sales enablement, category creation, or retention. Ask which one matters most this quarter.

### 2. Build the topic map
- Start from ICP pains and jobs-to-be-done, not keyword tools.
- Group into 3–6 **pillars** (core themes you want to own) → each with 8–20 **spokes**.
- Validate demand with keyword data (volume, difficulty, intent) and with sales/support questions.
- Details: [topic-clusters.md](references/topic-clusters.md).

### 3. Map to the funnel
Tag every topic TOFU / MOFU / BOFU with [funnel-mapping.md](references/funnel-mapping.md). B2B teams usually under-invest in BOFU (comparisons, alternatives, pricing, use cases, integrations), which converts best, so prioritize it first when the domain is new.

### 4. Prioritize
Score each topic: `Business value (1–3) × Ranking feasibility (1–3) × Effort inverse (1–3)`. Ship the highest scores first.

### 5. Calendar and operations
Cadence, owners, briefs, SME interviews, review SLAs, and distribution: [editorial-ops.md](references/editorial-ops.md).

### 6. Audit existing content (if any)
For each URL, decide **Keep / Refresh / Consolidate (301) / Prune**, based on traffic, conversions, backlinks, and topical fit.

## Output
A prioritized topic table: `pillar | topic | primary keyword | intent | funnel stage | format | score | owner | target date`, plus a 90-day calendar.

## References

Load these only when the task needs the detail:

- [Topic Clusters](references/topic-clusters.md)
- [Funnel Mapping for B2B Content](references/funnel-mapping.md)
- [Editorial Operations](references/editorial-ops.md)

## Related Skills

- [on-page-seo](../on-page-seo/SKILL.md) — optimizing each piece
- [copywriting](../copywriting/SKILL.md) — writing it
- [lead-magnets](../lead-magnets/SKILL.md) — MOFU gated assets
- [ai-search](../ai-search/SKILL.md) — content LLMs will cite
- [icp-targeting](../icp-targeting/SKILL.md) — the pains topics come from
- [social-media-strategy](../social-media-strategy/SKILL.md) — distribution
