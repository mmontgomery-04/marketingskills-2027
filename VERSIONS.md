# Versions

## ai-search 1.1.0 — 2026-11-17
- Baseline visibility now starts by finding fan-outs: run the user's root terms through AnswerThePublic and build the prompt set from the results.
- `references/visibility-tracking.md` covers picking root terms, sorting results into buckets, filtering, and rewriting fragments into natural prompts.
- AnswerThePublic added to `tools/README.md`; new eval for building a prompt set from root terms.

## cro 1.1.0 — 2026-11-17
- Intake now asks for page type, what happens after the conversion, research on hand, and past tests.
- Page audit reordered by impact, with common failure points, CTA wording, proof quality, and an objection-answer table.
- New `references/page-types.md`: priorities and test ideas for homepage, landing, pricing, product, demo, and blog pages.
- Output grouped into fix now / bigger bets / test first, with 2–3 rewritten options for headline, subhead, and CTA.
- New rules: real proof only, no dark patterns.
- Form optimization covers enrichment and routing fallbacks.
- Two new evals (pricing page, enrichment routing).

## copywriting 1.1.0 — 2026-11-17
- New **Don'ts** section: no claim without evidence (cut it or flag `[PROOF NEEDED]`), never invent proof, plus banned AI-ism words, phrases, and sentence structures.
- "Remember the Don'ts" added to Before You Start; quality checklist points to the list.
- New eval for stripping AI-isms and unsupported claims.

## 1.0.0 — 2026-11-17
- Initial release: 27 skills, each with `SKILL.md`, `references/`, and `evals/evals.json`.
- Foundation skill `marketing-context` creates the shared `.agents/marketing-context.md`.
- On-page SEO checklist and 10x framework from William Montgomery's On-Page SEO Checklist.
- AI search guidance aligned with Google's May 2026 "Optimizing your website for generative AI features on Google Search" guide.
- Claude Code plugin + marketplace manifests, Codex manifest, validator, tests, CI.
