# The Optimized Conlang – Full Foundational Spec (with Logical Numerals)

This document contains everything needed to **use** the language: phonology, morphology, semantic matrix, lexicon, syntax, derivation, numerals, and semantic typing.

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
     * Pronouns, conjunctions, prepositions, auxiliaries, digits, wh-words, quantifiers, complementizers.
     * No productive affixes in the core grammar.

   * **Content words**

     * One **CVCV root**, optionally with up to five **CV prefixes** (R/N/D/M/S/K series) and one final suffix.
     * Open-class lexemes (nouns, verbs, adjectives, adverbs, determiners).

3. **Semantic matrix**

   * CVCV root structure: **C V₁ C V₂**.
   * **V₁** (first vowel) = **domain** (Nature / Physics / Human / Social / Tech / Meta).
   * **V₂** (second vowel) = **semantic aspect** (Static / Force / Flow / Concept / Substance / System).
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
   * Closed classes: pronouns, particles, prepositions, auxiliaries, digits, wh-words, quantifiers, complementizers, powers-of-ten.
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

> Note: **Nu-** is the bound, verbal form of conditional marking. There is also an atomic **Nu** “if” used as a clausal subordinator (§7.10).

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

| Word | Meaning  |
| :--- | :------- |
| Mi   | I / me   |
| Tu   | you (sg) |
| Sa   | he / she |
| Su   | it       |
| Ma   | we       |
| Ta   | you (pl) |
| So   | they     |

> Some CV forms overlap with numerals (e.g. **Ta**, **Tu**), disambiguated by syntactic position and semantics.

### 4.2 Particles, Auxiliaries & Modals

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

### 4.3 Prepositions & Temporal Adverbs

| Word | Class | Meaning           |
| :--- | :---- | :---------------- |
| Ga   | prep  | from / than       |
| Ge   | prep  | to / towards      |
| Gi   | prep  | with / at / using |
| Go   | prep  | by / via          |
| Ra   | adv   | before (time)     |
| Ro   | adv   | now / currently   |
| Ri   | adv   | after (time)      |

### 4.4 Conditionals (Atomic)

| Word | Class | Meaning |
| :--- | :---- | :------ |
| Nu   | conj  | if      |

> *Nu* introduces conditional clauses (§7.10). It is related in meaning to the prefix **Nu-** in the Logic series.

### 4.5 Decimal Digits (0–9)

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

### 4.6 Powers of Ten (CVy series)

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

| Form | Value      | Role                            |
| :--- | :--------- | :------------------------------ |
| Py   | 10⁰ = 1    | unit (rarely used in cardinals) |
| Ty   | 10¹ = 10   | “ten”                           |
| Ky   | 10² = 100  | “hundred”                       |
| By   | 10³ = 1000 | “thousand”                      |
| Dy   | 10⁴        |                                 |
| Gy   | 10⁵        |                                 |
| Fy   | 10⁶        |                                 |
| Vy   | 10⁷        |                                 |
| Sy   | 10⁸        |                                 |
| My   | 10⁹        |                                 |
| Ny   | 10¹⁰       |                                 |
| Ly   | 10¹¹       |                                 |
| Ry   | 10¹²       |                                 |
| Jy   | 10¹³       |                                 |

In **ordinary cardinal numerals**, exponents ≥ 1 are used (`Ty, Ky, By, …`). `Py` is mostly for mathematical talk (“ten to the zero”).

These are also head kind **Number**.

### 4.7 Complex Cardinal Numbers

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

### 4.8 Wh-Words (F- series)

| Word | Meaning              |
| :--- | :------------------- |
| Fa   | what / which (thing) |
| Fe   | who / which (person) |
| Fi   | where / which place  |
| Fo   | why / reason         |
| Fu   | how / manner         |
| Fy   | when / which time    |

> In addition to interrogatives, F-series words can function as **relative pronouns** in relative clauses (§7.8).

