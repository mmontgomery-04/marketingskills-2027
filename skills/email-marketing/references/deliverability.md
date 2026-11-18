# Deliverability Essentials

- Authenticate: SPF, DKIM, and DMARC (at least `p=none` with reporting, moving toward `quarantine`). Gmail, Yahoo, and Microsoft (Outlook.com) require this for bulk senders; check each provider's current sender guidelines.
- One-click unsubscribe (RFC 8058 List-Unsubscribe header) for marketing mail; honor it within 2 days.
- Keep spam complaint rate under 0.1% (hard ceiling 0.3%) in Google Postmaster Tools.
- Send marketing mail from a subdomain (e.g. `news.example.com`) to protect the root domain's reputation.
- Sunset contacts with no engagement for 6+ months; remove hard bounces immediately.
- Warm up new domains/IPs gradually.
- Avoid image-only emails, URL shorteners, and spammy subject lines.
