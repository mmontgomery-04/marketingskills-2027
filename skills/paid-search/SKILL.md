---
name: paid-search
description: "Plans, builds, and optimizes paid search for B2B: Google Ads and Microsoft Ads strategy, account and campaign structure, keyword research and match types, negative keywords, responsive search ads, bidding strategies, Performance Max, brand and competitor campaigns, landing page alignment, offline conversion imports, and budget pacing. Use when the user mentions Google Ads, PPC, SEM, paid search, search ads, keywords for ads, CPCs, or ROAS/CPA on search."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# Paid Search (B2B)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Strategy first
Search **captures** demand that already exists, so it works best alongside channels that build awareness. In B2B, search volume for your category may be small. Prioritize:
1. **Brand** (protect your name; usually cheapest conversions)
2. **High-intent non-brand**: "[category] software", "[problem] tool", "[competitor] alternative", "[category] pricing"
3. **Competitor** terms (if economics work and policy allows)
4. **Problem/solution-aware** terms (higher volume, lower intent, often better as content via on-page-seo)

## Workflow

### 1. Measurement before spend
Conversion tracking in place (analytics). For B2B, import **offline conversions** from the CRM (SQL, opportunity, closed-won, with values) so bidding optimizes for pipeline, not form fills.

### 2. Structure
Use [account-structure.md](references/account-structure.md). Group by intent theme, keep ad groups tight, and don't over-fragment; modern smart bidding needs data.

### 3. Keywords and negatives
Match-type strategy and negative lists: [keywords-and-match-types.md](references/keywords-and-match-types.md).

### 4. Ads
Responsive Search Ads: up to 15 headlines (30 chars) and 4 descriptions (90 chars). Write varied angles: keyword, outcome, proof, offer, differentiator. Pin only when necessary. Add sitelinks, callouts, structured snippets, and images.

### 5. Landing pages
Message match with the query and ad. Send competitor terms to a comparison page and category terms to a solution page, not the homepage. Run them through cro.

### 6. Bidding
Start with Maximize Conversions or manual/Max Clicks until you have enough conversions (roughly 30+/month per campaign), then move to tCPA or tROAS using pipeline-based conversions.

### 7. Optimize weekly
Search terms review → negatives; pause losers; test ad angles; check impression share lost to budget vs rank; review by device, geo, and time.

## Output
Campaign plan table: `campaign | goal | keywords (examples) | match types | budget | bid strategy | landing page | conversion goal`.

More: [b2b-best-practices.md](references/b2b-best-practices.md).

## References

Load these only when the task needs the detail:

- [Account Structure](references/account-structure.md)
- [Keywords & Match Types](references/keywords-and-match-types.md)
- [B2B Paid Search Best Practices](references/b2b-best-practices.md)

## Related Skills

- [retargeting](../retargeting/SKILL.md): search remarketing and Customer Match
- [analytics](../analytics/SKILL.md): conversion tracking
- [cro](../cro/SKILL.md): landing page conversion
- [copywriting](../copywriting/SKILL.md): ad copy
- [competitor-research](../competitor-research/SKILL.md): conquesting angles
- [revops](../revops/SKILL.md): offline conversion data
- [on-page-seo](../on-page-seo/SKILL.md): organic vs paid keyword strategy
