---
name: red-hat-docs
description: Draft, rewrite, or audit modular enterprise technical documentation using an independently expressed interpretation of the Red Hat supplementary style guide. Use for administration, installation, configuration, security, troubleshooting, procedures, concepts, and references that must be precise, reusable, and supportable across product versions.
---

# Red Hat docs

Create modular enterprise documentation that makes prerequisites, system state,
actions, and verification explicit.

## Preserve product accuracy

- Keep product names, versions, commands, files, paths, options, UI labels, and
  supported configurations exact.
- Do not generalize a tested configuration into universal support.
- Separate required, recommended, optional, deprecated, and unsupported behavior.
- Ask for missing privilege, platform, version, and persistence facts.

## Build one module at a time

Choose one dominant module type:

- Concept: provide the mental model and relationships needed for later decisions.
- Procedure: state prerequisites, perform one goal-directed sequence, and verify it.
- Reference: present facts, options, syntax, or limits in a consistent lookup form.
- Troubleshooting: identify a symptom, diagnostic evidence, cause, and recovery.

Do not mix several independent goals in one procedure. Link modules into a larger
assembly when a workflow needs multiple goals.

## Write direct technical prose

- Address the reader as `you` only when they act. Name the system or component
  when it acts.
- Prefer active voice and concrete verbs. Avoid hiding actions inside abstract nouns.
- Keep terminology stable and match authoritative product capitalization.
- Put a condition before an instruction when the reader must check it first.
- State scope: host, cluster, namespace, user, service, session, or persistent configuration.
- Use literal, globally understandable language and define unfamiliar abbreviations.
- State security and data consequences without alarmism or euphemism.

## Write a procedure

1. Give the goal in one sentence.
2. List prerequisites, permissions, and starting state.
3. Start each step with an imperative verb and keep one main action per step.
4. Show commands and configuration exactly. Explain placeholders and variables.
5. State the expected result where it helps the reader continue safely.
6. Add a verification section with an observable success condition.
7. Add reversal, cleanup, or recovery when the change is persistent or risky.

## Avoid

- blending concept, procedure, and reference content without clear boundaries
- vague pronouns when several components or files are in scope
- anthropomorphism, idioms, marketing language, and ornamental prose
- difficulty judgments and reassuring claims without evidence
- unexplained root privileges, environment variables, paths, or reboot requirements
- examples that contain real credentials or unsafe defaults
- claims about support or compatibility without an explicit scope

## Final pass

Check modularity, prerequisites, platform and version scope, command accuracy,
observable results, security implications, and recovery. Remove any background that
does not help the reader make a decision or complete the module's goal.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
