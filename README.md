<p align="center">
  <img src="https://marbinner.github.io/luryt/assets/luryt-mark.svg" width="112" height="112" alt="Luryt logo">
</p>

# luryt

An engineered constructed language where form computes meaning — 20 consonants,
6 vowels, and a short list of rules from which every word is assembled, and into
which any word can be decomposed again.

```
ka   +   piri   +   m     →   kapirim — "a group of people"
│        │          │
│        │          └─ ending: -m makes an entity ("a thing")
│        └─ root: vowels are coordinates — i = Person domain, i = Individual aspect
└─ prefix: K-family, "as a group"
```

Nothing is irregular. Nothing has to be memorized that could instead be computed.

**Start here → [the interactive guide](https://marbinner.github.io/luryt/)** — the
whole language on one page, with a live word parser, the 6×6 root matrix, and
reading practice. Browse the separate [dictionary](https://marbinner.github.io/luryt/dictionary/),
or consult the normative [foundational spec](https://marbinner.github.io/luryt/spec.html)
([canonical Markdown](language/grammar/foundational.md) in the repo).

## How the language works, in three rules

1. **Every word wears its shape.** Most grammar words are two-letter particles
   (the numeral marker `num` is the sole longer fixed atom); content words end
   in one of six consonants. Any sentence segments itself.
2. **Vowels are coordinates.** A root's first vowel names a domain of reality
   (person, society, life, physical, artefact, abstract); its second names an
   aspect (individual, config, process, state, relation, quantity). A 6×6
   semantic matrix underlies the entire lexicon.
3. **One consonant, six vowels, one scale.** Particle families cross one
   consonant with the six vowels in fixed order `i y e a o u`, sweeping a
   semantic scale — `ti ty te ta to tu`: long ago → timeless.

## Contributing to the language

luryt is deliberately unfinished, and the grammar defines exactly where the
empty slots are:

- **6 consonants** (`b f v z l x`) are reserved for future particle families
  (four already earmarked: mood, coordination, subordination, discourse reference)
- the **36 matrix cells** each hold one core root — with room for many more
- **negative numbers, fractions, decimals, and ordinals**, **conjunctions**, and **complex-clause syntax** are open
- only the K-family works as a prefix so far; more prefix families are anticipated

Proposals go through issues (there are templates), discussion happens in
GitHub Discussions, and accepted changes land as PRs against the canonical
sources. See [CONTRIBUTING.md](CONTRIBUTING.md) for the process.

Canonical language sources live together under [`language/`](language/):
structured facts are modular JSON, and normative grammar is Markdown. A
deterministic compiler validates those sources and produces the identical
machine-readable bundle used by the Python package, guide, and dictionary.

## Tooling

A Python package (managed with [uv](https://docs.astral.sh/uv/)) ships with the
language: a parser/validator, reference lookups, and a number converter.

```bash
uv sync                     # install
uv run luryt parse kapirim  # segment + analyze a word
uv run luryt ref particles  # the 14 particle families
uv run luryt num --to-cv 12345678  # -> me do ly ja
uv run luryt num --to-num "py pi"  # -> 100 (quote a multi-block run)
```

(`uv run conlang …` works too, as an alias.)

## Repository layout

```
docs/spec.md                     generated published spec (served on Pages)
docs/index.html                  the interactive guide (GitHub Pages)
docs/dictionary/                 the data-driven dictionary page
docs/assets/css/ and js/         authored website presentation and behavior
docs/data/language.json          generated website data
language/data/                   canonical structured language facts
language/grammar/foundational.md canonical normative grammar
language/schema/                 compiled-data contract
src/conlang_tools/               Python tooling
src/conlang_tools/data/language.json   generated package snapshot
tests/                           parser tests + data/spec integrity checks
scripts/language.py              validate/generate/check canonical sources
archive/doc_v15.md              previous official specification
```

## Licensing

- **Code** (`src/`, `tests/`, `scripts/`): [MIT](LICENSE)
- **The language itself** — spec, lexicon data, guide, archive:
  [CC BY-SA 4.0](LICENSE-DOCS.md), so the language and everything derived from
  it stays open.

## About the name

The language has no official name yet. *luryt* is a self-description in the
language's own grammar: `lury` "language, system" + `-t` "the identifiable one" —
*the language*. Proposals for a real name are welcome (issue template: grammar
change).

The mark follows the same logic visually: two coordinate paths locate meaning in
the vowel matrix, and the filled cell identifies this particular system.
