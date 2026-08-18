---
name: kubernetes-docs
description: Draft, rewrite, or audit Kubernetes and cloud-native documentation using an independently expressed interpretation of Kubernetes documentation style. Use for concepts, tasks, tutorials, references, configuration, operations, and version-sensitive guidance involving clusters, workloads, APIs, kubectl, or Kubernetes resources.
---

# Kubernetes docs

Produce direct, version-aware cloud-native documentation that readers can apply
without guessing which object, namespace, context, or feature state is involved.

## Preserve operational accuracy

- Keep resource kinds, API versions, field names, commands, flags, YAML, output,
  feature states, and version boundaries exact.
- Do not promise future behavior or infer support across Kubernetes versions.
- State whether instructions affect a cluster, namespace, node, workload, or local context.
- Expose missing environment facts before drafting steps that depend on them.

## Choose the content shape

- Concept: explain a model, component, or relationship without turning it into a task.
- Task: achieve one operational outcome with prerequisites, steps, verification, and cleanup.
- Tutorial: connect several tasks into a learning path with an explicit starting state.
- Reference: document fields, syntax, or resource behavior in a stable pattern.

Keep conceptual context short in a task. Link or separate deep architecture when it
is not needed to execute safely.

## Write precisely

- Address the reader as `you`; avoid ambiguous `we`.
- Use present tense for behavior and active voice when the actor matters.
- Name the API object or component rather than using an unclear pronoun.
- Use `Kubernetes` for the system and exact resource-kind capitalization when
  referring to an API kind. Use ordinary lowercase words for general concepts.
- Define specialized terms and abbreviations where the intended audience first needs them.
- Prefer literal language that translates well. Avoid idioms and insider shorthand.
- Tie claims such as deprecated, beta, stable, or removed to a version or feature state.

## Write operational steps

- State the required cluster access, namespace, context, tools, and starting resources.
- Start each step with an imperative verb.
- Use angle-bracket placeholders in commands and explain every placeholder.
- Put filenames, paths, commands, flags, fields, and literal values in backticks.
- Show representative output only when the reader needs it to verify or diagnose.
- Include a success check and cleanup for resources created by a tutorial.
- Place cautions before commands that delete, expose, or disrupt resources.

## Avoid

- time-relative words such as `new`, `currently`, or `soon` without a version
- difficulty judgments such as `just`, `simply`, or `easy`
- future commitments and undocumented roadmaps
- `we` when it could mean the project, authors, maintainers, or reader
- unexplained slang, idioms, and human qualities assigned to components
- hiding a namespace, context, security, or persistence assumption
- examples that place secrets directly in command history or committed files

## Final pass

Confirm that the page identifies the applicable version and feature state, the
reader's starting context, every affected resource, the verification signal, and
cleanup. Check YAML and commands independently from the prose.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
