# Technical SEO Audit Checklist

## Crawl
- [ ] robots.txt doesn't block CSS/JS or key sections; sitemap is referenced
- [ ] No 5xx at scale; 4xx only on genuinely dead URLs
- [ ] Redirects are single-hop 301s; no chains >1 hop, no loops
- [ ] No orphan pages among indexable URLs

## Index
- [ ] Every indexable page has a self-referencing canonical
- [ ] No canonical pointing to a noindexed, redirected, or 404 URL
- [ ] XML sitemap contains only 200, indexable, canonical URLs; split at 50K URLs
- [ ] Search Console "Crawled – currently not indexed" reviewed for thin/duplicate patterns
- [ ] Faceted/parameter URLs controlled (canonical, noindex, or blocked)

## Architecture
- [ ] Money pages ≤3 clicks from home
- [ ] Descriptive, lowercase, hyphenated URLs; no session IDs
- [ ] Breadcrumbs with BreadcrumbList schema
- [ ] Hub/pillar pages link to every spoke in their cluster

## Rendering
- [ ] Titles, H1, body copy, and links exist in the server-rendered HTML
- [ ] Internal links are `<a href>` elements, not JS click handlers

## Performance (Core Web Vitals, 75th percentile field data)
- [ ] LCP ≤ 2.5s · INP ≤ 200ms · CLS ≤ 0.1
- [ ] Hero images sized, compressed (WebP/AVIF), and preloaded; below-fold lazy-loaded
- [ ] Third-party scripts (chat, tag managers, heatmaps) audited and deferred

## Misc
- [ ] HTTPS everywhere; HTTP and non-www/www consolidated
- [ ] hreflang reciprocal with x-default (if multi-region)
- [ ] Staging/dev environments noindexed and password-protected
