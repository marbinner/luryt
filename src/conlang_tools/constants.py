"""Constants for the conlang phonology and grammar.

The single source of truth for the language's data is
``src/conlang_tools/data/language.json``. This module loads it and exposes
the same names the rest of the package (and downstream users) rely on.
To change the language — add a root, define a particle series — edit the
JSON file, not this module. CI checks that the spec (``spec.md``) and the
web guide (``docs/index.html``) stay in sync with it.
"""

import json
from importlib import resources
from typing import Dict, Tuple

_DATA = json.loads(
    (resources.files(__package__) / "data" / "language.json").read_text(encoding="utf-8")
)

# Canonical consonant order (for indexing, sorting, numeric codes, series labels)
CONSONANTS: str = _DATA["consonants"]

# Canonical vowel order
VOWELS: str = _DATA["vowels"]

# Numeric vowels (for 00-99 system, excludes U)
NUMERIC_VOWELS: str = _DATA["numeric_vowels"]

# Final consonant pool (for content words)
FINAL_CONSONANTS: str = _DATA["final_consonants"]

CONSONANT_IPA: Dict[str, str] = _DATA["consonant_ipa"]
VOWEL_IPA: Dict[str, str] = _DATA["vowel_ipa"]

# Head kinds (final suffixes)
HEAD_KINDS: Dict[str, Tuple[str, str]] = {
    k: tuple(v) for k, v in _DATA["head_kinds"].items()
}

# Domains (V1 - first vowel of root)
DOMAINS: Dict[str, Tuple[str, str]] = {
    k: tuple(v) for k, v in _DATA["domains"].items()
}

# Aspects (V2 - second vowel of root)
ASPECTS: Dict[str, Tuple[str, str]] = {
    k: tuple(v) for k, v in _DATA["aspects"].items()
}

# Particle series definitions
PARTICLE_SERIES: Dict[str, Dict[str, Tuple[str, str]]] = {
    series: {form: tuple(meaning) for form, meaning in particles.items()}
    for series, particles in _DATA["particle_series"].items()
}

# Core lexicon (36 roots from the semantic matrix)
CORE_ROOTS: Dict[str, Dict[str, str]] = _DATA["core_roots"]

# Fixed atomic words longer than CV (e.g. NUM, the numeral marker)
ATOMIC_WORDS: Dict[str, Tuple[str, str]] = {
    k: tuple(v) for k, v in _DATA.get("atomic_words", {}).items()
}


def cv_to_number(cv: str) -> int:
    """Convert a CV syllable to a number (0-99).

    Args:
        cv: A two-character string (consonant + vowel)

    Returns:
        The numeric value (0-99)

    Raises:
        ValueError: If the CV is invalid
    """
    if len(cv) != 2:
        raise ValueError(f"CV must be exactly 2 characters, got: {cv}")
    if not cv.isascii():
        raise ValueError(f"CV must use ASCII Luryt letters, got: {cv!r}")

    c, v = cv[0].upper(), cv[1].upper()

    if c not in CONSONANTS:
        raise ValueError(f"Invalid consonant: {c}")
    if v not in NUMERIC_VOWELS:
        raise ValueError(f"Invalid numeric vowel: {v} (must be one of {NUMERIC_VOWELS})")

    c_index = CONSONANTS.index(c)
    v_index = NUMERIC_VOWELS.index(v)

    return 5 * c_index + v_index


def number_to_cv(n: int) -> str:
    """Convert a number (0-99) to a CV syllable.

    Args:
        n: An integer from 0 to 99

    Returns:
        The CV syllable representation

    Raises:
        ValueError: If n is not an integer or is out of range
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"Number must be an integer between 0 and 99, got: {n!r}")

    if not 0 <= n <= 99:
        raise ValueError(f"Number must be between 0 and 99, got: {n}")

    c_index = n // 5
    v_index = n % 5

    return CONSONANTS[c_index] + NUMERIC_VOWELS[v_index]
