# Site Migration Playbook

## Before
1. Crawl and export every live URL plus GSC/GA4 top landing pages (12 months).
2. Build a 1:1 redirect map: old URL → most relevant new URL. Never redirect everything to the homepage.
3. Benchmark rankings, traffic, and conversions for the top 100 pages.
4. Keep titles, H1s, and body content stable through the move where possible: change one variable at a time.

## Launch day
- Deploy 301s, update canonicals, internal links, and sitemaps to final URLs.
- Submit new sitemaps; keep the old sitemap live for ~2 weeks so Google recrawls the redirects.
- For domain changes, use GSC's Change of Address tool.

## After (weeks 1–8)
- Monitor 404s, redirect errors, and index coverage daily for week one, then weekly.
- Compare top-100 page traffic against the benchmark; investigate any page down >30%.
- A temporary dip is normal; a sustained drop past ~8 weeks usually means a redirect or content-parity problem.
