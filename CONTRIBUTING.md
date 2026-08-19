# Contributing

## Admission criteria

A proposed house style must have:

1. An authoritative public source maintained by the organization or community.
2. A documented source license or an explicit reference-only decision.
3. A distinct editorial system, not a short list of generic writing advice.
4. Independently written, operational instructions that change agent behavior.
5. A clear audience, artifact fit, drafting workflow, avoid list, and final check.
6. Original examples that do not reproduce the source guide's examples.

Do not add a source merely because its guide is public. Public access is not a
reuse license.

## Add a skill

1. Create `skills/<skill-name>/SKILL.md`.
2. Keep the directory and frontmatter `name` identical and in lowercase hyphen case.
3. Put all trigger guidance in the frontmatter `description`.
4. Add `agents/openai.yaml` with a matching explicit invocation.
5. Add `references/SOURCE.md` with source URLs, publisher, licence evidence, access date,
   classification, operationalized ideas, excluded source material, and non-affiliation.
   Add a short `references/provenance.md` compatibility summary.
6. Update `README.md`, `CATALOG.md`, the style matrix, provenance table, manifests, expected
   skill list in `scripts/validate_repo.py`, and examples if useful.
7. Run `python3 scripts/validate_repo.py`.

## Licensing rules

- Prefer public-domain, CC0, CC BY, OGL, and other clearly reusable sources.
- Treat share-alike sources carefully. This repository uses independently written
  rules and attribution rather than copying source expression.
- Treat non-commercial, proprietary, unclear, or restricted sources as
  reference-only. Do not paste their prose, tables, word lists, or examples.
- Record every source consulted. Do not conceal an inspiration behind a generic
  label.
- Keep trademarks and logos out of assets unless permission is explicit.

This checklist is project policy, not legal advice. Escalate uncertainty before
public release.

## Writing standard

Use imperative instructions. Replace vague rules such as "be professional" with
a testable decision: what to put first, what sentence subject to use, how to
structure a procedure, or what information an error must contain.

Keep each `SKILL.md` below 500 lines. Place provenance in `references/` so normal
skill use does not pay the context cost of licensing notes.

Use the GitHub **Request a Stylebook** form to propose a source and the **Report a
Stylebook Problem** form for interpretation, currency, licensing, or compatibility issues.
