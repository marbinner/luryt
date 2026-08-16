"""Regression tests for the canonical-source compiler itself."""

import json
import runpy
from copy import deepcopy
from pathlib import Path

import pytest


SCRIPT = runpy.run_path(
    Path(__file__).parents[1] / "scripts" / "language.py",
    run_name="luryt_language_compiler",
)
LanguageDataError = SCRIPT["LanguageDataError"]
compile_language = SCRIPT["compile_language"]
validate_bundle = SCRIPT["validate_bundle"]
ROOT = Path(__file__).parents[1]


def bundle():
    return deepcopy(compile_language()[0])


def test_canonical_records_use_named_fields():
    inventory = json.loads(
        (ROOT / "language" / "data" / "inventory.json").read_text()
    )
    particles = json.loads(
        (ROOT / "language" / "data" / "particles.json").read_text()
    )
    assert set(inventory["head_kinds"]["M"]) == {"label", "gloss"}
    assert set(particles["particle_series"]["T"]["TI"]) == {"label", "gloss"}


def test_validator_rejects_root_coordinate_drift():
    data = bundle()
    data["core_roots"]["PIRI"]["domain"] = "Y"
    with pytest.raises(LanguageDataError, match="root PIRI has wrong domain"):
        validate_bundle(data)


def test_validator_rejects_head_order_drift():
    data = bundle()
    data["head_kinds"] = dict(reversed(data["head_kinds"].items()))
    with pytest.raises(LanguageDataError, match="head order must match final order"):
        validate_bundle(data)


def test_validator_accepts_a_well_formed_curated_lexeme():
    data = bundle()
    data["lexemes"].append(
        {
            "id": "lexeme.pirim",
            "form": "PIRIM",
            "analysis": {"root": "PIRI", "head": "M", "prefixes": []},
            "senses": [
                {
                    "id": "sense.pirim.1",
                    "definition": "a person considered descriptively",
                    "gloss": "person",
                    "status": "core",
                    "examples": [],
                }
            ],
        }
    )
    validate_bundle(data)


def test_validator_rejects_a_lexeme_that_disagrees_with_its_analysis():
    data = bundle()
    data["lexemes"].append(
        {
            "id": "lexeme.pirim",
            "form": "PIRIT",
            "analysis": {"root": "PIRI", "head": "M", "prefixes": []},
            "senses": [
                {
                    "id": "sense.pirim.1",
                    "definition": "a person considered descriptively",
                    "gloss": "person",
                    "status": "core",
                    "examples": [],
                }
            ],
        }
    )
    with pytest.raises(LanguageDataError, match=r"form must equal PIRIM"):
        validate_bundle(data)
