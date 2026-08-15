# Governance

## The short version

Anyone can propose. One person decides. Everything is recorded.

## Roles

**Language editor** — [@marbinner](https://github.com/marbinner), the
language's creator. The editor has final say over changes to the language
itself: phonology, grammar, the particle inventory, the lexicon, and the spec's
normative text. This is deliberate: languages designed by majority vote drift
into incoherence, and luryt's value is its internal consistency.

**Contributors** — everyone else, including future co-maintainers the editor
may appoint. Contributors drive Discussions, file proposals, review each
other's ideas, and maintain the tooling.

## How a language change happens

1. A proposal is filed as an issue (templates exist for roots, particle
   families, and grammar changes).
2. Open discussion. The editor may ask for revisions, alternatives, or example
   sentences.
3. The editor labels it `accepted` or `declined`, with a stated reason either
   way. Declined proposals stay visible — they are part of the design record.
4. Accepted proposals are implemented in a PR that updates the canonical data
   (`language.json`), the spec, and the guide together. CI enforces that the
   three agree. Merging the PR is what makes a change official.

## What this does and doesn't cover

- **Covered (editor decides):** anything that changes what is or isn't valid
  luryt, or what any form means.
- **Not covered (normal open-source rules):** the Python tooling, the website,
  tests, CI, docs wording that doesn't change meaning. Maintainers merge these
  on ordinary code-review judgment.

## Stability promise

The spec's §0 lists what is **fixed** (phonology, word structure, the suffix
system, the matrix, existing series) and what is **open**. Fixed things change
only for serious reasons and are versioned loudly when they do; the `archive/`
directory preserves every prior spec version as the design record.
