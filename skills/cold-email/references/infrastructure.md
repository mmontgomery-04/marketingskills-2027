# Cold Email Infrastructure & Compliance

## Infrastructure
- Never send cold email from your primary domain. Use lookalike secondary domains (e.g. `getexample.com`) that redirect to the main site.
- 2–3 inboxes per domain; ~30–50 cold sends per inbox per day max.
- SPF, DKIM, DMARC on every sending domain; custom tracking domain if tracking clicks.
- Warm new inboxes for 2–4 weeks before sending.
- Verify every email (bounce rate <2%); remove catch-alls if risky. Re-verify right before upload; lists go stale within weeks.
- Switch off open tracking and link tracking for best deliverability; measure replies and meetings instead.
- Plain text only, with a simple opt-out line ("Not relevant? Reply 'no' and I won't email again") and your postal address.

## Mailbox provider rules
Google, Yahoo, and Microsoft (Outlook.com) require authentication (SPF, DKIM, DMARC), low spam complaint rates, and easy unsubscribes, with the strictest rules for high-volume senders. Cold programs sit close to those thresholds, so treat them as hard limits. Check each provider's current sender guidelines.

## Monitoring and stop rules (directional)
- Run inbox placement tests before launch and every couple of weeks after.
- Watch domain reputation (Google Postmaster Tools, Microsoft SNDS) and blocklists.
- Pause a mailbox when bounces pass ~3%, any spam complaints show up, or reply rate drops suddenly. Find the cause before resuming.
- Rotate in fresh warmed domains instead of pushing more volume through tired ones.

## Compliance (not legal advice; confirm with counsel)
- **US (CAN-SPAM):** accurate headers and subject, physical address, clear opt-out honored within 10 business days.
- **EU/UK (GDPR/PECR):** B2B cold email may rely on legitimate interest in some cases, but rules differ by country; document your basis and offer easy opt-out.
- **Canada (CASL):** stricter, generally needing consent; conspicuous publication exemptions are narrow.

## Benchmarks (directional)
Positive reply rate 1–5% is typical; 5%+ is strong. If under 1%, fix targeting and offer before copy.
