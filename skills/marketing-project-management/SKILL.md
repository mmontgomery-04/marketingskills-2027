---
name: marketing-project-management
description: "Plans and runs marketing projects and operations: campaign briefs, timelines planned back from launch dates, owners and approvals (RACI), sprint planning for marketing teams, request intake and prioritization, launch checklists, status reporting, retrospectives, and setups in tools like Asana, Monday.com, ClickUp, Jira, or Notion. Use when the user asks to plan a campaign timeline, organize a launch, build a marketing project plan, set up a workflow or intake process, prioritize requests, or run a retro."
metadata:
  version: 1.0.0
  author: William Montgomery
---

# Marketing Project Management

## Before You Start

1. **Load shared context.** If `.agents/marketing-context.md` exists, read it first and only ask for what's missing. If it doesn't exist, offer to run the [marketing-context](../marketing-context/SKILL.md) skill (5–10 minutes) or proceed with a few quick questions.
2. **Confirm the job.** Restate the task, the audience, and what "done" looks like in one or two sentences before producing work.
3. **Write like a person.** Any copy you produce (emails, posts, ads, pages, briefs) follows the [copywriting's Don'ts](../copywriting/SKILL.md): no em dashes, no "it's not X, it's Y" framing, no choppy fragment stacks or repetition for effect; use flowing prose in second person with contractions.

## Workflow

### 1. Start with a brief
Every project of meaningful size gets a one-page brief from [project-brief.md](references/project-brief.md) before work starts: goal, audience, deliverables, owner, budget, deadline, and how success is measured. It prevents most scope creep.

### 2. Plan backward from the launch date
List every deliverable, estimate effort, identify dependencies (copy before design, design before build, legal review before publish), and work back from the launch date. Add buffer for reviews, which usually take longer than the work. Templates are in [timelines-and-raci.md](references/timelines-and-raci.md).

### 3. Assign owners and approvers
Use a RACI so each task has one accountable owner and a short list of approvers. Too many approvers is the most common cause of missed marketing deadlines.

### 4. Choose the operating model
For ongoing teams, run two-week sprints or a Kanban board with work-in-progress limits, plus a single intake form so requests don't arrive through side channels. Details in [team-operations.md](references/team-operations.md).

### 5. Track and report
Give a short weekly status: done, in progress, at risk (with the reason and the fix), and decisions needed. Flag risks as soon as you see them rather than on the due date.

### 6. Close with a retro
After launch, review what happened against the brief's success measures and capture what to keep, stop, and try next time.

## Output
A project plan with the brief, deliverables list, timeline (as a table, or as a Gantt-style view when a tool supports it), RACI, risks, and a status report template. When the user's project tool is connected, create the tasks there with owners and dates instead of only describing them.

## References

Load these only when the task needs the detail:

- [Project Brief Template](references/project-brief.md)
- [Timelines & RACI](references/timelines-and-raci.md)
- [Team Operations](references/team-operations.md)

## Related Skills

- [product-marketing](../product-marketing/SKILL.md): launch tiers that set project scope
- [gtm-strategy](../gtm-strategy/SKILL.md): the plans being executed
- [event-marketing](../event-marketing/SKILL.md): event timelines
- [content-strategy](../content-strategy/SKILL.md): editorial workflow
- [analytics](../analytics/SKILL.md): tracking QA before launch
- [revops](../revops/SKILL.md): systems and process ownership
