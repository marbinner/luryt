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
    assert "[Q] [D] [ROOT-{m|t}]" in SPEC
    assert "qi/qy/qe/qa/qo/qu" in SPEC
    assert "q o" not in SPEC


def test_public_word_shape_summary_mentions_num_exception():
    assert "the numeral marker `num` is the sole longer fixed atom" in README


def test_intentionally_open_syntax_is_documented():
    open_topics = (
        "Scope and ordering of free K-series modifiers",
        "Combinations of exact numerals with Q-series quantifiers or D-series demonstratives",
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
