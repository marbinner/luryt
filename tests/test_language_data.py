"""Integrity checks for the canonical language data (language.json)."""

from pathlib import Path

import pytest

from conlang_tools.constants import (
    ASPECTS,
    CONSONANTS,
    CORE_ROOTS,
    DOMAINS,
    FINAL_CONSONANTS,
    HEAD_KINDS,
    NUMERIC_VOWELS,
    PARTICLE_SERIES,
    VOWELS,
)

SPEC = (Path(__file__).parent.parent / "docs" / "spec.md").read_text(encoding="utf-8").lower()


def test_inventories():
    assert len(CONSONANTS) == 20
    assert VOWELS == "IYEAOU"
    assert NUMERIC_VOWELS == "IYEAO"
    assert set(FINAL_CONSONANTS) == set("MTNSLR")
    assert set(HEAD_KINDS) == set(FINAL_CONSONANTS)
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


def test_spec_mentions_every_root_and_particle():
    """Drift alarm: anything in language.json must be documented in docs/spec.md."""
    missing = [r for r in CORE_ROOTS if f"**{r.lower()}**" not in SPEC]
    assert not missing, f"roots in language.json but not bolded in spec.md: {missing}"
    missing = [
        form
        for particles in PARTICLE_SERIES.values()
        for form in particles
        if f"**{form.lower()}**" not in SPEC
    ]
    assert not missing, f"particles in language.json but not bolded in spec.md: {missing}"
