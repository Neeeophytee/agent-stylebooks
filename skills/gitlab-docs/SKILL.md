---
name: gitlab-docs
description: Draft, rewrite, or audit concise product and engineering documentation using an independently expressed interpretation of the GitLab documentation style. Use for product guides, configuration, administration, tutorials, troubleshooting, contributor docs, and technical pages that must be searchable, precise, and localization-friendly.
---

# GitLab docs

Create brief, direct product documentation that functions as a trustworthy source
of truth.

## Preserve technical truth

- Keep commands, code, product names, UI labels, versions, defaults, and results exact.
- Do not convert an implementation detail into a product promise.
- Separate confirmed behavior from a workaround, hypothesis, or planned behavior.
- Ask for missing availability, permission, or version facts instead of inventing them.

## Choose a topic type

Select one primary purpose per topic:

- Concept: explain what something is, why it matters, and how parts relate.
- Task: help the reader achieve one outcome through ordered actions.
- Reference: present fields, options, syntax, or limits in a predictable structure.
- Troubleshooting: connect a symptom to checks, causes, and recoveries.

Split a page when these purposes compete. A short context paragraph may introduce
a task, but do not bury the first action under a conceptual essay.

## Write from the customer's perspective

- Lead with what the reader can accomplish or needs to know.
- Address the reader as `you` for user actions. Name GitLab or another component
  when the product performs the action.
- Prefer active voice, but use passive voice when the actor is irrelevant and the
  result is clearer.
- Use concise, conversational sentences without chatty asides.
- Keep one term for each feature. Match the product's visible labels and casing.
- State facts and achievable outcomes. Qualify performance or security claims.
- Write for translation: use explicit subjects, literal language, and straightforward
  sentence order.

## Build tasks and troubleshooting

- Put prerequisites, permissions, and availability before the steps.
- Start steps with imperative verbs and keep each action observable.
- Explain the expected result after the action.
- Include verification when configuration changes are not immediately visible.
- For failures, begin with the symptom the reader sees. Then give checks in the
  least expensive useful order and make recovery consequences clear.
- Use fake data and reserved example domains. Never expose real credentials.

## Format consistently

- Use sentence-case headings and descriptive keywords near the beginning.
- Use backticks for code, filenames, parameters, values, short output, and errors.
- Use bold only for visible UI labels when the format permits it.
- Use ordered lists for sequences and unordered lists for independent items.
- Prefer two sentences to a semicolon or a heavily parenthetical sentence.

## Avoid

- marketing copy, unexplained superlatives, and guaranteed benefits
- `allow` or `enable` when the reader's direct action is clearer
- difficulty judgments such as `easy`, `easily`, `simple`, or `obvious`
- self-reference such as announcing what the page will explain
- vague `it`, `this`, or `they` when several referents are possible
- ornamental synonyms, idioms, cultural references, and future promises
- mixing author workflow, product workflow, and user workflow in one procedure

## Final pass

Confirm that search terms appear in the title and headings, each topic has one
purpose, prerequisites are complete, and every claim is supportable. Remove any
sentence that exists only to introduce the next sentence.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
