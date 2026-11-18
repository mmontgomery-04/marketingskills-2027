---
name: ux-ui
description: "Reviews and improves UX and UI for marketing sites and B2B SaaS products using strategy and best practices: information architecture, navigation, usability heuristics, visual hierarchy, design systems, accessibility (WCAG), responsive and mobile design, onboarding flows, dashboards, forms, and empty states. Use when the user asks for a UX audit, UI critique, wireframe, site structure, navigation redesign, accessibility review, or design best practices."
metadata:
  version: 1.0.1
  author: William Montgomery
---

# UX & UI

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Clarify users and tasks
Who uses this page or product, and what are their top 3 tasks? Pull personas from icp-targeting. Design decisions are judged against those tasks.

### 2. Evaluate
- Usability: [heuristics.md](references/heuristics.md) (Nielsen's 10, applied to B2B)
- Patterns: [b2b-patterns.md](references/b2b-patterns.md) for marketing sites and SaaS products
- Accessibility: [accessibility.md](references/accessibility.md) (WCAG 2.2 AA)

### 3. Prioritize by severity
| Severity | Meaning |
|---|---|
| 4 – Blocker | Users can't complete a key task |
| 3 – Major | Significant friction or confusion; frequent |
| 2 – Minor | Annoying, workaround exists |
| 1 – Cosmetic | Polish |

### 4. Recommend concretely
For each issue: what's wrong, evidence (screenshot reference, heuristic, analytics), the recommended change, and a rough wireframe description or annotated layout when helpful.

### 5. Validate
Suggest the lightest validation that fits: 5-user usability test, first-click test, tree test (for IA), or an A/B test via cro.

## Principles
- Clarity over cleverness; conventions over novelty (logo top-left links home, nav top, CTA top-right).
- Hierarchy: one primary action per screen, visually dominant.
- Consistency through a design system (tokens, components, spacing scale).
- Performance is UX: fast pages convert better (technical-seo Core Web Vitals).

## References

Load these only when the task needs the detail:

- [Usability Heuristics (B2B Lens)](references/heuristics.md)
- [B2B Marketing Site & SaaS Patterns](references/b2b-patterns.md)
- [Accessibility (WCAG 2.2 AA) Essentials](references/accessibility.md)

## Related Skills

- [graphic-design](../graphic-design/SKILL.md): brand visuals and marketing graphics
- [cro](../cro/SKILL.md): conversion testing
- [copywriting](../copywriting/SKILL.md): microcopy and messaging
- [technical-seo](../technical-seo/SKILL.md): performance and Core Web Vitals
- [analytics](../analytics/SKILL.md): behavior data
- [icp-targeting](../icp-targeting/SKILL.md): personas and tasks
