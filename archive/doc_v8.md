Here’s a fresh “v3” foundational document with **all** the recent changes baked in: new consonants (C=/ts/, X=/ʃ/, Q=/χ/, R=/ʀ/), 6 vowels (no `'`), fixed C/V order, and the 20×5 CV-digit system.

I’ll keep it structured but not bloated, so you can actually use this as your living spec.

---

# 0. Big Picture

Core design:

* **Simple phonology**: 20 consonants, 6 vowels, syllables = CV or CVC only.
* **Strictly parseable morphology**:

  ```text
  (Time?) (Logic?) (Voice?) (Scale or Space?) (Group?) + CVCV root + PoS suffix
  ```

  with **fixed prefix order** and **one final PoS consonant**.
* **Semantic matrix** for roots:

  * Root = **C V₁ C V₂**
  * V₁ = **Domain** (HUMAN, META, PHYSICS, NATURE, SOCIAL, TECH)
  * V₂ = **Aspect** (FLOW, SYSTEM, FORCE, STATIC, FORM, SUBSTANCE)
* **Numeric layer**:

  * 20 consonants × 5 vowels → **100 CV codes** for 00–99.

This doc sets up **phonology, word structure, semantic typing, and CV codes**. Lexicon and syntax hang off this.

---

# 1. Phonology

## 1.1 Consonants

**Canonical consonant order (used for indexing, CV codes, sorting):**

> **P  B  M  F  V  W  T  D  N  C  S  Z  L  X  J  K  G  Q  R  H**

Articulation: roughly front → back, and within a place: stops → nasals/affricates → fricatives → liquids/approximants.

### Inventory

| Letter | IPA  | Description                      | Example-like sound            |
| ------ | ---- | -------------------------------- | ----------------------------- |
| P      | /p/  | voiceless bilabial stop          | *p* in *spin*                 |
| B      | /b/  | voiced bilabial stop             | *b* in *bat*                  |
| M      | /m/  | bilabial nasal                   | *m* in *map*                  |
| F      | /f/  | voiceless labiodental fricative  | *f* in *fan*                  |
| V      | /v/  | voiced labiodental fricative     | *v* in *van*                  |
| W      | /w/  | labial-velar approximant         | *w* in *we*                   |
| T      | /t/  | voiceless alveolar stop          | *t* in *stop*                 |
| D      | /d/  | voiced alveolar stop             | *d* in *dog*                  |
| N      | /n/  | alveolar nasal                   | *n* in *no*                   |
| C      | /ts/ | voiceless alveolar affricate     | *ts* in *tsar, cats*          |
| S      | /s/  | voiceless alveolar fricative     | *s* in *see*                  |
| Z      | /z/  | voiced alveolar fricative        | *z* in *zoo*                  |
| L      | /l/  | alveolar lateral approximant     | *l* in *lip*                  |
| X      | /ʃ/  | voiceless postalveolar fricative | *sh* in *she, ship*           |
| J      | /j/  | palatal approximant              | *y* in *yes*                  |
| K      | /k/  | voiceless velar stop             | *k* in *cat*                  |
| G      | /g/  | voiced velar stop                | *g* in *go*                   |
| Q      | /χ/  | voiceless uvular fricative       | German *Bach*, Scots *loch*   |
| R      | /ʀ/  | uvular trill (often [ʁ])         | “guttural R” in French/German |
| H      | /h/  | voiceless glottal fricative      | *h* in *hat*                  |

**Terminal consonants** (allowed word-final and used as PoS suffixes):

> **L, M, N, R, S, T**

---

## 1.2 Vowels

**Canonical vowel order (front → back, high → low):**

> **I  Y  E  A  O  U**

| Letter | IPA | Description          | Example-ish           |
| ------ | --- | -------------------- | --------------------- |
| I      | /i/ | high front unrounded | *i* in *machine*      |
| Y      | /y/ | high front rounded   | German *ü*            |
| E      | /e/ | mid front unrounded  | *é* / many “e” values |
| A      | /a/ | low (front/central)  | *a* in *father*       |
| O      | /o/ | mid back rounded     | pure “o”              |
| U      | /u/ | high back rounded    | *u* in *food*         |

