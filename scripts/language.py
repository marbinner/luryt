"""Validate and compile Luryt's canonical language sources.

Usage:
    python scripts/language.py validate
    python scripts/language.py generate
    python scripts/language.py check
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
LANGUAGE_ROOT = ROOT / "language"
MANIFEST_PATH = LANGUAGE_ROOT / "manifest.json"
SCHEMA_PATH = LANGUAGE_ROOT / "schema" / "language.schema.json"
SCHEMA_URL = "https://marbinner.github.io/luryt/schema/language.schema.json"
GENERATED_JSON_PATHS = (
    ROOT / "src" / "conlang_tools" / "data" / "language.json",
    ROOT / "docs" / "data" / "language.json",
)
GENERATED_SCHEMA_PATH = ROOT / "docs" / "schema" / "language.schema.json"
GENERATED_SPEC_PATH = ROOT / "docs" / "spec.md"
SPEC_HEADER = "<!-- Generated from language/grammar/foundational.md; do not edit. -->\n\n"
ID_RE = re.compile(r"^[a-z0-9]+(?:[._-][a-z0-9]+)*$")
STATUSES = {"core", "provisional", "deprecated"}


class LanguageDataError(ValueError):
    """Canonical language data violates its repository contract."""


def no_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise LanguageDataError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=no_duplicate_keys,
        )
    except (OSError, json.JSONDecodeError) as error:
        raise LanguageDataError(f"cannot read {path.relative_to(ROOT)}: {error}") from error
    if not isinstance(value, dict):
        raise LanguageDataError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def add_error(errors: list[str], condition: bool, message: str) -> None:
    if not condition:
        errors.append(message)


def pair_map(
    errors: list[str], name: str, value: object
) -> dict[str, list[str]]:
    if not isinstance(value, dict):
        errors.append(f"{name} must be an object")
        return {}
    for key, pair in value.items():
        add_error(
            errors,
            isinstance(pair, list)
            and len(pair) == 2
            and all(isinstance(item, str) and item for item in pair),
            f"{name}.{key} must be [label, gloss]",
        )
    return value


def compile_pair_records(name: str, value: object) -> dict[str, list[str]]:
    """Compile named authoring records to the stable public [label, gloss] shape."""
    if not isinstance(value, dict):
        raise LanguageDataError(f"{name} must be an object")
    compiled: dict[str, list[str]] = {}
    for form, record in value.items():
        if (
            not isinstance(record, dict)
            or set(record) != {"label", "gloss"}
            or not all(
                isinstance(record.get(field), str) and bool(record.get(field))
                for field in ("label", "gloss")
            )
        ):
            raise LanguageDataError(
                f"{name}.{form} must contain nonempty label and gloss fields"
            )
        compiled[form] = [record["label"], record["gloss"]]
    return compiled


def normalize_authoring_data(bundle: dict[str, Any]) -> None:
    """Normalize ergonomic canonical records into the public bundle contract."""
    for field in ("head_kinds", "domains", "aspects", "atomic_words"):
        bundle[field] = compile_pair_records(field, bundle.get(field))
    series = bundle.get("particle_series")
    if not isinstance(series, dict):
        raise LanguageDataError("particle_series must be an object")
    bundle["particle_series"] = {
        consonant: compile_pair_records(f"particle_series.{consonant}", forms)
        for consonant, forms in series.items()
    }


def compile_language() -> tuple[dict[str, Any], str]:
    manifest = load_json(MANIFEST_PATH)
    expected_manifest_keys = {
        "project",
        "display_name",
        "language_version",
        "schema_version",
        "data_sources",
        "grammar_source",
    }
    if set(manifest) != expected_manifest_keys:
        raise LanguageDataError("manifest keys do not match the contract")
    for field in ("project", "display_name", "language_version", "grammar_source"):
        if not isinstance(manifest[field], str) or not manifest[field]:
            raise LanguageDataError(f"manifest.{field} must be a nonempty string")
    if not isinstance(manifest["schema_version"], int) or manifest["schema_version"] < 1:
        raise LanguageDataError("manifest.schema_version must be a positive integer")
    sources = manifest["data_sources"]
    if (
        not isinstance(sources, list)
        or not sources
        or len(sources) != len(set(sources))
        or not all(isinstance(path, str) and path.endswith(".json") for path in sources)
    ):
        raise LanguageDataError("manifest.data_sources must be unique JSON paths")

    bundle: dict[str, Any] = {
        "$schema": SCHEMA_URL,
        "metadata": {
            "project": manifest["project"],
            "display_name": manifest["display_name"],
            "language_version": manifest["language_version"],
            "schema_version": manifest["schema_version"],
            "generated": True,
            "source": "language/",
        }
    }
    for relative in sources:
        path = (LANGUAGE_ROOT / relative).resolve()
        if not path.is_relative_to(LANGUAGE_ROOT):
            raise LanguageDataError(f"data source escapes language/: {relative}")
        part = load_json(path)
        duplicate = set(bundle) & set(part)
        if duplicate:
            raise LanguageDataError(
                f"{relative} repeats top-level keys: {', '.join(sorted(duplicate))}"
            )
        bundle.update(part)
    normalize_authoring_data(bundle)

    grammar_path = (LANGUAGE_ROOT / manifest["grammar_source"]).resolve()
    if not grammar_path.is_relative_to(LANGUAGE_ROOT):
        raise LanguageDataError("grammar source escapes language/")
    try:
        grammar = grammar_path.read_text(encoding="utf-8")
    except OSError as error:
        raise LanguageDataError(
            f"cannot read {grammar_path.relative_to(ROOT)}: {error}"
        ) from error
    expected_title = f"# Foundational Spec (v{manifest['language_version']})"
    if not grammar.startswith(expected_title):
        raise LanguageDataError(
            f"foundational grammar must begin with {expected_title!r}"
        )
    if not grammar.endswith("\n"):
        grammar += "\n"

    validate_bundle(bundle)
    validate_schema_contract(bundle)
    return bundle, grammar


def validate_schema_contract(bundle: dict[str, Any]) -> None:
    schema = load_json(SCHEMA_PATH)
    errors: list[str] = []
    add_error(
        errors,
        schema.get("$schema") == "https://json-schema.org/draft/2020-12/schema",
        "language schema must declare JSON Schema draft 2020-12",
    )
    add_error(
        errors,
        isinstance(schema.get("required"), list)
        and set(schema["required"]) == set(bundle),
        "language schema required keys do not match the compiled bundle",
    )
    add_error(
        errors,
        isinstance(schema.get("properties"), dict)
        and set(schema["properties"]) == set(bundle),
        "language schema properties do not match the compiled bundle",
    )
    if errors:
        raise LanguageDataError("\n".join(errors))


def validate_bundle(data: dict[str, Any]) -> None:
    errors: list[str] = []
    add_error(errors, data.get("$schema") == SCHEMA_URL, "compiled schema URL is incorrect")
    bundle_metadata = data.get("metadata")
    add_error(
        errors,
        isinstance(bundle_metadata, dict)
        and set(bundle_metadata)
        == {
            "project",
            "display_name",
            "language_version",
            "schema_version",
            "generated",
            "source",
        }
        and all(
            isinstance(bundle_metadata.get(field), str) and bool(bundle_metadata.get(field))
            for field in ("project", "display_name", "language_version", "source")
        )
        and isinstance(bundle_metadata.get("schema_version"), int)
        and bundle_metadata.get("schema_version", 0) >= 1
        and bundle_metadata.get("generated") is True
        and bundle_metadata.get("source") == "language/",
        "metadata does not match the compiled-bundle contract",
    )
    consonants = data.get("consonants")
    vowels = data.get("vowels")
    numeric_vowels = data.get("numeric_vowels")
    finals = data.get("final_consonants")

    for name, inventory in (
        ("consonants", consonants),
        ("vowels", vowels),
        ("numeric_vowels", numeric_vowels),
        ("final_consonants", finals),
    ):
        add_error(
            errors,
            isinstance(inventory, str)
            and inventory.isascii()
            and inventory.isupper()
            and len(inventory) == len(set(inventory)),
            f"{name} must be a unique uppercase ASCII inventory",
        )
    if not all(
        isinstance(value, str)
        for value in (consonants, vowels, numeric_vowels, finals)
    ):
        raise LanguageDataError("\n".join(errors))

    add_error(errors, set(numeric_vowels) <= set(vowels), "numeric vowels are not a vowel subset")
    add_error(errors, set(finals) <= set(consonants), "finals are not consonants")
    add_error(
        errors,
        data.get("numeral_base") == len(consonants) * len(numeric_vowels),
        "numeral_base must equal consonants × numeric_vowels",
    )

    for name, inventory in (
        ("consonant_ipa", consonants),
        ("vowel_ipa", vowels),
    ):
        mapping = data.get(name)
        add_error(
            errors,
            isinstance(mapping, dict) and list(mapping) == list(inventory),
            f"{name} must preserve canonical inventory order",
        )
        if isinstance(mapping, dict):
            for form, ipa in mapping.items():
                add_error(
                    errors,
                    isinstance(ipa, str) and ipa.startswith("/") and ipa.endswith("/"),
                    f"{name}.{form} must be slash-delimited IPA",
                )

    heads = pair_map(errors, "head_kinds", data.get("head_kinds"))
    domains = pair_map(errors, "domains", data.get("domains"))
    aspects = pair_map(errors, "aspects", data.get("aspects"))
    add_error(errors, list(heads) == list(finals), "head order must match final order")
    add_error(errors, list(domains) == list(vowels), "domain order must match vowel order")
    add_error(errors, list(aspects) == list(vowels), "aspect order must match vowel order")

    particle_series = data.get("particle_series")
    add_error(errors, isinstance(particle_series, dict), "particle_series must be an object")
    particle_forms: set[str] = set()
    if isinstance(particle_series, dict):
        for series, raw_forms in particle_series.items():
            add_error(
                errors,
                isinstance(series, str) and len(series) == 1 and series in consonants,
                f"invalid particle-series key {series!r}",
            )
            forms = pair_map(errors, f"particle_series.{series}", raw_forms)
            expected = [series + vowel for vowel in vowels]
            add_error(
                errors,
                list(forms) == expected,
                f"particle series {series} must contain {expected} in order",
            )
            for form in forms:
                add_error(errors, form not in particle_forms, f"duplicate particle {form}")
                particle_forms.add(form)

    metadata = data.get("particle_series_metadata")
    add_error(
        errors,
        isinstance(metadata, dict)
        and isinstance(particle_series, dict)
        and list(metadata) == list(particle_series),
        "particle-series metadata must match series and order",
    )
    if isinstance(metadata, dict):
        for series, record in metadata.items():
            add_error(
                errors,
                isinstance(record, dict)
                and set(record) == {"name"}
                and isinstance(record.get("name"), str)
                and bool(record.get("name")),
                f"particle_series_metadata.{series} must contain one name",
            )

    prefix_series = data.get("derivational_prefix_series")
    add_error(
        errors,
        isinstance(prefix_series, list)
        and len(prefix_series) == len(set(prefix_series))
        and isinstance(particle_series, dict)
        and all(series in particle_series for series in prefix_series),
        "derivational_prefix_series names undefined or duplicate series",
    )
    expected_prefixes: set[str] = set()
    if isinstance(prefix_series, list) and isinstance(particle_series, dict):
        for series in prefix_series:
            if series in particle_series:
                expected_prefixes.update(particle_series[series])
    prefixes = data.get("derivational_prefixes")
    add_error(
        errors,
        isinstance(prefixes, dict) and set(prefixes) == expected_prefixes,
        "derivational_prefixes must define every and only licensed prefix",
    )
    if isinstance(prefixes, dict):
        for form, gloss in prefixes.items():
            add_error(errors, isinstance(gloss, str) and bool(gloss), f"prefix {form} needs a gloss")

    atoms = pair_map(errors, "atomic_words", data.get("atomic_words"))
    add_error(errors, not (set(atoms) & particle_forms), "atomic words collide with particles")

    roots = data.get("core_roots")
    add_error(errors, isinstance(roots, dict), "core_roots must be an object")
    cells: set[tuple[str, str]] = set()
    if isinstance(roots, dict):
        for form, record in roots.items():
            shape_ok = (
                isinstance(form, str)
                and len(form) == 4
                and form[0] in consonants
                and form[1] in vowels
                and form[2] in consonants
                and form[3] in vowels
            )
            add_error(errors, shape_ok, f"root {form!r} is not CVCV")
            add_error(
                errors,
                isinstance(record, dict)
                and set(record) == {"domain", "aspect", "gloss", "semantic_range"},
                f"root {form!r} has unexpected fields",
            )
            if not isinstance(record, dict):
                continue
            domain, aspect = record.get("domain"), record.get("aspect")
            if shape_ok:
                add_error(errors, domain == form[1], f"root {form} has wrong domain")
                add_error(errors, aspect == form[3], f"root {form} has wrong aspect")
            for field in ("gloss", "semantic_range"):
                add_error(
                    errors,
                    isinstance(record.get(field), str) and bool(record.get(field)),
                    f"root {form} needs {field}",
                )
            if isinstance(domain, str) and isinstance(aspect, str):
                add_error(errors, (domain, aspect) not in cells, f"duplicate cell {domain}×{aspect}")
                cells.add((domain, aspect))
        add_error(
            errors,
            cells == {(domain, aspect) for domain in vowels for aspect in vowels},
            "core roots must cover every domain × aspect cell",
        )

    examples = data.get("examples")
    add_error(errors, isinstance(examples, list), "examples must be an array")
    example_ids: set[str] = set()
    if isinstance(examples, list):
        for index, example in enumerate(examples):
            where = f"examples[{index}]"
            add_error(errors, isinstance(example, dict), f"{where} must be an object")
            if not isinstance(example, dict):
                continue
            allowed = {"id", "luryt", "translation", "notes", "rules"}
            add_error(errors, set(example) <= allowed, f"{where} has unexpected fields")
            for field in ("id", "luryt", "translation"):
                add_error(
                    errors,
                    isinstance(example.get(field), str) and bool(example.get(field)),
                    f"{where}.{field} must be nonempty",
                )
            identifier = example.get("id")
            if isinstance(identifier, str):
                add_error(errors, bool(ID_RE.fullmatch(identifier)), f"invalid example id {identifier}")
                add_error(errors, identifier not in example_ids, f"duplicate example id {identifier}")
                example_ids.add(identifier)
            sentence = example.get("luryt")
            if isinstance(sentence, str):
                for token in re.findall(r"[A-Za-z]+", sentence.upper()):
                    add_error(
                        errors,
                        valid_surface_word(
                            token,
                            consonants=consonants,
                            vowels=vowels,
                            numeric_vowels=numeric_vowels,
                            finals=finals,
                            particles=particle_forms,
                            atoms=set(atoms),
                            prefixes=set(prefixes) if isinstance(prefixes, dict) else set(),
                        ),
                        f"{where}.luryt contains an invalid word: {token}",
                    )
            rules = example.get("rules", [])
            add_error(
                errors,
                isinstance(rules, list)
                and all(isinstance(rule, str) and rule for rule in rules),
                f"{where}.rules must contain strings",
            )
            if isinstance(rules, list) and all(isinstance(rule, str) for rule in rules):
                add_error(
                    errors,
                    len(rules) == len(set(rules)),
                    f"{where}.rules must not contain duplicates",
                )

    lexemes = data.get("lexemes")
    add_error(errors, isinstance(lexemes, list), "lexemes must be an array")
    lexeme_ids: set[str] = set()
    sense_ids: set[str] = set()
    if isinstance(lexemes, list):
        for index, lexeme in enumerate(lexemes):
            where = f"lexemes[{index}]"
            add_error(
                errors,
                isinstance(lexeme, dict)
                and set(lexeme) == {"id", "form", "analysis", "senses"},
                f"{where} must contain id, form, analysis, and senses",
            )
            if not isinstance(lexeme, dict):
                continue
            identifier = lexeme.get("id")
            add_error(
                errors,
                isinstance(identifier, str) and bool(ID_RE.fullmatch(identifier)),
                f"{where}.id is invalid",
            )
            if isinstance(identifier, str):
                add_error(errors, identifier not in lexeme_ids, f"duplicate lexeme id {identifier}")
                lexeme_ids.add(identifier)
            analysis = lexeme.get("analysis")
            add_error(
                errors,
                isinstance(analysis, dict)
                and set(analysis) == {"root", "head", "prefixes"},
                f"{where}.analysis is invalid",
            )
            if isinstance(analysis, dict):
                root, head = analysis.get("root"), analysis.get("head")
                form_prefixes = analysis.get("prefixes")
                add_error(errors, isinstance(roots, dict) and root in roots, f"{where} has unknown root")
                add_error(errors, head in heads, f"{where} has unknown head")
                add_error(
                    errors,
                    isinstance(form_prefixes, list)
                    and isinstance(prefixes, dict)
                    and all(
                        isinstance(item, str) and item in prefixes
                        for item in form_prefixes
                    ),
                    f"{where} has unknown prefixes",
                )
                if isinstance(root, str) and isinstance(head, str) and isinstance(form_prefixes, list):
                    assembled = "".join(form_prefixes) + root + head
                    add_error(errors, lexeme.get("form") == assembled, f"{where}.form must equal {assembled}")
            senses = lexeme.get("senses")
            add_error(errors, isinstance(senses, list) and bool(senses), f"{where}.senses must be nonempty")
            if not isinstance(senses, list):
                continue
            for sense_index, sense in enumerate(senses):
                sense_where = f"{where}.senses[{sense_index}]"
                required = {"id", "definition", "gloss", "status", "examples"}
                add_error(
                    errors,
                    isinstance(sense, dict)
                    and required <= set(sense)
                    and set(sense) <= required | {"notes"},
                    f"{sense_where} has invalid fields",
                )
                if not isinstance(sense, dict):
                    continue
                sense_id = sense.get("id")
                add_error(
                    errors,
                    isinstance(sense_id, str) and bool(ID_RE.fullmatch(sense_id)),
                    f"{sense_where}.id is invalid",
                )
                if isinstance(sense_id, str):
                    add_error(errors, sense_id not in sense_ids, f"duplicate sense id {sense_id}")
                    sense_ids.add(sense_id)
                for field in ("definition", "gloss"):
                    add_error(
                        errors,
                        isinstance(sense.get(field), str) and bool(sense.get(field)),
                        f"{sense_where}.{field} must be nonempty",
                    )
                add_error(errors, sense.get("status") in STATUSES, f"{sense_where}.status is invalid")
                refs = sense.get("examples")
                add_error(
                    errors,
                    isinstance(refs, list)
                    and all(
                        isinstance(ref, str) and ref in example_ids for ref in refs
                    ),
                    f"{sense_where}.examples has unknown or duplicate references",
                )
                if isinstance(refs, list) and all(isinstance(ref, str) for ref in refs):
                    add_error(
                        errors,
                        len(refs) == len(set(refs)),
                        f"{sense_where}.examples contains duplicates",
                    )

    if errors:
        raise LanguageDataError("\n".join(f"- {error}" for error in errors))


def valid_surface_word(
    word: str,
    *,
    consonants: str,
    vowels: str,
    numeric_vowels: str,
    finals: str,
    particles: set[str],
    atoms: set[str],
    prefixes: set[str],
) -> bool:
    """Return whether one punctuation-free token has a licensed word shape."""
    if word in atoms:
        return True
    if len(word) == 2:
        return word in particles or (
            word[0] in consonants and word[1] in numeric_vowels
        )
    if len(word) < 5 or word[-1] not in finals:
        return False
    root = word[-5:-1]
    if not (
        root[0] in consonants
        and root[1] in vowels
        and root[2] in consonants
        and root[3] in vowels
    ):
        return False
    prefix_text = word[:-5]
    return len(prefix_text) % 2 == 0 and all(
        prefix_text[index : index + 2] in prefixes
        for index in range(0, len(prefix_text), 2)
    )


def rendered_outputs() -> dict[Path, str]:
    bundle, grammar = compile_language()
    json_text = json.dumps(bundle, ensure_ascii=False, indent=2) + "\n"
    outputs = {path: json_text for path in GENERATED_JSON_PATHS}
    outputs[GENERATED_SCHEMA_PATH] = SCHEMA_PATH.read_text(encoding="utf-8")
    outputs[GENERATED_SPEC_PATH] = SPEC_HEADER + grammar
    return outputs


def generate() -> None:
    for path, content in rendered_outputs().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        print(f"generated {path.relative_to(ROOT)}")


def check() -> None:
    stale: list[Path] = []
    for path, expected in rendered_outputs().items():
        try:
            actual = path.read_text(encoding="utf-8")
        except OSError:
            actual = ""
        if actual != expected:
            stale.append(path)
    if stale:
        paths = "\n".join(f"- {path.relative_to(ROOT)}" for path in stale)
        raise LanguageDataError(
            "generated language files are missing or stale:\n"
            f"{paths}\n"
            "run: uv run python scripts/language.py generate"
        )
    print("canonical sources and generated language files are consistent")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("validate", "generate", "check"))
    command = parser.parse_args(argv).command
    try:
        if command == "validate":
            compile_language()
            print("canonical language sources are valid")
        elif command == "generate":
            generate()
        else:
            check()
    except LanguageDataError as error:
        print(f"language data error:\n{error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
