#!/usr/bin/env python3
"""Validate the agent-stylebooks repository with no third-party packages."""

from __future__ import annotations

import json
import re
import sys
from urllib.parse import unquote
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
REPOSITORY_URL = "https://github.com/Neeeophytee/agent-stylebooks"
AUTHOR_NAME = "Shilpa Mitra"
EXPECTED_SKILLS = (
    "18f-content",
    "apple-interface-writing",
    "github-docs",
    "gitlab-docs",
    "google-developer-docs",
    "govuk",
    "kubernetes-docs",
    "mailchimp-content",
    "mdn-web-docs",
    "microsoft-writing-style",
    "red-hat-docs",
)
REQUIRED_ROOT_FILES = (
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    ".claude-plugin/plugin.json",
    ".codex-plugin/plugin.json",
    ".github/workflows/validate.yml",
    "AGENTS.md",
    "CLAUDE.md",
    "COMPATIBILITY.md",
    "CONTRIBUTING.md",
    "EXAMPLES.md",
    "INSTALL.md",
    "LICENSE",
    "NOTICE.md",
    "PROVENANCE.md",
    "README.md",
    "STYLE-MATRIX.md",
)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_json(path: Path, errors: list[str]) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"{path.relative_to(ROOT)}: invalid JSON: {exc}")
        return {}


def parse_frontmatter(path: Path, errors: list[str]) -> tuple[dict[str, str], str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0] != "---":
        fail(errors, f"{path.relative_to(ROOT)}: missing opening frontmatter delimiter")
        return {}, text
    try:
        closing = lines.index("---", 1)
    except ValueError:
        fail(errors, f"{path.relative_to(ROOT)}: missing closing frontmatter delimiter")
        return {}, text

    metadata: dict[str, str] = {}
    for line in lines[1:closing]:
        if not line.strip() or line.startswith((" ", "\t")) or ":" not in line:
            fail(errors, f"{path.relative_to(ROOT)}: unsupported frontmatter line: {line!r}")
            continue
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    return metadata, "\n".join(lines[closing + 1 :]).strip()


def validate_skill(name: str, errors: list[str]) -> None:
    skill_dir = SKILLS_ROOT / name
    skill_file = skill_dir / "SKILL.md"
    agent_file = skill_dir / "agents" / "openai.yaml"
    provenance_file = skill_dir / "references" / "provenance.md"

    for path in (skill_file, agent_file, provenance_file):
        if not path.is_file():
            fail(errors, f"missing required skill file: {path.relative_to(ROOT)}")
    if not skill_file.is_file():
        return

    metadata, body = parse_frontmatter(skill_file, errors)
    if set(metadata) != {"name", "description"}:
        fail(errors, f"{skill_file.relative_to(ROOT)}: frontmatter must contain only name and description")
    if metadata.get("name") != name:
        fail(errors, f"{skill_file.relative_to(ROOT)}: name must match parent directory")
    if not NAME_RE.fullmatch(name) or len(name) > 64:
        fail(errors, f"{skill_file.relative_to(ROOT)}: invalid skill name")
    description = metadata.get("description", "")
    if not 1 <= len(description) <= 1024:
        fail(errors, f"{skill_file.relative_to(ROOT)}: description must be 1-1024 characters")
    if "Use for" not in description:
        fail(errors, f"{skill_file.relative_to(ROOT)}: description must state when to use the skill")
    if not body:
        fail(errors, f"{skill_file.relative_to(ROOT)}: empty instruction body")
    if len(skill_file.read_text(encoding="utf-8").splitlines()) > 500:
        fail(errors, f"{skill_file.relative_to(ROOT)}: exceeds 500 lines")
    if "references/provenance.md" not in body:
        fail(errors, f"{skill_file.relative_to(ROOT)}: does not link its provenance reference")

    if agent_file.is_file():
        agent_text = agent_file.read_text(encoding="utf-8")
        for key in ("display_name:", "short_description:", "default_prompt:"):
            if key not in agent_text:
                fail(errors, f"{agent_file.relative_to(ROOT)}: missing {key}")
        if f"${name}" not in agent_text:
            fail(errors, f"{agent_file.relative_to(ROOT)}: default prompt must mention ${name}")
        values: dict[str, str] = {}
        for key in ("display_name", "short_description", "default_prompt"):
            match = re.search(rf'^  {key}: "([^"]+)"$', agent_text, re.MULTILINE)
            if not match:
                fail(errors, f"{agent_file.relative_to(ROOT)}: {key} must be a quoted string")
            else:
                values[key] = match.group(1)
        short_description = values.get("short_description", "")
        if short_description and not 25 <= len(short_description) <= 64:
            fail(errors, f"{agent_file.relative_to(ROOT)}: short_description must be 25-64 characters")
        default_prompt = values.get("default_prompt", "")
        if default_prompt and default_prompt.count(".") != 1:
            fail(errors, f"{agent_file.relative_to(ROOT)}: default_prompt must be one sentence")

    if provenance_file.is_file():
        provenance = provenance_file.read_text(encoding="utf-8")
        for marker in (
            "Primary source:",
            "Classification:",
            "Accessed: 2026-08-18",
            "Method:",
            "Affiliation:",
            "https://",
        ):
            if marker not in provenance:
                fail(errors, f"{provenance_file.relative_to(ROOT)}: missing {marker}")


