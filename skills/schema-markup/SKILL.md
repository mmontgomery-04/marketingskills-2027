---
name: schema-markup
description: "Writes, audits, and validates schema.org structured data (JSON-LD) for rich results and entity clarity: Organization, WebSite, Article/BlogPosting, FAQPage, HowTo, Product, SoftwareApplication, Review, BreadcrumbList, Event, VideoObject, Person, and LocalBusiness. Use when the user mentions schema, structured data, JSON-LD, rich snippets, or rich results, or when an on-page or technical SEO task needs markup."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Schema Markup

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Workflow
1. **Identify the page type** and pick schema from [schema-by-page-type.md](references/schema-by-page-type.md).
2. **Use only what's visible.** Markup must describe content that users can see on the page. Never mark up fake reviews, hidden FAQs, or prices that aren't shown.
3. **Write JSON-LD** (preferred over Microdata) in the `<head>` or end of `<body>`. Start from [jsonld-templates.md](references/jsonld-templates.md).
4. **Connect entities with `@id`.** Give Organization, WebSite, and Person nodes stable `@id`s (e.g. `https://example.com/#organization`) and reference them from Article `publisher`/`author`, so engines build one knowledge graph.
5. **Validate** with Google's Rich Results Test and the Schema.org validator. Fix errors; review warnings.
6. **Monitor** Search Console → Enhancements for errors after deploy.

## Rich-result reality check
- Google limits some types: FAQ rich results show mainly for well-known government and health sites, and HowTo rich results were removed. Check Google's current "Search gallery" docs before promising any SERP feature.
- Structured data is **not required** for Google's AI Overviews/AI Mode, and there is no special "AI schema" (per Google's May 2026 guide). Use schema for eligible rich results and to describe entities accurately, not as an AI-visibility hack.
- Don't add markup for types that bring no rich result and no clear use just to "cover everything".

## Output
Ready-to-paste JSON-LD in a code block, plus a short list of required vs recommended properties still missing.

## References

Load these only when the task needs the detail:

- [Schema by Page Type](references/schema-by-page-type.md)
- [JSON-LD Templates](references/jsonld-templates.md)

## Related Skills

- [on-page-seo](../on-page-seo/SKILL.md) — the content the markup describes
- [technical-seo](../technical-seo/SKILL.md) — site-wide implementation and validation
- [ai-search](../ai-search/SKILL.md) — entity clarity for LLMs
- [event-marketing](../event-marketing/SKILL.md) — Event schema for webinars