### 4.9 Quantifiers

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

| V₁ | Domain  | Scope                                |
| :- | :------ | :----------------------------------- |
| A  | Nature  | environment, non-human natural world |
| E  | Physics | physical laws, forces, geometry      |
| I  | Human   | body, mind, immediate human states   |
| O  | Social  | persons, norms, communication        |
| U  | Tech    | artifacts, built environment         |
| Y  | Meta    | cosmos, data, abstractions           |

### 5.2 Semantic Aspects (columns, V₂)

This is a **semantic aspect** axis, distinct from grammatical TAM/aspect markers.

| V₂ | Aspect    | Scope                                      |
| :- | :-------- | :----------------------------------------- |
| A  | Static    | shapes, regions, stable entities           |
| E  | Force     | energies, intensities, powers              |
| I  | Flow      | agents, processes, dynamic interactions    |
| O  | Concept   | forms, patterns, representations           |
| U  | Substance | matter, resources, consumable states       |
| Y  | System    | systems, cycles, networks, structured sets |

### 5.3 Base Sense Grid

| V₁↓ / V₂→     | -A Static             | -E Force/Intensity | -I Flow/Agent              | -O Concept/Form                  | -U Substance/Resource | -Y System/Structure                 |
| :------------ | :-------------------- | :----------------- | :------------------------- | :------------------------------- | :-------------------- | :---------------------------------- |
| **A Nature**  | Terrain               | Weather/Air        | Animal life                | Plant form/growth                | Natural fluid         | Natural cycles/time                 |
| **E Physics** | Space/region          | Energy/light       | Motion/force               | Wave/signal                      | Matter/chemistry      | Math/geometry                       |
| **I Human**   | Body/anatomy          | Sensation          | Self/agency                | Emotion/attitude                 | Life state            | Spirit/identity system (reserved)   |
| **O Social**  | Person/role           | Power/conflict/law | Communication/exchange     | Belief/idea/norm                 | Resources/economy     | Culture/media/art (reserved)        |
| **U Tech**    | Artifact/surface/edge | Tool/machine       | Built environment & access | Transport/infrastructure concept | Covering/clothing     | Waste/maintenance system (reserved) |
| **Y Meta**    | Cosmos/world          | Data/network       | Micro-unit/instance        | Abstract thing/void/type         | Need/food/consumption | Variable/unknown                    |

> The mapping from vowels to Domain/Aspect is **systematic but not rigid**. Roots are generally chosen to “fit” their cell, but metaphor and convenience can bend them. The **type system** (§9) always reads Domain/Aspect from the root vowels, regardless of how the lexicon glosses a word.

---

## 6. CVCV Lexicon (Aligned with Matrix)

Roots listed bare; add suffixes in usage.

### 6.1 A- row: Nature

**A-A (Terrain)**

* **Gara** — land / earth
* **Pata** — stone / rock

**A-E (Weather/Air)**

* **Kale** — sky / air
* **Vate** — wind

**A-I (Animal life)**

* **Basi** — animal

**A-O (Plant form)**

* **Pano** — plant / tree

**A-U (Natural fluid)**

* **Laru** — water

**A-Y (Natural cycles/time)**

* **Tamy** — natural time / cycles (day, seasons)

---

### 6.2 E- row: Physics

**E-A (Space/region)**

* **Sepa** — space / area

**E-E (Energy/light)**

* **Sele** — light / sun

**E-I (Motion/force)**

* **Mevi** — move / go
* **Pesi** — push
* **Peli** — pull

**E-O (Wave/signal)**

* **Seno** — sound

**E-U (Matter/chemistry)**

* **Metu** — matter / chemistry

**E-Y (Math/geometry)**

* **Leny** — line / mathematical structure

---

### 6.3 I- row: Human

**I-A (Body/anatomy)**

* **Kipa** — head / body
* **Mina** — hand
* **Kila** — eye
* **Rina** — mouth

