# Installing

## Claude Code
```
/plugin marketplace add mmontgomery-04/marketingskills-2027
/plugin install marketing-skills-2027
```

## skills CLI (Claude Code, Codex, Cursor, and other agents)
```
npx skills add mmontgomery-04/marketingskills-2027                          # all skills
npx skills add mmontgomery-04/marketingskills-2027 --skill cro copywriting  # specific skills
npx skills add mmontgomery-04/marketingskills-2027 --list                   # list skills
```

## Manual
```
git clone https://github.com/mmontgomery-04/marketingskills-2027.git
cp -r marketingskills-2027/skills/* ~/.claude/skills/
```
Project-only: copy into `.claude/skills/` (or `.agents/skills/` for agents that use that path) in your repo.

## Claude.ai / Claude desktop
Zip a single skill folder (e.g. `skills/copywriting/`) and upload it under Settings → Capabilities → Skills.

Install commands depend on each tool's current version; check its docs if a command changes.
