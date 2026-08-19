# ASD-STE100 integration recommendation

## Recommendation

Do not add an `asd-ste100-adapter` production skill in v0.2. A safe future implementation is
possible only as a bring-your-own-standard adapter that reads the user's authorized official
copy at runtime. It must never embed or reconstruct ASD-STE100 rules, dictionary entries,
tables, examples, or substantial source text.

## Why the adapter must remain external to the catalog

ASD states that ASD-STE100 is fully owned by the Aerospace, Security and Defence Industries
Association of Europe. The current standard is Issue 9, dated 15 January 2025. An official copy
can be requested without charge, but free access is not an open-content licence. ASD also says
that tools do not replace the standard and that ASD and the maintenance group do not endorse or
certify vendors that claim full compliance.

Official references:

- <https://www.asd-ste100.org/>
- <https://www.asd-ste100.org/STE_downloads.html>
- <https://www.asd-ste100.org/STE_faq.html>

Accessed: 2026-08-19.

## Proposed runtime contract

1. Require the user to supply a local path to their official Issue 9 copy. Do not download,
   commit, cache, transmit, or redistribute it.
2. Verify that the file is readable and ask the user to confirm that it is the official copy
   they are authorized to use. Record only a local checksum, issue number, and date in the
   session report; never store the document in the repository.
3. If no copy is supplied, stop the verification workflow. Offer only clearly labelled general
   controlled-English suggestions and state that STE compliance cannot be assessed.
4. If a copy is supplied, retrieve applicable rules and vocabulary directly from that file for
   the current audit. Do not rely on model memory or a bundled rule summary.
5. For every finding, cite the user-supplied issue, rule or dictionary location, and source page.
   Separate deterministic checks from judgment calls and unresolved cases.
6. Return a report that distinguishes `verified against supplied Issue 9`, `approximate general
   guidance`, and `requires qualified human review`.
7. Delete any temporary extracted text at the end of the session and never include source text
   beyond the minimum location needed to explain a finding.

## Detection and failure behavior

The adapter should fail closed when the file is missing, unreadable, the issue cannot be
identified, or the source appears incomplete. It should not fetch unofficial mirrors. A changed
checksum should require a new source confirmation. Issue 8, summaries, training slides, and
model-recalled rules must not be presented as Issue 9 verification.

## Claims the adapter must prohibit

- `ASD certified`, `STEMG approved`, or `official checker`
- `fully compliant` based on automated or model-only review
- Issue 9 verification when the supplied source is another issue
- reproduction of the official dictionary, rule tables, examples, logo, copyright notice,
  or registered mark as product branding

## Validation needed before implementation

- written licensing review of runtime parsing, temporary extraction, citations, and user reports
- threat model for confidential technical documents and the supplied standard
- tests for issue detection, missing sources, partial scans, optical-character-recognition errors,
  conflicting project terminology, and false compliance claims
- qualified STE practitioner review of audit categories and human escalation

Until those items are complete, the repository should link to this plan only and keep the
production catalog at 16 stylebooks.
