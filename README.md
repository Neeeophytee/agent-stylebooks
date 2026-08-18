# Agent Stylebooks

> Pick the writing system before the model picks one for you.

Eleven installable writing systems for AI agents, based on the public editorial
guidance behind Google developer docs, GOV.UK, GitLab, GitHub, Kubernetes, MDN,
Red Hat, 18F, Microsoft, Mailchimp, and Apple.

Pick the system that fits the work. Each skill tells an agent what to lead with,
how to order information, which sentence-level choices to make, what to avoid, and
how to check the result. The goal is a defined editorial target—not a generic
“make this sound human” rewrite.

> These are community interpretations, not official vendor skills. Source names
> identify the public guides that informed each skill. No organization listed here
> endorses this repository.

## The 11 skills

| Skill | Best fit |
| --- | --- |
| `google-developer-docs` | Developer guides, tutorials, concepts, and API documentation |
| `govuk` | Public-service, policy, eligibility, and transactional content |
| `gitlab-docs` | Searchable product and engineering documentation |
| `github-docs` | Developer workflows, product help, and troubleshooting |
| `kubernetes-docs` | Versioned cloud-native concepts, tasks, and references |
| `mdn-web-docs` | Web-platform reference and learning content |
| `red-hat-docs` | Modular enterprise product documentation |
| `18f-content` | US digital-government services and forms |
| `microsoft-writing-style` | Product help, UX content, and support messages |
| `mailchimp-content` | Friendly customer education and product communication |
| `apple-interface-writing` | Labels, settings, alerts, onboarding, and UI flows |

Use one house style at a time unless the user explicitly asks for a hybrid. When
a product terminology guide conflicts with a house skill, keep the product terms
and apply the skill to structure and prose.

## Install

List the catalog or install one skill with the portable installer:

The portable installer currently requires Node.js 22.20 or newer.

```sh
npx skills add Neeeophytee/agent-stylebooks --list
npx skills add Neeeophytee/agent-stylebooks --skill govuk
```

To install the complete catalog, omit `--skill`:

```sh
npx skills add Neeeophytee/agent-stylebooks
```

Claude Code and Codex can also install the repository as a plugin through their
marketplace manifests. Manual, project-level, and agent-specific instructions are
in [INSTALL.md](INSTALL.md).

## Compatibility

Every skill uses the open `SKILL.md` format and lives directly under `skills/` so
installers and native skill loaders do not need category-specific path handling.

| Agent | Supported route |
| --- | --- |
| OpenAI Codex | Codex plugin or `.agents/skills/` |
| Claude Code | Claude plugin or `.claude/skills/` |
| Kimi Code CLI | Native Agent Skills directories or portable installer |
| Cursor | Portable installer or native project skills directory |
| Hermes Agent | `skills.external_dirs` or `~/.hermes/skills/` |
| GitHub Copilot | `.github/skills/`, `.agents/skills/`, or `.claude/skills/` |
| Gemini CLI | `.gemini/skills/` or portable installer |
| Other compatible agents | Any loader that implements the Agent Skills specification |

Compatibility means the repository follows each documented discovery shape. It
does not imply that the source organizations created or tested these skills. See
[COMPATIBILITY.md](COMPATIBILITY.md) for test evidence and [INSTALL.md](INSTALL.md)
for the exact routes.

## Use

```text
Use $google-developer-docs to turn these notes into a setup guide.
Use $govuk to rewrite this eligibility page around the user's decision.
Use $apple-interface-writing to tighten these labels and error messages.
```

Each skill can draft new content, edit an existing artifact, or audit a draft. It
must preserve facts, code behavior, legal meaning, and product terminology. It
changes presentation, not substance.

## Why skills rather than prompts

- The trigger description tells an agent when the style fits.
- The body defines a repeatable workflow and concrete editorial decisions.
- Provenance stays beside the skill but loads only for licensing or source work.
- CI checks structure, naming, manifests, provenance, and catalog consistency.

## Provenance and licensing

The source audit is in [PROVENANCE.md](PROVENANCE.md). Eight skills use guides
with public-domain or Creative Commons-style reuse terms. Three are conservative,
reference-only interpretations because their source terms are restricted or do
not clearly support an MIT adaptation.

The repository's original text and scripts are MIT licensed. Third-party source
guides retain their own terms. See [NOTICE.md](NOTICE.md). This classification is
a careful publication policy, not legal advice.

## Validate

```sh
python3 scripts/validate_repo.py
```

The validator requires only Python's standard library. CI runs the same command.

## Contribute

Read [CONTRIBUTING.md](CONTRIBUTING.md) before proposing a style. A new skill needs
an authoritative source, a licensing decision, independently written instructions,
operational rules, original examples, and validation coverage.

Version 0.1 does not claim multi-model behavioral certification. Compatibility
evidence separates structural discovery from subjective output quality.