def validate_manifests(errors: list[str]) -> None:
    codex_path = ROOT / ".codex-plugin" / "plugin.json"
    claude_path = ROOT / ".claude-plugin" / "plugin.json"
    codex = load_json(codex_path, errors)
    claude = load_json(claude_path, errors)
    for label, manifest in (("Codex", codex), ("Claude", claude)):
        if not isinstance(manifest, dict):
            fail(errors, f"{label} manifest: expected an object")
            continue
        if manifest.get("name") != "agent-stylebooks":
            fail(errors, f"{label} manifest: incorrect name")
        if not SEMVER_RE.fullmatch(str(manifest.get("version", ""))):
            fail(errors, f"{label} manifest: version must be strict semver")
        if not isinstance(manifest.get("author"), dict) or manifest["author"].get("name") != AUTHOR_NAME:
            fail(errors, f"{label} manifest: author.name must be {AUTHOR_NAME}")
        if manifest.get("license") != "MIT":
            fail(errors, f"{label} manifest: license must be MIT")
        if manifest.get("homepage") != REPOSITORY_URL:
            fail(errors, f"{label} manifest: incorrect homepage")
        if manifest.get("repository") != REPOSITORY_URL:
            fail(errors, f"{label} manifest: incorrect repository URL")

    if isinstance(codex, dict):
        if codex.get("skills") != "./skills/":
            fail(errors, "Codex manifest: skills path must be ./skills/")
        interface = codex.get("interface")
        if not isinstance(interface, dict):
            fail(errors, "Codex manifest: missing interface object")
        else:
            required = {
                "displayName",
                "shortDescription",
                "longDescription",
                "developerName",
                "category",
                "capabilities",
                "defaultPrompt",
            }
            missing = sorted(required - set(interface))
            if missing:
                fail(errors, f"Codex manifest: missing interface fields: {', '.join(missing)}")
            if interface.get("developerName") != AUTHOR_NAME:
                fail(errors, f"Codex manifest: developerName must be {AUTHOR_NAME}")
            prompts = interface.get("defaultPrompt", [])
            if not isinstance(prompts, list) or len(prompts) > 3:
                fail(errors, "Codex manifest: defaultPrompt must contain at most 3 entries")
            elif any(not isinstance(item, str) or len(item) > 128 for item in prompts):
                fail(errors, "Codex manifest: defaultPrompt entries must be strings of at most 128 characters")

    expected_paths = [f"./skills/{name}" for name in EXPECTED_SKILLS]
    if isinstance(claude, dict) and sorted(claude.get("skills", [])) != expected_paths:
        fail(errors, "Claude manifest: skill path inventory does not match the 11 expected skills")

    relative = ".claude-plugin/marketplace.json"
    data = load_json(ROOT / relative, errors)
    if not isinstance(data, dict) or data.get("name") != "agent-stylebooks":
        fail(errors, f"{relative}: incorrect marketplace name")
    if not isinstance(data, dict) or data.get("owner") != {"name": AUTHOR_NAME}:
        fail(errors, f"{relative}: owner must be {AUTHOR_NAME}")
    plugins = data.get("plugins") if isinstance(data, dict) else None
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail(errors, f"{relative}: expected exactly one plugin entry")
    elif plugins[0].get("name") != "agent-stylebooks":
        fail(errors, f"{relative}: incorrect plugin entry name")

    relative = ".agents/plugins/marketplace.json"
    data = load_json(ROOT / relative, errors)
    if not isinstance(data, dict) or data.get("name") != "agent-stylebooks":
        fail(errors, f"{relative}: incorrect marketplace name")
    plugins = data.get("plugins") if isinstance(data, dict) else None
    if not isinstance(plugins, list) or len(plugins) != 1:
        fail(errors, f"{relative}: expected exactly one plugin entry")
    else:
        plugin = plugins[0]
        if not isinstance(plugin, dict) or plugin.get("name") != "agent-stylebooks":
            fail(errors, f"{relative}: incorrect plugin entry name")
        else:
            expected_source = {
                "source": "url",
                "url": f"{REPOSITORY_URL}.git",
            }
            if plugin.get("source") != expected_source:
                fail(errors, f"{relative}: source must point to the repository-root plugin")
            expected_policy = {
                "installation": "AVAILABLE",
                "authentication": "ON_INSTALL",
            }
            if plugin.get("policy") != expected_policy:
                fail(errors, f"{relative}: incorrect policy fields")
            if plugin.get("category") != "Productivity":
                fail(errors, f"{relative}: category must be Productivity")