**I-E (Sensation)**

* **Sine** — sense / feel

**I-I (Self/agency)**

* **Kiri** — self / core

**I-O (Emotion/attitude)**

* **Vilo** — emotion / will

**I-U (Life state)**

* **Vitu** — life / health
* **Dimu** — sleep
* **Viku** — wake / see
* **Mitu** — die

**I-Y (Spirit/identity system)**

* (reserved)

---

### 6.4 O- row: Social

**O-A (Person/role)**

* **Pora** — person / social role

**O-E (Power/conflict/law)**

* **Gome** — war / conflict
* **Loge** — law (enforcing social power)

**O-I (Communication/exchange)**

* **Nomi** — name / word (linguistic sign)
* **Dogi** — give / transfer / exchange
* **Bobi** — book / record (container of words)
* **Somi** — say / speak / express

**O-O (Belief/idea/norm)**

* **Voro** — truth / idea / doctrine; to think/believe
* **Fono** — goal / end / purpose
* **Keno** — knowledge / to know

**O-U (Resources/economy)**

* **Monu** — money / economy

**O-Y (Culture/media/art)**

* (reserved)

---

### 6.5 U- row: Technology

**U-A (Artifact/surface/edge)**

* **Mura** — wall (constructed barrier surface)
* **Kuta** — knife / blade / cut

**U-E (Tool/machine)**

* **Muke** — tool / machine
* **Kuve** — key (tool to open/close)

**U-I (Built environment & access)**

* **Dumi** — house / building; to build
* **Puti** — door / gateway

**U-O (Transport/infrastructure concept)**

* **Vugo** — vehicle

**U-U (Covering/clothing)**

* **Vusu** — clothing

**U-Y (Waste/maintenance system)**

* (reserved)

---

### 6.6 Y- row: Meta

**Y-A (Cosmos/world)**

* **Kyma** — system / cosmos
* **Gyla** — galaxy

**Y-E (Data/network)**

* **Dyte** — data / net

**Y-I (Micro-unit/instance)**

* **Pyki** — pixel / point

**Y-O (Abstract thing/void/type)**

* **Vyro** — (abstract) thing / entity
* **Nyfo** — void / null / nothingness

**Y-U (Need/food/consumption)**

* **Gyfu** — food / nourishment; to eat

**Y-Y (Variable/unknown)**

* **Vyry** — variable / X / unknown

---

## 7. Syntax

### 7.1 Roles & Marking

Analytic: position + prepositions mark roles.

| Role       | Marking                                                |
| :--------- | :----------------------------------------------------- |
| Agent      | subject NP (before verb)                               |
| Patient    | direct object NP (after verb)                          |
| Recipient  | NP with **Ge** (“to”)                                  |
| Source     | NP with **Ga** (“from”)                                |
| Location   | NP with **Gi** (“with/at/by”) or spatial prefix/adverb |
| Instrument | NP with **Gi** (“with, using”)                         |
| Comparand  | NP with **Ga** (“from, than”)                          |

### 7.2 Clause Order

Canonical order: **SVO**.

**Intransitive**

```text
[NP-AGENT] [V]
```

> **Sa dimun.**
> *sa* 3sg
> *dimu-n* sleep-V
> “He sleeps.”

**Transitive**

```text
[NP-AGENT] [V] [NP-PATIENT]
```

> **Tu vikun kalet.**
> *tu* you
> *viku-n* see-V
> *kale-t* sky-DET
> “You see the sky.”

**Ditransitive**

```text
[NP-AGENT] [V] [NP-PATIENT] [Ge NP-RECIPIENT]
```

> **Ro mi dogin monut ge tu.**
> *ro* now
> *mi* I
> *dogi-n* give-V
> *monu-t* money-DET
> *ge tu* to you
> “Now I give the money to you.”

Adjuncts (time, place, manner) usually follow SVO but can be fronted for focus:

