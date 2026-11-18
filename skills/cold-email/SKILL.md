---
name: cold-email
description: "Writes and optimizes B2B cold outbound email: first-touch emails, multi-step sequences, follow-ups, personalization at scale, subject lines, offers/CTAs, reply handling, LinkedIn and multichannel touches, and the sending infrastructure and compliance that keep cold email deliverable. Use when the user asks for cold emails, outbound sequences, SDR emails, reply-rate help, what to say when a prospect replies, or setting up cold email domains and inboxes. For finding and researching who to email, use prospecting; for opt-in nurture, use email-marketing."
metadata:
  version: 1.1.0
  author: William Montgomery
---

# Cold Email

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Gather the five inputs.** Ask only for what's missing:
   - **Recipient:** role, company, and why this person in particular
   - **Goal:** a reply, a meeting, an intro to the right person, a trial
   - **Problem:** the specific pain you remove for people in their seat
   - **Proof:** one result, customer, or credential that backs the claim
   - **Signal:** the recent event that makes now a good time (hiring, funding, new leader, a post they wrote, a stack change)

   Don't stall on gaps. Write with what you have and list what would make the email stronger.

## Principles
- **Relevance beats cleverness.** The reader should know within one line why *they* got this email.
- **Short.** 50–125 words. Readable on a phone without scrolling.
- **One low-friction ask.** An interest question ("Worth a look?") beats a calendar link on first touch.
- **No attachments or images, minimal links** on first touch (deliverability).
- **Sound like a peer who did their homework,** not a brochure. Contractions, plain words, read it out loud.
- **Make the personalization carry weight.** Delete the opening line: if the email still reads the same, the personalization was decoration. The observation should lead straight into the problem.
- **Their world first.** "You" and "your" should outnumber "I", "we", and "our". Don't open with your name, your company, or what you sell.
- **Match the seniority.**
  | Reader | Length and tone |
  |---|---|
  | C-suite / VP | Three or four sentences, peer-to-peer, no detail they didn't ask for |
  | Manager / director | A little more specifics on the problem and the result |
  | Technical buyer | Exact terms, real numbers, zero hype |

## Workflow
1. Get the account and persona research from [prospecting](../prospecting/SKILL.md) (trigger, signal, pain hypothesis).
2. Pick a framework from [frameworks.md](references/frameworks.md), or pick an outbound play from [outbound-plays.md](references/outbound-plays.md) when the offer itself should do the work.
3. Write the first touch: personalized opener (trigger or observation) → problem hypothesis → proof/credibility → soft CTA.
4. Build the sequence: 4–6 touches over 2–3 weeks, each adding a new angle (case study, insight, resource, breakup). Never "just bumping this."
   - Space touches further apart as the sequence goes on.
   - Write every email so it makes sense alone; most people never read the earlier ones.
   - When you send a breakup email, mean it: no more touches in that sequence.
5. Give 3 subject lines: 2–4 words, lowercase, look internal ("q1 pipeline gaps").
6. Plan the other channels with [multichannel.md](references/multichannel.md). **Once they answer anywhere (email, LinkedIn, phone), every automated step for that person ends.**
7. Check infrastructure, monitoring, and compliance before sending: [infrastructure.md](references/infrastructure.md).
8. Handle replies with [reply-handling.md](references/reply-handling.md).

## Personalization tiers
| Tier | Use for | Example |
|---|---|---|
| 1:1 | Tier 1 accounts | Reference their podcast quote or 10-K language |
| 1:few | Clustered by trigger | "Saw you're hiring 4 SDRs…" |
| 1:many | Persona + industry | Pain specific to role + vertical |

## Quality check
Before handing over copy, confirm:
- [ ] You'd reply to it yourself if it landed in your inbox
- [ ] It passes the delete-the-opener test above
- [ ] Each sentence is there for the reader's benefit
- [ ] One proof point, not a feature list
- [ ] One ask, answerable in a single line
- [ ] Nothing from copywriting's Don'ts or the list below

## Don'ts
Everything in [copywriting's Don'ts](../copywriting/SKILL.md) applies (evidence for every claim, no AI-isms). Cold email adds:
- Openers about yourself ("My name is…", "I'm reaching out from…") or stock pleasantries ("hope your week is going well", "saw your profile and wanted to connect")
- A feature tour. One proof point lands harder than a catalog
- Asking for a 30-minute meeting in the first email
- Fake "Re:" or "Fwd:" subjects, emojis, urgency, or the prospect's first name in the subject
- The same email to everyone with only `{{first_name}}` changed
- HTML templates, images, attachments, or more than one link
- "Just following up", "bumping this", or any touch that adds nothing new

## Output
Sequence table (`step | day | channel | angle | subject | body`) and full copy. Flag any claim that needs proof.

## References

Load these only when the task needs the detail:

- [Cold Email Frameworks](references/frameworks.md)
- [Outbound Plays](references/outbound-plays.md)
- [Multichannel & LinkedIn](references/multichannel.md)
- [Cold Email Infrastructure & Compliance](references/infrastructure.md)
- [Reply Handling](references/reply-handling.md)

## Related Skills

- [prospecting](../prospecting/SKILL.md) — account research and list building
- [icp-targeting](../icp-targeting/SKILL.md) — who to target
- [copywriting](../copywriting/SKILL.md) — copy craft and the Don'ts list
- [email-marketing](../email-marketing/SKILL.md) — opt-in nurture after a reply
- [revops](../revops/SKILL.md) — sequencing tools, CRM logging, attribution
- [social-media-targeting](../social-media-targeting/SKILL.md) — account-based ads that warm up outbound
