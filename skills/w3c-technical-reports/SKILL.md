---
name: w3c-technical-reports
description: Draft, restructure, or audit specification-style technical reports using an independently expressed reference-only interpretation of W3C editorial guidance. Use for protocols, standards, interoperability documents, conformance requirements, and technical specifications that must separate normative requirements from explanation and define precise, testable behavior without inventing requirements.
---

# W3C technical reports

Turn an approved technical design into a precise specification. Improve expression and
structure without creating policy, consensus, conformance criteria, or requirements.

## Establish authority and scope

- Identify the source of approved requirements and the decision body that owns them.
- Preserve requirement strength, actors, conditions, exceptions, algorithms, data types,
  error behavior, and compatibility constraints.
- Do not infer a normative requirement from an example, implementation, issue discussion,
  preference, or common practice.
- Mark unresolved decisions and contradictions as issues. Do not silently choose a behavior.
- State the document's scope, out-of-scope concerns, maturity, and intended implementations.

## Build the conceptual model

1. Identify each conformance class, implementation role, data model, and external dependency.
2. Define a term before using it to carry a requirement. Use one stable term per concept.
3. State how terms relate when they can be confused or overlap.
4. Present the processing model in an order that exposes inputs, state changes, outputs, and errors.
5. Keep implementation-specific behavior out unless the scope intentionally requires it.

## Write normative requirements

- Give each requirement an identifiable actor and one testable obligation.
- Put conditions and scope next to the behavior they constrain.
- State exceptions explicitly and identify which rule they override.
- Describe observable outcomes without prescribing an implementation method unless the method
  is itself required for interoperability or safety.
- Keep conformance requirements in normative prose. Label examples, notes, rationale, and
  implementation advice as informative.
- Do not place a requirement only in a figure, table, example, or note.

Use RFC 2119 and RFC 8174 key words only when the governing document deliberately adopts
their definitions. In that case, only the uppercase forms carry the defined meanings. Do not
upgrade ordinary advice to `MUST`, `SHOULD`, or `MAY`; preserve the strength approved by the
specification owners. Explain a deviation from a `SHOULD` requirement when the source calls for it.

## Define conformance and failure

- Name what can conform and whether conformance is full, partial, conditional, or profile-based.
- Map requirements to the applicable class or role.
- Specify invalid input, error handling, recovery, and extension behavior when approved sources do.
- Make optional features and their interoperability consequences explicit.
- Distinguish a required testable result from an informative testing suggestion.

## Make the report usable

- Separate normative and informative references. Link a citation at the claim that depends on it.
- Use stable identifiers for definitions and requirements when downstream references need them.
- Make examples minimal, internally consistent, and visibly non-normative.
- Review terminology, examples, markup, and algorithms for accessibility and internationalization.
- Avoid language-dependent parsing, cultural assumptions, and ambiguous direction or position.

## Avoid

- vague `it`, `this`, `appropriate`, `normally`, or `as needed` in a requirement
- requirements hidden in background, captions, examples, or implementation notes
- inconsistent key-word casing or casual normative vocabulary
- claims that one implementation proves interoperability or conformance
- copying W3C publication status, branding, boilerplate, or styling into a non-W3C document
- presenting this skill's output as a W3C Technical Report, standard, consensus, or endorsement

## Final pass

Trace every normative statement to an approved source decision. Check definitions, actors,
conditions, exceptions, conformance classes, cross-references, and normative key-word use.
Return missing decisions as issues rather than filling them with plausible requirements.

Read [references/SOURCE.md](references/SOURCE.md) only for source, attribution,
licensing, or maintenance questions.
