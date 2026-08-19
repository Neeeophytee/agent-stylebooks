# Installation

Each directory in `skills/` is a complete, independent skill. Preserve its
`SKILL.md`, `agents/`, and `references/` contents when copying it.

## Portable installer

List the catalog, install one skill, or install the complete catalog:

The portable installer currently requires Node.js 22.20 or newer.

```sh
npx skills add Neeeophytee/agent-stylebooks --list
npx skills add Neeeophytee/agent-stylebooks --skill cdc-clear-communication
npx skills add Neeeophytee/agent-stylebooks
```

The first lists the catalog, the second installs one skill, and the third starts
installation for the complete catalog. Review the detected targets before
confirming changes.

## Manual project install

Copy the selected directory into the agent’s project-level skill root. For
example, Codex and other agents that read `.agents/skills/` can use:

```sh
cp -R skills/govuk /path/to/project/.agents/skills/govuk
```

Common project-level roots include:

| Agent | Project skill root |
| --- | --- |
| OpenAI Codex | `.agents/skills/` |
| Claude Code | `.claude/skills/` |
| Gemini CLI | `.gemini/skills/` |
| GitHub Copilot | `.github/skills/`, `.agents/skills/`, or `.claude/skills/` |
| Kimi Code CLI | `.kimi/skills/`, plus supported compatible roots |

Cursor and other Agent Skills clients can use their native skills directory or
the portable installer. Keep each skill as an immediate child of the destination
root; do not add an extra `house/` level.

## Codex plugin

Register the GitHub-backed marketplace and install the plugin:

```sh
codex plugin marketplace add Neeeophytee/agent-stylebooks
codex plugin add agent-stylebooks@agent-stylebooks
```

For a manual user-level installation of one skill, copy it to
`~/.agents/skills/<skill-name>/`.

## Claude Code plugin

From Claude Code, add the repository marketplace and install its plugin:

```text
/plugin marketplace add Neeeophytee/agent-stylebooks
/plugin install agent-stylebooks@agent-stylebooks
```

For a manual installation, use `.claude/skills/<skill-name>/` in a project or
`~/.claude/skills/<skill-name>/` for the user scope.

## Hermes Agent

Copy selected skill directories to `~/.hermes/skills/`, or add this repository’s
`skills/` directory to `skills.external_dirs` in Hermes configuration. Point to
`skills/`, not the repository root, so all 16 directories are direct children of
the configured collection.

## Verify an install

Ask the agent to list available skills and reconcile the names with
[STYLE-MATRIX.md](STYLE-MATRIX.md). Then run an explicit invocation:

```text
Use $gitlab-docs to rewrite this troubleshooting draft. Preserve every command.
```

The output should apply the selected editorial decisions, preserve the supplied
facts, and avoid claiming affiliation with the source organization.

[COMPATIBILITY.md](COMPATIBILITY.md) records live discovery checks separately from
format conformance. Recheck an installation route when its client changes.

## Uninstall

Remove only the copied skill directory, or use the uninstall command provided by
the plugin or portable installer. The skills do not create state elsewhere.
