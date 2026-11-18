---
name: cold-email
description: "Writes and optimizes B2B cold outbound email: first-touch emails, multi-step sequences, follow-ups, personalization at scale, subject lines, offers/CTAs, and the sending infrastructure and compliance that keep cold email deliverable. Use when the user asks for cold emails, outbound sequences, SDR emails, reply-rate help, or setting up cold email domains and inboxes. For finding and researching who to email, use prospecting; for opt-in nurture, use email-marketing."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Cold Email

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.

## Principles
- **Relevance beats cleverness.** The reader should know within one line why *they* got this email.
- **Short.** 50–125 words. Readable on a phone without scrolling.
- **One low-friction ask.** Interest-based CTAs ("Worth a look?") beat calendar links on first touch.
- **No attachments or images, minimal links** on first touch (deliverability).
- **Write like a peer, not a brochure.** No "I hope this email finds you well."

## Workflow
1. Get the account and persona research from [prospecting](../prospecting/SKILL.md) (trigger, signal, pain hypothesis).
2. Pick a framework from [frameworks.md](references/frameworks.md).
3. Write the first touch: personalized opener (trigger or observation) → problem hypothesis → proof/credibility → soft CTA.
4. Build the sequence: 4–6 touches over 2–3 weeks, each adding a new angle (case study, insight, resource, breakup). Never "just bumping this."
5. Give 3 subject lines: 2–4 words, lowercase, look internal ("q1 pipeline gaps").
6. Check infrastructure and compliance before sending: [infrastructure.md](references/infrastructure.md).

## Personalization tiers
| Tier | Use for | Example |
|---|---|---|
| 1:1 | Tier 1 accounts | Reference their podcast quote or 10-K language |
| 1:few | Clustered by trigger | "Saw you're hiring 4 SDRs…" |
| 1:many | Persona + industry | Pain specific to role + vertical |

## Output
Sequence table (`step | day | channel | angle | subject | body`) and full copy. Flag any claim that needs proof.

## References

Load these only when the task needs the detail:

- [Cold Email Frameworks](references/frameworks.md)
- [Cold Email Infrastructure & Compliance](references/infrastructure.md)

## Related Skills

- [prospecting](../prospecting/SKILL.md) — account research and list building
- [icp-targeting](../icp-targeting/SKILL.md) — who to target
- [copywriting](../copywriting/SKILL.md) — copy craft
- [email-marketing](../email-marketing/SKILL.md) — opt-in nurture after a reply
- [revops](../revops/SKILL.md) — sequencing tools, CRM logging, attribution
