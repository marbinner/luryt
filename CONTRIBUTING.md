# Contributing

There are two very different ways to contribute here, with different rules.

## Track 1: the language

Changes to the language itself — new roots, new particle families, grammar,
naming — are **design decisions, not patches**. The flow:

1. **Not sure yet? Open a Discussion.** Half-formed ideas are welcome there.
2. **Concrete idea? Open an issue** using one of the proposal templates
   (new root / new particle family / grammar change). A good proposal states
   what slot it fills, why this form, and shows example sentences.
3. **The language editor decides** (see [GOVERNANCE.md](GOVERNANCE.md)).
   Accepted proposals get the `accepted` label.
4. **A PR lands the change everywhere at once.** The language lives in three
   synchronized places, and CI fails unless they agree:
   - `src/conlang_tools/data/language.json` — the canonical data
   - `docs/spec.md` — the normative prose (roots and particles appear **bolded**,
     which is what the sync test checks for)
   - `docs/index.html` — the guide's inline data block (structural facts only;
     the guide may reword glosses for teaching)

Run the checks locally before pushing:

```bash
uv sync
uv run pytest -q
node scripts/check_guide_sync.mjs
```

### What makes a proposal easy to accept

- It fills a slot the spec already reserves (an unused consonant series, an
  under-populated matrix cell, numbers ≥ 100, conjunctions…).
- It follows the existing design language: series use one consonant crossed
  with `i y e a o u` mapped to a monotone semantic scale; roots are CVCV with
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
- read language data from `constants.py` (which loads `language.json`) —
  never hardcode roots or particles in code.

## Setup

```bash
git clone git@github.com:marbinner/luryt.git
cd luryt
uv sync
uv run pytest -q          # should pass
uv run luryt parse kapirim  # should segment ka-piri-m
```
