---
name: github-docs
description: Draft, rewrite, or audit approachable developer product documentation using an independently expressed interpretation of the GitHub Docs style. Use for product workflows, how-to guides, conceptual overviews, troubleshooting, security guidance, and documentation that should move developers from prerequisites to a verified outcome.
---

# GitHub docs

Help developers complete a product workflow with accurate, approachable guidance.

## Establish the contract

- Preserve commands, UI labels, permissions, plan or product availability, code,
  versions, and security consequences.
- Do not claim a feature exists for a plan, host, or version without evidence.
- Distinguish a supported workflow from a workaround or community convention.
- Surface missing facts as review questions.

## Design the page

1. Name the reader's goal in the title and opening.
2. State prerequisites, permissions, supported environments, and risks before the
   reader reaches a dependent action.
3. Give only enough concept to make the action understandable and safe.
4. Present the shortest supported path first. Place alternatives in separate sections.
5. Close the loop with verification, troubleshooting, or a useful next step.

## Write for developers

- Address the reader as `you` and keep the tone calm and collaborative.
- Use active voice and concrete verbs. Name the component that performs an automatic action.
- Define product-specific terms on first use and keep terminology stable.
- Put the most important qualifier near the claim it limits.
- Explain why a step matters when the reason affects security, data, or the choice
  between alternatives.
- Use inclusive language and examples that do not assume geography, identity, or
  a single development environment.
- Separate normative instructions from optional suggestions.

## Write procedures

- Begin steps with imperative verbs and use one main action per step.
- State the location before the control when the reader must navigate to it.
- Keep commands copyable. Explain substitutions and show the expected output only
  when it helps verify success.
- Put warnings directly before irreversible or security-sensitive actions.
- Offer recovery paths that state what data or configuration may change.

## Make the page scannable

- Use sentence case and front-load meaningful words in headings.
- Use descriptive link text instead of generic destinations.
- Use numbered lists for sequences, bullets for options, and tables for repeated
  comparisons with the same fields.
- Use backticks for code and literal technical elements. Use bold for visible UI labels.
- Keep notes exceptional. Move essential information into the main flow.

## Avoid

- assuming a step is obvious, trivial, or familiar
- long scene-setting introductions and repeated summaries
- vague references to `this`, `that`, or `it`
- blaming the reader in warnings and error explanations
- promises that a workflow is secure, fast, or reliable without scope and evidence
- examples with real personal data, tokens, organization names, or secrets

## Final pass

Walk the page as the intended reader. Verify that every prerequisite arrives in
time, every control and command is identifiable, branching is explicit, and the
reader can tell whether the workflow succeeded.

Read [references/provenance.md](references/provenance.md) only for source,
attribution, licensing, or maintenance questions.
