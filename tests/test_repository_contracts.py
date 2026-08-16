"""Contracts for canonical-source automation and generated consumers."""

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).parents[1]


def test_ci_requires_the_committed_lockfile():
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    assert "run: uv sync --locked" in workflow


def test_canonical_language_generation_is_current():
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "language.py"), "check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_ci_checks_generation_and_web_modules():
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text()
    assert "uv run python scripts/language.py check" in workflow
    assert "node --check docs/assets/js/guide.mjs" in workflow
    assert "node --check docs/assets/js/dictionary.mjs" in workflow


def test_generated_json_consumers_are_identical():
    package_data = (
        ROOT / "src" / "conlang_tools" / "data" / "language.json"
    ).read_bytes()
    website_data = (ROOT / "docs" / "data" / "language.json").read_bytes()
    assert package_data == website_data


def test_website_consumers_load_generated_data():
    guide = (ROOT / "docs" / "assets" / "js" / "guide.mjs").read_text()
    dictionary = (ROOT / "docs" / "assets" / "js" / "dictionary.mjs").read_text()
    assert 'new URL("../../data/language.json", import.meta.url)' in guide
    assert 'new URL("../../data/language.json", import.meta.url)' in dictionary
    assert 'const CONS = "' not in guide
    assert "const ROOTS = {" not in guide


def test_published_spec_identifies_its_canonical_source():
    published = (ROOT / "docs" / "spec.md").read_text()
    canonical = (ROOT / "language" / "grammar" / "foundational.md").read_text()
    assert published.startswith(
        "<!-- Generated from language/grammar/foundational.md; do not edit. -->"
    )
    assert published.endswith(canonical)
