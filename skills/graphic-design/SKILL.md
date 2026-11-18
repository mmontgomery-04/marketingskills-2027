---
name: graphic-design
description: "Directs and produces marketing graphic design: creative briefs, brand visual systems (color, type, imagery, layout grids), ad and social creative specs, one-pagers, infographics, slide decks, data visualization, email and web graphics, accessibility and contrast, and prompts or briefs for designers and AI design tools. Use when the user asks for a design, layout, visual, graphic, creative brief, ad creative, infographic, deck design, brand guidelines, or feedback on a visual. For product interfaces use ux-ui."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Graphic Design (Marketing)

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Brief first
Every design starts with a brief from [creative-brief.md](references/creative-brief.md): goal, audience, where it will appear, the one message, mandatory elements, specs, and deadline. Many design problems are really unclear briefs.

### 2. Apply the brand system
Use the colors, fonts, logo rules, and imagery style from the brand guidelines. If none exist, build a lightweight system with [brand-visual-system.md](references/brand-visual-system.md) before producing assets, so everything looks related.

### 3. Design for the placement
Check size, safe zones, and text limits for the platform in [specs-by-placement.md](references/specs-by-placement.md). Design for the smallest screen it will appear on, which for social and email is usually a phone.

### 4. Build the hierarchy
Decide what the viewer should see first, second, and third. One focal point, a clear headline, supporting detail, and a visible CTA or brand mark. Use whitespace generously; crowded layouts get skipped.

### 5. Check accessibility
Text contrast of at least 4.5:1 (3:1 for large text), no meaning carried by color alone, readable font sizes on mobile, and alt text for every image used on the web or in email.

### 6. Review and deliver
Use the critique checklist in [design-principles.md](references/design-principles.md). Deliver the right formats: PNG or JPG for social, SVG for logos and icons on the web, PDF for print and documents, with source files kept in a shared folder.

## When producing visuals directly
When you can create the asset yourself (HTML/CSS, SVG, slides, or a design tool), follow the brand system and specs above. When briefing a designer or an AI image or design tool, write the brief so it states the message, layout, style references, colors, and exact text, and keep text out of AI-generated images whenever exact wording matters, adding it afterward in a layout tool.

## Rules
- Use only images you have rights to: owned photography, licensed stock, or properly generated images. Never use other brands' logos, characters, or copyrighted artwork without permission.
- Copy on visuals follows the [copywriting's Don'ts](../copywriting/SKILL.md) too.
- Show real product screenshots where possible; buyers trust them more than abstract illustrations.

## References

Load these only when the task needs the detail:

- [Creative Brief Template](references/creative-brief.md)
- [Brand Visual System](references/brand-visual-system.md)
- [Specs by Placement](references/specs-by-placement.md)
- [Design Principles & Critique Checklist](references/design-principles.md)

## Related Skills

- [copywriting](../copywriting/SKILL.md): the words on every visual
- [lead-magnets](../lead-magnets/SKILL.md): one-pagers, guides, infographics
- [paid-social](../paid-social/SKILL.md): ad creative
- [social-media-strategy](../social-media-strategy/SKILL.md): organic social visuals
- [ux-ui](../ux-ui/SKILL.md): product interface design
- [event-marketing](../event-marketing/SKILL.md): booth and event graphics
- [retargeting](../retargeting/SKILL.md): creative sequences for retargeting
