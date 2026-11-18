# Writing a Skill

1. Copy an existing skill folder as a template.
2. Frontmatter:
   ```yaml
   ---
   name: my-skill            # matches folder
   description: "What it does. Use when ... (trigger phrases). For X, use other-skill."
   metadata:
     version: 1.0.0
     author: Your Name
   ---
   ```
3. Body: Before You Start (context) → Workflow (numbered steps) → Output format → Rules → References → Related Skills.
4. Put long checklists, templates, and examples in `references/` and link them from the body.
5. Write 2–3 evals: realistic prompts, expected output, and checkable assertions. Add a negative eval if a neighboring skill could steal the trigger.
6. Add trigger cases to `evals/triggers/triggers.json`.
7. Run the validator and tests.
