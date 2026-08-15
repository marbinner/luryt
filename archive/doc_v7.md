# The Language

This document contains everything needed to **use** the language: phonology, morphology, semantic matrix, lexicon, syntax, derivation, numerals, pronouns/demonstratives, and semantic typing.

---

## 0. Design Philosophy

1. **Strict parsability**

  Content words follow a fixed template:

  ```text
  (Time?) (Logic?) (Voice?) (Scale or Space?) (Group?) + CVCV root + (PoS suffix)
  ```

In running text, every content word ends in exactly one **part-of-speech suffix**; bare CVCV roots appear only in the **lexicon**, not in normal sentences.

Strict parsability means **morphological segmentation is deterministic**: for any surface form you can uniquely recover prefixes, root, and suffix.

It does **not** mean that every CV syllable has a single function. Forms like *ra* can be both:

* a free atomic word (*ra* “before”), and
* a bound prefix (*Ra-* Time=PST),

but they are disambiguated by **word length** and **position in the template**.

2. **Two word classes**

   * **Atomic words**

     * Mostly **CV**, plus a few fixed multi-syllabic particles.
     * Pronouns, demonstratives, conjunctions, prepositions, auxiliaries, digits, wh-words, quantifiers, complementizers.
     * No productive affixes in the core grammar.

   * **Content words**

     * One **CVCV root**, optionally with up to five **CV prefixes** (R/N/D/M/S/K series) and one final suffix.
     * Open-class lexemes (nouns, verbs, adjectives, adverbs, determiners).

3. **Semantic matrix**

   * CVCV root structure: **C V₁ C V₂**.
   * **V₁** (first vowel) = **domain** (Nature / Physics / Human / Social / Tech / Meta).
   * **V₂** (second vowel) = **semantic aspect** (Region / Matter / Force / Flow / Form / System).
   * Each root is assigned to **exactly one** cell in a 6×6 domain×aspect grid (multiple roots can share a cell).

---

## 0.5 Quick Reference

**Phoneme sets**

* Consonants (C): **B, D, F, G, J, K, L, M, N, P, R, S, T, V**
* Vowels (V): **A, E, I, O, U, Y**

**Content word template**

```text
[Time (R)] [Logic (N)] [Voice (D)] [Scale (M) | Space (S)] [Group (K)] + CVCV root + PoS suffix
```

* Time: R- series (Ra, Ri, Re, Ro, Ry, Ru)
* Logic: N- series (Na, Ni, Ne, No, Ny, Nu)
* Voice: D- series (Da, Di, De, Do, Du, Dy)
* Scale: M- series (Ma, Mi, Me, Mo, My, Mu)
* Space: S- series (Sa, Si, Se, So, Sy, Su)
* Group: K- series (Ka, Ki, Ke, Ko, Ky, Ku)

> At most one prefix from each series; **Scale** and **Space** compete for slot 4 (only one of M-/S-).

**PoS suffixes (obligatory on content words)**

| Suffix | PoS | Function                       |
| :----- | :-- | :----------------------------- |
| -M     | N   | Noun (entity)                  |
| -S     | ADJ | Adjective (quality)            |
| -N     | V   | Verb (finite)                  |
| -L     | ADV | Adverb (manner/location)       |
| -R     | GEN | Genitive (“of X”)              |
| -T     | DET | Specific instance / determiner |

**Canonical clause order:** SVO.

**Numerals (high-level)**

* Decimal digits: **Pa, Pe, Pi, Po, Pu, Ta, Te, Ti, To, Tu** = 0–9
* Powers of 10: **Py, Ty, Ky, By, Dy, Gy, …** where `Cy = 10^n` based on consonant order
* Complex numbers: `[digit] [Cy] [digit] [Cy] … [digit]` (highest exponent first)
* Number phrases behave like: `[Number] [N-M]`

---

## 1. Phonology & Orthography

### 1.1 Alphabet

**Consonants (Set C)**
B, D, F, G, J, K, L, M, N, P, R, S, T, V

| Letter | IPA     | Notes                                       |
| :----- | :------ | :------------------------------------------ |
| J      | /j/     | like **y** in *yes*                         |
| R      | /ɾ ~ ʁ/ | tap (American “bu**tt**er”) or uvular **r** |
| G      | /g/     | always hard, as in *go*                     |
| S      | /s/     | always [s], never [z]                       |
| Others | —       | roughly standard English values             |

**Vowels (Set V)**
A, E, I, O, U, Y

| Letter | IPA   | Example            |
| :----- | :---- | :----------------- |
| A      | /a/   | *spa, father*      |
| E      | /e~ɛ/ | *bet, met*         |
| I      | /i/   | *machine, ski*     |
| O      | /o/   | pure [o], no glide |
| U      | /u/   | *rule, food*       |
| Y      | /y/   | German **ü**       |

> **Y is only a vowel.** There is no consonant /y/.

**Terminal consonants (Set F)**
L, M, N, R, S, T

Only these may appear at the **end of a word** (as suffixes).

> Orthography is **case-insensitive**. Examples often use initial capitals for readability, but regexes below assume lowercase.

### 1.2 Syllable Structure

Allowed syllables: **CV** or **CVC**.

Content words:

```text
(CV prefix)* + (CVCV root) + (optional final C from F)
```

Atomic words are usually **CV**, sometimes multi-syllabic.

### 1.3 Stress

Stress always falls on the **penultimate** syllable:

* **GA**-ra
* **GA**-ra-m
* Ma-**GA**-ra-s

---

## 2. Word Classes & Morphology

### 2.1 Word Classes

1. **Atomic words**

   * Typically **CV**, plus some fixed multi-syllabic particles.
   * Closed classes: pronouns, demonstratives, particles, prepositions, auxiliaries, digits, wh-words, quantifiers, complementizers, powers-of-ten.
   * No productive prefixes/suffixes.

2. **Content words**

   * Built from exactly one **CVCV root**.
   * May take up to **five** CV prefixes (R/N/D/M/S/K series; at most one from each series and at most one of M- vs S-) and one suffix (L/M/N/R/S/T).

### 2.2 Content Word Template

```text
Word = Time? Logic? Voice? (Scale? | Space?) Group? + RootCVCV + Suffix
```

* **Time (slot 1)**: R- series
* **Logic (slot 2)**: N- series
* **Voice (slot 3)**: D- series
* **Scale or Space (slot 4)**: M- or S- series (at most one)
* **Group (slot 5)**: K- series
* **RootCVCV**: lexical root
* **Suffix**: one consonant from F for part of speech

> At most one prefix from each series.
> Scale (M-) and Space (S-) **compete** for the same slot.
> In surface forms, the PoS suffix is obligatory; bare CVCV roots appear only in the dictionary.

### 2.3 Part-of-Speech Suffixes

Suffixes are **obligatory** for content words in running text.

| Suffix | PoS | Function                       |
| :----- | :-- | :----------------------------- |
| -M     | N   | Noun (entity)                  |
| -S     | ADJ | Adjective (quality)            |
| -N     | V   | Verb (finite)                  |
| -L     | ADV | Adverb (manner/location)       |
| -R     | GEN | Genitive (“of X”)              |
| -T     | DET | Specific instance / determiner |

