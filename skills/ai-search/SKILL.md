---
name: ai-search
description: "Improves visibility and citations in AI search and answer engines (ChatGPT, Perplexity, Gemini, Claude, Copilot, Google AI Overviews and AI Mode), also called GEO, AEO, or LLM SEO. Use when the user asks how to show up in ChatGPT, get cited by AI, track AI share of voice, optimize for AI Overviews, or write content LLMs will quote. Traditional ranking work belongs to on-page-seo and technical-seo."
metadata:
  version: 1.1.1
  author: William Montgomery
---

# AI Search (GEO / AEO)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## How AI search works (and what not to fall for)
- **Google AI Overviews / AI Mode run on the normal Search index and ranking systems.** Google's own guide ("Optimizing your website for generative AI features on Google Search", May 2026) says optimizing for them *is still SEO*. A page must be indexed and eligible for a snippet. So on-page-seo and technical-seo come first.
- Google's guide explicitly says you **don't** need: llms.txt files, content "chunking", AI-specific rewrites, special "AI schema", or manufactured ("inauthentic") brand mentions, which can backfire. Don't sell or recommend these as visibility levers.
- Other assistants (ChatGPT, Perplexity, Claude, Copilot) retrieve from web search indexes (often Bing or their own crawlers) and cite pages that answer the question clearly and are trusted elsewhere on the web. Genuine third-party mentions (reviews, communities, press, listicles) matter alongside your own site.
- Nobody publishes a stable "AI ranking algorithm". Treat tactics as hypotheses and measure.

## Workflow

### 1. Baseline visibility
**Find the fan-outs first.** AI engines break a question into many related sub-searches before they answer (Google calls this "query fan-out" in AI Mode). Map those sub-questions with AnswerThePublic (answerthepublic.com):
1. Take the root terms the user gave (e.g. "expense management"). If they gave none, use the category and core product terms from the context file, or ask for 1–3.
2. Run each root term in AnswerThePublic, set to the user's main country and language.
3. Collect the questions, prepositions ("for", "with", "without"), and comparisons ("vs", "or") it returns. These are your fan-outs.

How to sort, filter, and rewrite them: [visibility-tracking.md](references/visibility-tracking.md#finding-fan-outs-with-answerthepublic).

Then build a prompt set of 25–50 questions your ICP actually asks, drawn from the fan-outs plus sales and support questions (problem-aware, solution-aware, and comparison prompts such as "best X for Y", "X vs Y"). Run them across ChatGPT, Perplexity, Gemini, and AI Overviews. Log brand mentions, citations, position, and which sources get cited. Template: [visibility-tracking.md](references/visibility-tracking.md).

### 2. Fix the owned content
Apply [citable-content.md](references/citable-content.md). This is good writing for people first; it also happens to be easy for AI systems to quote:
- Answer the question directly near the top of each section.
- Use headings that match how buyers phrase questions.
- Include specific numbers, dates, definitions, and named entities; cite sources.
- Add comparison tables and "best for" statements where they genuinely help readers.
- Publish something only you can say: original data, first-hand experience, expert POV.
- Show freshness (real updates, not just a changed date) and a credible author.

### 3. Fix the off-site footprint
Find the third-party pages AI engines cite for your category (G2, Capterra, Reddit threads, "best of" listicles, YouTube, industry publications). Earn genuine inclusion: customer review campaigns, listicle and media outreach via digital-pr, and real community participation with disclosed affiliation. Never fake reviews, sockpuppet posts, or paid mentions without disclosure.

### 4. Technical access
- Make sure pages are indexed and snippet-eligible in Google (no `nosnippet` on pages you want in AI features).
- Decide which AI crawlers to allow in robots.txt. Search/retrieval bots (e.g. OAI-SearchBot, PerplexityBot, Claude-SearchBot) affect whether you can be cited; training bots (e.g. GPTBot, Google-Extended) are a separate choice. Blocking Google-Extended does not remove you from AI Overviews. Check each vendor's current docs, since bot names change.
- Make sure Bing indexes you (Bing Webmaster Tools); several assistants rely on it.
- Server-render key content.
- llms.txt: optional. Google says Search doesn't use it and studies show AI search crawlers rarely fetch it. It's mainly useful for developer documentation read by coding agents.
- Keep normal schema (Organization, Product, Article) for rich results and entity clarity. There is no special "AI schema".

### 5. Re-measure monthly
Re-run the same prompt set; report share of voice and citation changes. Use Search Console's generative AI performance reporting where available. AI referral traffic shows up in GA4 as referrals from chatgpt.com, perplexity.ai, gemini.google.com, copilot.microsoft.com, claude.ai, and similar.

## Output
A scorecard (prompt × engine × mentioned/cited/absent), the top 10 content fixes, and a list of target third-party sources.

## References

Load these only when the task needs the detail:

- [Writing Citable Content for LLMs](references/citable-content.md)
- [AI Visibility Tracking](references/visibility-tracking.md)

## Related Skills

- [customer-advocacy](../customer-advocacy/SKILL.md) — reviews and customer stories AI cites
- [on-page-seo](../on-page-seo/SKILL.md) — the page fundamentals AI retrieval still relies on
- [schema-markup](../schema-markup/SKILL.md) — entity and FAQ markup
- [digital-pr](../digital-pr/SKILL.md) — earning mentions on the sources LLMs cite
- [competitor-research](../competitor-research/SKILL.md) — seeing who gets cited instead of you
- [analytics](../analytics/SKILL.md) — tracking AI referral traffic
