# Provenance and source-license audit

Last audited: **2026-08-18**.

This file records the source, stated terms, and treatment of every skill. It is a
maintainer audit trail, not legal advice.

## Classification

- **A — open source:** the authoritative source states public-domain, CC0, OGL,
  CC BY, or CC BY-SA terms. The skill still uses independently written expression.
- **B — reference only:** the guide is public, but its terms are restricted,
  non-commercial, unclear for MIT reuse, or otherwise unsuitable for copying.
- **C — unresolved:** not eligible for inclusion until the terms are resolved.

## Catalog

| Skill | Primary source | Source terms | Class | Repository treatment |
| --- | --- | --- | --- | --- |
| `google-developer-docs` | [Google developer documentation style guide](https://developers.google.com/style/) | CC BY 4.0 for page content unless noted; code samples Apache 2.0 | A | Independent operational rules; attribution and source link retained |
| `govuk` | [GOV.UK writing guidelines](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/) | Open Government Licence v3.0 for GOV.UK content unless noted | A | Independent operational rules; source and Crown attribution context retained |
| `gitlab-docs` | [GitLab documentation style guide](https://docs.gitlab.com/development/documentation/styleguide/) | Natural-language documentation under CC BY-SA 4.0 | A | Independent operational rules; no copied examples or prose |
| `github-docs` | [GitHub Docs content style guide](https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide) | GitHub Docs content under CC BY 4.0 | A | Independent operational rules; no source passages included |
| `kubernetes-docs` | [Kubernetes documentation style guide](https://kubernetes.io/docs/contribute/style/style-guide/) | Website documentation under CC BY 4.0 | A | Independent operational rules; project-specific facts minimized |
| `mdn-web-docs` | [MDN writing style guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide) | Documentation CC BY-SA 2.5 or later unless noted; code examples have separate terms | A | Independent operational rules and original examples only |
| `red-hat-docs` | [Red Hat supplementary style guide](https://github.com/redhat-documentation/supplementary-style-guide) and [Modular Documentation Project](https://github.com/redhat-documentation/modular-docs) | Both repositories state CC BY-SA 4.0 | A | Independent operational rules; no guide text or examples copied |
| `18f-content` | [18F Content Guide](https://github.com/18F/content-guide) | US public domain; worldwide CC0 dedication | A | Independent operational rules; archived source status recorded |
| `microsoft-writing-style` | [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) | Microsoft Learn terms restrict copying unless otherwise specified | B | Reference-only interpretation; no copied prose, tables, or examples |
| `mailchimp-content` | [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/) | CC BY-NC 4.0 | B | Reference-only interpretation to keep the MIT repository free of NC material |
| `apple-interface-writing` | [Apple HIG: Writing](https://developer.apple.com/design/human-interface-guidelines/writing) | No permissive content license identified for this use | B | Reference-only interpretation; no copied prose, screenshots, or examples |

## Attribution and adaptation policy

Each skill links to its primary source in `references/provenance.md`. The skill
text expresses editorial ideas as new agent instructions and uses original
organization, wording, and examples. It does not reproduce source chapters,
word lists, screenshots, logos, or distinctive example pairs.

For CC BY-SA sources, maintainers must avoid copying protectable expression into
MIT files. If a future contribution adapts source expression closely enough to
trigger share-alike terms, either rewrite it independently or place it in a
clearly marked, compatibly licensed file and update this audit.

For class B sources, consultation is limited to identifying high-level editorial
principles and factual attribution. Any proposed quotation or close adaptation
requires a new licensing review before merge.

## Non-affiliation

Source names identify the editorial system. They do not imply endorsement,
certification, sponsorship, or authorship by the named organization. See
[NOTICE.md](NOTICE.md).

## Maintenance checks

For each source audit:

1. Open every source and license link.
2. Confirm no source has added page-specific exceptions.
3. Run a similarity review against each source, especially class B and CC BY-SA.
4. Confirm attribution format with counsel or a qualified licensing reviewer if
   the project will be used commercially or distributed at scale.
5. Replace or remove any class C entry. This catalog has none.