Bare CVCV roots appear only in the dictionary, not in normal sentences.

### 2.4 Regex Validation

Assuming lowercase:

* **Content words**:

  ```regex
  ^([rndmsk][aeiouy]){0,5}[bdfgjklmnprstv][aeiouy][bdfgjklmnprstv][aeiouy][lmnrst]?$
  ```

* **Atomic CV words**:

  ```regex
  ^[bdfgjklmnprstv][aeiouy]$
  ```

Orthography is case-insensitive; these regexes assume lowercase.

### 2.5 Parsing Algorithm (Content Words)

Given a token:

1. If length = 2 and matches CV → atomic word.
2. Otherwise:

   1. If final char ∈ {l,m,n,r,s,t}, treat as **suffix**, else no suffix.
   2. Take the preceding 4 letters as the **CVCV root**.
   3. Any remaining leftmost letters must form a sequence of **CV prefixes**.
   4. Parse prefixes left-to-right, enforcing:

      * prefix consonant ∈ {r, n, d, m, s, k};
      * at most one prefix from each series:

        * Time (R-), Logic (N-), Voice (D-), Scale (M-), Space (S-), Group (K-);
      * at most one of M-/S- total;
      * series must be in slot order: Time (R) → Logic (N) → Voice (D) → Scale/Space (M/S) → Group (K).

If all checks pass, the word is a valid content word.

---

## 3. Prefix System

Prefixes are **CV** and use only consonants **R, N, D, M, S, K**.

**Slot order (left to right):**

```text
[Time (R)] + [Logic (N)] + [Voice (D)] + [Scale or Space (M/S)] + [Group (K)] + Root + (Suffix)
```

**Series and slots:**

1. **Time (R-)**: Ra, Ri, Re, Ro, Ry, Ru
2. **Logic (N-)**: Na, Ni, Ne, No, Ny, Nu
3. **Voice (D-)**: Da, Di, De, Do, Du, Dy
4. **Scale (M-)** *or* **Space (S-)**: choose at most one
5. **Group (K-)**: Ka, Ki, Ke, Ko, Ky, Ku

> At most one prefix from each series.
> Scale (M-) and Space (S-) share the same slot and are **mutually exclusive**.

These same series are also used in some **lexicalised derivational patterns** (§8); in those patterns they still occupy their usual slots.

### 3.1 Time (R- series, slot 1)

| Prefix | Meaning             |
| :----- | :------------------ |
| Ra-    | past / before       |
| Ri-    | future / after      |
| Re-    | completed / stopped |
| Ro-    | ongoing / during    |
| Ry-    | again / repeated    |
| Ru-    | tempo / speed       |

### 3.2 Logic (N- series, slot 2)

| Prefix | Meaning          |
| :----- | :--------------- |
| Na-    | true / asserted  |
| Ni-    | pseudo / pretend |
| Ne-    | not / negation   |
| No-    | both / inclusive |
| Ny-    | maybe / possible |
| Nu-    | if / conditional |

> **Ne-** (negation) can attach to any content word: verbs (*negyfun* “not eat”), adjectives (*nevitus* “unhealthy”), and nouns (*negaram* “non-land / something that is not land”).
> **Nu-** is the bound, verbal form of conditional marking. There is also an atomic **Nu** “if” used as a clausal subordinator (§7.10).

### 3.3 Voice (D- series, slot 3)

Valency / voice operations on verbs.

| Prefix | Meaning / Function on a verb `V`   |
| :----- | :--------------------------------- |
| Da-    | cause / make X V (causative)       |
| Di-    | do V oneself / middle / reflexive  |
| De-    | V to/for Y (applicative)           |
| Do-    | V each other (reciprocal)          |
| Du-    | be V-ed / undergo V (passive-like) |
| Dy-    | begin to V / become V (inchoative) |

Examples (with *gome-n* “fight”):

* *Dagomen* — cause to fight / make (someone) fight
* *Digomen* — fight oneself / engage oneself in conflict
* *Dogomen* — fight each other
* *Dugomen* — be fought / be under attack
* *Dygomen* — begin to fight / enter into conflict

Voice prefixes normally attach to **verbs (-N)**, but derived forms in -M/-S/-L from voice-marked roots are allowed (e.g. *Kadugomem* “one who is usually attacked”).

### 3.4 Scale (M- series, slot 4a)

| Prefix | Meaning            |
| :----- | :----------------- |
| Ma-    | mega / big         |
| Mi-    | micro / small      |
| Me-    | neutral / average  |
| Mo-    | mass / collective  |
| My-    | varying / changing |
| Mu-    | form / shaped      |

> In derivational patterns (§8), **Mu-** is also conventionalised as “instrument/tool for X” when combined with roots in a fixed template. This is a specialisation of the “shaped-for / form-for X” sense and still occupies the Scale slot.

### 3.5 Space (S- series, slot 4b)

Mutually exclusive with Scale.

| Prefix | Meaning              |
| :----- | :------------------- |
| Sa-    | out / from           |
| Si-    | in / into            |
| Se-    | away / off           |
| So-    | around / surrounding |
| Sy-    | through / across     |
| Su-    | at / located at      |

> **S-series** expresses **internal** spatial direction or configuration on content words (e.g. motion verbs), while **G-series prepositions** (§4.4) express **external** roles between NPs and events (source, goal, location, instrument, etc.).

### 3.6 Group (K- series, slot 5)

| Prefix | Meaning                    |
| :----- | :------------------------- |
| Ka-    | union / all                |
| Ki-    | part / some                |
| Ke-    | void / no members          |
| Ko-    | group / plural set         |
| Ky-    | array / ordered series     |
| Ku-    | link / relational grouping |

Plural nouns often use **Ko-**:

* *Koporam* = *Ko-pora-m* — “people”
* *Kogaram* — “lands, regions”

---

## 4. Atomic Dictionary

### 4.1 Pronouns

Pronouns follow a regular CV grid:

* M- = 1st person
* T- = 2nd person
* S- = 3rd person
* i = singular
* a = plural

| Word | Person/Number  | Meaning       |
| :--- | :------------- | :------------ |
| Mi   | 1sg            | I / me        |
| Ma   | 1pl            | we / us       |
| Ti   | 2sg            | you (sg)      |
| Ta   | 2pl            | you (pl)      |
| Si   | 3sg            | he / she / it |
| Sa   | 3pl            | they (pl)     |
| Su   | 3 impers (opt) | dummy “it”    |

> Some CV forms overlap with numerals (e.g. **Ti, Ta**). They are disambiguated by syntactic position and semantics: pronouns typically occupy NP slots without a following noun, while digits appear inside explicit number phrases (§4.6–4.8).

### 4.2 Demonstrative Determiners

Demonstrative determiners are a regular K-series:

* K- = deictic anchor
* Vowel encodes distance (proximal/medial/distal) and number (sg/pl)

| Word | Features           | Meaning                     |
| :--- | :----------------- | :-------------------------- |
| Ka   | proximal, singular | this (near speaker)         |
| Ke   | proximal, plural   | these (near speaker)        |
| Ki   | medial, singular   | that (near hearer/context)  |
| Ko   | medial, plural     | those (near hearer/context) |
| Ku   | distal, singular   | that (far from both)        |
| Ky   | distal, plural     | those (far from both)       |

