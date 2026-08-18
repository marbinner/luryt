# Contributing

There are two very different ways to contribute here, with different rules.

## Track 1: the language

Changes to the language itself — new roots, new particle families, grammar,
naming — are **design decisions, not patches**. The flow:

1. **Not sure yet? Open a Discussion.** Half-formed ideas are welcome there.
2. **Concrete idea? Open an issue** using one of the proposal templates
   (new root / dictionary word or sense / new particle family / grammar
   change). A good proposal states what slot it fills, why this form, and shows
   example sentences.
3. **The language editor decides.**
   Accepted proposals get the `accepted` label.
4. **A PR edits the canonical source and regenerates its consumers.**
   - `language/data/*.json` — structured facts such as inventories,
     morphemes, roots, established lexemes, and examples
   - `language/grammar/foundational.md` — normative grammar and interpretation
   - generated files under `docs/` and `src/conlang_tools/data/` — never
     edited directly

   The authority boundary is documented in `language/README.md`. The compiler
   validates the source model and deterministically creates the package,
   website, schema, and published-spec snapshots.

Run the checks locally before pushing:

```bash
uv sync
uv run python scripts/language.py generate
uv run python scripts/language.py check
uv run pytest -q
node --check docs/assets/js/guide.mjs
node --check docs/assets/js/dictionary.mjs
```

### What makes a proposal easy to accept

- It fills a slot the spec already reserves (an unused consonant series, an
  under-populated matrix cell, negative numbers, fractions, decimals, and ordinals…).
- It follows the existing design language: series use one consonant crossed
  with `i y e a o u` mapped to a monotone semantic scale; two-category series
  interleave major–minor, and no participant- or polarity-flipping contrast may
  sit on the weak vowel pairs `i/y` or `o/u` (spec §2.4); roots are CVCV with
  vowels matching their matrix cell; particles should double as prefixes where
  that makes sense.
- It comes with 3–5 example sentences using existing vocabulary.

### What doesn't need a proposal

Typo fixes, clearer wording in the spec that doesn't change meaning, better
glosses, translations of examples — just open a PR.

## Track 2: the tooling

The Python package (`src/conlang_tools/`), tests, and the guide's code are
ordinary open-source code: fork, branch, PR. Please:

- use `uv` (`uv sync`, `uv run pytest`),
- add tests for behavior changes,
- read language data from `constants.py` (which loads the generated package
  snapshot) — never hardcode roots or particles in code.

## Setup

```bash
git clone git@github.com:marbinner/luryt.git
cd luryt
uv sync
uv run python scripts/language.py check
uv run pytest -q          # should pass
uv run luryt parse kapirim  # should segment ka-piri-m
```
