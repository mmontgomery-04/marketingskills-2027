---
name: technical-seo
description: "Audits and fixes site-level SEO: crawlability, indexation, robots.txt, XML sitemaps, canonicals, redirects, site architecture, internal link depth, Core Web Vitals, JavaScript rendering, hreflang, and site migrations. Use when pages aren't indexed, traffic dropped after a redesign or migration, Search Console shows errors, the site is slow, or the user asks for a technical SEO audit. For single-page content optimization use on-page-seo."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Technical SEO

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Inputs
- Domain, CMS/framework (WordPress, Webflow, Next.js, HubSpot…), and whether JS renders content client-side
- Google Search Console access or exports (Pages/Indexing, Core Web Vitals, Sitemaps)
- A crawl export if available (Screaming Frog, Sitebulb, Ahrefs Site Audit)
- Recent changes: migration, redesign, URL changes, new CDN

## Audit order (fix in this order: each layer depends on the one before)

1. **Crawlability:** robots.txt, blocked resources, server errors (5xx), redirect chains/loops, orphan pages.
2. **Indexability:** noindex tags, canonical conflicts, duplicate content, thin/soft-404 pages, parameter bloat.
3. **Architecture:** click depth (important pages ≤3 clicks), internal links to money pages, breadcrumb trails, URL structure.
4. **Rendering:** is critical content in the initial HTML? Test with URL Inspection → View crawled page.
5. **Performance:** Core Web Vitals (LCP, INP, CLS) on field data first, lab data second.
6. **International & special cases:** hreflang, pagination, faceted navigation, staging leaks.

Use [audit-checklist.md](references/audit-checklist.md) for the item-level checks.

## Output format
Group findings by severity:

| Severity | Issue | Affected URLs | Evidence | Fix | Owner (dev/content/SEO) |
|---|---|---|---|---|---|

- **Critical:** blocks indexing of revenue pages
- **High:** wastes crawl budget or splits ranking signals at scale
- **Medium/Low:** hygiene

End with a 30/60/90-day fix plan.

## Migrations
If the user is planning or recovering from a migration, use [migrations.md](references/migrations.md).

## References

Load these only when the task needs the detail:

- [Technical SEO Audit Checklist](references/audit-checklist.md)
- [Site Migration Playbook](references/migrations.md)

## Related Skills

- [on-page-seo](../on-page-seo/SKILL.md) — page-level content and keyword optimization
- [schema-markup](../schema-markup/SKILL.md) — structured data validation
- [ai-search](../ai-search/SKILL.md) — AI crawler access decisions and Bing indexing for AI assistants
- [analytics](../analytics/SKILL.md) — measuring organic traffic recovery
- [ux-ui](../ux-ui/SKILL.md) — Core Web Vitals overlap with UX performance
