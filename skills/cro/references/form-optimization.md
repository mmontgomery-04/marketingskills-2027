# Form Optimization

- Ask only for what you'll use now; enrich the rest. Email + company + one qualifier is often enough.
- Use business email validation instead of asking for company size and industry.
- Multi-step forms (easy questions first) often outperform one long form.
- Label every field; don't rely on placeholders.
- Inline validation with helpful error messages.
- Say what happens next ("A specialist will reply within 1 business day").
- Embed a scheduler (Chili Piper, HubSpot Meetings, Calendly) on demo forms so qualified leads book instantly.
- Privacy note near the submit button.
- Track form start → submit rate to find abandonment.

## When enrichment or routing picks the next step
Many B2B forms look up the company (HubSpot Breeze Intelligence, Clay, ZoomInfo) and then choose what to show: a scheduler for qualified leads, a thank-you page for everyone else. Build it so a slow or failed lookup never costs you the lead:
- **Save first, enrich second.** A lookup error must never drop or block a valid submission.
- **Cap the wait.** If enrichment hasn't answered within a few seconds, move on.
- **Plan for "unknown".** Give unmatched leads a useful default (the scheduler, or a clear "we'll reply within one business day"), never a spinner or a blank page.
- **Log every outcome** (qualified, not qualified, unknown, timed out) so RevOps can spot a broken lookup.
- **Re-test the flow** whenever the form tool, enrichment vendor, or routing rules change.
