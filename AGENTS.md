# AGENTS.md

Guidance for AI agents working **in** this repository (editing skills), and a summary of how the skills are meant to be **used**.

## Using the skills
- Start with `skills/marketing-context/SKILL.md` if `.agents/marketing-context.md` doesn't exist in the user's project.
- Pick the skill whose `description` best matches the task. Follow its `Related Skills` links when the task crosses domains.
- Load files in `references/` only when the task needs that depth.

## Repository layout
| Path | Purpose |
|---|---|
| `skills/<name>/SKILL.md` | The skill: YAML frontmatter (`name`, `description`, `metadata`) + instructions |
| `skills/<name>/references/*.md` | Supporting playbooks, checklists, templates |
| `skills/<name>/evals/evals.json` | Test prompts, expected output, assertions |
| `evals/triggers/triggers.json` | Cross-skill routing tests (which skill should fire) |
| `.claude-plugin/` | Claude Code plugin + marketplace manifests |
| `.codex-plugin/` | Codex plugin manifest |
| `docs/` | Install guide, skill map, authoring guide |
| `tools/` | Notes on using skills with common marketing tools |
| `scripts/validate_skills.py` | Structural validator (run before every commit) |
| `tests/` | Unit tests wrapping the validator |

## Editing rules
1. `name` must be kebab-case and match the folder name.
2. `description` ≤ 1024 characters, says **what** the skill does and **when** to use it (include trigger phrases), and names the neighboring skill for out-of-scope requests.
3. Keep `SKILL.md` focused (under ~300 lines); move depth to `references/`.
4. Every relative link must resolve. Run `python3 scripts/validate_skills.py`.
5. Add or update evals when behavior changes. Include at least one negative eval that should route elsewhere when skills overlap.
6. Fast-changing facts (ad specs, platform features, bot names, benchmarks) must be marked as "check current docs" or "directional".
7. Bump `metadata.version` in the skill and add an entry to `VERSIONS.md`.
8. Never add advice that encourages fake reviews, undisclosed sponsorships, spam, scraping in violation of terms, or privacy violations.
