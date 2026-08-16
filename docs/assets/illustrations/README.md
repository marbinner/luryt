# Luryt visual teaching system

The main guide uses a hybrid visual system as of 2026-08-15:

- seventeen responsive HTML/SVG teaching diagrams rendered from the same
  JavaScript data that powers the guide;
- twelve text-free scene fragments for concepts that benefit from concrete
  people, objects, and places;
- ordinary live text for every Luryt form, English gloss, formula, label, and
  arrow.

This keeps the information layer exact and readable at any width. The diagrams
include the complete sound inventory, all 36 semantic root cells, full six-form
particle scales, number indices, clause slots, worked contrasts, and parser
decisions. They reflow on small screens instead of shrinking a 16:9 screenshot.

## OpenRouter scene generation

Four source plates were generated through OpenRouter's dedicated Image API
using the requested model:

- model: `google/gemini-3.1-flash-image`
- resolution: `2K`
- source aspect ratio: `16:9`
- successful generation calls: 4
- recorded generation cost: $0.4075785

The four briefs covered semantic domains, event roles, spatial grammar, and
quantifier scope. A user-provided spatial-relations infographic was supplied as
a style-only reference. It established the shared direction: pale cool-blue
teaching plates, crisp 2.5D vector-like scenes, dark outlines, a restrained
six-color palette, clear separation, and concrete relationships.

The model was explicitly asked not to draw words. Where it nevertheless added
headings to two source plates, those regions were cropped out. No model-rendered
text appears on the page.

No API credential is stored here. The OpenRouter key remains in the ignored
project `.env` file.

## Selected scene fragments

| Assets | Use |
| --- | --- |
| `scene-domain-{i,y,e,a,o,u}.webp` | Six concrete anchors for Person, Society, Life, Physical, Artefact, and Abstract. |
| `scene-role-builder.webp` | One construction event containing an agent, recipient, patient, instrument, location, and path. |
| `scene-space-{static,setting,path}.webp` | The same person and house across static location, an event setting, and directed motion. |
| `scene-scope-{not-all,none}.webp` | Matched gate scenes for “not all go” versus “all do not go.” |

The scene fragments are decorative support for the adjacent live labels. Their
meaning is also present as accessible text inside each diagram.

## Shared scene brief

> Polished scientific-educational illustration with crisp vector-like 2.5D
> objects, a pale cool-blue and white background, precise dark outlines,
> restrained shadows, and a coherent six-color teaching palette. Use concrete,
> instantly recognizable objects and people, strong grid alignment, generous
> clear space, and textbook clarity. Do not draw text, letters, numbers, labels,
> captions, logos, watermarks, paper-cut collage, abstract filler, or
> photorealism.

Legacy full-frame WebP infographics remain in this directory for now, but
`docs/index.html` no longer references them.
