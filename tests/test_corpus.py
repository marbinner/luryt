"""Every example sentence in the spec's style must parse, token by token.

This corpus mirrors the examples in docs/spec.md (v2). If a language change
invalidates one of these sentences, the spec prose needs updating too.
"""

import pytest

from conlang_tools.parser import WordParser

CORPUS = [
    # minimal clauses and operators
    "ji zifen",
    "te py ji zifen",
    "te py na ji zifen",
    "ho qa pirim gyfen",
    "na qo pirim pasen",
    "qo pirim na pasen",
    # pivot and roles
    "ji koryt re tokim ra gosen",
    "ji jy ry qy rufim re zifen",
    "ty di koryt re gosen",
    # noun phrases
    "qy pirim",
    "qe da fenit",
    "qo du koryt",
    # space: static, adjunct, oriented path
    "di pirit si di koryt",
    "ji si di koryt ro zifen",
    "ji pasen sa sarym",
    "ji go si di koryt ru pasen",
    "ji gi si di koryt ru pasen",
    "ja ge su belym ru pasen",
    "je gu si di koryt ru pasen",
    # questions and answers
    "wo zifen",
    "wi ju pasen",
    "ni",
    "na",
    # comparison
    "ji ca gusas de pirit re",
    "ji co gusas",
    # grouping: particle vs prefix
    "ka pirim pasen sa sarym",
    "kapirim pasen",
    # numerals
    "num pi",
    "num te",
    "num pa pirim pasen",
    "pi ji zifen",
]

parser = WordParser()


@pytest.mark.parametrize("sentence", CORPUS)
def test_corpus_sentence_tokens_are_well_formed(sentence):
    bad = [w for w in sentence.split() if not parser.validate(w)]
    assert not bad, f"invalid tokens in “{sentence}”: {bad}"
