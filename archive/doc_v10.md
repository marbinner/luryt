Here’s the updated **foundation doc** with the new semantic matrix fully locked in. Anything in here we now treat as *fixed*. Everything else (prefix meanings, particles, syntax details) stays open for later.

---

# 0. Scope

**Fixed now:**

* Consonant inventory **and canonical order**
* Vowel inventory **and canonical order**
* Syllable structure & stress
* Two word types: **atomic CV** vs **content words**
* Content-word template: **(CV prefixes) + CVCV root + final suffix**
* Final suffix system: **M T N S L R** and what each means
* Principle that **CV series use one consonant + vowels in I Y E A O U order**
* Root semantics: **6 Domains × 6 Aspects** (the matrix below)
* Numeric **00–99 → CV** system

**Still open (not fixed yet):**

* Which consonants are used as **prefix series** (Time, Scale, Logic, Voice, etc.)
* Exact set and meaning of **particles** (pronouns, preps, conjunctions, etc.)
* Concrete **lexicon** (except a few illustration examples)
* Detailed **syntax** and derivational patterns

---

# 1. Phonology

## 1.1 Consonants

Canonical consonant order (used for indexing, sorting, numeric codes):

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

| Letter | IPA  | Description                             |
| ------ | ---- | --------------------------------------- |
| P      | /p/  | bilabial voiceless stop                 |
| B      | /b/  | bilabial voiced stop                    |
| M      | /m/  | bilabial nasal                          |
| F      | /f/  | labiodental voiceless fricative         |
| V      | /v/  | labiodental voiced fricative            |
| T      | /t/  | alveolar voiceless stop                 |
| D      | /d/  | alveolar voiced stop                    |
| N      | /n/  | alveolar nasal                          |
| Q      | /ts/ | alveolar voiceless affricate            |
| S      | /s/  | alveolar voiceless fricative            |
| Z      | /z/  | alveolar voiced fricative               |
| L      | /l/  | alveolar lateral approximant            |
| C      | /tʃ/ | postalveolar voiceless affricate (“ch”) |
| W      | /dʒ/ | postalveolar voiced affricate (“j”)     |
| X      | /ʃ/  | postalveolar voiceless fricative (“sh”) |
| J      | /j/  | palatal approximant (“y”)               |
| K      | /k/  | velar voiceless stop                    |
| G      | /g/  | velar voiced stop                       |
| R      | /ʀ/  | uvular trill (or [ʁ])                   |
| H      | /h/  | glottal voiceless fricative             |

**Final consonant pool (suffixes):**

In canonical order:

> **M  T  N  S  L  R**

Only these six may appear as the **final consonant of a content word**.

---

## 1.2 Vowels

Canonical vowel order:

> **I  Y  E  A  O  U**

| Letter | IPA | Description          |
| ------ | --- | -------------------- |
| I      | /i/ | high front unrounded |
| Y      | /y/ | high front rounded   |
| E      | /e/ | mid front unrounded  |
| A      | /a/ | low (front/central)  |
| O      | /o/ | mid back rounded     |
| U      | /u/ | high back rounded    |

This order is used for:

* groupings / series (Time series, wh-series, etc.)
* root semantic matrix (V₁, V₂)
* numeric CV codes (first 5 vowels)

---

## 1.3 Syllable Structure & Stress

* Allowed syllables: **CV** or **CVC**
* No onsetless syllables; no consonant clusters
* **Stress**: always on the **penultimate syllable** of the word

---

# 2. Word Structure

## 2.1 Two Word Types

1. **Atomic words (particles)**

   * Shape: typically **CV**; a few fixed longer forms allowed
   * Used for: pronouns, demonstratives, prepositions, conjunctions, auxiliaries, particles, digits, etc.
   * **No productive morphology** (no prefixes/suffixes in the core system)

2. **Content words**

   * Exactly **one CVCV root**

   * Optional **prefix block** of one or more **CV prefixes**

   * Exactly **one final consonant suffix** from {M, T, N, S, L, R}

   * Surface template:

     ```text
     (CV prefix)* + CVCV (root) + final suffix (M/T/N/S/L/R)
     ```

   * Open-class lexemes: all “content” meanings (entity, event, property, etc.)

In running text:

* bare **CV** → atomic word or numeric CV code
* **CVCV + suffix** → content word

---

## 2.2 Final Suffix System (Head Kinds)

Final suffix set (canonical order):

> **-M  -T  -N  -S  -L  -R**

Each encodes a **head kind**:

| Suffix | Head kind            | Function / typical use                            |
| ------ | -------------------- | ------------------------------------------------- |
| **-M** | Entity head          | generic noun: “an X-thing / X-entity”             |
| **-T** | Specific entity head | specific/determiner-ish: “that/the X”             |
| **-N** | Event head           | verb: “to X / X happens”                          |
| **-S** | Property head        | adjective: “X-like, having X-property”            |
| **-L** | Manner head          | adverb: “X-ly, in an X way”                       |
| **-R** | Relational head      | genitive/relational NP: “of X, X’s, from X, etc.” |

We **do not** add more suffix classes later. Extra roles (agent, tool, gerund, etc.) are derived with **prefix patterns** + these six head kinds.

---

## 2.3 Content Word Template & Parsing

**Template:**

```text
[Prefix Block] + C₁ V₁ C₂ V₂ (root) + [FinalSuffix]
```

* Prefix Block: zero or more **CV** prefixes
* Root: exactly **CVCV**
* FinalSuffix: one consonant from **M T N S L R**

**Parsing algorithm (fixed):**

Given a token (lowercase):

1. If length = 2 and matches `C V` → treat as **atomic CV word** (or numeric code).
2. Else:

   * If final char ∉ `{m, t, n, s, l, r}` → **not** a well-formed content word.
   * Else:

     * final char = **FinalSuffix**
     * preceding 4 chars must be **C V C V** → the **root**
     * any remaining leftmost chars must form a **Prefix Block** = sequence of **CV** chunks (later restricted by prefix series rules).

If that holds, segmentation is unique:

```text
(CV prefix)*  +  CVCV(root)  + 1 suffix
```

---

## 2.4 Series Principle for CV Prefixes & Particles

We fix a structural rule:

> Any **series** (Time prefixes, wh-words, demonstratives, etc.) uses:
>
> * **one consonant**,
> * all six vowels in canonical order **I Y E A O U**,
> * and maps that vowel order to a semantic gradient.

So for any series with consonant **X**:

> Xi, Xy, Xe, Xa, Xo, Xu

are the six elements, ordered, and their meanings must follow some internally consistent progression.

(We haven’t chosen which consonants/meanings yet; just the pattern.)

---

# 3. Root Semantics: 6×6 Matrix (Locked)

Every content root is **C₁ V₁ C₂ V₂**.

* **V₁ (first vowel)** → **Domain** (row) — which “world”
* **V₂ (second vowel)** → **Aspect** (column) — what “concept shape”

Both use the vowel order:

> **I  Y  E  A  O  U**

So there are **6 Domains × 6 Aspects = 36** semantic buckets.
Each root belongs to exactly one bucket.

## 3.1 Domains (Rows, V₁)

> “Which world-layer is this concept about?”

| V₁ | Domain   | World covered                                        |
| -- | -------- | ---------------------------------------------------- |
| I  | PERSON   | individual humans: body, mind, experience            |
| Y  | SOCIETY  | families, groups, institutions, culture              |
| E  | LIFE     | non-human living things: animals, plants, ecosystems |
| A  | PHYSICAL | non-living world: space, matter, energy, weather     |
| O  | ARTEFACT | tools, objects, machines, buildings, infrastructure  |
| U  | ABSTRACT | ideas, language, math, logic, information            |

Pairs:

* (I, Y) → individual vs social
* (E, A) → living vs nonliving environment
* (O, U) → concrete artefact vs abstract system

---

## 3.2 Aspects (Columns, V₂)

> “What kind of conceptual shape is this?”

| V₂ | Aspect     | Intuition                                                                         |
| -- | ---------- | --------------------------------------------------------------------------------- |
| I  | INDIVIDUAL | basic “things/actors” of that domain (person, animal, tree, tool)                 |
| Y  | CONFIG     | parts, wholes, groups, layouts, structures, systems (body, forest, city, network) |
| E  | PROCESS    | activities, processes, changes, doing (run, grow, trade, think)                   |
| A  | STATE      | relatively stable conditions/qualities (alive, hot, hungry, broken)               |
| O  | RELATION   | links/roles between things (friend-of, parent-of, in, above, equal-to)            |
| U  | QUANTITY   | measures, magnitudes, degrees (number, distance, strength, price)                 |

Pairs:

* (I, Y) → individual vs whole/structure
* (E, A) → change vs condition
* (O, U) → link vs amount

These are **ontological**, not “noun/verb/adjective” — PoS is handled by suffixes.

---

## 3.3 Matrix Overview (Examples)

Short sketch with typical concept types in each cell:

