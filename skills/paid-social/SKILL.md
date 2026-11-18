---
name: paid-social
description: "Plans, launches, and optimizes paid social for B2B on LinkedIn Ads, Meta, YouTube, X, and Reddit: objectives, funnel structure, ad formats (single image, document, video, conversation, Thought Leader ads, lead gen forms), creative strategy and testing, budgets and bidding, frequency, CRM-integrated lead forms, and measurement. Use when the user mentions LinkedIn ads, Facebook/Meta ads, paid social, social ads, ad creative, lead gen forms, or CPL/cost per opportunity on social."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# Paid Social (B2B)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Strategy
Paid social **creates demand**: it reaches buyers before they search. Plan for a full funnel, not just lead forms:

| Stage | Audience (social-media-targeting) | Objective | Content | Offer |
|---|---|---|---|---|
| Awareness | Cold ICP | Brand awareness / engagement / video views | POV, education, Thought Leader ads, short video | None or soft |
| Consideration | Engaged + site visitors | Engagement / website visits / lead gen | Case studies, guides, webinars | Lead magnet, event |
| Conversion | High-intent retargeting, Tier 1 accounts | Lead gen / website conversions | Proof, comparisons, demo previews | Demo, trial, assessment |

## Workflow
1. **Measurement:** Insight Tag / Pixel + Conversions API (server-side), lead form → CRM sync, offline conversion upload where possible (analytics, revops).
2. **Audiences:** from social-media-targeting with exclusions.
3. **Creative:** the biggest lever. See [creative-testing.md](references/creative-testing.md).
4. **Platform setup:** [linkedin-ads.md](references/linkedin-ads.md), [meta-and-others.md](references/meta-and-others.md).
5. **Budget:** enough per campaign to exit learning and get signal; fewer campaigns with more budget beat many starved ones.
6. **Optimize:** weekly creative and audience review; refresh creative when frequency rises and CTR falls; judge success by cost per opportunity and pipeline, not CPL alone.

## Output
Campaign plan: `campaign | stage | platform | objective | audience | format | offer | budget | KPI`, plus 3–5 creative concepts with copy.

## References

Load these only when the task needs the detail:

- [LinkedIn Ads](references/linkedin-ads.md)
- [Meta, YouTube, X & Reddit](references/meta-and-others.md)
- [Creative Strategy & Testing](references/creative-testing.md)

## Related Skills

- [retargeting](../retargeting/SKILL.md): warm-audience sequences
- [social-media-targeting](../social-media-targeting/SKILL.md): audience building
- [copywriting](../copywriting/SKILL.md): ad copy
- [analytics](../analytics/SKILL.md): pixels and conversions
- [cro](../cro/SKILL.md): landing pages
- [lead-magnets](../lead-magnets/SKILL.md): offers
- [influencer-marketing](../influencer-marketing/SKILL.md): Thought Leader and creator ads
- [social-media-reporting](../social-media-reporting/SKILL.md): reporting paid social
