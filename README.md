# Marketing Skills 2027

**27 plug-and-play marketing skills for AI agents** (Claude Code, Claude, Codex, Cursor, and any agent that reads `SKILL.md`). Built for B2B marketers: SEO and AI search, content and copy, email and outbound, paid, social, PR, CRO, UX, analytics, and RevOps.

Created by **William (Monty) Montgomery**

## How it works

Each skill is a folder an agent can load when a task matches it:

```
skills/on-page-seo/
├── SKILL.md          # instructions + trigger description the agent reads
├── references/       # deep-dive playbooks, checklists, templates (loaded only when needed)
└── evals/evals.json  # test prompts + assertions that check the skill does its job
```

Skills share context through one file. Run **`marketing-context`** first: it writes `.agents/marketing-context.md` (product, ICP, positioning, voice, competitors) and every other skill reads it, so you never repeat yourself.

Skills are interlinked. Each `SKILL.md` ends with **Related Skills**, so an agent writing a landing page knows to pull positioning from `product-marketing`, audiences from `icp-targeting`, and test plans from `cro`. See the [skill map](docs/skill-map.md).

## Install

**Claude Code (plugin marketplace)**
```
/plugin marketplace add mmontgomery-04/marketingskills-2027
/plugin install marketing-skills-2027
```

**Any agent via the skills CLI**
```
npx skills add mmontgomery-04/marketingskills-2027
npx skills add mmontgomery-04/marketingskills-2027 --skill on-page-seo copywriting
```

**Manual:** copy any `skills/<name>/` folder into `~/.claude/skills/` (personal) or `.claude/skills/` (project).

More options: [docs/installing.md](docs/installing.md).

## Skills

### Foundation

| Skill | What it does |
|---|---|
| [marketing-context](skills/marketing-context/SKILL.md) | Creates and maintains the shared marketing context file (.agents/marketing-context.md) that every other skill in this repo reads first: company, product, ICP, positioning, voice, competitors, channels, and goals. |

### SEO & AI Search

| Skill | What it does |
|---|---|
| [on-page-seo](skills/on-page-seo/SKILL.md) | Optimizes individual pages and blog posts to rank in search and get cited by LLMs: title tags, H1s, meta descriptions, header structure, keyword coverage, intros, TOCs, FAQs, image naming, internal/outbound links, and '10x' content upgrades. |
| [technical-seo](skills/technical-seo/SKILL.md) | Audits and fixes site-level SEO: crawlability, indexation, robots.txt, XML sitemaps, canonicals, redirects, site architecture, internal link depth, Core Web Vitals, JavaScript rendering, hreflang, and site migrations. |
| [ai-search](skills/ai-search/SKILL.md) | Improves visibility and citations in AI search and answer engines (ChatGPT, Perplexity, Gemini, Claude, Copilot, Google AI Overviews and AI Mode), also called GEO, AEO, or LLM SEO. |
| [schema-markup](skills/schema-markup/SKILL.md) | Writes, audits, and validates schema.org structured data (JSON-LD) for rich results and entity clarity: Organization, WebSite, Article/BlogPosting, FAQPage, HowTo, Product, SoftwareApplication, Review, BreadcrumbList, Event, VideoObject, Person, and LocalBusiness. |

### Content & Copy

| Skill | What it does |
|---|---|
| [content-strategy](skills/content-strategy/SKILL.md) | Plans what content to create and why: topic clusters, pillar/spoke architecture, keyword-to-funnel mapping (TOFU/MOFU/BOFU), editorial calendars, content audits, refresh/prune decisions, and distribution. |
| [copywriting](skills/copywriting/SKILL.md) | Writes and edits B2B marketing copy in the right framework, style, and format for each application: homepages, landing pages, product pages, ads, emails, sales one-pagers, case studies, social posts, video scripts, and microcopy. Covers frameworks (PAS, AIDA, BAB, 4Ps, StoryBrand, JTBD), voice styles (authoritative, conversational, technical, provocative, executive), and audience-specific angles for economic buyers, champions, and technical evaluators. |
| [lead-magnets](skills/lead-magnets/SKILL.md) | Plans and builds MOFU/BOFU content assets that generate and convert leads: one-pagers, guides and ebooks, infographics, checklists, templates, calculators, benchmark reports, toolkits, assessments, and sales leave-behinds, plus gating strategy and follow-up. |

### Email & Outbound

| Skill | What it does |
|---|---|
| [email-marketing](skills/email-marketing/SKILL.md) | Plans, writes, and optimizes opt-in email marketing: welcome and onboarding sequences, lead nurture, newsletters, product announcements, re-engagement, trial-to-paid, and customer lifecycle emails, plus segmentation, deliverability, and email metrics. |
| [cold-email](skills/cold-email/SKILL.md) | Writes and optimizes B2B cold outbound email: first-touch emails, multi-step sequences, follow-ups, personalization at scale, subject lines, offers/CTAs, and the sending infrastructure and compliance that keep cold email deliverable. |
| [prospecting](skills/prospecting/SKILL.md) | Finds, researches, and prioritizes prospects for outbound: building target account and contact lists, buying signals and intent data, account research briefs, multi-threading the buying committee, and multichannel outreach cadences (email, LinkedIn, phone). |

### Strategy & Positioning

