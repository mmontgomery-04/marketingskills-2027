---
name: on-page-seo
description: "Optimizes individual pages and blog posts to rank in search and get cited by LLMs: title tags, H1s, meta descriptions, header structure, keyword coverage, intros, TOCs, FAQs, image naming, internal/outbound links, and '10x' content upgrades. Use when the user asks to optimize a blog post, write an SEO brief, fix titles/metas, outrank competitors for a keyword, or review a page's on-page SEO. For crawl/indexing/site speed use technical-seo; for LLM citation strategy use ai-search."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# On-Page SEO

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Inputs to collect
- Target page URL or draft, **primary keyword**, 2–5 secondary/related keywords
- The top 3–4 ranking URLs for the primary keyword (or ask the user to paste them)
- People Also Ask (PAA) questions and any Semrush/Ahrefs question data
- Page type: pillar (~2.5K–3K words), sub-blog (~1K–1.5K words), landing page, or product page

## Workflow

### 1. SERP analysis
Look at the top 3–4 results. Note title patterns, H2 coverage, format (listicle, guide, comparison), content length, and what they all miss. Gaps become your differentiation.

### 2. Run the checklist
Work through [blog-checklist.md](references/blog-checklist.md) element by element: title tag → H1 → meta description → intro → TOC → headers → formatting → length → keyword coverage → image naming → linking → FAQs.

### 3. 10x the page
Apply [10x-framework.md](references/10x-framework.md): be the most comprehensive, most authoritative, easiest to understand, most visual, with the best title and the widest FAQ net.

### 4. Approachability pass
Optimizing for bots doesn't mean writing like one. Strip fluff and buzzwords, use contractions, speak to the reader in second person (if the brand guide allows), and chunk walls of text.

### 5. Deliver
Output an **SEO brief or a redline**, not an essay:

| Element | Current | Recommended | Why |
|---|---|---|---|

Then list the top 5 priority fixes in order of impact.

## Non-negotiables
- Primary keyword near the front of the title tag; describe the content plainly. Ranking beats clickbait.
- Answer the core query directly in the intro and under each question-based H2. If competitors take two sentences, take one.
- Cite an external source for every stat or third-party claim.
- Maintain brand voice, but no buzzwords, hollow claims, or "marketing speak."

## References

Load these only when the task needs the detail:

- [On-Page SEO Checklist (Blogs)](references/blog-checklist.md)
- [10x Content Framework](references/10x-framework.md)
- [Title & Meta Formulas](references/title-meta-formulas.md)

## Related Skills

- [technical-seo](../technical-seo/SKILL.md) — crawlability, indexing, and speed issues
- [ai-search](../ai-search/SKILL.md) — making the page citable by ChatGPT, Perplexity, and AI Overviews
- [schema-markup](../schema-markup/SKILL.md) — Article, FAQPage, and BreadcrumbList structured data for the page
- [content-strategy](../content-strategy/SKILL.md) — deciding which keywords and clusters to target
- [copywriting](../copywriting/SKILL.md) — voice and clarity passes
