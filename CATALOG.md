# Stylebook catalog

Choose by artifact, reader, and consequence. Each entry links to the executable instructions;
the install command installs only that stylebook.

## Technical & Developer Documentation

### [Google Developer Docs](skills/google-developer-docs/SKILL.md)

- **Best for:** API guides, tutorials, concepts, setup, and command-line documentation.
- **Defining characteristics:** explicit actors, stable terms, prerequisite-first procedures, global English.
- **Use when:** a developer must understand or complete a technical task.
- **Avoid when:** the artifact is a formal specification or an enterprise support module.
- **Source category:** openly licensed organizational style guide.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill google-developer-docs`

### [GitLab Docs](skills/gitlab-docs/SKILL.md)

- **Best for:** searchable product, administration, contributor, and engineering documentation.
- **Defining characteristics:** one topic type, customer perspective, precise and localization-friendly prose.
- **Use when:** product documentation must act as a concise source of truth.
- **Avoid when:** the main task is patient, public-service, or interface microcopy.
- **Source category:** openly licensed organizational style guide.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill gitlab-docs`

### [GitHub Docs](skills/github-docs/SKILL.md)

- **Best for:** developer workflows, product help, troubleshooting, and security guidance.
- **Defining characteristics:** outcome-led pages, visible prerequisites, approachable recovery paths.
- **Use when:** developers need to move from starting state to verified outcome.
- **Avoid when:** requirements, not a product workflow, are the primary artifact.
- **Source category:** openly licensed organizational style guide.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill github-docs`

### [Kubernetes Docs](skills/kubernetes-docs/SKILL.md)

- **Best for:** cluster concepts, tasks, tutorials, API resources, and versioned operations.
- **Defining characteristics:** explicit version, feature state, resource scope, verification, and cleanup.
- **Use when:** namespace, context, feature state, or version can change the result.
- **Avoid when:** the artifact is generic developer prose with no cloud-native operational state.
- **Source category:** openly licensed community documentation guide.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill kubernetes-docs`

### [MDN Web Docs](skills/mdn-web-docs/SKILL.md)

- **Best for:** HTML, CSS, JavaScript, Web API reference, and learning material.
- **Defining characteristics:** audience-aware definitions, focused examples, standards and browser distinctions.
- **Use when:** web developers must transfer knowledge beyond one copied example.
- **Avoid when:** the output defines new normative protocol behavior.
- **Source category:** openly licensed community documentation guide.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill mdn-web-docs`

### [Red Hat Docs](skills/red-hat-docs/SKILL.md)

- **Best for:** modular enterprise concepts, procedures, references, and troubleshooting.
- **Defining characteristics:** strict module type, system state, privileges, verification, and reversal.
- **Use when:** documentation must remain reusable and supportable across configurations.
- **Avoid when:** a conversational product flow or short interface string is the artifact.
- **Source category:** openly licensed enterprise documentation guides.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill red-hat-docs`

## Public Service & Health

### [GOV.UK](skills/govuk/SKILL.md)

- **Best for:** eligibility, policy, transactions, forms, and public-service guidance.
- **Defining characteristics:** user need first, decision-focused order, exact legal conditions.
- **Use when:** a person must decide, qualify, apply, or comply with a public service.
- **Avoid when:** the content needs clinical triage or patient safety-netting.
- **Source category:** Open Government Licence public-sector guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill govuk`

### [18F Content](skills/18f-content/SKILL.md)

- **Best for:** US government services, forms, applications, notices, and recovery messages.
- **Defining characteristics:** reduced administrative burden, inclusive transactions, alternative routes.
- **Use when:** service design and content must work together across success and failure.
- **Avoid when:** a house voice or technical reference is the dominant need.
- **Source category:** US public-domain and CC0 government guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill 18f-content`

### [CDC Clear Communication](skills/cdc-clear-communication/SKILL.md)

