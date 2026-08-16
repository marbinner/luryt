"""Textual regressions for v2 syntax contracts not enforced by the word parser."""

import re
from pathlib import Path


ROOT = Path(__file__).parent.parent
SPEC = (ROOT / "docs" / "spec.md").read_text(encoding="utf-8")
GUIDE = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
README = (ROOT / "README.md").read_text(encoding="utf-8")


def test_path_neutral_motion_is_verb_final():
    assert "`ji sa sary-m pase-n.`" in SPEC
    assert "`ka piri-m sa sary-m pase-n.`" in SPEC
    assert "ji pase-n sa sary-m" not in SPEC
    assert "ka piri-m pase-n sa sary-m" not in SPEC
    sentence_section = GUIDE.split('<section class="ch" id="sentences">', 1)[1].split(
        '<section class="ch" id="practice">', 1
    )[0]
    forms = re.findall(r'<span class="lx">([^<]+)</span>', sentence_section)
    assert any(forms[i:i + 4] == ["ji", "sa", "sarym", "pasen."] for i in range(len(forms) - 3))
    assert not any(
        forms[i:i + 4] == ["ji", "pasen", "sa", "sarym."]
        for i in range(len(forms) - 3)
    )


def test_guide_drills_follow_v2_path_and_pivot_rules():
    assert "ti ja go do saryt ru pasen." in GUIDE
    assert "ti ja ru do sarym pasen." not in GUIDE
    assert "pu ju qo koryt re gosen." in GUIDE
    assert "pu ju qo koryt gosen." not in GUIDE


def test_event_clause_template_allows_pivot_omission():
    assert "[PIVOT] [other NPs + R/S] VERB" in SPEC
    assert "The pivot may be absent in a fully" in SPEC
    assert "Every slot but subject and verb is optional" not in GUIDE
    assert '["pivot","unmarked NP","optional"' in GUIDE


def test_questioned_nonpivot_keeps_its_event_role():
    assert "[W (+R)?] [T] [P] [H] [M] [N]" in SPEC
    for sentence in (
        "`wo zife-n?`",
        "`wa re ji nife-n?`",
        "`wo ry ji qy rufi-m re zife-n?`",
        "`wa ra ji di kory-t re gose-n?`",
        "`wo ri di kory-t re gose-n?`",
        "`we ro je nife-n?`",
    ):
        assert sentence in SPEC
    assert "`wa ji nife-n?`" not in SPEC
    question_section = GUIDE.split("<h3>Questions</h3>", 1)[1].split(
        "<h3>Comparing things</h3>", 1
    )[0]
    forms = re.findall(r'<span class="lx">([^<]+)</span>', question_section)
    assert "he/she/it · pivot" in question_section
    assert "they · pivot" not in question_section
    assert any(forms[i:i + 4] == ["wa", "re", "ji", "nifen?"] for i in range(len(forms) - 3))
    assert any(forms[i:i + 4] == ["we", "ro", "je", "nifen?"] for i in range(len(forms) - 3))
    assert '["w– (+ r–)","question + role"' in GUIDE


def test_noun_phrase_template_allows_both_entity_heads():
    assert "[K] [Q] [D] [NUM] [ROOT-{m|t}]" in SPEC
    assert "qi/qy/qe/qa/qo/qu" in SPEC
    assert "q o" not in SPEC


def test_free_k_has_outer_np_scope_while_bound_k_stays_lexical():
    assert "configures the participants selected by the complete following Q/D/NUM/head" in SPEC
    assert "At most one free K-particle fills this slot" in SPEC
    for contrast in (
        "`ka qa piri-m` – “most people, configured together”",
        "`qa ka-piri-m` – “most crowds”",
        "`ky qe da feni-t` – “some of those animals, configured in pairs”",
        "`qe da ky-feni-t` – “some of those identifiable animal pairs”",
        "`ki qu dy kory-t re gose-n.` – each of these houses, configured singly, was built",
    ):
        assert contrast in SPEC
    assert '<span class="lx">[k] [q] [d] [num cv+] noun</span>' in GUIDE
    assert '<span class="lx">ka qa pirim</span>' in GUIDE
    assert '<span class="lx">qa kapirim</span>' in GUIDE
    assert '<span class="lx">ky qe da fenit</span>' in GUIDE
    assert '<span class="lx">qe da kyfenit</span>' in GUIDE


