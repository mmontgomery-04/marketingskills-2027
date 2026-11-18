---
name: retargeting
description: "Plans and optimizes cross-channel retargeting (remarketing) for B2B: audience segments by behavior and recency, sequenced creative by page or content viewed, frequency caps, exclusions and burn pixels, CRM list retargeting, and setup on Google Ads, LinkedIn, Meta, YouTube, and Microsoft Ads, within consent and privacy limits. Use when the user mentions retargeting, remarketing, re-engaging website visitors, warm audiences, abandoned demo or trial flows, or sequential ads."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Retargeting

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

Retargeting reaches people who already showed interest: site visitors, content engagers, video viewers, event attendees, and known contacts. It usually produces the most efficient paid conversions, but only when audiences are segmented by intent and the creative moves people to the next step.

## Workflow

### 1. Check tracking and consent
You need the LinkedIn Insight Tag, Meta Pixel with Conversions API, and Google tag installed through [analytics](../analytics/SKILL.md), firing only after consent where consent is required (Consent Mode v2 for EEA/UK traffic). Expect cookie-based audiences to be smaller than raw traffic because of browser restrictions and consent opt-outs, which is why CRM lists and on-platform engagement audiences matter more each year.

### 2. Build intent-based segments
Use [audience-segments.md](references/audience-segments.md). Group by what people did (pricing page, demo page, blog, case study, video) and how recently they did it. A pricing-page visitor from last week deserves a different ad from someone who read one blog post two months ago.

### 3. Sequence the creative
Map each segment to the next logical step with [sequencing.md](references/sequencing.md). Blog readers get a deeper guide or webinar, case study readers get a demo-oriented proof ad, pricing visitors get objection handling and a demo or trial CTA.

### 4. Set frequency and exclusions
Cap frequency so warm prospects don't get annoyed, exclude converters and current customers (unless it's an expansion campaign), and use burn pixels or CRM syncs so people stop seeing an offer once they've taken it.

### 5. Launch per platform
Platform setup notes are in [platform-setup.md](references/platform-setup.md). Keep naming consistent across platforms so reporting is easy.

### 6. Measure incrementally
Retargeting often takes credit for conversions that would have happened anyway. Judge it by cost per opportunity and pipeline, watch conversion lag, and run a holdout test (exclude a random share of the audience) when spend is significant.

## Output
A retargeting map: `segment | definition | window | platform | creative/offer | frequency cap | exclusions | KPI`, plus ad concepts per segment written with [copywriting](../copywriting/SKILL.md).

## References

Load these only when the task needs the detail:

- [Audience Segments](references/audience-segments.md)
- [Creative Sequencing](references/sequencing.md)
- [Platform Setup Notes](references/platform-setup.md)

## Related Skills

- [paid-social](../paid-social/SKILL.md): campaign structure and creative
- [paid-search](../paid-search/SKILL.md): search remarketing and Customer Match
- [social-media-targeting](../social-media-targeting/SKILL.md): audience building across layers
- [analytics](../analytics/SKILL.md): pixels, tags, and consent
- [abm](../abm/SKILL.md): target-account retargeting
- [graphic-design](../graphic-design/SKILL.md): creative for each segment
- [cro](../cro/SKILL.md): the landing pages retargeting sends to