|            | I = INDIVIDUAL          | Y = CONFIG                | E = PROCESS              | A = STATE                    | O = RELATION                 | U = QUANTITY                |
| ---------: | ----------------------- | ------------------------- | ------------------------ | ---------------------------- | ---------------------------- | --------------------------- |
|   I PERSON | person, self            | body, hand, heart, family | act, speak, eat, see     | hungry, tired, sad, healthy  | friend-of, parent-of         | age, strength, habit freq   |
|  Y SOCIETY | group, tribe, city      | institution, hierarchy    | trade, talk, fight, vote | peace, war, crisis, trust    | citizen-of, boss-of, rule    | money, price, wealth        |
|     E LIFE | animal, plant           | forest, herd, ecosystem   | grow, hunt, migrate      | alive, dead, sick, poisonous | predator-of, symbiont-of     | population, biomass, yield  |
| A PHYSICAL | rock, river, mountain   | landscape, region         | flow, fall, rain, blow   | hot, cold, solid, liquid     | in, on, under, near, around  | length, mass, time, energy  |
| O ARTEFACT | tool, knife, cup, phone | house, road, car, network | cut, build, drive, send  | broken, fixed, open, off     | key-of, lock-for, plug-in    | size, capacity, speed       |
| U ABSTRACT | idea, word, symbol      | theory, language, model   | think, learn, compute    | know, believe, remember      | cause-of, equal-to, means-of | number, amount, probability |

Examples of **where your earlier concerns land**:

* “animal”, “plant” → LIFE × INDIVIDUAL (E–I)
* “forest”, “herd” → LIFE × CONFIG (E–Y)
* “hand”, “heart”, “eye” → PERSON × CONFIG (I–Y)
* “tool” → ARTEFACT × INDIVIDUAL (O–I)
* “house” → ARTEFACT × CONFIG (O–Y)
* “friendship / friend-role” → SOCIETY × RELATION (Y–O) or PERSON × RELATION (I–O), depending on perspective
* “number” → ABSTRACT × QUANTITY (U–U)

When we coin roots later, we pick:

1. Domain (row) and Aspect (column) → choose **V₁, V₂**.
2. Two consonants **C₁, C₂** → make **C₁ V₁ C₂ V₂** = root.

Suffix then chooses how we talk about it.

---

# 4. Interaction: Matrix × Suffixes (Pattern)

Given a root in some cell (Domain×Aspect), say **C₁ V₁ C₂ V₂ = R**:

* **R-M** → entity head: “an R-thing”
* **R-T** → specific entity: “that/the R-thing”
* **R-N** → event: “to R / R happens”
* **R-S** → property: “R-like, having R”
* **R-L** → manner: “R-ly, in an R way”
* **R-R** → relational noun: “of R / R’s / [X related-by-R]”

Example sketch (friend-type SOCIAL×RELATION root, say **syro** in Y–O):

* **syrom** — a friend (entity)
* **syrot** — that friend
* **syron** — to befriend / to be friends / act as a friend
* **syros** — friendly
* **syrol** — in a friendly way
* **syror** — of a friend / friend’s

Matrix: “SOCIAL RELATION concept”.
Suffix: PoS and head-kind.

Prefixes (later) will add **time, scale, logic, voice, derivation**.

---

# 5. Numeric CV System (00–99)

We keep the previously fixed CV-number system.

## 5.1 Consonant and Vowel Indices

Consonants in canonical order, used for `c_index`:

0. P
1. B
2. M
3. F
4. V
5. T
6. D
7. N
8. Q
9. S
10. Z
11. L
12. C
13. W
14. X
15. J
16. K
17. G
18. R
19. H

Vowels for the numeric system use the **first 5** vowels in canonical order, index `v_index`:

0. I
1. Y
2. E
3. A
4. O

(U is not used for 00–99.)

## 5.2 Mapping Number → CV

For any integer **d** with 0 ≤ d ≤ 99:

```text
c_index = d // 5      # 0..19
v_index = d % 5       # 0..4

CV(d) = C[c_index] + V[v_index]
```

Examples:

* 00 → **PI**

* 01 → **PY**

* 02 → **PE**

* 03 → **PA**

* 04 → **PO**

* 05 → **BI**

* 06 → **BY**

* …

* 95 → **HI**

* 96 → **HY**

* 97 → **HE**

* 98 → **HA**

* 99 → **HO**

Inverse: given a CV with C in the consonant list and V in {I,Y,E,A,O}, recover d by:

```text
d = 5 * c_index + v_index
```

These CVs can function as:

* atomic numerals,
* labels/codes,
* and (where sensible) also as particles, disambiguated by context.

---

This locks in:

* phonology & orthographic constraints,
* word-shape architecture (atomic CV vs prefixed CVCV+suffix),
* final suffix system and head kinds,
* series structure for CV prefixes/particles,
* the 6×6 **semantic matrix** (Domains × Aspects),
* numeric CV coding.

Next step, when you’re ready, is to start fixing a **prefix system** (Time, Scale, Logic, Voice, plus Esperanto-style derivational prefixes) that plays nicely with this matrix.
