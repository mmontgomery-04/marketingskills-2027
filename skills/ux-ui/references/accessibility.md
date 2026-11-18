# Accessibility (WCAG 2.2 AA) Essentials

- Color contrast: 4.5:1 for body text, 3:1 for large text and UI components.
- Never rely on color alone to convey meaning.
- Every interactive element is keyboard reachable with a visible focus state.
- Semantic HTML: real buttons, links, headings in order (one H1), landmarks.
- Alt text for informative images; empty alt for decorative ones.
- Form fields have visible labels and programmatic association; errors are announced.
- Touch targets at least 24×24 CSS px (44×44 recommended).
- Captions for video; transcripts for audio/webinars.
- Respect `prefers-reduced-motion`.
- Test with a screen reader (VoiceOver/NVDA) and an automated checker (axe, Lighthouse); automated tools catch only part of the issues.
