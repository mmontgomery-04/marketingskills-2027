---
name: marketing-context
description: "Creates and maintains the shared marketing context file (.agents/marketing-context.md) that every other skill in this repo reads first: company, product, ICP, positioning, voice, competitors, channels, and goals. Use at the start of any new project, when the user says 'set up context', 'here's my company', 'remember my product', or when another skill finds the context file missing or stale."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Marketing Context (Foundation Skill)

Every other skill in this library starts by reading one file: `.agents/marketing-context.md`. This skill creates and maintains it, so the user never has to re-explain their company, audience, or voice.

## Workflow

### 1. Check for an existing file
- If `.agents/marketing-context.md` exists, read it, show a 5-line summary, and ask what changed.
- If it doesn't, offer two paths:
  - **Auto-draft (recommended):** read the website, README, pitch deck, or docs the user points to, draft every section, then ask the user to correct it.
  - **Interview:** walk through the sections below in batches of 3–4 questions.

### 2. Fill the sections
Use the template in [context-template.md](references/context-template.md). Minimum viable context is: one-liner, ICP, top 3 pains, differentiators, top 3 competitors, voice rules, and primary conversion goal. Everything else can be "TBD".

### 3. Capture customer language verbatim
Pull exact phrases from reviews, sales calls, support tickets, and G2/Capterra. Copy, landing pages, and ads all reuse this section, so it's the highest-leverage part of the file.

### 4. Save and confirm
Write the file, tell the user where it is, and list which skills will now pick it up automatically.

## Rules
- Mark anything inferred (not stated by the user) with `(inferred — confirm)`.
- Keep it under ~1,500 words. Link out to longer docs instead of pasting them.
- Add a `Last updated:` date. If a skill finds a file older than 90 days, it should suggest a refresh.
- Never store secrets, API keys, or customer PII in the file.

## Which skills read which sections
See [section-usage-map.md](references/section-usage-map.md).

## References

Load these only when the task needs the detail:

- [Marketing Context Template](references/context-template.md)
- [Section Usage Map](references/section-usage-map.md)

## Related Skills

- [icp-targeting](../icp-targeting/SKILL.md) — builds the full ICP that this file summarizes
- [product-marketing](../product-marketing/SKILL.md) — owns positioning and messaging that feed this file
- [competitor-research](../competitor-research/SKILL.md) — keeps the competitor table current