> **Ro, mi dimun.**
> “Now, I sleep.”

### 7.3 Noun Phrases (NP)

Canonical NP structure:

```text
[Quantifier/Number] [Group-Prefix + N-M(+T?)] [Adjectives] [Genitive-NP] [PPs]
```

* **Head noun**: CVCV + **-M**

  * *Garam* — land
  * *Poram* — person

* **Definiteness / specificity**: suffix **-T** on the head, or quantifiers like *kafa*.

  * *Garat* — that/the land
  * *Kafa* — everything

* **Plural/group**: **Ko-** as group prefix.

  * *Koporam* — people
  * *Kogaram* — lands

* **Adjectives**: follow head, suffix -S.

  * *Garam vitus* — “healthy land”

* **Genitive**: possessor NP as noun with **-R**, after head.

  * *Garam porar.* — “the person’s land”
  * *Garat porar.* — “the land of the person”

* **Prepositional modifiers**: typically follow NP.

  * *Garat gi poram* — “the land with the person”

#### 7.3.1 Quantifier & Number Interaction

Quantifiers and K-series prefixes both express quantity and grouping.

General conventions:

* **Number phrases** precede the NP:

  * *Po koporam* — “three people”
  * *Pi by ty tu koporam* — “2019 people”

* **Quantifier words** (*kafa, kefe, nefa, nyfa*) typically also precede:

  * *Kefe koporam* — “everyone / all people”
  * *Nyfa poram* — “some person(s)”
  * *Nefa poram* — “no person / nobody”

* **Group prefix Ko-** marks plurality/group on the head noun:

  * *Koporam* — “(the) people, a group of persons”

* **Ka-/Ki-/Ke- prefixes** on the noun itself:

  * *Kaporam* — “all person(s)” (union of the person-set)
  * *Kiporam* — “some part of the people; some person(s)”
  * *Keporam* — “no members; nobody (as a noun head)”

Both patterns are allowed; subtle distinctions:

* *Kefe koporam* — discourse-wide quantification “everyone”
* *Kaporam* — lexically group-marked “the whole group in question”

Position is fixed: quantifiers and number phrases **before** the NP; K-prefixes on the head.

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
    “The people built the wall.”

  * *Murat radudumin (gi koporam).*
    “The wall was built (by the people).”
    (*Ra-du-dumi-n* PST-PASS-build-V)

### 7.5 Questions

**Wh-Questions**

Start with an F-series wh-word.

```text
Wh-Word + Clause
```

> **Fa tu gyfun gyfut?**
> “What do you eat?”

> **Fe ravikun garat?**
> “Who saw the land?”

**Yes/No Questions**

Start with **Jo**.

```text
Jo + Clause
```

> **Jo tu gyfun gyfut?**
> “Do you eat the food?”

> **Jo sa ragaran garam?**
> “Did he land on the land?”

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
> **Tu! Negyfun gyfut!** — “You! Don’t eat the food!”

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

**Examples**

> **Porat fe ravikun kalet dimun.**
> *pora-t* person-DET
> *fe* who
> *Ra-viku-n* PST-see-V
> *kale-t* sky-DET
> *dimu-n* sleep-V
> “The person who saw the sky is sleeping.”

> **Garat fa tu vikun fe dimun.**
> “The land that you saw is sleeping (metaphorically).”

> **Dumit fi koporam dimun garam.**
> “The house where the people sleep is on the land.”

The relative clause directly follows the head NP.

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

> **Mi kenon sa rimevin.**
> *mi* I
> *keno-n* know-V
> *sa* he
> *Ri-mevi-n* FUT-move/go-V
> “I know he will come.”

#### 7.9.2 Complementizer *Lo*

Pattern:

```text
[Matrix Subject] [Matrix Verb] lo [Embedded Clause]
```

> **Mi kenon lo sa rimevin.**
> “I know that he will come.”

