---
name: google-developer-docs
description: Draft, rewrite, or audit developer documentation using an independently expressed interpretation of the Google developer documentation style. Use for API guides, tutorials, concepts, setup instructions, code explanations, command-line documentation, and technical content for a global developer audience.
---

# Google developer docs

Produce developer documentation that helps a reader understand or complete a
technical task without decoding the prose.

## Protect the source material

- Preserve facts, code, commands, names, URLs, prerequisites, and constraints.
- Do not invent product behavior, defaults, compatibility, or results.
- Mark a missing fact as a question or placeholder instead of guessing.
- Follow a project-specific terminology or API guide before this style.

## Plan the page

1. Identify the reader, their assumed knowledge, and the outcome they need.
2. Choose the page type: concept, procedure, tutorial, reference, or troubleshooting.
3. Put prerequisites before the first action that depends on them.
4. Lead with the outcome and the shortest useful context. Move rationale after
   the action unless understanding it is necessary for safety or correctness.
5. Decide one term for each concept and use it throughout.

## Write the prose

- Address the reader as `you` when describing their actions.
- Give every important action a visible actor and verb.
- Prefer active voice when the actor matters. Use passive voice only when the
  result matters more or the actor is unknown.
- Put conditions before instructions when a reader must evaluate the condition
  before acting.
- Keep one main idea in each sentence and one purpose in each paragraph.
- Define an unfamiliar term on first use. Expand an uncommon abbreviation once.
- Use literal, globally understandable language. Remove idioms, wordplay, and
  culture-specific comparisons from instructional content.
- Use present tense for current behavior. Attach time-sensitive claims to a
  version or date.
- State limitations directly. Do not soften them with promotional language.

## Write procedures

- Start each step with an imperative verb.
- Keep one primary action per numbered step. Put the expected result after it.
- Tell the reader where to act before naming a UI control if context is unclear.
- Provide copyable commands and code. Explain placeholders next to the example.
- Add a verification step when success is not visible.
- Add cleanup or rollback when the procedure creates persistent resources.

## Format for scanning

- Use sentence case for headings and front-load the distinguishing words.
- Use numbered lists for sequences and bullets for unordered choices.
- Use backticks for code, commands, filenames, literal values, and text to enter.
- Use bold for visible interface labels when the output format supports it.
- Use descriptive link text that states the destination or purpose.
- Introduce a table or list so the reader knows how to use it.

## Avoid

- `simply`, `easily`, `obviously`, and similar judgments about difficulty
- vague pronouns whose referent could be a service, file, command, or result
- `allows you to` when a direct action states the same fact
- unnecessary `please`, filler introductions, and recap paragraphs
- unexplained metaphors, jokes in errors, and human traits assigned to software
- swapping synonyms for variety when they name one technical concept

## Final pass

Confirm that the reader can identify the outcome, prerequisites, first action,
success signal, and next step. Then remove words that do not change meaning,
resolve ambiguous references, and test that examples still match the prose.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
