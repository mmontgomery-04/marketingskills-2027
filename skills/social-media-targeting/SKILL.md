---
name: social-media-targeting
description: "Defines who social content and ads reach: translating the ICP into platform audiences on LinkedIn, Meta, X, YouTube, and Reddit, including job title/function/seniority targeting, company lists and matched audiences, retargeting, lookalikes and predictive audiences, ABM audiences, exclusions, and organic audience-building. Use when the user asks how to target a specific buyer on social, build audiences, upload account lists, set up retargeting, or reach decision makers on LinkedIn or Meta."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# Social Media Targeting

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Start from the ICP
Pull firmographics, personas, and tiers from icp-targeting. Write each audience as a sentence first: "Directors+ in Finance at US companies with 200–2,000 employees in SaaS and fintech."

### 2. Build audiences by layer
| Layer | Purpose | Examples |
|---|---|---|
| **Prospecting (cold)** | Reach ICP who don't know you | Job function + seniority + company size + industry; company lists |
| **Engaged (warm)** | People who interacted | Video viewers, post engagers, lead form openers, event attendees |
| **Retargeting (hot)** | Site visitors and known leads | Pricing/demo page visitors, contact lists from the CRM |
| **Customers** | Expansion, advocacy, exclusion | CRM customer list |

Platform-by-platform options: [platform-audiences.md](references/platform-audiences.md).

### 3. Size and overlap
Keep audiences large enough for the platform to deliver efficiently (on LinkedIn, ~50K+ for cold prospecting is a common starting point; smaller ABM lists are fine with realistic expectations). Don't let audiences overlap across campaigns.

### 4. Exclusions
Always exclude: current customers (unless it's an expansion campaign), employees, competitors, open opportunities when appropriate, and recent converters.

### 5. ABM
Upload Tier 1/2 account lists as company matched audiences; sync from the CRM where possible so lists stay current. Coordinate timing with prospecting outreach.

### 6. Organic targeting
Organic posts can be "targeted" too: write to one persona per post, use language and examples from their world, engage with their creators, and build connections with ICP titles.

## Output
Audience matrix: `audience name | layer | platform | criteria | est. size | exclusions | campaign using it`.

## Privacy
Only upload lists you have a lawful basis to use, hash data through the platform's tools, and follow each platform's policies on special categories.

## References

Load these only when the task needs the detail:

- [Platform Audience Options](references/platform-audiences.md)

## Related Skills

- [retargeting](../retargeting/SKILL.md): the warm and hot audience layers
- [abm](../abm/SKILL.md): account-based programs
- [icp-targeting](../icp-targeting/SKILL.md): the source of targeting criteria
- [paid-social](../paid-social/SKILL.md): campaigns using these audiences
- [prospecting](../prospecting/SKILL.md): coordinating ABM outreach
- [social-media-strategy](../social-media-strategy/SKILL.md): organic audience building
- [analytics](../analytics/SKILL.md): pixels and retargeting data
