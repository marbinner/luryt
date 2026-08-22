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
    # event-modifying manner: one ROOT-l in the clause-final event tail
    "ji gusel zifen",
    "ji koryt re tokim ra gusel gosen",
    "ji si di koryt ro gusel zifen",
    "ji go si di koryt ru vyral pasen",
    "ji gusel na zifen",
    # zero-copula simple property predicates
    "ji gusas",
    "di koryt vosas",
    "korym vosas",
    "qa dy num pa koryt vosas",
    "ky qe da fenit melas",
    "di tokit vosas",
    # property-local M degree: all six values and varied complete subjects
    "di koryt mi hatas",
    "di koryt my hatas",
    "di koryt me hatas",
    "di koryt ma hatas",
    "di koryt mo hatas",
    "di koryt mu hatas",
    "ji mo gusas",
    "dy num pa tokit mu vosas",
    "num bi koryr vosas tokim mo hatas",
    # simple-property polarity: any front N, or narrow na before optional M + ROOT-s
    "ni di koryt vosas",
    "ny di koryt vosas",
    "ne di koryt vosas",
    "na di koryt vosas",
    "no di koryt vosas",
    "nu di koryt vosas",
    "na qo dy koryt vosas",
    "qo dy koryt na vosas",
    "nu ka dy num pa koryt vosas",
    "na di tokit vosas",
    "ni di koryt mo hatas",
    "na qo dy koryt mo hatas",
    "qo dy koryt na mo hatas",
    "di tokit mu vosas",
    # pivot and roles
    "ji koryt re tokim ra gosen",
    "ji je ry qy rufim re zifen",
    "ty di koryt re gosen",
    # noun phrases
    "qy pirim",
    # monotone Q-scale: qi = few; none is compositional (front N over existential)
    "qi pirim",
    "qi pirim pasen",
    "qi da fenit melas",
    "ti qi vosas korym re gosen",
    "na qy pirim pasen",
    "nu qy pirim pasen",
    "ka qi pirim pasen",
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
    # relational restrictions: ROOT-r* precedes ROOT-s* and the entity head
    "zifer rufim",
    "di zifer rufit",
    "zifer luryr rufim",
    "luryr zifer rufim",
    "num bi koryr vosas tokim",
    "qe da zifer rufit",
    "ji zifer rufim re gusen",
    "zifer vosas tokim",
    "di pirit si tokir korym",
    # space: static, adjunct, oriented path
    "di pirit si di koryt",
    "ji si di koryt ro zifen",
    "ji sa sarym pasen",
    "ji go si di koryt ru pasen",
    "ji gi si di koryt ru pasen",
    "jy ge su belym ru pasen",
    "jo gu si di koryt ru pasen",
    # questions and answers
    "wo zifen",
    "wa re ji nifen",
    "wo ry ji qy rufim re zifen",
    "wa ra ji di koryt re gosen",
    "wo ri di koryt re gosen",
    "we ro jo nifen",
    "wu jo zifen",
    "wi ju pasen",
    "ni",
    "na",
    # comparison
    "ji ca gusas de pirit re",
    "ji co gusas",
    # symmetric C-scale: superlative-low + comparative polarity + compositional bounds
    "ji ci gusas",
    "di tokit ci vosas",
    "di pirit ci hisas",
    "na ji ca gusas de pirit re",
    "na ji cy gusas de pirit re",
    "na ji ce gusas de pirit re",
    "ni ji ca gusas de pirit re",
    "nu ji ca gusas de pirit re",
    "na ji co gusas",
    "na qa dy koryt ca vosas di koryt re",
    # grouping: particle vs prefix
    "ka pirim sa sarym pasen",
    "kapirim pasen",
    # corrected guide drills
    "ti jy go do saryt ru pasen",
    "pu ju qo koryt re gosen",
    # numerals
    # F-series coordination: same-kind linking, discourse-initial use
    "ji koryt fi tokim re gosen",
    "pirim fe fenim pasen",
    "di koryt vosas fa di tokit na vosas",
    "di koryt mo vosas fa di tokit mi vosas",
    "di koryt vosas fo ji gosen",
    "ty jo zifen fy jo pasen",
    "na qy pirim fe qy fenim pasen",
    "di tokit vosas fe di tokit hatas",
    "ji go si di koryt fi di saryt ru pasen",
    "pirim fi fenim fi katim pasen",
    "tokim fi zifer rufim pasen",
    "qa korym fi qe tokim vosas",
    "te ji zifen fi to je zifen",
    "je zifen fu ji pasen",
    "num pa korym fi num bi fenim pasen",
    "fo ji gosen",
    "di vosas koryt fi vosas tokim re gosen",
    # attributive property modifiers: prenominal, restrictive, close a num run
    "vosas korym",
    "di vosas koryt",
    "qa vosas korym",
    "qe da vosas koryt",
    "dy num pa vosas koryt",
    "ka hisas pirim",
    "di hatas vosas tokit",
    "tu hatas katim pasen",
    "ti di vosas koryt re gosen",
    "qu vosas koryt re gosen",
    "jo go si do vosas koryt ru pasen",
    "di vosas koryt hatas",
    "di pirit si di vosas koryt",
    "ka qe da num pa vosas koryt",
    "num pi",
    "num te",
    "num pa pirim pasen",
    "num py pi pirim pasen",
    "num py py koryt re gosen",
    "ka qo da num py pi pi fenit",
    "num me do ly jy pirim pasen",
    "pi ji zifen",
]

parser = WordParser()


@pytest.mark.parametrize("sentence", CORPUS)
def test_corpus_sentence_tokens_are_well_formed(sentence):
    bad = [w for w in sentence.split() if not parser.validate(w)]
    assert not bad, f"invalid tokens in “{sentence}”: {bad}"
