"""Selected v2 example sentences must contain well-formed words.

This is deliberately a word-shape check, not a sentence-grammar parser.
Semantic and word-order contracts have separate regression tests.
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
    "ka qa pirim pasen",
    "qa kapirim pasen",
    "ky qe da fenit pasen",
    "qe da kyfenit pasen",
    "ki qu dy koryt re gosen",
    "dy num pa pirit",
    "qe da num bi fenit",
    "qu dy num pa koryt re gosen",
    "qe num qe pirit",
    "ka num ka pirim pasen",
    "num pa kapirim",
    # space: static, adjunct, oriented path
    "di pirit si di koryt",
    "ji si di koryt ro zifen",
    "ji sa sarym pasen",
    "ji go si di koryt ru pasen",
    "ji gi si di koryt ru pasen",
    "ja ge su belym ru pasen",
    "je gu si di koryt ru pasen",
    # questions and answers
    "wo zifen",
    "wa re ji nifen",
    "wo ry ji qy rufim re zifen",
    "wa ra ji di koryt re gosen",
    "wo ri di koryt re gosen",
    "we ro je nifen",
    "wu je zifen",
    "wi ju pasen",
    "ni",
    "na",
    # comparison
    "ji ca gusas de pirit re",
    "ji co gusas",
    # grouping: particle vs prefix
    "ka pirim sa sarym pasen",
    "kapirim pasen",
    # corrected guide drills
    "ti ja go do saryt ru pasen",
    "pu ju qo koryt re gosen",
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
