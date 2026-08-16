"""Tests for the word parser and the numeric CV system."""

import pytest

from conlang_tools.constants import (
    CONSONANTS,
    NUMERAL_BASE,
    NUMERIC_VOWELS,
    cv_to_number,
    number_to_cv,
)
from conlang_tools.parser import WordParser


@pytest.fixture(scope="module")
def parser():
    return WordParser()


def test_content_word_with_prefix(parser):
    r = parser.parse("kapirim")
    assert r.is_valid
    assert r.word_type == "content"
    assert r.prefixes == ["KA"]
    assert r.root == "PIRI"
    assert r.suffix == "M"
    assert (r.domain, r.aspect) == ("I", "I")


def test_parse_preserves_original_input(parser):
    r = parser.parse("  kapirim ")
    assert r.is_valid
    assert r.original == "  kapirim "
    assert r.root == "PIRI"


def test_bare_content_word(parser):
    r = parser.parse("zifes")
    assert r.is_valid
    assert r.prefixes == []
    assert r.root == "ZIFE"
    assert r.suffix == "S"


def test_atomic_particle_and_numeral(parser):
    r = parser.parse("te")
    assert r.is_valid
    assert r.word_type == "atomic"
    assert r.particle_series == "T"
    assert r.numeric_value == 27


def test_num_is_a_valid_fixed_atomic_form(parser):
    r = parser.parse("num")
    assert r.is_valid
    assert r.word_type == "atomic"
    assert r.particle_meaning[0] == "numeral marker"


def test_atomic_u_vowel_has_no_numeric_reading(parser):
    r = parser.parse("tu")
    assert r.is_valid
    assert r.numeric_value is None


@pytest.mark.parametrize("bad", ["pı", "ſi"])
def test_non_ascii_lookalikes_are_rejected(parser, bad):
    r = parser.parse(bad)
    assert not r.is_valid
    assert "ASCII" in r.errors[0]


@pytest.mark.parametrize("bad", ["piri", "abc", "kkapirim", "pirix", "zif", ""])
def test_invalid_words(parser, bad):
    assert not parser.parse(bad).is_valid


def test_number_round_trip():
    for n in range(10_001):
        cv = number_to_cv(n)
        assert cv_to_number(cv) == n
    assert NUMERAL_BASE == 100
    assert number_to_cv(0) == "PI"
    assert number_to_cv(27) == "TE"
    assert number_to_cv(42) == "QE"
    assert number_to_cv(99) == "HO"
    assert number_to_cv(100) == "PY PI"
    assert number_to_cv(101) == "PY PY"
    assert number_to_cv(10_000) == "PY PI PI"
    assert number_to_cv(12_345_678) == "ME DO LY JA"


def test_number_rejects_negative_and_nonnumeric_blocks():
    with pytest.raises(ValueError):
        number_to_cv(-1)
    with pytest.raises(ValueError):
        cv_to_number("tu")  # U is not a numeric vowel
    with pytest.raises(ValueError):
        cv_to_number("py qu")


def test_multiblock_number_canonicality():
    assert cv_to_number("py pi") == 100
    assert cv_to_number("PY PI PY") == 10_001
    assert cv_to_number("me do ly ja") == 12_345_678
    with pytest.raises(ValueError, match="cannot begin with the zero block"):
        cv_to_number("pi py")
    with pytest.raises(ValueError, match="at least one block"):
        cv_to_number("")


def test_arbitrary_precision_number_round_trip():
    n = int("1234567890" * 10)
    assert cv_to_number(number_to_cv(n)) == n


@pytest.mark.parametrize("bad", ["pı", "ſi"])
def test_number_rejects_non_ascii_lookalikes(bad):
    with pytest.raises(ValueError, match="ASCII"):
        cv_to_number(bad)


@pytest.mark.parametrize("bad", [1.5, True, "1", None])
def test_number_rejects_non_integers(bad):
    with pytest.raises(ValueError, match="must be a nonnegative integer"):
        number_to_cv(bad)


@pytest.mark.parametrize("bad", [1.5, True, None])
def test_numeric_cv_run_rejects_non_strings(bad):
    with pytest.raises(ValueError, match="must be a string"):
        cv_to_number(bad)
