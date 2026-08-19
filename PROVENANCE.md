# Provenance and source-license audit

Last audited: **2026-08-19**.

This file records the authoritative source, publisher, reuse decision, and treatment of every
stylebook. It is a maintainer audit trail, not legal advice.

## Classification

- **A — open/source-grounded:** the authoritative source states public-domain, CC0, OGL,
  CC BY, CC BY-SA, or comparable reuse terms. Instructions still use original expression.
- **B — reference-only interpretation:** the guide is public, but its terms are restricted,
  non-commercial, unclear for MIT reuse, or unsuitable for derivative editorial material.
- **C — unresolved:** not eligible for inclusion until the terms are resolved.

## Catalog

| Skill | Authoritative source and publisher | Reuse classification | Operationalized; not copied |
| --- | --- | --- | --- |
| `google-developer-docs` | [Google developer documentation style guide](https://developers.google.com/style/), Google | A — CC BY 4.0 for page content unless noted; code has separate terms | Developer-doc decisions; no source examples or passages |
| `govuk` | [GOV.UK writing guidelines](https://guidance.publishing.service.gov.uk/writing-to-gov-uk-standards/writing-guidelines/), UK Government | A — Open Government Licence v3.0 unless noted | Public-service content design; no source examples or passages |
| `gitlab-docs` | [GitLab documentation style guide](https://docs.gitlab.com/development/documentation/styleguide/), GitLab | A — natural-language documentation under CC BY-SA 4.0 | Topic and product-doc decisions; no source expression |
| `github-docs` | [GitHub Docs content style guide](https://docs.github.com/en/contributing/style-guide-and-content-model/style-guide), GitHub | A — GitHub Docs content under CC BY 4.0 | Workflow and support decisions; no source passages |
| `kubernetes-docs` | [Kubernetes documentation style guide](https://kubernetes.io/docs/contribute/style/style-guide/), Kubernetes Authors | A — website documentation under CC BY 4.0 | Versioned operational decisions; no source examples |
| `mdn-web-docs` | [MDN writing style guide](https://developer.mozilla.org/en-US/docs/MDN/Writing_guidelines/Writing_style_guide), Mozilla Contributors | A — documentation CC BY-SA 2.5 or later unless noted | Web-doc and example decisions; no source examples |
| `red-hat-docs` | [Supplementary style guide](https://github.com/redhat-documentation/supplementary-style-guide) and [Modular Documentation Project](https://github.com/redhat-documentation/modular-docs), contributors | A — both repositories state CC BY-SA 4.0 | Modular-doc decisions; no guide text or examples |
| `18f-content` | [18F Content Guide](https://github.com/18F/content-guide), 18F contributors | A — US public domain and worldwide CC0 | Digital-service decisions; no source passages |
| `microsoft-writing-style` | [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/), Microsoft | B — Microsoft Learn terms restrict copying unless specified | High-level product-help principles; no prose, tables, or word lists |
| `mailchimp-content` | [Mailchimp Content Style Guide](https://styleguide.mailchimp.com/), Mailchimp | B — CC BY-NC 4.0 is not imported into the MIT repository | High-level voice decisions; no source prose or examples |
| `apple-interface-writing` | [Apple HIG: Writing](https://developer.apple.com/design/human-interface-guidelines/writing), Apple | B — no permissive content licence identified | High-level interface-writing decisions; no prose, screenshots, or examples |
| `cdc-clear-communication` | [CDC Clear Communication Index](https://www.cdc.gov/ccindex/tool/index.html), Centers for Disease Control and Prevention | A — most CDC site information is US public domain, with [agency conditions and exceptions](https://www.cdc.gov/other/agencymaterials.html) | Audience, message, action, numbers, and risk decisions; no checklist, scoring, examples, or visuals |
| `nhs-health-content` | [NHS digital service manual content guide](https://service-manual.nhs.uk/content), NHS England | B — no page-specific OGL grant was identified for the reviewed service-manual pages | Patient need, clinical boundary, urgency, inclusion; no source prose, templates, A-to-Z entries, or identity assets |
| `sec-plain-english` | [A Plain English Handbook](https://www.sec.gov/pdf/handbook.pdf) and [Plain English Disclosure](https://www.sec.gov/rules-regulations/1998/01/plain-english-disclosure), US Securities and Exchange Commission | A — handbook states it is not copyrighted | Investor structure and disclosure clarity; no handbook examples, artwork, or rule text |
| `w3c-technical-reports` | [W3C Manual of Style](https://www.w3.org/guide/manual-of-style/), World Wide Web Consortium | B — W3C Document License permits copying with notices but restricts derivative technical specifications | Normative structure, conformance, references; no W3C boilerplate, template, markup, or specification text |
| `nasa-technical-writing` | [NASA STI resources](https://sti.nasa.gov/for-sti-publishers/), National Aeronautics and Space Administration | B — public availability does not resolve contractor, grantee, third-party, or foreign rights | Technical-report evidence and traceability decisions; no source prose, templates, figures, or third-party style content |

The 11 original skill-level audits use `references/provenance.md`. The five v0.2 additions
include a full `references/SOURCE.md` record plus a compatibility provenance summary.

## New-source decisions

### CDC Clear Communication

The source model was operationalized without reproducing its 20 questions, scoring thresholds,
score sheets, or examples. CDC's reuse policy says most site material is public domain but
identifies exceptions and conditions. This repository uses attribution, a non-endorsement
statement, original expression, and no CDC logo or third-party media.

### NHS Health Content

Official NHS guidance informed the patient-need, evidence, clinical review, plain-language,
inclusion, and accessibility decisions. Some NHS sites expressly use OGL v3.0, but the reviewed
service-manual pages did not expose a clear reuse grant for their content. The conservative
reference-only decision avoids assuming that public access or pattern adaptation equals an
MIT-compatible content licence.

### SEC Plain English

The official handbook says it is not copyrighted and may be distributed freely. The skill is
still independently written and deliberately excludes contributed examples and presentation.
It adds a strong preservation workflow and repeatedly states that readable text is not legal
or securities-law compliance advice.

### W3C Technical Reports

The W3C Document License permits copying and distribution with required notices but limits
derivative technical specifications. The skill therefore uses only an independent interpretation
of general editorial decisions and cannot create W3C status, consensus, or conformance. RFC
2119/8174 are linked only to keep normative-keyword guidance accurate.

### NASA Technical Writing

NASA states that US-government employee works are generally not protected by US copyright, but
its STI can include contractor, grantee, transferred, and third-party rights. A source record's
public distribution status is not treated as permission to adapt it under MIT. The skill is an
independent evidence-and-reporting system, not NASA publication guidance or approval.

## Attribution and adaptation policy

Skill text expresses editorial ideas as new agent instructions with original organization and
wording. It does not reproduce source chapters, checklists, dictionaries, word lists, screenshots,
logos, templates, or distinctive example pairs.

For share-alike sources, maintainers avoid copying protectable expression into MIT files. For
class B sources, consultation is limited to high-level principles and factual attribution. Any
quotation, close adaptation, or classification change requires a new licensing review.

## Non-affiliation

Source names identify editorial systems. They do not imply endorsement, certification,
sponsorship, authorship, medical or legal approval, standards status, or publication review by
the named organization. See [NOTICE.md](NOTICE.md).

## Maintenance checks

1. Open every source and licence link.
2. Confirm page-specific exceptions and current publisher ownership.
3. Review similarity, especially for class B and share-alike sources.
4. Confirm attribution with a qualified licensing reviewer before commercial or large-scale use.
5. Remove any class C entry from the release catalog. This catalog has none.
