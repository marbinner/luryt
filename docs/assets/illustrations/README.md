# Luryt illustration system

The illustrations referenced by `docs/index.html` were regenerated on
2026-08-15 through OpenRouter's dedicated Image API with:

- model: `google/gemini-3.1-flash-image`
- generation resolution: `2K`
- final delivery: 1920 × 1072 WebP at quality 84
- production refresh: 24 successful generations or edits, 17 selected assets

No API credentials are stored here. The generation key stays in the ignored
project `.env` file.

## Visual reference and art direction

A user-provided spatial-relations infographic was used as a non-shipped style
reference. It established the useful qualities missing from the first set:
explicit mappings, concrete mini-scenes, large readable labels, and a clear
teaching hierarchy.

The corrected word-anatomy result then became the shared style anchor for the
rest of the suite. Each new image followed this direction:

> Polished scientific-educational infographic on a pale cool-blue background;
> crisp vector-like 2.5D illustrations, gentle depth, soft shadows, rounded
> colored teaching modules, strong grid alignment, large black sans-serif
> typography, explicit arrows, concrete mini-scenes, generous whitespace, and
> friendly textbook clarity. The image must explain a rule rather than merely
> symbolize it. No paper-cut collage, abstract blobs, fake writing, tiny text,
> decorative filler, logo, or watermark.

Every brief supplied exact Luryt forms and English labels. Outputs were checked
as review sheets, and images with invented or misleading micro-labels received
narrow edit passes through the same OpenRouter model. HTML captions and alt text
repeat the important relationships for accessibility and small-screen reading.

## Selected teaching briefs

| Asset | Lesson-specific request |
| --- | --- |
| `word-machine-v2.webp` | Four-step overview: sounds → root grid → word assembly → verb-final clause, with `kapirim` as the worked result. |
| `sound-inventory.webp` | The canonical twenty consonants, six vowels, and stress in `ka·PI·rim`. |
| `word-anatomy.webp` | `ka` + `piri` + `m` → `kapirim`, with a concrete scene for every morpheme. |
| `ending-wheel.webp` | Root `zife` branching into the six labeled forms `zifem/t/n/s/l/r`. |
| `semantic-domains-v2.webp` | Six first-vowel domain cards: Person, Society, Life, Physical, Artefact, Abstract. |
| `semantic-aspects.webp` | One token transformed through the six second-vowel aspects. |
| `meaning-grid.webp` | A labeled 6 × 6 domain/aspect matrix with worked roots `piri`, `pase`, and `byru`. |
| `time-scale.webp` | The T-family from `ti` long ago through `tu` timeless. |
| `grouping-scale-v2.webp` | The K-family from `ki` singled through `ku` scattered, plus `ka pirim` versus `kapirim`. |
| `number-encoder.webp` | Exact consonant and vowel indices, the number formula, and 27 → `num te`. |
| `clause-track.webp` | Nine ordered stations ending in the verb, with `te py na ji zifen` as the worked clause. |
| `scope-contrast.webp` | `na qo pirim pasen` contrasted with `qo pirim na pasen` using two concrete crowd scenes. |
| `role-markers.webp` | Builder, house, and tool aligned with `ji`, `koryt re`, `tokim ra`, and `gosen`. |
| `spatial-relations.webp` | Six explicit figure-ground panels for `si sy se sa so su`. |
| `spatial-grammar-v3.webp` | Static location, event setting, and oriented path using the same person and house. |
| `questions-comparison.webp` | W-family missing value beside the C-family less/equal/more/most scale. |
| `parser-diagnostic.webp` | Outside-in parsing of `kapirim` into `ka`, `piri`, and `m`. |
