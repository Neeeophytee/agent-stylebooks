---
name: mdn-web-docs
description: Draft, rewrite, or audit web-platform documentation using an independently expressed interpretation of MDN Web Docs writing guidance. Use for HTML, CSS, JavaScript, Web API references, browser-facing concepts, tutorials, learning material, compatibility notes, and examples for web developers at a stated experience level.
---

# MDN Web Docs

Explain the web platform clearly enough that readers can transfer the knowledge
beyond a single copied example.

## Preserve platform truth

- Keep syntax, values, exceptions, standards status, browser behavior, and code exact.
- Distinguish specification requirements from observed implementation behavior.
- Do not infer compatibility. Request or link authoritative compatibility data.
- Mark experimental, deprecated, and non-standard features explicitly when known.

## Set the audience and page purpose

1. Choose the reader level and list the knowledge the page assumes.
2. Choose reference, guide, tutorial, or conceptual explanation as the primary purpose.
3. State what the feature is and why a developer would use it before deep detail.
4. Order reference information predictably; order learning content from a working
   mental model to a useful example and then edge cases.
5. Link prerequisites instead of reteaching an entire foundational topic.

## Explain clearly

- Use clear, concise, consistent terminology.
- Keep one main idea per sentence and use active voice when it clarifies the actor.
- Define an unfamiliar term before relying on it.
- Explain what code does and why the relevant line matters. Do not narrate every token.
- Use examples to reveal behavior, parameters, and edge cases, not as decoration.
- State assumptions about document structure, security context, network state, or browser support.
- Prefer inclusive, literal language and avoid jokes that obscure technical meaning.

## Build useful examples

- Make the smallest example that still demonstrates realistic behavior.
- Include all required setup or label omitted scaffolding clearly.
- Use safe placeholder data and accessible markup.
- Keep names consistent across HTML, CSS, JavaScript, and prose.
- Explain the expected result and a common failure when it adds learning value.
- Do not present a clever shortcut as the default if it harms readability or safety.

## Format the page

- Use sentence-case headings that describe the section's information.
- Use backticks for elements, attributes, properties, methods, values, and code.
- Put sequential instructions in numbered lists and independent criteria in bullets.
- Use notes sparingly. Put facts required for correct use in the main text.
- Link to the relevant specification or authoritative source when normative detail matters.

## Avoid

- assuming the reader knows an abbreviation, API family, or programming pattern
- calling a feature easy, obvious, or simple
- excessive detail that obscures the primary use or reference value
- examples that work only because of undeclared global state
- mixing opinion, recommendation, specification, and browser behavior as one claim
- repeating the same definition with different terminology

## Final pass

Confirm that the introduction identifies the feature and use, prerequisites match
the audience, examples run in the stated context, terms stay consistent, and factual
claims are separated from advice.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