They appear before the noun:

> **Ka garam.** — “this land”
> **Ke koporam.** — “these people”

They can also stand alone as pronouns:

> **Ka** — “this (one)”
> **Ky** — “those (over there)”

The suffix **-T** on a noun encodes **specificity** but not deixis:

* *garam* — some land
* *garat* — the land / that specific land
* *Ka garat* — “this specific land (we’ve been talking about)”

### 4.3 Particles, Auxiliaries & Modals

| Word | Class    | Meaning                                    |
| :--- | :------- | :----------------------------------------- |
| Ja   | conj     | and                                        |
| Je   | conj     | or                                         |
| Jo   | particle | yes; clause-initial **yes/no marker**      |
| Ju   | particle | no                                         |
| Ba   | aux      | be                                         |
| Va   | aux      | have                                       |
| Vi   | aux      | do / perform                               |
| La   | aux/mod  | must / have to / necessary                 |
| Le   | aux/mod  | can / be able to                           |
| Li   | aux/mod  | want to / intend                           |
| Lo   | comp     | that (complementizer, clause subordinator) |

> *Lo* is used to mark clausal complements explicitly (§7.9).

### 4.4 Prepositions & Temporal Adverbs

The **G-series** is a systematic prepositional grid:

| Word | Class | Core Role               | Meaning / Use                             |
| :--- | :---- | :---------------------- | :---------------------------------------- |
| Ga   | prep  | SOURCE / STANDARD       | from, out of, than (comparative standard) |
| Ge   | prep  | GOAL                    | to, towards                               |
| Gi   | prep  | LOCATION                | in, at, on (static location)              |
| Go   | prep  | PATH / MEDIUM           | via, along, through (route/medium)        |
| Gu   | prep  | INSTRUMENT / COMITATIVE | with, using, together with                |
| Gy   | prep  | CAUSE / REASON          | because of, due to, on account of         |

Temporal adverbs (not prepositions):

| Word | Class | Meaning         |
| :--- | :---- | :-------------- |
| Ra   | adv   | before (time)   |
| Ro   | adv   | now / currently |
| Ri   | adv   | after (time)    |

### 4.5 Conditionals (Atomic)

| Word | Class | Meaning |
| :--- | :---- | :------ |
| Nu   | conj  | if      |

> *Nu* introduces conditional clauses (§7.10). It is related in meaning to the prefix **Nu-** in the Logic series.

### 4.6 Decimal Digits (0–9)

Digits are **atomic CV numerals** using a **block-of-5** system:

* Consonant = **block index**
* Vowel (a/e/i/o/u) = **offset 0–4 in the block**

For **decimal digits**, only two consonants are used:

```text
P → block 0  → digits 0–4
T → block 1  → digits 5–9
```

Vowel offsets:

```text
a → 0
e → 1
i → 2
o → 3
u → 4
```

So the value of a digit CV is:

```text
value(CV) = 5 * block(C) + offset(V)
```

Digit table:

| Value | Form | Block/offset |
| :---- | :--- | :----------- |
| 0     | Pa   | P-block, a=0 |
| 1     | Pe   | P-block, e=1 |
| 2     | Pi   | P-block, i=2 |
| 3     | Po   | P-block, o=3 |
| 4     | Pu   | P-block, u=4 |
| 5     | Ta   | T-block, a=0 |
| 6     | Te   | T-block, e=1 |
| 7     | Ti   | T-block, i=2 |
| 8     | To   | T-block, o=3 |
| 9     | Tu   | T-block, u=4 |

Numeric ordering is:

> Pa < Pe < Pi < Po < Pu < Ta < Te < Ti < To < Tu

**Zero** is **Pa**. In ordinary counting, speakers may start from **Pe** (“one”), but numerically, Pa = 0.

Digits are of semantic head kind **Number** (no domain/aspect).

### 4.7 Powers of Ten (CVy series)

The vowel **Y** marks **powers of 10**:

```text
Cy = 10^n
```

where `n` depends only on consonant **C**.

We define an ordered **exponent consonant series**:

```text
P, T, K, B, D, G, F, V, S, M, N, L, R, J
```

Index in this list = exponent:

```text
P → 10^0
T → 10^1
K → 10^2
B → 10^3
D → 10^4
G → 10^5
F → 10^6
V → 10^7
S → 10^8
M → 10^9
N → 10^10
L → 10^11
R → 10^12
J → 10^13
```

So:

| Form | Value     | Role                            |
| :--- | :-------- | :------------------------------ |
| Py   | 10⁰ = 1   | unit (rarely used in cardinals) |
| Ty   | 10¹ = 10  | “ten”                           |
| Ky   | 10² = 100 | “hundred”                       |
| By   | 10³       | “thousand”                      |
| Dy   | 10⁴       |                                 |
| Gy   | 10⁵       |                                 |
| Fy   | 10⁶       |                                 |
| Vy   | 10⁷       |                                 |
| Sy   | 10⁸       |                                 |
| My   | 10⁹       |                                 |
| Ny   | 10¹⁰      |                                 |
| Ly   | 10¹¹      |                                 |
| Ry   | 10¹²      |                                 |
| Jy   | 10¹³      |                                 |

> Note: **Pe** is the **digit** 1. **Py** is the **power-of-10 unit** 10⁰, used mainly in mathematical contexts (“ten to the zero”). In ordinary counting, *Py* is not used to mean “one”.

These are also head kind **Number**.

### 4.8 Complex Cardinal Numbers

Any non-negative integer is built compositionally from:

* **digits**: Pa–Tu (0–9)
* **powers of 10**: Py, Ty, Ky, By, … (10^n)

Algorithm:

1. Write `n` in base 10:
   `n = Σ (dᵢ * 10^i)`, with digits `dᵢ ∈ {0,…,9}`.

2. For each exponent `i` where `dᵢ ≠ 0`:

   * if `i = 0` (units place):
     `phrase(i) = [digit(d₀)]` (just the digit; omit for n with zero units, unless n=0)
   * if `i > 0`:

     * let `Cᵢy` be the power-of-10 atom with `10^i`,
     * if `dᵢ = 1`:
       `phrase(i) = Cᵢy`  (optional **Pe Cᵢy** for emphasis)
     * if `dᵢ > 1`:
       `phrase(i) = [digit(dᵢ)] Cᵢy`.

3. Concatenate phrases from highest `i` down to 0.

**Examples**

* 0 = **Pa**

* 3 = **Po**

* 7 = **Ti**

* 10 = 1×10¹ → **Ty**

* 20 = 2×10¹ → **Pi ty**

* 42 = 4×10¹ + 2

  * 4 → *Pu*

  * 2 → *Pi*

  > **Pu ty pi.**

* 100 = 1×10² → **Ky**

* 300 = 3×10² → **Po ky**

* 304 = 3×10² + 4 → **Po ky pu**

* 1000 = 1×10³ → **By**

* 2000 = 2×10³ → **Pi by**

* 2019 = 2×10³ + 1×10¹ + 9

  * 2×10³ → **Pi by**

  * 1×10¹ → **Ty**

  * 9 → **Tu**

  > **Pi by ty tu.**

Number phrases function syntactically as **determiner-like modifiers**:

```text
[NumberPhrase] [Noun-M]
```

Examples:

* “three people”:

  > **Po koporam.**
  > 3 people

* “twenty-four houses”:

  * 24 = 2×10 + 4 → **Pi ty pu**

  > **Pi ty pu dumim.**

### 4.9 Wh-Words (F- series)

| Word | Meaning              |
| :--- | :------------------- |
| Fa   | what / which (thing) |
| Fe   | who / which (person) |
| Fi   | where / which place  |
| Fo   | why / reason         |
| Fu   | how / manner         |
| Fy   | when / which time    |

> In addition to interrogatives, F-series words can function as **relative pronouns** in relative clauses (§7.8).

### 4.10 Quantifiers

| Word | Meaning    |
| :--- | :--------- |
| Kafa | everything |
| Kefe | everyone   |
| Nefa | nothing    |
| Nyfa | something  |

---

## 5. Semantic Matrix

CVCV root: **C V₁ C V₂**.
V₁ → domain, V₂ → (semantic) aspect.

### 5.1 Domains (rows, V₁)

Domains come in **pairs**, forming a 3×2 structure:

1. **World without people**

   * **A – NATURE**: environment, unbuilt world, non-human life
   * **E – PHYSICS**: physical laws, geometry, forces as abstract structure

2. **People**

   * **I – HUMAN**: bodies, minds, individual psychology, personal states
   * **O – SOCIAL**: roles, norms, institutions, communication between people

3. **Constructed / abstract**

   * **U – TECH**: artifacts, tools, buildings, clothing, infrastructure
   * **Y – META**: data, mathematics, logic, higher-order abstractions, models

| V₁ | Domain  | Scope                                       |
| :- | :------ | :------------------------------------------ |
| A  | Nature  | environment, non-human natural world        |
| E  | Physics | physical laws, geometry, fields             |
| I  | Human   | body, mind, immediate human states          |
| O  | Social  | persons, norms, communication, institutions |
| U  | Tech    | artifacts, built environment, clothing      |
| Y  | Meta    | cosmos, data, abstractions, formal systems  |

### 5.2 Semantic Aspects (columns, V₂)

Aspects also come in **pairs**, forming another 3×2 structure:

1. **Static / “what is there”**

   * **A – REGION / SHAPE (STATIC)**: bounded regions, objects-as-loci, shapes
   * **U – MATTER / RESOURCE (SUBSTANCE)**: stuff, material, consumables, resources

2. **Dynamic / “what happens”**

   * **E – ENERGY / CAPACITY (FORCE)**: intensity, power, potential to cause change
   * **I – PROCESS / INTERACTION (FLOW)**: events, flows, actions, interactions

3. **Abstract / “how it’s organized”**

   * **O – FORM / REPRESENTATION (CONCEPT)**: patterns, ideas, representations
   * **Y – SYSTEM / NETWORK (SYSTEM)**: structured sets, cycles, networks, whole systems

| V₂ | Aspect    | Scope                                                             |
| :- | :-------- | :---------------------------------------------------------------- |
| A  | Static    | regions, shaped entities, locations, structured “chunks” in space |
| U  | Substance | matter, resources, consumables, “stuff”                           |
| E  | Force     | energy, intensity, capacity, power to cause change                |
| I  | Flow      | processes, events, motion, interactions, doings                   |
| O  | Concept   | forms, patterns, representations, views, concepts                 |
| Y  | System    | systems, cycles, networks, structured multi-part configurations   |

Heuristics:

* (A,U) = **static pair**: object/region vs stuff/resource.
* (E,I) = **dynamic pair**: potential vs actual process.
* (O,Y) = **abstract pair**: single pattern vs whole system.

### 5.3 Base Sense Grid

| V₁↓ / V₂→     | -A Region/Shape (Static) | -E Energy/Force      | -I Process/Flow              | -O Form/Representation            | -U Matter/Resource          | -Y System/Network                    |
| :------------ | :----------------------- | :------------------- | :--------------------------- | :-------------------------------- | :-------------------------- | :----------------------------------- |
| **A Nature**  | Terrain / landscape      | Weather / air energy | Animal behaviour / activity  | Plant form / growth pattern       | Natural fluid / material    | Natural cycles/time (day, seasons)   |
| **E Physics** | Space/region, geometry   | Energy/light, fields | Motion, forces in action     | Wave/signal forms                 | Matter/chemistry            | Math/geometry as systems             |
| **I Human**   | Body/anatomy regions     | Sensation intensity  | Self/agency, action          | Emotion/attitude patterns         | Life state / vitality       | Spirit/identity systems (reserved)   |
| **O Social**  | Person/role positions    | Power/conflict/law   | Communication/exchange acts  | Belief/idea/norm representations  | Resources/economy           | Culture/media/art as social systems  |
| **U Tech**    | Artifact/surface/edge    | Tool/machine power   | Built environment & access   | Transport/infrastructure concepts | Covering/clothing/materials | Waste/maintenance systems (reserved) |
| **Y Meta**    | Cosmos/world “as a unit” | Data/network “load”  | Micro-unit/instance dynamics | Abstract thing/void/type          | Need/resource/consumption   | Variables/unknowns, formal systems   |

Notes:

* Y–U is interpreted as **need/resource/consumption**: the “meta” view of resource/necessity rather than concrete food only. *Gyfu* fits here as “food/need/consumption”.
* O–Y is the natural home for **culture/media/art** as social systems.
* Y–Y is the home of **formal systems** (math, software, logics, etc.).

### 5.4 Vowel Neighbourhoods & Semantic Shifts (Design Heuristics)

The matrix can be used as a **feature space** when coining new roots. Certain vowel changes correspond to intuitive conceptual moves.

#### 5.4.1 Domain pairs (V₁ shifts)

Within each pair:

* **A ↔ E (Nature ↔ Physics)**

  * shift between “concrete environment” and “formal physical structure”.
  * e.g. `gara` (A–A) “land/terrain” vs hypothetical `gera` (E–A) “space/region” as a more geometric abstraction.

* **I ↔ O (Human ↔ Social)**

  * shift between “individual” and “social/institutional” view.
  * e.g. `kiri` (I–I) “self/core” vs hypothetical `kori` (O–I) “social persona/role”.

* **U ↔ Y (Tech ↔ Meta)**

  * shift between “concrete artifact/system” and “abstract model/system”.
  * e.g. `dumi` (U–I) “building” vs hypothetical `dymi` (Y–I) “architecture/design pattern”.

These shifts don’t have to be fully productive morphophonology; they’re **design conventions** for related lexical families.

#### 5.4.2 Aspect pairs (V₂ shifts)

Within each pair:

* **A ↔ U (Region ↔ Matter)**

  * object/shape vs stuff/material:
  * e.g. `pano` (A–O) “plant form” vs hypothetical `panu` (A–U) “plant matter / wood / leaves”.

* **E ↔ I (Force ↔ Flow)**

  * capacity vs process:
  * e.g. hypothetical `kene` (E–E) “ability/power” vs `keni` (E–I) “use of ability / performance”.

* **O ↔ Y (Form ↔ System)**

  * single pattern vs multi-part system:
  * e.g. `voro` (O–O) “doctrine / belief pattern” vs hypothetical `vory` (O–Y) “doctrine system / ideology”.