def validate_relative_links(errors: list[str]) -> None:
    link_re = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for path in ROOT.rglob("*.md"):
        text = path.read_text(encoding="utf-8")
        for raw_target in link_re.findall(text):
            target = raw_target.strip().split()[0].strip("<>")
            if target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative and not (path.parent / relative).resolve().exists():
                fail(errors, f"{path.relative_to(ROOT)}: broken relative link {target}")


def validate_catalog(errors: list[str]) -> None:
    actual = tuple(sorted(path.name for path in SKILLS_ROOT.iterdir() if path.is_dir()))
    if actual != EXPECTED_SKILLS:
        fail(errors, f"skill inventory mismatch: expected {EXPECTED_SKILLS}, found {actual}")

    catalog_files = ("README.md", "PROVENANCE.md", "STYLE-MATRIX.md")
    for relative in catalog_files:
        text = (ROOT / relative).read_text(encoding="utf-8")
        for name in EXPECTED_SKILLS:
            if name not in text:
                fail(errors, f"{relative}: missing catalog entry {name}")

    provenance = (ROOT / "PROVENANCE.md").read_text(encoding="utf-8")
    if provenance.count("| A |") != 8 or provenance.count("| B |") != 3:
        fail(errors, "PROVENANCE.md: expected eight A and three B classifications")
    if "| C |" in provenance:
        fail(errors, "PROVENANCE.md: unresolved class C entry present")


def main() -> int:
    errors: list[str] = []
    for relative in REQUIRED_ROOT_FILES:
        if not (ROOT / relative).is_file():
            fail(errors, f"missing required repository file: {relative}")

    if not SKILLS_ROOT.is_dir():
        fail(errors, "missing skills directory")
    else:
        validate_catalog(errors)
        for name in EXPECTED_SKILLS:
            validate_skill(name, errors)

    validate_manifests(errors)
    validate_relative_links(errors)

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if f"Copyright (c) 2026 {AUTHOR_NAME}" not in license_text:
        fail(errors, f"LICENSE: copyright holder must be {AUTHOR_NAME}")

    if (ROOT / "evals").exists():
        fail(errors, "v0.1 must not contain an evals directory")

    for path in ROOT.rglob("*"):
        if path.is_symlink():
            fail(errors, f"unexpected symbolic link: {path.relative_to(ROOT)}")
        if path.is_file() and path.stat().st_size == 0:
            fail(errors, f"empty file: {path.relative_to(ROOT)}")
        if path.is_file() and path.suffix.lower() in {".zip", ".tar", ".gz", ".pyc"}:
            fail(errors, f"generated or archive file: {path.relative_to(ROOT)}")
        if path.is_dir() and path.name in {"__pycache__", ".pytest_cache", ".mypy_cache"}:
            fail(errors, f"generated cache directory: {path.relative_to(ROOT)}")

    forbidden = (
        "[" + "TODO:",
        "REPLACE" + "_ME",
        "example" + "@example.com",
        "after this repository is " + "public",
        "once this repository is " + "public",
        "before making it " + "public",
        "review " + "repository",
        "co-authored" + "-by:",
        "generated by " + "codex",
        "created by " + "codex",
        "authored by " + "codex",
        "generated by " + "chatgpt",
        "generated by " + "openai",
    )
    for path in ROOT.rglob("*"):
        if path.is_file() and path.suffix.lower() in {".md", ".json", ".yaml", ".yml", ".py"}:
            text = path.read_text(encoding="utf-8")
            for token in forbidden:
                if token.lower() in text.lower():
                    fail(errors, f"{path.relative_to(ROOT)}: forbidden placeholder {token}")

    if errors:
        print(f"Validation failed with {len(errors)} issue(s):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Validation passed: {len(EXPECTED_SKILLS)} skills and all required repository files are present.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
