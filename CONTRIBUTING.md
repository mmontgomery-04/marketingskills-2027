# Contributing

Thanks for helping improve these skills.

## Propose a new skill
Open an issue with the **New skill** template first, explaining the job it does and how it differs from existing skills.

## Improve an existing skill
1. Fork and branch: `git checkout -b skill/<name>-<change>`.
2. Edit `skills/<name>/SKILL.md` and/or its `references/`.
3. Update `evals/evals.json` if behavior changes.
4. Run:
   ```
   python3 scripts/validate_skills.py
   python3 -m unittest discover tests
   ```
5. Bump `metadata.version` and add a line to `VERSIONS.md`.
6. Open a pull request using the template.

## Standards
- Practical over theoretical: checklists, templates, and decision rules an agent can act on.
- Cite or flag claims that depend on platform specifics; mark benchmarks as directional.
- Plain language. No buzzwords.
- Ethical marketing only: no fake reviews, undisclosed paid endorsements, spam tactics, or privacy-violating data practices.
