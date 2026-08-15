"""Tests for the word parser and the numeric CV system."""

import pytest

from conlang_tools.constants import CONSONANTS, NUMERIC_VOWELS, cv_to_number, number_to_cv
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


def test_atomic_u_vowel_has_no_numeric_reading(parser):
    r = parser.parse("tu")
    assert r.is_valid
    assert r.numeric_value is None


@pytest.mark.parametrize("bad", ["piri", "abc", "kkapirim", "pirix", "zif", ""])
def test_invalid_words(parser, bad):
    assert not parser.parse(bad).is_valid


def test_number_round_trip():
    for n in range(100):
        cv = number_to_cv(n)
        assert cv_to_number(cv) == n
    assert number_to_cv(0) == "PI"
    assert number_to_cv(27) == "TE"
    assert number_to_cv(42) == "QE"
    assert number_to_cv(99) == "HO"


def test_number_out_of_range():
    with pytest.raises(ValueError):
        number_to_cv(100)
    with pytest.raises(ValueError):
        cv_to_number("tu")  # U is not a numeric vowel
