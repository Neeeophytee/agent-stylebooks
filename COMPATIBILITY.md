# Compatibility and verification

Verification date: **2026-08-18**.

This repository uses the open Agent Skills directory format. Each installable
unit is a direct child of `skills/` and contains `SKILL.md`; optional Codex UI
metadata and provenance sit below the same directory.

## Verification matrix

| Agent | Route | Verification |
| --- | --- | --- |
| OpenAI Codex 0.143.0 | Isolated project `.agents/skills/` | Live discovery check passed: all 11 names, descriptions, and paths appeared in the model-visible skill catalog |
| Hermes Agent 0.15.1 | Isolated `HERMES_HOME/skills/` | Live discovery check passed: 11 local skills listed, all enabled |
| Claude Code | `skills/<name>/`, `.claude/skills/`, and Claude plugin manifests | Format-conformant; no execution receipt recorded |
| Kimi Code CLI | Immediate child of a supported skills root | Format-conformant; no execution receipt recorded |
| Cursor | Portable installer or native project skills root | Portable structure checked; no execution receipt recorded |
| GitHub Copilot | `.github/skills/`, `.agents/skills/`, or `.claude/skills/` | Format-conformant; no execution receipt recorded |
| Gemini CLI | `.gemini/skills/<name>/SKILL.md` | One-directory-deep discovery requirement satisfied; no execution receipt recorded |
| Other Agent Skills clients | `skills/<name>/SKILL.md` | Core name, description, directory, and reference rules checked by the repository validator |

The Codex and Hermes tests used isolated temporary copies and made no persistent
configuration changes.

## What these checks prove

- All 11 skills are parseable and discoverable in the two agents with live
  execution receipts.
- Every skill has a unique trigger description and a complete instruction file.
- Claude and Codex manifests point to the same 11 direct skill directories.
- The remaining clients receive the directory depth and portable frontmatter shape
  documented by their current skill loaders.

## What these checks do not prove

Discovery is not behavioral certification. Model choice, surrounding instructions,
source material, and prompt quality can change output. The skills received a manual
instruction-level synthesis audit, but v0.1 does not include multi-model A/B evals
or claim identical behavior across agents.

When adding a compatibility claim, test the current client version and record the
result here.
