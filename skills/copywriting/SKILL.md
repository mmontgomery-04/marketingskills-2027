---
name: copywriting
description: "Writes and edits B2B marketing copy in the right framework, style, and format for each application: homepages, landing pages, product pages, ads, emails, sales one-pagers, case studies, social posts, video scripts, and microcopy. Covers frameworks (PAS, AIDA, BAB, 4Ps, StoryBrand, JTBD), voice styles (authoritative, conversational, technical, provocative, executive), and audience-specific angles for economic buyers, champions, and technical evaluators. Use for any request to write, rewrite, punch up, or critique marketing copy, headlines, CTAs, or value propositions. All claims must have evidence or support; if not, they must not be included."
metadata:
  version: 1.1.1
  author: William Montgomery
---

# Copywriting (B2B)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Remember the Don'ts.** Read the **Don'ts** section below before drafting, and check the finished copy against it before handing it over.

## Choose before you write
Every brief needs four decisions. Ask if they're not obvious:

1. **Application:** where will this live? See [copy-by-application.md](references/copy-by-application.md) for length, structure, and rules per format.
2. **Reader:** economic buyer, champion, technical evaluator, or end user? Each cares about different things (see [b2b-frameworks.md](references/b2b-frameworks.md#writing-for-the-buying-committee)).
3. **Awareness stage:** unaware → problem-aware → solution-aware → product-aware → most aware. The less aware, the more the copy must lead with the problem.
4. **Style:** pick from [styles-and-voice.md](references/styles-and-voice.md), always subordinate to the brand voice in the context file.

## Process
1. Pull the customer's own words from the context file's Customer Language section.
2. Pick a framework that fits the format and awareness stage.
3. Write the headline and one-line value prop first. If those don't work, nothing else will.
4. Draft. Then cut 20%.
5. Run the quality checklist below.
6. Give **2–3 variants** for headlines and CTAs, each with a one-line rationale.

## Quality checklist
- [ ] Specific outcome, not a feature ("close books in 3 days", not "powerful automation")
- [ ] Every claim has evidence next to it (metric, logo, quote, third-party rating, or source); unsupported claims are cut
- [ ] One primary CTA per asset; the CTA states what happens next ("Get a 20-min demo")
- [ ] Nothing from the Don'ts below: no listed words, phrases, or structures
- [ ] Contractions, short sentences, second person (unless the brand guide says otherwise)
- [ ] Readable at ~grade 8 for business audiences, even when the topic is technical
- [ ] Every sentence earns its place. If you delete it and nothing is lost, delete it.

## Don'ts

### Claims
- **No claim without evidence.** Every claim needs support: a metric, a named customer, a quote, a third-party source, or a fact the user gave you. If there's no support, cut the claim. Don't soften it with "can help" or "up to" and keep it.
- **Never invent proof.** No made-up stats, customers, quotes, logos, awards, or ratings. Where proof is needed and missing, leave `[PROOF NEEDED: what would support this]` and flag it to the user.
- **No unsourced superlatives:** *best, leading, #1, only, first, fastest*.

### AI-isms: words
Never use: *delve, tapestry, testament, realm, landscape* (as in "the evolving landscape"), *navigate* (figuratively), *journey* (for a purchase or process), *embark, elevate, unleash, harness, foster, empower, unlock, supercharge, revolutionize, transform* (as a vague verb), *game-changer, cutting-edge, best-in-class, world-class, seamless, robust, holistic, synergy, leverage* (as a verb), *pivotal, paramount, crucial, myriad, plethora, meticulous, vibrant, bustling, intricate*.

### AI-isms: phrases
- **Openers:** "In today's fast-paced world", "In the world of…", "When it comes to…", "Imagine a world where…", "Are you tired of…?", "Look no further", "We're thrilled to announce".
- **Filler:** "It's important to note", "It's worth noting", "Let's dive in", "deep dive", "Here's the thing:", "The best part?", "At the end of the day", "take it to the next level", "Say goodbye to X and hello to Y", "Whether you're an X or a Y".
- **Endings:** "In conclusion", "In summary", a recap of what was just said, or a generic close like "Ready to take the next step?".

### AI-isms: structure
- "It's not X. It's Y." and "This isn't just X, it's Y" contrast frames.
- Groups of three by reflex, especially adjective triplets ("fast, simple, and secure").
- Em dashes as the default punctuation. Use a period or a comma.
- Rhetorical questions as openers or transitions, and colon reveals ("The result? …", "The secret: …").
- Emoji bullets, bold on every other phrase, exclamation points.
- Stacked hedges ("can potentially help").
- Every sentence the same length and rhythm. Vary it.

## Headlines
Use [headline-formulas.md](references/headline-formulas.md) for proven patterns.

## Editing someone else's copy
Return a redline table (`original | revised | why`) rather than silently rewriting. Preserve what's working.

## References

Load these only when the task needs the detail:

- [B2B Copy Frameworks](references/b2b-frameworks.md)
- [Styles & Voice](references/styles-and-voice.md)
- [Copy by Application](references/copy-by-application.md)
- [Headline Formulas](references/headline-formulas.md)

## Related Skills

- [graphic-design](../graphic-design/SKILL.md) — visual execution of the copy
- [customer-advocacy](../customer-advocacy/SKILL.md) — case studies and customer quotes
- [product-marketing](../product-marketing/SKILL.md) — positioning and messaging the copy expresses
- [cro](../cro/SKILL.md) — testing and improving converting copy
- [on-page-seo](../on-page-seo/SKILL.md) — search requirements for web copy
- [email-marketing](../email-marketing/SKILL.md) — lifecycle email copy
- [cold-email](../cold-email/SKILL.md) — outbound copy
- [paid-search](../paid-search/SKILL.md) — ad copy constraints
- [paid-social](../paid-social/SKILL.md) — ad creative
- [lead-magnets](../lead-magnets/SKILL.md) — copy for one-pagers and guides
