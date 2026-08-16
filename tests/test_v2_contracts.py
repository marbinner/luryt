"""Textual regressions for v2 syntax contracts not enforced by the word parser."""

import re
from pathlib import Path


ROOT = Path(__file__).parent.parent
SPEC = (ROOT / "language" / "grammar" / "foundational.md").read_text(encoding="utf-8")
GUIDE_HTML = (ROOT / "docs" / "index.html").read_text(encoding="utf-8")
GUIDE_STYLE = (ROOT / "docs" / "assets" / "css" / "guide.css").read_text(
    encoding="utf-8"
)
GUIDE_SCRIPT = (ROOT / "docs" / "assets" / "js" / "guide.mjs").read_text(
    encoding="utf-8"
)
GUIDE = "\n".join((GUIDE_HTML, GUIDE_STYLE, GUIDE_SCRIPT))
README = (ROOT / "README.md").read_text(encoding="utf-8")
CONTRIBUTING = (ROOT / "CONTRIBUTING.md").read_text(encoding="utf-8")


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
    assert "[PIVOT] [other NPs + R/S] [MANNER] [na] VERB" in SPEC
    assert "The pivot may be absent in a fully" in SPEC
    assert "Every slot but subject and verb is optional" not in GUIDE
    assert '["pivot","unmarked NP","optional"' in GUIDE


def test_event_manner_has_one_clause_final_slot():
    template = (
        "[W (+R)?] [T] [P] [H] [M] [N] [PIVOT] "
        "[other NPs + R/S] [MANNER] [na] VERB"
    )
    assert template in SPEC
    assert "after the pivot and every role-marked or spatial phrase" in SPEC
    assert "The slot is optional and single" in SPEC
    assert "multiple event-manner heads are not licensed" in SPEC
    for sentence in (
        "`ji guse-l zife-n.`",
        "`ji kory-t re toki-m ra guse-l gose-n.`",
        "`ji si di kory-t ro guse-l zife-n.`",
        "`ji go si di kory-t ru vyra-l pase-n.`",
        "`ji guse-l na zife-n.`",
        "`je guse-l zife-n.`",
    ):
        assert sentence in SPEC

    assert '["manner−l","event manner","optional · one"' in GUIDE
    assert (
        '<span class="lx">[pivot] · NPs+role/space · '
        '[manner‑l] · [na] · event‑n</span>'
    ) in GUIDE
    assert '<span class="lx">ji gusel na zifen</span>' in GUIDE
    assert '<span class="lx">wu je zifen?</span>' in GUIDE
    assert '<span class="lx">je gusel zifen.</span>' in GUIDE


def test_simple_property_clause_is_zero_copula_and_property_final():
    assert "### 7.5 Properties and Comparatives" in SPEC
    assert "`SUBJECT PROPERTY`" in SPEC
    assert "SUBJECT is exactly one pronoun or complete" in SPEC
    assert "PROPERTY is exactly one clause-final `ROOT-s`" in SPEC
    assert "No copula, event head, role marker, or agreement" in SPEC
    assert "simple property clauses have no T/P/H/M operator track" in SPEC
    assert "An overt C-series form keeps the existing comparative" in SPEC
    for sentence in (
        "`ji gusa-s.`",
        "`di kory-t vosa-s.`",
        "`kory-m vosa-s.`",
        "`qa dy num pa kory-t vosa-s.`",
        "`ky qe da feni-t mela-s.`",
        "`di toki-t vosa-s?`",
    ):
        assert sentence in SPEC

    assert "<h3>Describe a subject with one property</h3>" in GUIDE
    assert '<span class="lx">subject · property‑s</span>' in GUIDE
    assert '<span class="lx">gusas.</span>' in GUIDE
    assert '<span class="lx">di koryt</span>' in GUIDE
    assert '<span class="lx">qa dy num pa koryt</span>' in GUIDE
    assert '<span class="lx">di tokit vosas?</span>' in GUIDE
    assert '<span class="lx">di koryt vosas</span>' in GUIDE


def test_simple_property_polarity_has_broad_and_narrow_scope():
    assert "[N] SUBJECT PROPERTY" in SPEC
    assert "SUBJECT na PROPERTY" in SPEC
    assert "Any N-series form (`ni/ny/ne/na/no/nu`) may occupy the front position" in SPEC
    assert "Only `na` may instead occur immediately before" in SPEC
    assert "The two positions cannot co-occur" in SPEC
    assert "N particles do not stack" in SPEC
    assert "including its K/Q/D/NUM scope" in SPEC
    assert "The two N patterns above likewise do not extend by analogy to" in SPEC
    for sentence in (
        "`ni di kory-t vosa-s.`",
        "`ny di kory-t vosa-s.`",
        "`ne di kory-t vosa-s.`",
        "`na di kory-t vosa-s.`",
        "`no di kory-t vosa-s.`",
        "`nu di kory-t vosa-s.`",
        "`na qo dy kory-t vosa-s.`",
        "`qo dy kory-t na vosa-s.`",
        "`na di toki-t vosa-s?`",
    ):
        assert sentence in SPEC

    assert '<span class="lx">[n] · subject · property‑s</span>' in GUIDE
    assert '<span class="lx">subject · na · property‑s</span>' in GUIDE
    assert '<span class="lx">qo dy koryt</span>' in GUIDE
    assert '<span class="lx">na di tokit vosas?</span>' in GUIDE
    assert "These are alternative positions; do not" in GUIDE


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
    assert "Where does he/she eat?" in question_section
    assert "Where do they eat?" not in question_section
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


def test_unfinished_numeric_surfaces_are_consistent():
    open_surfaces = "negative numbers, fractions, decimals, and ordinals"
    assert open_surfaces in SPEC.lower()
    assert open_surfaces in GUIDE.lower()
    assert open_surfaces in README.lower()
    assert open_surfaces in CONTRIBUTING.lower()
    assert "numbers ≥ 100" not in CONTRIBUTING


def test_clause_visualization_tracks_its_actual_slot_and_zone_counts():
    assert (
        ".dd-clause{display:grid;grid-auto-flow:column;grid-auto-columns:92px;"
        in GUIDE
    )
    assert "grid-template-columns:repeat(9,92px)" not in GUIDE
    assert (
        'class="visual-key space-key four-key" '
        'aria-label="The four zones of a canonical event clause"'
        in GUIDE
    )
    assert ".four-key{grid-template-columns:repeat(4,1fr)}" in GUIDE


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
        "Distribution and scope of T/P/H/M operators in property clauses",
        "Non-event distribution of manner (`ROOT-l`)",
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
    assert GUIDE_HTML.startswith('<!doctype html>\n<html lang="en">\n<head>')
    assert "</head>\n<body>" in GUIDE_HTML
    assert GUIDE_HTML.rstrip().endswith("</body>\n</html>")


def test_guide_exposes_github_contribution_link_at_the_top():
    contribution_link = (
        '<a class="github-link" href="https://github.com/marbinner/luryt">'
    )
    assert contribution_link in GUIDE
    assert GUIDE.index(contribution_link) < GUIDE.index('<header class="hero">')
    assert "Contribute on GitHub" in GUIDE
