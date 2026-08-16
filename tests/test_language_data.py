"""Integrity checks for the canonical language data (language.json)."""

import re
from pathlib import Path

import pytest

from conlang_tools.constants import (
    ASPECTS,
    ATOMIC_WORDS,
    CONSONANTS,
    CORE_ROOTS,
    DOMAINS,
    FINAL_CONSONANTS,
    HEAD_KINDS,
    NUMERAL_BASE,
    NUMERIC_VOWELS,
    PARTICLE_SERIES,
    VOWELS,
)

SPEC = (Path(__file__).parent.parent / "docs" / "spec.md").read_text(encoding="utf-8").lower()


def _normalized(text):
    """Compare semantic labels while ignoring Markdown punctuation."""
    return " ".join(re.findall(r"[a-z0-9]+", text.lower()))


def _bold_rows(form):
    marker = f"**{form.lower()}**"
    return [line for line in SPEC.splitlines() if marker in line]


def _assert_semantic_label_on_bold_row(form, meaning):
    rows = _bold_rows(form)
    assert rows, f"{form} has no bolded row in spec.md"
    expected = set(_normalized(meaning).split())
    assert any(expected <= set(_normalized(row).split()) for row in rows), (
        f"{form} is documented, but its canonical meaning {meaning!r} is not on that row"
    )


def test_inventories():
    assert CONSONANTS == "PBMFVTDNQSZLCWXJKGRH"
    assert len(set(CONSONANTS)) == 20
    assert VOWELS == "IYEAOU"
    assert NUMERIC_VOWELS == "IYEAO"
    assert NUMERAL_BASE == len(CONSONANTS) * len(NUMERIC_VOWELS) == 100
    assert FINAL_CONSONANTS == "MTNSLR"
    assert list(HEAD_KINDS) == list(FINAL_CONSONANTS)
    assert set(DOMAINS) == set(VOWELS)
    assert set(ASPECTS) == set(VOWELS)


def test_core_roots_cover_matrix_exactly_once():
    cells = {(r["domain"], r["aspect"]) for r in CORE_ROOTS.values()}
    assert len(CORE_ROOTS) == 36
    assert len(cells) == 36, "two core roots occupy the same domain x aspect cell"


@pytest.mark.parametrize("root,info", CORE_ROOTS.items())
def test_root_shape_and_coordinates(root, info):
    assert len(root) == 4
    c1, v1, c2, v2 = root
    assert c1 in CONSONANTS and c2 in CONSONANTS
    assert v1 in VOWELS and v2 in VOWELS
    # the declared cell must match the vowels actually in the root
    assert info["domain"] == v1
    assert info["aspect"] == v2


@pytest.mark.parametrize("series,particles", PARTICLE_SERIES.items())
def test_series_use_own_consonant_and_full_vowel_scale(series, particles):
    assert list(particles) == [series + v for v in VOWELS]


def test_spec_documents_every_canonical_form():
    """Inventory drift alarm for language.json versus docs/spec.md."""
    missing = [r for r in CORE_ROOTS if f"**{r.lower()}**" not in SPEC]
    assert not missing, f"roots in language.json but not bolded in spec.md: {missing}"
    missing = [
        form
        for particles in PARTICLE_SERIES.values()
        for form in particles
        if f"**{form.lower()}**" not in SPEC
    ]
    assert not missing, f"particles in language.json but not bolded in spec.md: {missing}"
    missing = [form for form in ATOMIC_WORDS if f"**{form.lower()}**" not in SPEC]
    assert not missing, f"fixed atomic words in language.json but not bolded in spec.md: {missing}"


def test_spec_preserves_canonical_semantic_labels():
    """A form-only check cannot catch a documented meaning changing underneath it."""
    for suffix, (meaning, _gloss) in HEAD_KINDS.items():
        _assert_semantic_label_on_bold_row(f"-{suffix}", meaning)

    for vowel, (meaning, _gloss) in DOMAINS.items():
        assert f"**{vowel.lower()} = {meaning.lower()}**" in SPEC
    for vowel, (meaning, _gloss) in ASPECTS.items():
        assert f"**{vowel.lower()} = {meaning.lower()}**" in SPEC

    for root, info in CORE_ROOTS.items():
        _assert_semantic_label_on_bold_row(root, info["gloss"])

    for particles in PARTICLE_SERIES.values():
        for form, (meaning, _gloss) in particles.items():
            _assert_semantic_label_on_bold_row(form, meaning)

    for form, (meaning, _gloss) in ATOMIC_WORDS.items():
        _assert_semantic_label_on_bold_row(form, meaning)


def test_ru_is_only_a_path_frame_closer():
    meaning, gloss = PARTICLE_SERIES["R"]["RU"]
    assert meaning == "path-frame closer"
    assert "closes a G-oriented path phrase" in gloss
    assert "orientation comes from the G-series" in gloss