Again, this is a **heuristic**: when you need a new root for a related concept, you can often get a nicely organized lexicon by:

* keeping the consonants roughly similar, and
* moving V₁ and/or V₂ along the pair axes in ways that mirror the conceptual shift.

---

## 6. CVCV Lexicon (Aligned with Matrix)

Roots listed bare; add suffixes in usage.

### 6.1 A- row: Nature

**A-A (Terrain / landscape)**

* **Gara** — land / earth
* **Pata** — stone / rock

**A-E (Weather / air energy)**

* **Kale** — sky / air
* **Vate** — wind

**A-I (Animal behaviour/life)**

* **Basi** — animal

**A-O (Plant form / growth pattern)**

* **Pano** — plant / tree

**A-U (Natural fluid / material)**

* **Laru** — water

**A-Y (Natural cycles/time)**

* **Tamy** — natural time / cycles (day, seasons)

---

### 6.2 E- row: Physics

**E-A (Space/region, geometry)**

* **Sepa** — space / area

**E-E (Energy/light)**

* **Sele** — light / sun

**E-I (Motion/force in action)**

* **Mevi** — move / go
* **Pesi** — push
* **Peli** — pull

**E-O (Wave/signal forms)**

* **Seno** — sound

**E-U (Matter/chemistry)**

* **Metu** — matter / chemistry

**E-Y (Math/geometry as systems)**

* **Leny** — line / mathematical structure

---

### 6.3 I- row: Human

**I-A (Body/anatomy regions)**

* **Kipa** — head / body
* **Mina** — hand
* **Kila** — eye
* **Rina** — mouth

**I-E (Sensation intensity)**

* **Sine** — sense / feel

**I-I (Self/agency process)**

* **Kiri** — self / core

**I-O (Emotion/attitude patterns)**

* **Vilo** — emotion / will

**I-U (Life state / vitality)**

* **Vitu** — life / health
* **Dimu** — sleep
* **Viku** — wake / see
* **Mitu** — die

**I-Y (Spirit/identity systems)**

* (reserved)

---

### 6.4 O- row: Social

**O-A (Person/role positions)**

* **Pora** — person / social role

**O-E (Power/conflict/law)**

* **Gome** — war / conflict
* **Loge** — law (enforcing social power)

**O-I (Communication/exchange acts)**

* **Nomi** — name / word (linguistic sign)
* **Dogi** — give / transfer / exchange
* **Bobi** — book / record (container of words)
* **Somi** — say / speak / express

**O-O (Belief/idea/norm representations)**

* **Voro** — truth / idea / doctrine
* **Fono** — goal / end / purpose
* **Keno** — knowledge / to know

**O-U (Resources/economy)**

* **Monu** — money / economy

**O-Y (Culture/media/art systems)**

* (reserved)

---

### 6.5 U- row: Technology

**U-A (Artifact/surface/edge)**

* **Mura** — wall (constructed barrier surface)
* **Kuta** — knife / blade / cut

**U-E (Tool/machine power)**

* **Muke** — tool / machine
* **Kuve** — key (tool to open/close)

**U-I (Built environment & access)**

* **Dumi** — house / building; to build
* **Puti** — door / gateway

**U-O (Transport/infrastructure concept)**

* **Vugo** — vehicle

**U-U (Covering/clothing/materials)**

* **Vusu** — clothing

**U-Y (Waste/maintenance systems)**

* (reserved)

---

### 6.6 Y- row: Meta

**Y-A (Cosmos/world as a unit)**

* **Kyma** — system / cosmos
* **Gyla** — galaxy

**Y-E (Data/network load)**

* **Dyte** — data / net

**Y-I (Micro-unit/instance dynamics)**

* **Pyki** — pixel / point

**Y-O (Abstract thing/void/type)**

* **Vyro** — (abstract) thing / entity
* **Nyfo** — void / null / nothingness

**Y-U (Need/resource/consumption)**

* **Gyfu** — food / nourishment; to eat

**Y-Y (Variables/unknowns, formal systems)**

* **Vyry** — variable / X / unknown

---

## 7. Syntax

### 7.1 Roles & Marking

Analytic: position + **G-series prepositions** mark roles.

| Role               | Marking                                                |
| :----------------- | :----------------------------------------------------- |
| Agent              | subject NP (before verb)                               |
| Patient            | direct object NP (after verb)                          |
| Recipient / Goal   | NP with **Ge** (“to, towards”)                         |
| Source / Comparand | NP with **Ga** (“from; than (standard of comparison)”) |
| Location           | NP with **Gi** (“in, at, on”) or spatial prefix/adverb |
| Instrument/Comit.  | NP with **Gu** (“with, using, together with”)          |
| Path / Medium      | NP with **Go** (“via, along, through”)                 |
| Cause / Reason     | NP with **Gy** (“because of, due to, on account of”)   |

### 7.2 Clause Order

Canonical order: **SVO**.

**Intransitive**

```text
[NP-AGENT] [V]
```

> **Si dimun.**
> *si* 3sg
> *dimu-n* sleep-V
> “He/she/it sleeps.”

**Transitive**

```text
[NP-AGENT] [V] [NP-PATIENT]
```

> **Ti vikun kalet.**
> *ti* you (sg)
> *viku-n* see-V
> *kale-t* sky-DET
> “You see the sky.”

**Ditransitive**

```text
[NP-AGENT] [V] [NP-PATIENT] [Ge NP-RECIPIENT]
```

> **Ro mi dogin monut ge ti.**
> *ro* now
> *mi* I
> *dogi-n* give-V
> *monu-t* money-DET
> *ge ti* to you (sg)
> “Now I give the money to you.”

Adjuncts (time, place, manner) usually follow SVO but can be fronted for focus:

> **Ro, mi dimun.**
> “Now, I sleep.”

### 7.2.1 Adverbs & Clause Skeleton

There are three main classes of adverbial material:

1. **Frame adverbs** (clause-level / temporal / discourse)

   * Include atomic *Ra, Ro, Ri* (“before, now, after”), and sometimes G-phrases with *Gy NP* (“because of X”) when they scope over the clause.

   * Canonical position: **clause-initial** to set the frame, but clause-final is possible for emphasis.

   > **Ro, mi dimun.** — “Now, I sleep.”
   > **Mi dimun ro.** — “I sleep now.” (more afterthought-like)

2. **VP adverbs** (manner, lexical location, aspect-like)

   * Mostly **-L** forms from content roots: `root + -L` (ADV).
   * Express manner (“slowly”), lexical location (“on land”), or more abstract shades.
   * Canonical position: **immediately after the verb phrase**, before PPs.

   Example root: *gara* — land.
   *gara-l* → **garal** — land-ADV “on land / in a land-like domain”.

3. **Prepositional phrases (PPs)**

   * G-series prepositions + NP: `ga/ge/gi/go/gu/gy + NP`.
   * Canonical position: **after** VP adverbs.

Putting this together, the **canonical clause skeleton** is:

```text
[Frame Adv*] [Subject NP] [Aux*] [Verb] [Object NP*] [VP Adv(-L)*] [PP*] [Frame Adv*]
```