| Skill | What it does |
|---|---|
| [icp-targeting](skills/icp-targeting/SKILL.md) | Defines and operationalizes the Ideal Customer Profile and buyer personas: firmographics, technographics, trigger events, buying committee mapping, account tiering and scoring, and negative ICP. |
| [product-marketing](skills/product-marketing/SKILL.md) | Owns positioning, messaging, and product launches: positioning statements, messaging houses, value propositions, competitive differentiation, launch tiering and plans, sales enablement (pitch narratives, battlecards, one-pagers), pricing and packaging messaging, and customer research. |
| [gtm-strategy](skills/gtm-strategy/SKILL.md) | Builds go-to-market strategy and plans: market and segment selection, motion choice (product-led, sales-led, partner-led, ABM, hybrid), channel strategy, pricing go-to-market, launch plans, pipeline targets and funnel math, and GTM team alignment. |
| [competitor-research](skills/competitor-research/SKILL.md) | Researches and analyzes competitors: positioning, messaging, pricing and packaging, product features, SEO and content footprint, paid ads, reviews (G2/Capterra), social presence, and AI search visibility; then turns findings into battlecards, comparison pages, and differentiation. |

### Paid Acquisition

| Skill | What it does |
|---|---|
| [paid-search](skills/paid-search/SKILL.md) | Plans, builds, and optimizes paid search for B2B: Google Ads and Microsoft Ads strategy, account and campaign structure, keyword research and match types, negative keywords, responsive search ads, bidding strategies, Performance Max, brand and competitor campaigns, landing page alignment, offline conversion imports, and budget pacing. |
| [paid-social](skills/paid-social/SKILL.md) | Plans, launches, and optimizes paid social for B2B on LinkedIn Ads, Meta, YouTube, X, and Reddit: objectives, funnel structure, ad formats (single image, document, video, conversation, Thought Leader ads, lead gen forms), creative strategy and testing, budgets and bidding, frequency, CRM-integrated lead forms, and measurement. |

### Social

| Skill | What it does |
|---|---|
| [social-media-strategy](skills/social-media-strategy/SKILL.md) | Builds organic B2B social media strategy: platform selection (LinkedIn, X, YouTube, Instagram, TikTok, Reddit, communities), content pillars, formats, posting cadence, founder/executive and employee-led social, community engagement, and repurposing. |
| [social-media-targeting](skills/social-media-targeting/SKILL.md) | Defines who social content and ads reach: translating the ICP into platform audiences on LinkedIn, Meta, X, YouTube, and Reddit, including job title/function/seniority targeting, company lists and matched audiences, retargeting, lookalikes and predictive audiences, ABM audiences, exclusions, and organic audience-building. |
| [social-media-reporting](skills/social-media-reporting/SKILL.md) | Measures and reports organic and paid social performance: KPI selection by goal, metric definitions, dashboards, weekly/monthly/quarterly reports, benchmarking, attribution of social to pipeline (including self-reported and dark social), and insight-led recommendations. |

### Brand, PR & Community

| Skill | What it does |
|---|---|
| [digital-pr](skills/digital-pr/SKILL.md) | Plans and executes digital PR to earn media coverage, high-authority backlinks, brand mentions, and AI search citations: data-driven stories and original research, newsjacking and reactive commentary, expert sourcing (Qwoted, Featured, HARO-style requests), journalist pitching, press releases, and podcast placements. |
| [influencer-marketing](skills/influencer-marketing/SKILL.md) | Plans and runs B2B influencer and creator marketing: finding and vetting creators and niche experts (LinkedIn, YouTube, podcasts, newsletters), partnership models, briefs, compensation, contracts and FTC disclosure, employee advocacy, and measuring creator-driven pipeline. |
| [event-marketing](skills/event-marketing/SKILL.md) | Plans, promotes, runs, and follows up on B2B events: webinars, virtual summits, trade shows and conferences, field events and executive dinners, user conferences, workshops, and community meetups, including budgets, promotion plans, booth strategy, lead capture, and post-event follow-up and ROI. |

### Conversion & Experience

| Skill | What it does |
|---|---|
| [cro](skills/cro/SKILL.md) | Improves conversion rates on landing pages, homepages, pricing pages, forms, signup and demo flows, and in-product upgrade paths through audits, prioritized recommendations, and A/B testing. |
| [ux-ui](skills/ux-ui/SKILL.md) | Reviews and improves UX and UI for marketing sites and B2B SaaS products using strategy and best practices: information architecture, navigation, usability heuristics, visual hierarchy, design systems, accessibility (WCAG), responsive and mobile design, onboarding flows, dashboards, forms, and empty states. |

### Measurement & Ops

| Skill | What it does |
|---|---|
| [analytics](skills/analytics/SKILL.md) | Plans and implements marketing analytics and measurement: tracking plans, event taxonomies, GA4 setup, Google Tag Manager implementation, UTM governance, conversion tracking for ad platforms, dashboards, attribution, and turning data into decisions. |
| [revops](skills/revops/SKILL.md) | Designs and fixes revenue operations across marketing, sales, and CS: lifecycle stages (lead → MQL → SQL → opportunity → customer), lead scoring and routing, SLAs, CRM/MAP data hygiene, attribution, funnel and pipeline reporting, forecasting inputs, and GTM tech stack. |

## Quick start

1. Install the skills.
2. Ask your agent: *"Set up my marketing context."*
3. Then just ask for work: *"Write an SEO brief for 'b2b lead scoring'"*, *"Plan a LinkedIn Ads program for enterprise data leaders"*, *"Fix our MQL definition"*.

## Quality

- `python3 scripts/validate_skills.py` checks frontmatter, names, description length, every internal link, and every evals file.
- `python3 -m unittest discover tests` runs the same checks as tests.
- `evals/triggers/triggers.json` lists prompts and which skill should handle them, to catch overlap between skills.
- CI runs all of this on every pull request.

Advice is reviewed against current platform documentation (last reviewed: November 2026). Platforms change; skills tell agents to verify fast-moving specifics (ad specs, bot names, targeting options) in current docs.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Version history: [VERSIONS.md](VERSIONS.md).

## License

[MIT](LICENSE) © 2026 William Montgomery
