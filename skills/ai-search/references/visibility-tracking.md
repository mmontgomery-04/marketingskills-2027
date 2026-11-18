# AI Visibility Tracking

## Finding fan-outs with AnswerThePublic
AnswerThePublic turns a root term into the questions and phrases people type around it, based on search autocomplete data. Those are a good stand-in for the sub-questions AI engines fan out into.

### Pick root terms
- Use the root terms the user included. Otherwise take 1–3 from the context file's category and core product terms, or ask.
- Keep them short (1–3 words) and in the buyer's words, not internal product or feature names: "expense management", not the name of your expenses module.
- Run the brand name on its own only for the Brand bucket.

### Run it
- If you can browse, run each root term on answerthepublic.com with the user's main country and language.
- If you can't reach it (sign-in, daily search limit), ask the user to run each root term and paste or export the results. The free tier caps daily searches; check current limits.

### Sort the results into buckets
| Result group | Example (root: "expense management") | Bucket |
|---|---|---|
| Questions (how, what, why, which, can) | "how does expense management software work" | Problem-aware |
| Prepositions (for, with, without) | "expense management for small business" | Category |
| Comparisons (vs, or, and) | "expense management vs accounting software" | Comparison |
| Alphabeticals and related terms | "expense management policy", "expense management app" | New root terms: rerun the promising ones |

### Filter and rewrite
- Drop results outside the ICP (consumer, jobs, students, other countries), plus duplicates and near-duplicates.
- Rewrite fragments into the full question a buyer would type to an assistant. Prompts are longer and more conversational than searches: "expense management for small business" becomes "What's the best expense management software for a 50-person company?"
- Add competitor and brand prompts from the context file; AnswerThePublic rarely surfaces smaller brands.
- Fan-out clusters with no good page on the site are content gaps: hand them to content-strategy and on-page-seo.
- Rerun AnswerThePublic quarterly to catch new questions, but keep the core prompt set stable month to month so results stay comparable.

## Prompt set design
| Bucket | Example | Share of set |
|---|---|---|
| Problem-aware | "How do startups get SOC 2 compliant fast?" | 30% |
| Category | "Best SOC 2 compliance software" | 30% |
| Comparison | "Vanta vs Drata vs [Brand]" | 25% |
| Brand | "Is [Brand] good for startups?" | 15% |

## Tracking sheet columns
`prompt | bucket | engine | date | brand mentioned (Y/N) | position in answer | brand cited URL | competitor mentions | cited sources (domains) | sentiment`

## Metrics
- **AI share of voice:** prompts where you're mentioned ÷ total prompts, per engine
- **Citation rate:** prompts where your URL is cited ÷ total prompts
- **Source gap list:** domains cited for competitors but not you
- **AI referral sessions and conversions** (GA4 custom channel group for AI referrers)

Run the same prompts monthly; answers vary run to run, so sample each prompt 2–3 times.