def test_exact_numeral_has_inner_np_slot_and_fixed_scope():
    assert "NUM = num numeric-CV+" in SPEC
    assert "All K/Q/D particles precede NUM" in SPEC
    assert "Q scopes over the following D/NUM/head cardinal frame" in SPEC
    assert "The marker governs the maximal following run of numeric" in SPEC
    for contrast in (
        "`dy num pa piri-t` – these three people / exactly three of these people",
        "`qe da num bi feni-t` – some but not all of those five animals",
        "`qu dy num pa kory-t re gose-n.` – each of these three houses was built",
        "`qe num qe piri-t` – some but not all of an identifiable forty-two-person set",
        "`da num da piri-t` – thirty-three of those people",
        "`ka num ka piri-m` – eighty-three people, configured together",
        "`num py pi piri-m` – one hundred people",
        "`num py pi pi kory-t` – ten thousand identifiable houses",
    ):
        assert contrast in SPEC
    assert '<span class="lx">[k] [q] [d] [num cv+] noun</span>' in GUIDE
    assert '<span class="lx">dy num pa pirit</span>' in GUIDE
    assert '<span class="lx">qe da num bi fenit</span>' in GUIDE
    assert '<span class="lx">ka num ka pirim</span>' in GUIDE
    assert '<span class="lx">num pa kapirim</span>' in GUIDE
    assert "Combinations of exact numerals with Q-series" not in SPEC
    assert "How exact-number phrases headed by" not in GUIDE


def test_exact_numerals_compose_canonically_in_base_100():
    for rule in (
        "most-significant first in base 100",
        "the first block must be nonzero",
        "`num pi` is the sole",
        "form of zero. There is no maximum block count",
        "later `num` begins a separate NUM constituent",
        "never an unmarked alias of `num py pi` “100.”",
    ):
        assert rule in SPEC
    for example in (
        "`num py pi` – “one hundred”",
        "`num py py` – “one hundred one”",
        "`num py pi pi` – “ten thousand”",
        "`num me do ly ja`",
    ):
        assert example in SPEC

    assert "Numbers above 99 aren’t specified yet" not in GUIDE
    assert "Values above 99 are not specified yet" not in GUIDE
    assert "Numbers beyond 99." not in GUIDE
    assert "**numbers above 99**" not in README
    assert '<span class="lx">num py pi</span> = 100' in GUIDE
    assert "const n = BigInt(t)" in GUIDE
    assert "n > 99" not in GUIDE


def test_public_word_shape_summaries_mention_num_exception():
    assert "the numeral marker `num` is the sole longer fixed atom" in README
    assert "the sole longer fixed atom" in GUIDE
    assert "First check the list of longer fixed atoms" in GUIDE
    for false_absolute in (
        "Two-letter words are grammar. Longer words are vocabulary",
        "longer than two letters, so it must be a content word",
        "All of Luryt’s grammar lives in two-letter words",
        "Particles are exactly CV.",
    ):
        assert false_absolute not in GUIDE


def test_intentionally_open_syntax_is_documented():
    open_topics = (
        "Direct event-level use and ordering of free K-series modifiers",
        "General clause/phrase distribution of manner (`ROOT-l`)",
        "W-extraction from inside static-location and oriented-path phrases",
    )
    for topic in open_topics:
        assert topic in SPEC


def test_numeric_collision_count_is_precise():
    assert "Seventy of the hundred numeric CVs" in SPEC
    assert "Seventy of the hundred number syllables" in GUIDE
    assert "Every numeric CV collides" not in SPEC
    assert "Every numeric CV collides" not in GUIDE


def test_guide_uses_standards_mode_document_structure():
    assert GUIDE.startswith('<!doctype html>\n<html lang="en">\n<head>')
    assert "</head>\n<body>" in GUIDE
    assert GUIDE.rstrip().endswith("</body>\n</html>")