> **Sa somin lo tu nevikun garat.**
> *sa* he
> *somi-n* say/speak-V
> *lo* that
> *tu* you
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

> **Sa somin lo fa tu gyfun.**
> “He said what you eat.”

---

### 7.10 Conditionals

Conditionals are primarily formed with atomic **Nu** “if” introducing the **protasis** (if-clause).

Basic pattern:

```text
Nu [Protasis Clause], [Apodosis Clause].
```

> **Nu sa rimevin, mi rigyfun gyfut.**
> “If he comes, I will eat the food.”

> **Nu tu negyfun gyfut, tu rivitus ne.**
> “If you do not eat the food, you will not be healthy.”

The **Nu-** prefix in the Logic series can also be used on verbs to mark conditional semantics in a more local way (e.g. *Nugyfun* “eat if/when…”), but clausal **Nu** is the primary conditional construction.

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

```text
A → STATIC
E → FORCE
I → FLOW
O → CONCEPT
U → SUBSTANCE
Y → SYSTEM
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

* **Pronouns**: `Pronoun` (no domain/aspect, or `HUMAN` if desired).
* **Prepositions** (`ga, ge, gi, go, ra, ro, ri`): `Relator`.
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
> **Tu! Negyfun gyfut!**

* *tu* — you
* *Ne-gyfu-n* — NEG-eat-V (Event<META, SUBSTANCE> with [NEG] from Logic slot)
* *gyfu-t* — that food (Entity<META, SUBSTANCE>)

### 10.3 Yes/No Question

> **Did you see the big galaxy?**
> **Jo tu ravikun magylat.**

* *Jo* — yes?/question
* *tu* — you
* *Ra-viku-n* — past-see-V (Event<HUMAN, SUBSTANCE>; root *viku* has V₁=I, V₂=U)
* *Ma-gyla-t* — that big galaxy (Entity<META, STATIC>)

### 10.4 Comparative

> **The earth is smaller than the sky.**
> **Garam misepas ga kalet.**

* *Gara-m* — earth (Entity<NATURE, STATIC>)
* *Mi-sepa-s* — micro-space-ADJ “smaller in area” (Property<PHYSICS, STATIC>)
* *ga kale-t* — than the sky (Relator + Entity<PHYSICS, STATIC>)

### 10.5 Passive & Causative with Voice

> **The wall was built by the people.**
> **Murat radudumin gi koporam.**

* *mura-t* — wall-DET (Entity<TECH, STATIC>)
* *Ra-du-dumi-n* — PST-PASS-build-V “was built”
* *gi koporam* — with/by the people

> **The people made the machine move.**
> **Koporam radamevin muket.**

* *Koporam* — Ko-pora-m, group-person-N “people”
* *Ra-da-mevi-n* — PST-CAUS-move-V “made (something) move”
* *muke-t* — machine-DET (Entity<TECH, FORCE>)

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
> **Mi voron lo sa rimevin.**

* *mi* — I
* *voro-n* — think/believe-V
* *lo* — that (complementizer)
* *sa* — he
* *Ri-mevi-n* — FUT-move/go-V “will come”

### 10.8 Conditional

> **If you do not eat the food, you will be weak.**
> **Nu tu negyfun gyfut, tu rivitus ne.**

* *Nu* — if
* *tu* — you
* *Ne-gyfu-n* — NEG-eat-V
* *gyfu-t* — the food
* *tu* — you
* *Ri-vitu-s* — FUT-healthy-ADJ
* *ne* — negation (via Logic or negative property; implementation can be refined)

Intended: “If you do not eat the food, you will not be healthy.”

### 10.9 Number Example

> **There are 2019 people in the house.**
> **Pi by ty tu koporam gi dumit.**

* *Pi by ty tu* — 2×10³ + 1×10¹ + 9 = 2019
* *koporam* — people
* *gi dumi-t* — at the house-DET

---