* All **CVCV roots** use these 6 vowels.
* **Numeric CV codes** use only **I, Y, E, A, O** (see §4; U is not used in CV-digits).

---

## 1.3 Syllable Structure & Stress

* Allowed syllables: **CV** or **CVC**.
* No consonant clusters; no onsetless syllables.
* Stress is always on the **penultimate syllable** of the word.

Examples (schematic):

* **GA-ra**, **ga-RAM**, **ma-GA-ram**.

---

# 2. Word Structure

## 2.1 Word Classes

1. **Atomic words**

   * Mostly **CV**, plus a few fixed longer particles.
   * Closed classes: pronouns, demonstratives, prepositions, conjunctions, auxiliaries, wh-words, quantifiers, numeric CV codes, some particles.
   * No productive internal morphology.

2. **Content words**

   * Exactly one **CVCV root**.
   * Up to **five CV prefixes** from fixed series (R/N/D/M-S/K).
   * Exactly one final **PoS suffix** (L/M/N/R/S/T).
   * Open classes: nouns, verbs, adjectives, adverbs, determiners.

---

## 2.2 Content Word Template

```text
[Time] [Logic] [Voice] [Scale or Space] [Group] + CVCV root + PoS suffix
```

Slots (left → right):

1. **Time**: R- series (Ra/Ri/Re/Ro/Ru/Ry…)
2. **Logic**: N- series
3. **Voice**: D- series
4. **Scale**: M- series *or* **Space**: S- series (mutually exclusive)
5. **Group**: K- series
6. Root: **C₁ V₁ C₂ V₂**
7. PoS suffix: one of **L, M, N, R, S, T**

Constraints:

* At most one prefix from each series (R, N, D, M/S, K).
* At most one of M-/S- (Scale vs Space).
* Series must appear in this slot order if present.

---

## 2.3 Part-of-Speech Suffixes

Final consonant = PoS marker:

| Suffix | PoS | Function                       |
| ------ | --- | ------------------------------ |
| -M     | N   | noun (entity)                  |
| -S     | ADJ | adjective (quality)            |
| -N     | V   | finite verb                    |
| -L     | ADV | adverb (manner/place/etc.)     |
| -R     | GEN | genitive “of X”                |
| -T     | DET | determiner / specific instance |

Content words *always* carry one of these in running text; bare CVCV roots are lexicon-only.

---

## 2.4 Prefix Series (Summary)

All prefixes are **CV** with consonant from {R, N, D, M, S, K}.

* **Time (slot 1, R-)**

  * Ra- past / before
  * Ri- future / after
  * Re- completed
  * Ro- ongoing / during
  * Ru- speed/tempo
  * Ry- again/repeated

* **Logic (slot 2, N-)**

  * Na- asserted / true
  * Ne- not / negative
  * Ny- maybe / possible
  * Nu- if / conditional
  * (others as needed)

* **Voice (slot 3, D-)**

  * Da- causative (“make X V”)
  * Di- middle/reflexive
  * Do- reciprocal (“each other”)
  * Du- passive/undergo
  * Dy- inchoative (“begin, become V”)

* **Scale (slot 4a, M-)**

  * Ma- big/large
  * Mi- small
  * Me- neutral/average
  * Mo- mass/collective
  * My- variable/changing
  * Mu- “shaped for / instrument” (especially in derivation)

* **Space (slot 4b, S-)** — spatial configuration/direction

  * Sa- out/from
  * Si- in/into
  * Se- away/off
  * So- around
  * Su- at/located at
  * Sy- through/across

* **Group (slot 5, K-)**

  * Ka- all/union
  * Ki- some/part
  * Ke- none/void
  * Ko- group, plural set
  * Ky- ordered series
  * Ku- link/relationship

(You can keep all your old detailed semantics; structurally this is unchanged.)

---

## 2.5 Parsing Content Words

Given a lowercased token:

