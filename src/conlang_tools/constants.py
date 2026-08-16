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

# Numeric vowels (for 00-99 blocks, excludes U)
NUMERIC_VOWELS: str = _DATA["numeric_vowels"]

# Positional base for multi-block cardinal numerals
NUMERAL_BASE: int = _DATA["numeral_base"]
if NUMERAL_BASE != len(CONSONANTS) * len(NUMERIC_VOWELS):
    raise ValueError(
        "numeral_base must equal the numeric CV inventory size "
        f"({len(CONSONANTS) * len(NUMERIC_VOWELS)})"
    )

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


def _cv_block_to_number(cv: str) -> int:
    """Convert one numeric CV block to its value from 0 to 99."""
    if len(cv) != 2:
        raise ValueError(f"Numeric CV block must be exactly 2 characters, got: {cv}")
    if not cv.isascii():
        raise ValueError(f"Numeric CV block must use ASCII Luryt letters, got: {cv!r}")

    c, v = cv[0].upper(), cv[1].upper()

    if c not in CONSONANTS:
        raise ValueError(f"Invalid consonant: {c}")
    if v not in NUMERIC_VOWELS:
        raise ValueError(f"Invalid numeric vowel: {v} (must be one of {NUMERIC_VOWELS})")

    return len(NUMERIC_VOWELS) * CONSONANTS.index(c) + NUMERIC_VOWELS.index(v)


def cv_to_number(cv: str) -> int:
    """Convert a canonical numeric-CV run to a nonnegative integer.

    One block retains its original 0-99 value. Multiple whitespace-separated
    blocks compose most-significant first in base 100. Multi-block runs may
    contain zero internally or finally but may not begin with the zero block PI.

    Args:
        cv: One or more whitespace-separated numeric CV blocks

    Returns:
        The decoded nonnegative integer

    Raises:
        ValueError: If the run is empty, noncanonical, or contains an invalid block
    """
    if not isinstance(cv, str):
        raise ValueError(f"Numeric CV run must be a string, got: {cv!r}")

    blocks = cv.split()
    if not blocks:
        raise ValueError("Numeric CV run must contain at least one block")

    values = [_cv_block_to_number(block) for block in blocks]
    if len(values) > 1 and values[0] == 0:
        raise ValueError("Multi-block numeral cannot begin with the zero block PI")

    number = 0
    for value in values:
        number = number * NUMERAL_BASE + value
    return number


def _number_to_cv_block(n: int) -> str:
    """Convert one value from 0 to 99 to its numeric CV block."""
    c_index, v_index = divmod(n, len(NUMERIC_VOWELS))
    return CONSONANTS[c_index] + NUMERIC_VOWELS[v_index]


def number_to_cv(n: int) -> str:
    """Convert a nonnegative integer to its canonical numeric-CV run.

    Args:
        n: Any nonnegative integer

    Returns:
        One or more space-separated CV blocks, most-significant first in base 100

    Raises:
        ValueError: If n is not a nonnegative integer
    """
    if isinstance(n, bool) or not isinstance(n, int):
        raise ValueError(f"Number must be a nonnegative integer, got: {n!r}")

    if n < 0:
        raise ValueError(f"Number must be a nonnegative integer, got: {n}")

    if n == 0:
        return _number_to_cv_block(0)

    blocks = []
    while n:
        n, value = divmod(n, NUMERAL_BASE)
        blocks.append(_number_to_cv_block(value))
    return " ".join(reversed(blocks))
