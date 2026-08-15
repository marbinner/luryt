# Luryt illustration system

The illustrations referenced by `docs/index.html` were generated on 2026-08-15
through OpenRouter's Image API with:

- model: `google/gemini-3.1-flash-image`
- resolution: `1K`
- output workflow: model output → visually curated → WebP at quality 82
- production run: 23 successful generations, 17 selected assets

No API credentials are stored here. Exact linguistic labels remain in HTML so
they are selectable, accessible, and independent of generated pixels.

## Shared art-direction prompt

> Front-on archival cut-paper relief and screenprinted scientific field-guide
> diagram on warm off-white fibrous paper. Charcoal structure, deep forest-green
> paths, and six recurring vowel accents: cobalt, violet, green, ochre,
> vermilion, magenta. Soft diffuse upper-left light, subtle paper-layer shadows,
> crisp geometric silhouettes, restrained museum-catalog polish. Clear at small
> website sizes. No written text, letters, numbers, labels, logos, watermark,
> border, pseudo-writing, glossy 3D, or decorative clutter.

After the hero established this style, it was supplied as the style-only image
reference for every new concept. Correction passes used the previous candidate
as the edit target and changed only the stated count or forbidden-text issue.

## Selected prompt set

| Asset | Lesson-specific request |
| --- | --- |
| `word-machine-v2.webp` | Three linked stations: optional two-part module, four-slot root chamber, six-position ending selector. |
| `sound-inventory.webp` | Five banks of four consonant keys above exactly six colored vowel resonators. |
| `word-anatomy.webp` | Optional two-cell chips, one four-cell root with vowel inlays, and one ending selector. |
| `ending-wheel.webp` | One semantic seed branching into six grammatical outcomes. |
| `semantic-domains-v2.webp` | Six domain dioramas in a 3×2 grid: person, society, life, physical, artefact, abstract. |
| `semantic-aspects.webp` | One token viewed as individual, configuration, process, state, relation, and quantity. |
| `meaning-grid.webp` | Exact 6×6 cabinet of 36 drawers selected by one row and one column. |
| `time-scale.webp` | Six stages from remote past through present and future to timelessness. |
| `grouping-scale-v2.webp` | Six configurations from one singled-out token to a dispersed set. |
| `number-encoder.webp` | Four trays of five consonant positions plus exactly five vowel sockets. |
| `clause-track.webp` | Six optional operator stations, participants, and a final action module. |
| `scope-contrast.webp` | Two panels contrasting partial passage with a barrier stopping the entire group. |
| `role-markers.webp` | Builder, affected house, and instrument connected by role-marked action paths. |
| `spatial-relations.webp` | The same figure shown inside, on, beside, around, outside, and among. |
| `spatial-grammar-v3.webp` | Static location, event setting, and one-figure outside-to-inside path. |
| `questions-comparison.webp` | Unknown-participant search paired with a short-to-tall degree scale. |
| `parser-diagnostic.webp` | A blank strip separated into prefix chips, four-cell root, and ending selector. |