1. If length = 2 and matches **C V** (C in consonant set, V in {i,y,e,a,o,u}) → **atomic word**.
2. Else, attempt content word parse:

   1. Check final char ∈ {l, m, n, r, s, t} → PoS suffix.
   2. Take the preceding 4 letters as the **CVCV root**.
   3. Remaining prefix string (possibly empty) must be a sequence of **CV** prefixes.
   4. Parse prefixes left→right, enforcing:

      * each prefix consonant ∈ {r, n, d, m, s, k};
      * no more than one prefix from each series;
      * at most one of M-/S-;
      * series appear in slot order: Time → Logic → Voice → Scale/Space → Group.
3. If all checks pass, segmentation is unique and valid.

This guarantees **deterministic morphological segmentation**.

---

# 3. Semantic Matrix of Roots

Each root is **C₁ V₁ C₂ V₂**, with the consonants largely free and **the two vowels doing the semantic typing**:

* **V₁** = **Domain** (what “world” it talks about)
* **V₂** = **Aspect** (how we view that world: process, system, material, etc.)

Both V₁ and V₂ are from:

> **I  Y  E  A  O  U**

---

## 3.1 Domains (V₁)

Suggested:

| V₁ | Domain  | Scope                                              |
| -- | ------- | -------------------------------------------------- |
| I  | HUMAN   | bodies, minds, individual psychology, self         |
| Y  | META    | logic, math, data, abstractions, models            |
| E  | PHYSICS | space, geometry, physical law, measurable fields   |
| A  | NATURE  | environment, terrain, weather, non-human life      |
| O  | SOCIAL  | persons, norms, roles, communication, institutions |
| U  | TECH    | tools, artifacts, machines, infrastructure         |

Pairs:

* I–O: individual vs social/institutional.
* A–E: concrete environment vs abstract physical structure.
* U–Y: concrete artifacts vs abstract systems/models.

---

## 3.2 Aspects (V₂)

Suggested:

| V₂ | Aspect    | Scope                                                  |
| -- | --------- | ------------------------------------------------------ |
| I  | FLOW      | events, processes, motion, interactions, actions       |
| Y  | SYSTEM    | networks, organized systems, cycles, multi-part wholes |
| E  | FORCE     | energy, intensity, capacity, potential to cause change |
| A  | STATIC    | regions, shapes, persistent configurations             |
| O  | FORM      | patterns, representations, conceptual forms/images     |
| U  | SUBSTANCE | matter, stuff, resources, consumables, “what of”       |

Heuristics:

* (A, U) = static vs substance (object vs stuff).
* (E, I) = potential vs process.
* (O, Y) = form vs system.

---

## 3.3 HeadKind from Suffixes / Derivations

For any surface **content word**:

* Root vowel pair gives **Domain, Aspect**.
* PoS suffix and certain derivational prefixes choose **HeadKind**.

Basic mapping:

* `root + -M / -R / -T` → **Entity<Domain,Aspect>**
* `root + -N` → **Event<Domain,Aspect>**
* `root + -S` → **Property<Domain,Aspect>**
* `root + -L` → **Manner<Domain,Aspect>**

Optional derivational patterns (same as before):

* **Na- + root + -M** → abstract event/state

  * e.g. “sleeping”, “conflict” as an abstract state.
* **Ka- + root + -M** → agent/doer

  * “sleeper”, “fighter”, “giver”.
* **Mu- + root + -M** → instrument/tool

  * “sleeping aid”, “weapon”, “tool for X”.

TAM/Voice prefixes (Ra-, Ne-, Da-, Du-…) enrich the event with tense, negation, valency, etc. without touching Domain/Aspect.

---

# 4. CV Codes for 00–99

We exploit:

* **20 consonants** (in canonical order), and
* **5 numeric vowels** (subset of the 6 vowel set),

to get exactly **100 distinct CV syllables**.

## 4.1 Consonants & Vowels for Codes

**Consonant list for digits (C_index 0–19):**

0. P
1. B
2. M
3. F
4. V
5. W
6. T
7. D
8. N
9. C
10. S
11. Z
12. L
13. X
14. J
15. K
16. G
17. Q
18. R
19. H

**Numeric vowels (V_index 0–4):**

> **I, Y, E, A, O**

---

## 4.2 Number → CV

For any integer **d** with 0 ≤ d ≤ 99:

```text
c_index = d // 5      # 0–19
v_index = d % 5       # 0–4

CV(d) = C[c_index] + V[v_index]
```