* The **VP adverb block** (-L words) attaches tightly to the predicate.
* **PPs** follow the VP adverb block.
* **Frame adverbs** may appear at the beginning, optionally also at the end.

Example with everything:

> **Ro mi gyfun gyfut garal gi dumit.**
> *Ro* — now (frame adv)
> *mi gyfu-n gyfut* — I eat the food
> *gara-l* — on-land-ADV (VP adverb)
> *gi dumi-t* — at the house-DET (PP, location)
> “Now I eat the food on land at the house.”

---

### 7.3 Noun Phrases (NP)

Canonical NP structure:

```text
[Quantifier/Number] [DemDet]
[Head = Group-Prefix + N-M(+T?)]
[Adjectives(-S)*] [Genitive-NP?] [RelativeClause*] [PP*]
```

* **Head noun**: CVCV + **-M**

  * *Garam* — land
  * *Poram* — person

* **Definiteness / specificity**: suffix **-T** on the head, or quantifiers like *kafa*.

  * *Garat* — that/the land
  * *Kafa* — everything

* **Demonstratives**: K-series determiners (§4.2) before the noun.

  * *Ka garam* — this land
  * *Ke koporam* — these people
  * *Ku garat* — that specific land (far)

* **Plural/group**: **Ko-** as group prefix on the head.

  * *Koporam* — people
  * *Kogaram* — lands

* **Adjectives**: suffix -S, **form a single block immediately after the head noun**.

  * *Garam vitus* — “healthy land”
  * *Garam vitus misepas* — “small healthy land” (order within the adjective block is free / stylistic)

* **Genitive**: possessor NP as noun with **-R**, after the adjective block.

  * *Garam vitus porar.* — “the healthy land of the person”
  * *Koporam misepas porar.* — “the smaller people of the person”

* **Relative clauses**: attach after adjectives and any genitive NP (§7.8).

  * *Garat vitus porar fe radumin dumit.*
    “the healthy land of the person who built the house”

* **Prepositional modifiers (PPs)**: typically last in the NP.

  * *Garat vitus porar gi sepam.* — “the healthy land of the person by the road”

#### 7.3.1 Adjective Block & Modifier Order

Within an NP:

1. The **head noun** (with any group prefix and -M/-T suffix) comes first.
2. All **adjectives (-S)** modifying that head form **one contiguous block** immediately after the head.
3. A **genitive NP** (*-R* possessor) follows that block.
4. **Relative clauses** follow the genitive (if any).
5. **PPs** (G-series phrases) come last.

Example with everything:

> **Po ke koporam vitus misepas porar fe radumin dumit gi garal.**
> 3 these people healthy small person-GEN who built house-DET in-land-ADV
> “These three small healthy people of the person who built the house (are) on land.”

This makes NP parsing deterministic:

* Find the head (first N-M or N-T).
* Everything until the first -R noun / relative pronoun / PP is adjectives.
* Next comes possessor (-R), then relative clauses, then PPs.

#### 7.3.2 -L vs Gi for Location

There are two ways to express location:

1. **-L adverbs from roots**:

   * *gara-l* → **garal** “on land / in a land-like domain”.

   These are **lexical adverbs**: more generic, often integrated into the predicate’s meaning (manner-ish).

2. **Gi + NP**:

   * *gi garat* — “at that land”
   * *gi dumit* — “in/at the house”

   This keeps a **full NP**: you can add determiners, adjectives, genitives, etc.

Functional difference:

* **-L**: compact, lexical, slightly more abstract (“land-wise, on land in general”).
* **Gi + NP**: explicit, referential location (“at that specific land/house we’re talking about”).

They can co-exist in the same clause:

> **Ro mi gyfun gyfut garal gi dumit.**
> “Now I eat the food on land at the house.”

---

### 7.4 Verbs, TAM, Polarity & Voice

Finite verbs: **root + -N**, with optional prefixes:

```text
[Time (R-)] [Logic (N-)] [Voice (D-)] [Scale/Space (M-/S-)] [Group (K-)] Root + -N
```

* **Time** and **Logic** prefixes function as **TAM/polarity** markers.
* **Voice (D-)** modifies verbal valency and perspective (causative, passive, etc.).
* All of these are independent of the **semantic aspect** encoded by the root’s second vowel (STATIC/FORCE/FLOW/...).

- Neutral:

  * *Garan* — land (verb)
  * *Gyfun* — eat

- Time:

  * *Ragaran* — landed / did land
  * *Rigaran* — will land
  * *Rogaran* — is landing (ongoing)

- Negation (Logic slot):

  * *Negaran* — does not land
  * *Negyfun* — does not eat
  * *Rinegaran* — will not land

- Voice:

  For *gome-n* “fight”:

  * *Dagomen* — cause/make (someone) fight
  * *Dogomen* — fight each other
  * *Dugomen* — be fought / be under attack
  * *Radugomen* — was attacked (PST-PASS-fight-V)

  For *dumi-n* “build” and *mura-t* “the wall”:

  * *Koporam radumin murat.*
    “The people built the wall.” (Ra-dumi-n PST-build-V)

  * *Murat radudumin gu koporam.*
    “The wall was built (by/with the people).”
    (*Ra-du-dumi-n* PST-PASS-build-V + **Gu** INSTR/COMIT)

### 7.5 Questions

**Wh-Questions**

Start with an F-series wh-word.

```text
Wh-Word + Clause
```

> **Fa ti gyfun gyfut?**
> “What do you (sg) eat?”

> **Fe ravikun garat?**
> “Who saw the land?”

**Yes/No Questions**

Start with **Jo**.

```text
Jo + Clause
```

> **Jo ti gyfun gyfut?**
> “Do you eat the food?”

> **Jo si ragaran garam?**
> “Did he/she/it land on the land?”

### 7.6 Comparatives

Pattern:

```text
[Subject NP] [Adjective] ga [Reference NP]
```

> **Garam misepas ga kalet.**
> *gara-m* earth-N
> *mi-sepa-s* micro-space-ADJ (“smaller”)
> *ga kale-t* than sky-DET
> “The earth is smaller than the sky.”

### 7.7 Imperatives

* Use the verb in **-N**.
* Optional subject.
* `!` marks command.

```text
([Subject]) [V] ([Object]) !
```

> **Gyfun gyfut!** — “Eat the food!”
> **Negyfun gyfut!** — “Do not eat the food!”
> **Ti! Negyfun gyfut!** — “You! Don’t eat the food!”

---

### 7.8 Relative Clauses

Relative clauses attach to a **head NP** and are introduced by F-series words acting as **relative pronouns**:

* *Fe* — “who / that (person)”
* *Fa* — “which / that (thing)”
* *Fi* — “where”
* *Fy* — “when”

General pattern (head-initial):

```text
[Head NP] [RelPronoun] [Clause-with-gap]
```

The relative pronoun stands for a missing NP inside the clause (subject or object).

Per §7.3.1, relative clauses come **after the adjective block and any genitive NP**, but **before** NP-internal PPs.

**Examples**

> **Porat fe ravikun kalet dimun.**
> *pora-t* person-DET
> *fe* who
> *Ra-viku-n* PST-see-V
> *kale-t* sky-DET
> *dimu-n* sleep-V
> “The person who saw the sky is sleeping.”

