# Event Library (B2B)

## Naming
`object_action` in snake_case: `form_submit`, `demo_request`, `pricing_view`. Keep names stable; put variation in parameters.

| Event | Trigger | Key parameters | Conversion? |
|---|---|---|---|
| `generate_lead` | Any lead form success | form_name, form_type, page_type | Yes |
| `demo_request` | Demo form success | form_name, plan_interest | Yes (primary) |
| `sign_up` | Account created | method, plan | Yes |
| `trial_start` | Trial activated | plan | Yes |
| `content_download` | Gated asset delivered | asset_name, asset_type | Secondary |
| `webinar_register` | Registration success | event_name, event_date | Secondary |
| `pricing_view` | Pricing page view | plan_toggle | Micro |
| `cta_click` | Primary CTA click | cta_text, cta_location | Micro |
| `video_progress` | 25/50/75/100% | video_title, percent | Micro |
| `chat_start` | Chat opened and message sent | chat_tool | Micro |
| `meeting_booked` | Calendar booking confirmed | router, rep | Yes |

Mark 3–5 events as key events (conversions) in GA4; too many dilute bidding and reporting.