### Examples

Block 0 (C = P, c_index = 0):

* 00 → **PI**
* 01 → **PY**
* 02 → **PE**
* 03 → **PA**
* 04 → **PO**

Block 1 (C = B, c_index = 1):

* 05 → **BI**
* 06 → **BY**
* 07 → **BE**
* 08 → **BA**
* 09 → **BO**

Block 2 (C = M, c_index = 2):

* 10 → **MI**
* 11 → **MY**
* 12 → **ME**
* 13 → **MA**
* 14 → **MO**

…

Last block (C = H, c_index = 19):

* 95 → **HI**
* 96 → **HY**
* 97 → **HE**
* 98 → **HA**
* 99 → **HO**

---

## 4.3 CV → Number

Given a CV syllable where:

* C is one of the 20 consonants in order above,
* V is one of {I, Y, E, A, O},

you can recover its number:

```text
d = 5 * c_index + v_index
```

using the indices of that C and V in their lists.

These CV forms can be:

* atomic numerals,
* mnemonic codes,
* or just a structured “two-digit syllable” system you reuse elsewhere.

---

# 5. Atomic Core (Mini Skeleton)

These are outside the CVCV-root system; they’re just CV (or fixed) forms.

## 5.1 Pronouns

| Word | Person/Number | Meaning    |
| ---- | ------------- | ---------- |
| Mi   | 1sg           | I / me     |
| Ma   | 1pl           | we / us    |
| Ti   | 2sg           | you (sg)   |
| Ta   | 2pl           | you (pl)   |
| Si   | 3sg           | he/she/it  |
| Sa   | 3pl           | they       |
| Su   | 3 impers      | dummy “it” |

## 5.2 Demonstratives (K-series)

| Word | Features     | Meaning                     |
| ---- | ------------ | --------------------------- |
| Ka   | proximal, sg | this                        |
| Ke   | proximal, pl | these                       |
| Ki   | medial, sg   | that (near hearer/context)  |
| Ko   | medial, pl   | those (near hearer/context) |
| Ku   | distal, sg   | that (far)                  |
| Ky   | distal, pl   | those (far)                 |

## 5.3 G-series Prepositions

| Word | Role         | Meaning                    |
| ---- | ------------ | -------------------------- |
| Ga   | SOURCE/STD   | from, out of, than         |
| Ge   | GOAL         | to, towards                |
| Gi   | LOCATION     | in, at, on                 |
| Go   | PATH/MEDIUM  | via, along, through        |
| Gu   | INSTR/COMIT  | with, using, together with |
| Gy   | CAUSE/REASON | because of, due to         |

## 5.4 Particles & Auxiliaries (examples)

* Ja — and

* Je — or

* Jo — yes / yes–no question marker

* Ju — no

* Nu — if (subordinator)

* Lo — that (complementizer)

* Ba — be

* Va — have

* Vi — do/perform

* La — must / necessary

* Le — can / be able

* Li — want / intend

All of these stay “outside” the CVCV root morphology; they’re just atomic items.

---

# 6. Syntax (Very Short Skeleton)

You can keep the same basic syntax as in your earlier version:

* **Clause order:** SVO.

  ```text
  [Frame adv*] [Subject NP] [Aux*] [Verb] [Object NP*] [Adv(-L)*] [PP*]
  ```

* **Role marking:**

  * Subject position = agent-like.
  * Object position = patient-like.
  * G-series PPs for source/goal/instrument/etc.

* **NP structure:**

  ```text
  [Number/Quant] [Dem] [Head N-M/T (+ Ko-)] [Adj-S*] [Genitive N-R?] [RelClause*] [PP*]
  ```

* **Questions:**

  * Wh-questions: F-series wh-word fronted + clause.
  * Yes/no: Jo + clause.

* **Conditionals:**

  * Nu + protasis, then apodosis.

You can re-import your detailed syntax from the previous doc almost verbatim; nothing in the phonology changes the basic syntactic design.

---

If you’d like, next step I can help you:

* rebuild the **6×6 domain/aspect table cell-by-cell** with more precise labels, or
* start designing a **new root lexicon** that deliberately populates the grid with your favorite semantic neighborhoods.