> **Garat fa ti vikun.**
> “The land that you (sg) saw.”

> **Ka dumit fi koporam dimun garal.**
> *ka dumi-t* this house-DET
> *fi* where
> *kopora-m* people-N
> *dimu-n* sleep-V
> *gara-l* land-ADV “on the land”
> “This house where the people sleep is on the land.”

The relative clause directly follows the head NP’s adjective/genitive block.

---

### 7.9 Clause Embedding (Complements)

Certain verbs and auxiliaries (e.g. “say, think, know, want, must, can”) can take **clausal complements**.

There are two main patterns:

1. **Bare complement** (juxtaposed clause)
2. **Complementizer *Lo*** (“that”)

#### 7.9.1 Bare Complement

Pattern:

```text
[Matrix Subject] [Matrix Verb] [Embedded Clause]
```

> **Mi kenon si rimevin.**
> *mi* I
> *keno-n* know-V
> *si* he/she/it
> *Ri-mevi-n* FUT-move/go-V
> “I know he will come.”

#### 7.9.2 Complementizer *Lo*

Pattern:

```text
[Matrix Subject] [Matrix Verb] lo [Embedded Clause]
```

> **Mi kenon lo si rimevin.**
> “I know that he will come.”

> **Si somin lo ti nevikun garat.**
> *si* he
> *somi-n* say/speak-V
> *lo* that
> *ti* you (sg)
> *Ne-viku-n* NEG-see-V
> *gara-t* land-DET
> “He said that you did not see the land.”

#### 7.9.3 Embedded Questions

Wh-words can also introduce **embedded questions** inside complements:

```text
[Matrix Subject] [Matrix Verb] lo [Wh-Clause]
```

> **Mi kenon lo fe rimevin.**
> “I know who came.”

> **Si somin lo fa ti gyfun.**
> “He said what you eat.”

---

### 7.10 Conditionals

Conditionals are primarily formed with atomic **Nu** “if” introducing the **protasis** (if-clause).

Basic pattern:

```text
Nu [Protasis Clause], [Apodosis Clause].
```

> **Nu si rimevin, mi rigyfun gyfut.**
> “If he comes, I will eat the food.”

> **Nu ti negyfun gyfut, ti rinevitus.**
> *Nu* — if
> *ti* — you (sg)
> *Ne-gyfu-n* → *negyfun* — NEG-eat-V
> *gyfu-t* — the food
> *ti* — you
> *Ri-ne-vitu-s* → *rinevitus* — FUT-NEG-healthy-ADJ
> “If you do not eat the food, you will not be healthy.”

The **Nu-** prefix in the Logic series can also be used on verbs to mark conditional semantics in a more local way (e.g. *Nugyfun* “eat if/when…”), but clausal **Nu** is the primary conditional construction.

---

### 7.11 Extra Examples of G-series Roles

**Path / Medium (Go)**

> **Si mevin go vugot.**
> *si* he
> *mevi-n* move/go-V
> *go vugo-t* via vehicle-DET
> “He goes via the vehicle.”

**Cause / Reason (Gy)**

> **Mi dimun gy Nagomem.**
> *mi* I
> *dimu-n* sleep-V
> *gy Nagomem* because-of conflict-ABSTRACT
> “I sleep because of the conflict.”

---

## 8. Derivational Layer

This layer gives **regular patterns** for:

* abstract action/state nouns,
* agent nouns,
* instrument/tool nouns.

All derivation uses existing prefixes and suffixes.

In this layer, we fix three **canonical templates** using existing prefixes (**Na-**, **Ka-**, **Mu-**) plus **-M**. The compositional meanings of these prefixes (truth, union, form) bleed into the derived sense, but the patterns themselves are treated as **lexicalised shortcuts**.

* **Na-** still fills the **Logic** slot (2)
* **Mu-** still fills the **Scale** slot (4)
* **Ka-** still fills the **Group** slot (5)

The Voice slot (D-) remains available and can combine with these, e.g.:

* *Rakadagomem* — “one who used to cause fighting” (Ra-Time + Ka-Agent + Da-Voice + gome-M)

### 8.1 Base from a Root

For any root **R**:

* **R + -N** — base verb (“to R”)
* **R + -M** — base noun (“an R-entity”)
* **R + -S** — adjective (“R-like”)
* **R + -L** — adverb (“in an R way / at R”)

### 8.2 Abstract Event / State

**Form:**

```text
Na- + R + -M
```

**Meaning:** “the act / process / state of R-ing”.

Examples:

* *gome-n* — to fight

  * **Nagomem** — “the act/state of conflict”

* *gyfu-n* — to eat

  * **Nagyfum** — “the act of eating”

* *dimu-n* — to sleep

  * **Nadimum** — “sleeping (as a state)”

### 8.3 Agent Noun (“doer of X”)

**Form:**

```text
Ka- + R + -M
```

**Meaning:** “one who typically does R / role defined by R”.

Examples:

* *gyfu-n* — eat

  * **Kagyfum** — “eater”

* *dogi-n* — give

  * **Kadogim** — “giver / donor”

* *viku-n* — wake/see

  * **Kavikum** — “watcher / observer”

* *gome-n* — fight

  * **Kagomem** — “fighter / warrior”

Voice-marked agents are also possible:

* *Kadagomem* — “instigator; one who causes fighting”
  (*Ka-da-gome-m*)

### 8.4 Instrument Noun (“tool for X”)

**Form:**

```text
Mu- + R + -M
```

**Meaning:** “instrument/tool used for R”.

Examples:

* *gyfu-n* — eat

  * **Mugyfum** — “eating tool” (fork, spoon, etc.)

* *mevi-n* — move/go

  * **Mumevim** — “moving device; propulsion tool”

* *gome-n* — fight

  * **Mugomem** — “weapon” (tool for conflict)

* *dumi-n* — build

  * **Mudumim** — “building tool”

> Here **Mu-** is a lexicalised use of the M-series meaning “shaped-for / form-for X”, conventionalised as “instrument for X”. It still occupies the Scale slot and can combine with Time, Logic, and Voice prefixes in the normal order.

---

## 9. Semantic Typing Scheme

We want a simple, deterministic mapping from any content word to a **semantic type** like:

* `Event<SOCIAL, FORCE>`
* `Agent<META, SUBSTANCE>`

### 9.1 Type Primitives

**Domain (from V₁)**

```text
A → NATURE
E → PHYSICS
I → HUMAN
O → SOCIAL
U → TECH
Y → META
```

**Semantic Aspect (from V₂)**

We keep the six abstract labels, now with the refined interpretations:

```text
A → STATIC    // Region/Shape view
U → SUBSTANCE // Matter/Resource view
E → FORCE     // Energy/Capacity view
I → FLOW      // Process/Interaction view
O → CONCEPT   // Form/Representation view
Y → SYSTEM    // System/Network view
```

> Domain and (semantic) Aspect always come from the **root vowels**.
> Prefixes and suffixes never change them; they only change the **head kind** or add TAM/polarity/voice.

**Head kind (from suffix and derivational prefixes)**