- **Best for:** public-health campaigns, risk messages, emergency notices, and health education.
- **Defining characteristics:** one primary message, visible action, meaningful numbers, contextual risk.
- **Use when:** a defined public audience must understand and act on verified health information.
- **Avoid when:** the task is individualized diagnosis or unsupported medical advice.
- **Source category:** US public-domain, source-grounded public-health guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill cdc-clear-communication`

### [NHS Health Content](skills/nhs-health-content/SKILL.md)

- **Best for:** patient information, symptoms, appointments, treatments, and digital health services.
- **Defining characteristics:** patient need, clinical boundaries, explicit urgency, uncertainty, inclusion.
- **Use when:** people need clinically careful information and an unambiguous next step.
- **Avoid when:** no verified clinical or service source is available.
- **Source category:** reference-only interpretation of official health-content guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill nhs-health-content`

## Product & UX

### [Microsoft Writing Style](skills/microsoft-writing-style/SKILL.md)

- **Best for:** product help, support, setup, errors, and technical UX content.
- **Defining characteristics:** important point first, warm direct voice, solution-oriented recovery.
- **Use when:** users need concise help that feels conversational without losing precision.
- **Avoid when:** formal conformance or regulated disclosure controls the artifact.
- **Source category:** reference-only proprietary guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill microsoft-writing-style`

### [Mailchimp Content](skills/mailchimp-content/SKILL.md)

- **Best for:** customer education, onboarding, campaigns, and brand communication.
- **Defining characteristics:** useful familiar voice, context-sensitive tone, restrained personality.
- **Use when:** clarity can support a warm brand relationship.
- **Avoid when:** failure, security, money, or compliance makes playfulness unsafe.
- **Source category:** reference-only interpretation of non-commercially licensed guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill mailchimp-content`

### [Apple Interface Writing](skills/apple-interface-writing/SKILL.md)

- **Best for:** buttons, labels, alerts, settings, onboarding, and multi-screen flows.
- **Defining characteristics:** verb-led labels, predictable consequences, minimal supporting text.
- **Use when:** language must make an action clear in limited interface space.
- **Avoid when:** the artifact needs long-form explanation or a detailed support procedure.
- **Source category:** reference-only proprietary guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill apple-interface-writing`

## Standards & Specialist Writing

### [SEC Plain English](skills/sec-plain-english/SKILL.md)

- **Best for:** investor disclosures, risk factors, offering summaries, and shareholder letters.
- **Defining characteristics:** material-fact inventory, cause-risk-consequence logic, qualification preservation.
- **Use when:** financial or legal disclosure must be clearer without becoming broader or more certain.
- **Avoid when:** qualified securities counsel is unavailable for a filing or regulated distribution.
- **Source category:** public-domain US government handbook and official rule guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill sec-plain-english`

### [W3C Technical Reports](skills/w3c-technical-reports/SKILL.md)

- **Best for:** protocols, specifications, conformance criteria, and interoperability documents.
- **Defining characteristics:** normative/informative separation, testable actors and conditions, stable terms.
- **Use when:** approved requirements must become a precise specification without new policy.
- **Avoid when:** requirements are undecided or ordinary documentation is the actual artifact.
- **Source category:** reference-only interpretation of W3C and RFC guidance.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill w3c-technical-reports`

### [NASA Technical Writing](skills/nasa-technical-writing/SKILL.md)

- **Best for:** engineering reports, test reports, experiments, design descriptions, and memoranda.
- **Defining characteristics:** reproducible methods, measurement fidelity, evidence-to-conclusion traceability.
- **Use when:** a technical record must separate observations, analysis, limitations, and recommendations.
- **Avoid when:** source measurements or test conditions are incomplete and cannot be surfaced as gaps.
- **Source category:** reference-only interpretation of official NASA STI resources.
- **Install:** `npx skills add Neeeophytee/agent-stylebooks --skill nasa-technical-writing`

## Selection rule

Choose one stylebook to govern the artifact. If a narrow secondary constraint is necessary,
state which system governs structure and which contributes the constraint. Do not blend voices
or decision systems merely because two organizations appear in the subject matter.
