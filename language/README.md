# Canonical language sources

This directory is the only place where the language itself is authored.

Authority is divided by subject, rather than duplicated:

- `data/*.json` owns structured facts: inventories, morphemes, roots,
  dictionary senses, and reusable examples.
- `grammar/foundational.md` owns normative grammar, scope, syntax, and
  interpretation.
- `manifest.json` identifies the language and data-schema versions and fixes
  the source-file order used by the compiler.
- `schema/language.schema.json` documents the compiled public data contract.

Files under `src/conlang_tools/data/` and `docs/data/`, plus `docs/spec.md`, are
generated consumer copies. Do not edit them directly.

## Editing workflow

1. Edit the relevant canonical source in this directory.
2. Run `uv run python scripts/language.py generate`.
3. Run `uv run python scripts/language.py check` and `uv run pytest -q`.
4. Commit the source change and its generated snapshots together.

`check` validates structural and semantic invariants and fails when a generated
file is missing or stale. Generation is deterministic and adds no timestamps.
Canonical records use named fields such as `label` and `gloss`; the compiler
may adapt them to a stable consumer representation.

## Data boundaries

The compiled JSON intentionally contains structured facts, not a lossy rewrite
of the foundational document. Entries may link to grammar rule identifiers as
that model grows, but normative prose remains Markdown until a rule has a real
machine-readable representation.

Roots and dictionary lexemes are also distinct. A root supplies a productive
semantic nucleus; a lexeme records an established sense of a complete word.
The website may analyze regularly formed words without claiming that every
root-and-head combination has a conventional dictionary definition.

## Adding dictionary content

Add reusable sentences to `data/examples.json` first, then add complete-word
senses to `data/lexemes.json`. Every record uses a stable lowercase ID,
while Luryt forms and morphology references use canonical uppercase spelling.

A lexeme must provide:

- an `id` and complete `form`,
- an `analysis` containing `root`, `head`, and an ordered prefix list,
- one or more senses with their own IDs, definitions, short glosses, status,
  and example references.

The validator reconstructs the form from its analysis, verifies all prefixes
and references, and validates the word shapes in reusable examples. Allowed
sense statuses are `core`, `provisional`, and `deprecated`.
