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
reading practice. The normative reference is the [foundational spec](https://marbinner.github.io/luryt/spec.html)
([`docs/spec.md`](docs/spec.md) in the repo).

## How the language works, in three rules

1. **Every word wears its shape.** Two-letter words are grammar (particles);
   longer words are vocabulary and always end in one of six consonants. Any
   sentence segments itself.
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
- **numbers above 99**, **conjunctions**, and **complex-clause syntax** are open
- only the K-family works as a prefix so far; more prefix families are anticipated

Proposals go through issues (there are templates), discussion happens in
GitHub Discussions, and accepted changes land as PRs against the spec and data.
See [CONTRIBUTING.md](CONTRIBUTING.md) for the process.

The single machine-readable source of truth is
[`src/conlang_tools/data/language.json`](src/conlang_tools/data/language.json);
CI keeps the spec, the tooling, and the guide honest against it.

## Tooling

A Python package (managed with [uv](https://docs.astral.sh/uv/)) ships with the
language: a parser/validator, reference lookups, and a number converter.

```bash
uv sync                     # install
uv run luryt parse kapirim  # segment + analyze a word
uv run luryt ref particles  # the 14 particle families
uv run luryt num --to-cv 42 # numbers <-> syllables
```

(`uv run conlang …` works too, as an alias.)

## Repository layout

```
docs/spec.md                     the normative language spec (also served on Pages)
docs/index.html                  the interactive guide (GitHub Pages)
src/conlang_tools/               Python tooling
src/conlang_tools/data/language.json   canonical language data
tests/                           parser tests + data/spec integrity checks
scripts/check_guide_sync.mjs     guide <-> data drift check
archive/doc_v15.md              previous official specification
```

## Licensing

- **Code** (`src/`, `tests/`, `scripts/`): [MIT](LICENSE)
- **The language itself** — spec, lexicon data, guide, archive:
  [CC BY-SA 4.0](LICENSE-DOCS.md), so the language and everything derived from
  it stays open.

## About the name

The language has no official name yet. *luryt* is a self-description in the
language's own grammar: `lury` "language, system" + `-t` "this specific one" —
*the language*. Proposals for a real name are welcome (issue template: grammar
change).
