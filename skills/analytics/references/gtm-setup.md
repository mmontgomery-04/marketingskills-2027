# Google Tag Manager Implementation

## Structure
- Naming: `[Type] - [Platform] - [Description]`, e.g. `Tag - GA4 - Event - demo_request`, `Trigger - Form Success - Demo`.
- Folders per platform. Use workspaces and descriptive version notes.
- Base tags (GA4 Google Tag, LinkedIn Insight, Meta Pixel) fire on consent-aware triggers.

## Reliable form tracking
1. Best: the developer pushes a `dataLayer` event on genuine success:
```js
window.dataLayer = window.dataLayer || [];
window.dataLayer.push({ event: 'demo_request', form_name: 'demo-main', plan_interest: 'enterprise' });
```
2. HubSpot forms: listen for the `hsFormCallback` / `onFormSubmitted` message event and push to the dataLayer.
3. Avoid click triggers on submit buttons; they fire on failed validation.

## QA
Preview mode → confirm tag fires once, with correct parameters → GA4 DebugView → publish with notes → spot-check realtime reports.