```text
HeadKind ∈ {
  Entity,     // base -M, -R, -T
  Event,      // base -N
  Property,   // base -S
  Manner,     // base -L
  Agent,      // Ka- + -M
  Instrument, // Mu- + -M
  Abstract,   // Na- + -M
  SystemType, // could be used for Aspect=SYSTEM if you want
  Relator,    // prepositions
  Operator,   // particles, auxiliaries, complementizers
  Pronoun,
  Number,
  Unknown
}
```

A semantic type is:

```text
SemType = HeadKind<Domain?, Aspect?>
```

Domain/Aspect are `None` for many function words.

### 9.2 Base Types from CVCV + Suffix

Given a content word with:

* root **R = C V₁ C V₂**,
* domain **D** and aspect **A** from vowels,
* suffix **Suf** ∈ {m,n,s,l,r,t},

we map:

```text
if Suf = "m":   HeadKind = Entity
if Suf = "r":   HeadKind = Entity
if Suf = "t":   HeadKind = Entity
if Suf = "n":   HeadKind = Event
if Suf = "s":   HeadKind = Property
if Suf = "l":   HeadKind = Manner
```

So:

* *garam* (gara-m) → `Entity<NATURE, STATIC>`
* *garan* (gara-n) → `Event<NATURE, STATIC>`
* *gomes* (gome-s) → `Property<SOCIAL, FORCE>`

Voice and TAM prefixes don’t change HeadKind; they are extra features of Events.

### 9.3 Overrides from Derivational Prefixes

Certain prefixes override the **HeadKind** when used in the canonical templates:

* If word has **Na-** (and ends with -M) → `Abstract<D, A>`
* If word has **Ka-** (and ends with -M) → `Agent<D, A>`
* If word has **Mu-** (and ends with -M) → `Instrument<D, A>`

Examples:

* `Nagomem` ⇒ `Abstract<SOCIAL, FORCE>`
* `Kagomem` ⇒ `Agent<SOCIAL, FORCE>`
* `Mugomem` ⇒ `Instrument<SOCIAL, FORCE>`

### 9.4 Function Words & Numerals

* **Pronouns** (`mi, ma, ti, ta, si, sa, su`): `Pronoun` (no domain/aspect, or `HUMAN` if desired).
* **Demonstratives** (`ka, ke, ki, ko, ku, ky`): `Pronoun` or `Entity<NATURE, STATIC>` if you want to type them as deictic entities.
* **Prepositions** (`ga, ge, gi, go, gu, gy`): `Relator`.
* **Particles & auxiliaries** (`jo, ju, ja, je, ba, va, vi, la, le, li, lo`): `Operator`.
* **Digits** (`pa, pe, ... tu`) and **powers-of-ten** (`py, ty, ky, ...`): `Number` (no domain/aspect).
* **Wh-words / relativizers** (`fa, fe, fi, fo, fy`): `Operator` or `Relator`.
* **Quantifiers** (`kafa, kefe, nefa, nyfa`): `Operator`, optionally `Entity<META, SYSTEM>`.

---

## 10. Worked Examples

### 10.1 Basic Statement

> **The big machine destroys the water.**
> **Mamukem gomen larum.**

* *Ma-muke-m* — big machine (Entity<TECH, FORCE>)
* *gome-n* — destroy/fight (Event<SOCIAL, FORCE>)
* *laru-m* — water (Entity<NATURE, SUBSTANCE>)

### 10.2 Negative Imperative

> **Hey you! Do not eat the food.**
> **Ti! Negyfun gyfut!**

* *ti* — you (sg)
* *Ne-gyfu-n* — NEG-eat-V (Event<META, SUBSTANCE> with [NEG] from Logic slot)
* *gyfu-t* — that food (Entity<META, SUBSTANCE>)

### 10.3 Yes/No Question

> **Did you see the big galaxy?**
> **Jo ti ravikun magylat.**

* *Jo* — yes?/question
* *ti* — you (sg)
* *Ra-viku-n* — past-see-V (Event<HUMAN, SUBSTANCE>; root *viku* has V₁=I, V₂=U)
* *Ma-gyla-t* — that big galaxy (Entity<META, STATIC>)

### 10.4 Comparative

> **The earth is smaller than the sky.**
> **Garam misepas ga kalet.**

* *Gara-m* — earth (Entity<NATURE, STATIC>)
* *Mi-sepa-s* — micro-space-ADJ “smaller in area” (Property<PHYSICS, STATIC>)
* *ga kale-t* — than the sky (Relator + Entity<PHYSICS, STATIC>)

### 10.5 Passive, Instrument & Causative with Voice and G-series

> **The wall was built by the people.**
> **Murat radudumin gu koporam.**

* *mura-t* — wall-DET (Entity<TECH, STATIC>)
* *Ra-du-dumi-n* — PST-PASS-build-V “was built”
* *gu koporam* — with/by the people (INSTR/COMIT)

> **The people made the machine move via the road.** (assuming *Sepam* “road/area”)
> **Koporam radamevin muket go sepam.**

* *Koporam* — Ko-pora-m, group-person-N “people”
* *Ra-da-mevi-n* — PST-CAUS-move-V “made (something) move”
* *muke-t* — machine-DET (Entity<TECH, FORCE>)
* *go sepa-m* — via road/space-N (PATH/MEDIUM)

### 10.6 Relative Clause

> **The people who built the house were attacked.**
> **Koporam fe radumin dumit radugomen.**

* *Koporam* — the people
* *fe* — who (relative pronoun, subject of embedded clause)
* *Ra-dumi-n* — PST-build-V
* *dumi-t* — house-DET
* *Ra-du-gome-n* — PST-PASS-fight-V “were attacked”

### 10.7 Complement Clause with *Lo*

> **I think that he will come.**
> **Mi voron lo si rimevin.**

* *mi* — I
* *voro-n* — think/believe-V
* *lo* — that (complementizer)
* *si* — he/she/it
* *Ri-mevi-n* — FUT-move/go-V “will come”

### 10.8 Conditional

> **If you do not eat the food, you will not be healthy.**
> **Nu ti negyfun gyfut, ti rinevitus.**

* *Nu* — if
* *ti* — you (sg)
* *Ne-gyfu-n* → *negyfun* — NEG-eat-V
* *gyfu-t* — the food
* *ti* — you
* *Ri-ne-vitu-s* → *rinevitus* — FUT-NEG-healthy-ADJ
* “If you do not eat the food, you will not be healthy.”

### 10.9 Number Example

> **There are 2019 people in the house.**
> **Pi by ty tu koporam gi dumit.**

* *Pi by ty tu* — 2×10³ + 1×10¹ + 9 = 2019
* *koporam* — people
* *gi dumi-t* — in/at the house-DET (LOCATION)

### 10.10 Adjectives, Adverbs, and PPs Together

> **Now these three small healthy people of the person eat the food on land at the house.**
> **Ro po ke koporam misepas vitus porar gyfun gyfut garal gi dumit.**

Breakdown:

* *Ro* — now (frame adverb)
* *Po ke koporam* — three these people (Number + DemDet + head)
* *misepa-s vitu-s* — small-ADJ healthy-ADJ (adjective block)
* *pora-r* — of the person (genitive NP)
* *gyfu-n gyfut* — eat the food (V + object NP)
* *gara-l* — on-land-ADV (VP adverb)
* *gi dumi-t* — at the house-DET (PP, location)

---