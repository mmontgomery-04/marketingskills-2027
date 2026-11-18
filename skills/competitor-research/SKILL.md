---
name: competitor-research
description: "Researches and analyzes competitors: positioning, messaging, pricing and packaging, product features, SEO and content footprint, paid ads, reviews (G2/Capterra), social presence, and AI search visibility; then turns findings into battlecards, comparison pages, and differentiation. Use when the user asks about competitors, competitive analysis, 'who are we up against', battlecards, 'X vs Y' pages, win/loss insight, or how a rival is marketing."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Competitor Research

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow

### 1. Define the competitive set
- **Direct:** same category, same buyer
- **Indirect:** different approach to the same problem
- **Status quo:** spreadsheets, agencies, in-house builds, doing nothing (often the biggest competitor)

### 2. Gather evidence by dimension
Use [analysis-template.md](references/analysis-template.md). Sources:
- Website, pricing page, changelog, docs, careers page (hiring = strategy signals)
- G2/Capterra/TrustRadius reviews; mine 1–3 star reviews for weaknesses
- Ad libraries: LinkedIn Ad Library, Meta Ad Library, Google Ads Transparency Center
- SEO tools (Semrush/Ahrefs): top pages, keyword gaps, backlinks
- AI engines: run category prompts to see who gets recommended (ai-search)
- Win/loss notes and sales call recordings

### 3. Synthesize
Where they win, where they lose, what they claim vs what customers say, and **openings for us**.

### 4. Activate
- **Battlecards** for sales: [battlecard-template.md](references/battlecard-template.md)
- **Comparison/alternative pages** (copywriting + on-page-seo)
- **Conquesting** keywords and audiences (paid-search, paid-social)
- Update the competitor table in `.agents/marketing-context.md`

## Rules
- Cite sources and dates; competitor info goes stale fast.
- Be accurate and fair in anything public. Never make claims you can't substantiate.

## References

Load these only when the task needs the detail:

- [Competitive Analysis Template](references/analysis-template.md)
- [Battlecard Template](references/battlecard-template.md)

## Related Skills

- [product-marketing](../product-marketing/SKILL.md) — differentiation and positioning
- [ai-search](../ai-search/SKILL.md) — AI share of voice vs competitors
- [paid-search](../paid-search/SKILL.md) — competitor keyword conquesting
- [on-page-seo](../on-page-seo/SKILL.md) — comparison page SEO
- [copywriting](../copywriting/SKILL.md) — comparison pages
- [marketing-context](../marketing-context/SKILL.md) — competitor table
