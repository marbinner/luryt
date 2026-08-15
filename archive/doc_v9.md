Got it — here’s a clean “v5” foundational document where **every place that uses consonants** is aligned with the new **canonical consonant order**:

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

and every consonant-based series respects that order.

---

# 0. Big Picture

Core ideas:

* **Simple phonology**

  * 20 consonants, 6 vowels.
  * Syllables = **CV** or **CVC** only, no clusters.

* **Strictly parseable morphology**
  Content words always have this shape:

  ```text
  [Time?] [Logic?] [Voice?] [Scale or Space?] [Group?] + CVCV root + PoS suffix
  ```

  with **prefix consonants restricted to a small set** and **exactly one final PoS suffix**.

* **Semantic matrix for roots**

  * Root = **C₁ V₁ C₂ V₂**
  * **V₁** = Domain (HUMAN, SOCIAL, NATURE, PHYSICS, TECH, META)
  * **V₂** = Aspect (FLOW, SYSTEM, FORCE, STATIC, FORM, SUBSTANCE)

* **Numeric CV codes**

  * Use the **canonical consonant order** and a **fixed vowel order** to map 00–99 to CV syllables.

---

# 1. Phonology

## 1.1 Consonants

**Canonical consonant order (used everywhere: indexing, series, CV codes):**

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

This order follows articulation:

* **Place**: labial → alveolar → postalveolar/palatal → velar → uvular → glottal
* **Manner** (within a place): stops → nasals/affricates → fricatives → liquids/approximants.

### Inventory

| Letter | IPA  | Description                          | Like in…              |
| ------ | ---- | ------------------------------------ | --------------------- |
| P      | /p/  | bilabial voiceless stop              | *p* in *spin*         |
| B      | /b/  | bilabial voiced stop                 | *b* in *bat*          |
| M      | /m/  | bilabial nasal                       | *m* in *map*          |
| F      | /f/  | labiodental voiceless fricative      | *f* in *fan*          |
| V      | /v/  | labiodental voiced fricative         | *v* in *van*          |
| T      | /t/  | alveolar voiceless stop              | *t* in *stop*         |
| D      | /d/  | alveolar voiced stop                 | *d* in *dog*          |
| N      | /n/  | alveolar nasal                       | *n* in *no*           |
| Q      | /ts/ | alveolar voiceless **affricate**     | *ts* in *cats, tsar*  |
| S      | /s/  | alveolar voiceless fricative         | *s* in *see*          |
| Z      | /z/  | alveolar voiced fricative            | *z* in *zoo*          |
| L      | /l/  | alveolar lateral approximant         | *l* in *lip*          |
| C      | /tʃ/ | postalveolar voiceless **affricate** | *ch* in *change*      |
| W      | /dʒ/ | postalveolar voiced **affricate**    | *j* in *judge*        |
| X      | /ʃ/  | postalveolar voiceless fricative     | *sh* in *she*         |
| J      | /j/  | palatal approximant                  | *y* in *yes*          |
| K      | /k/  | velar voiceless stop                 | *k* in *cat*          |
| G      | /g/  | velar voiced stop                    | *g* in *go*           |
| R      | /ʀ/  | uvular trill (often [ʁ])             | guttural R (Fr./Ger.) |
| H      | /h/  | glottal voiceless fricative          | *h* in *hat*          |

**Terminal consonants** (used as PoS suffixes and allowed word-final):

> **L, M, N, R, S, T**

These are a subset of the canonical order and keep their own internal relative order (L < M < N < R < S < T is not semantically important, just a closed set).

---

## 1.2 Vowels

**Canonical vowel order** (front → back, high → low / central):

> **I  Y  E  A  O  U**

| Letter | IPA | Description          | Example-ish       |
| ------ | --- | -------------------- | ----------------- |
| I      | /i/ | high front unrounded | *i* in *machine*  |
| Y      | /y/ | high front rounded   | German *ü*        |
| E      | /e/ | mid front unrounded  | *é* in many langs |
| A      | /a/ | low (front/central)  | *a* in *father*   |
| O      | /o/ | mid back rounded     | pure “o”          |
| U      | /u/ | high back rounded    | *u* in *food*     |

* CVCV roots may use **all 6**.
* CV-digit codes use **only the first 5**: **I, Y, E, A, O**.

---

## 1.3 Syllable Structure & Stress

* Allowed syllables: **CV** or **CVC**.
* No clusters; no onsetless syllables.
* Stress falls on the **penultimate** syllable of the word.

---

# 2. Word Structure

## 2.1 Word Classes

1. **Atomic words**

   * Mostly **CV**, plus a few fixed longer particles.
   * Closed classes: pronouns, demonstratives, prepositions, conjunctions, auxiliaries, wh-words, some quantifiers, numeric CV codes.
   * No productive internal morphology.

2. **Content words**

   * Exactly one **CVCV root**.
   * Up to **five CV prefixes** in fixed slots.
   * Exactly one **final PoS suffix** from {L, M, N, R, S, T}.
   * Open classes: nouns, verbs, adjectives, adverbs, determiners.

---

## 2.2 Content Word Template & Prefix Consonants

Template:

```text
[Time] [Logic] [Voice] [Scale or Space] [Group] + CVCV root + PoS suffix
```

**Only these consonants are allowed in prefixes** (and in this slot order):

> **P (Time), B (Logic), M (Voice), F (Scale), V (Space), W (Group)**

That sequence **P B M F V W** is the subset of the global consonant order used for prefixes.

Within a word:

1. **Time** (slot 1): P- series
2. **Logic / Reality** (slot 2): B- series
3. **Voice / Valency** (slot 3): M- series
4. **Scale / Degree** (slot 4a): F- series
   **or** **Space** (slot 4b): V- series
5. **Group / Quantification** (slot 5): W- series

Constraints:

* At most one prefix from each of P-, B-, M-, F-, V-, W-series.
* At most one of F- vs V- total.
* Prefixes must appear in the slot order **P → B → M → F/V → W**.

Root and suffix may use **any consonants** (from P through H).

---

## 2.3 PoS Suffixes (Final Consonants)

Final consonant = PoS:

| Suffix | PoS | Function                       |
| ------ | --- | ------------------------------ |
| -M     | N   | noun (entity)                  |
| -S     | ADJ | adjective (quality)            |
| -N     | V   | finite verb                    |
| -L     | ADV | adverb (manner/place/etc.)     |
| -R     | GEN | genitive (“of X”)              |
| -T     | DET | determiner / specific instance |

These six come from the global consonant set and are a closed class.

---

## 2.4 Prefix Series (All Respect Vowel Order I Y E A O U)

For each prefix consonant C ∈ {P, B, M, F, V, W}, we define a **series**:

* C + I
* C + Y
* C + E
* C + A
* C + O
* C + U

always in that order.

### 2.4.1 Time (P-series, slot 1)

| Prefix  | Meaning                      |
| ------- | ---------------------------- |
| **Pi-** | remote past (“long ago”)     |
| **Py-** | recent past (“lately”)       |
| **Pe-** | present / now                |
| **Pa-** | near future                  |
| **Po-** | remote future                |
| **Pu-** | gnomic / timeless / habitual |

### 2.4.2 Logic / Reality (B-series, slot 2)

| Prefix  | Meaning                      |
| ------- | ---------------------------- |
| **Bi-** | certain / factual / asserted |
| **By-** | likely / typical             |
| **Be-** | possible                     |
| **Ba-** | unknown / neutral            |
| **Bo-** | unlikely                     |
| **Bu-** | impossible / counterfactual  |

### 2.4.3 Voice / Valency (M-series, slot 3)

| Prefix  | Meaning (applied to verb V)      |
| ------- | -------------------------------- |
| **Mi-** | basic / default voice (active)   |
| **My-** | middle / reflexive (“V oneself”) |
| **Me-** | reciprocal (“V each other”)      |
| **Ma-** | applicative (“V for/on Y”)       |
| **Mo-** | causative (“make X V”)           |
| **Mu-** | passive (“be V-ed / undergo V”)  |

### 2.4.4 Scale / Degree (F-series, slot 4a)

| Prefix  | Meaning           |
| ------- | ----------------- |
| **Fi-** | micro / tiny      |
| **Fy-** | small             |
| **Fe-** | neutral / average |
| **Fa-** | big               |
| **Fo-** | huge / very big   |
| **Fu-** | mass / collective |

### 2.4.5 Space (V-series, slot 4b, competes with F-series)

| Prefix  | Meaning                   |
| ------- | ------------------------- |
| **Vi-** | in / inside               |
| **Vy-** | at / on (contact/surface) |
| **Ve-** | near / around             |
| **Va-** | towards / into            |
| **Vo-** | from / out of / away      |
| **Vu-** | through / across          |

### 2.4.6 Group / Quantification (W-series, slot 5)

| Prefix  | Meaning                              |
| ------- | ------------------------------------ |
| **Wi-** | no members / empty set               |
| **Wy-** | one / single                         |
| **We-** | some / a few                         |
| **Wa-** | many                                 |
| **Wo-** | all / entire set                     |
| **Wu-** | structured group / network / linkage |

All these series **use vowels in the I Y E A O U order**, and the consonant for each series respects the global consonant order in §1.1.

---

## 2.5 Parsing Content Words

Given a token:

1. If length = 2 and matches **C V**, with C in the full consonant set (P…H) and V in {i,y,e,a,o,u} → treat as **atomic word**.
2. Else:

   1. Check final char ∈ {l, m, n, r, s, t} → PoS suffix.
   2. Take the preceding 4 letters as the **CVCV root**.
   3. Remaining leftmost part is the **prefix block**, possibly empty.
   4. Parse prefix block as a sequence of CV prefixes where:

      * prefix consonants are in {p, b, m, f, v, w}, i.e. the six series letters ordered P B M F V W,
      * at most one P-, one B-, one M-, one F-, one V-, one W-,
      * at most one of F- vs V- total,
      * and series appear in P → B → M → F/V → W order.
3. If all constraints are met, segmentation is unique and valid.

This uses the **restricted prefix consonants** and **global C/V orders** to guarantee strict parsability.

---

# 3. Semantic Matrix of CVCV Roots

Each root is **C₁ V₁ C₂ V₂**. The consonants are arbitrary; the **vowels** encode semantic type.

We use the global vowel order:

> **I  Y  E  A  O  U**

* **V₁** (first vowel) → **Domain**
* **V₂** (second vowel) → **Aspect**

## 3.1 Domains (V₁ in I Y E A O U order)

| V₁    | Domain  | Scope                                                    |
| ----- | ------- | -------------------------------------------------------- |
| **I** | HUMAN   | self, body, mind, individual persons                     |
| **Y** | SOCIAL  | relationships, roles, norms, institutions, communication |
| **E** | NATURE  | terrain, weather, non-human life, environment            |
| **A** | PHYSICS | physical laws, fields, geometry                          |
| **O** | TECH    | tools, devices, machines, built infrastructure           |
| **U** | META    | data, logic, math, abstract systems                      |

The **domain list is explicitly in vowel order I → Y → E → A → O → U**.

## 3.2 Aspects (V₂ in I Y E A O U order)

| V₂    | Aspect    | Scope                                                  |
| ----- | --------- | ------------------------------------------------------ |
| **I** | FLOW      | events, processes, interactions, motion                |
| **Y** | SYSTEM    | organized systems, networks, cycles, multi-part wholes |
| **E** | FORCE     | energy, intensity, potential to cause change           |
| **A** | STATIC    | regions, shapes, stable configurations                 |
| **O** | FORM      | patterns, representations, conceptual “forms”          |
| **U** | SUBSTANCE | matter, stuff, resources, “what it’s made of”          |

Again, listed strictly as I → Y → E → A → O → U.

## 3.3 HeadKind from Suffixes & Derivation

For any **content word**:

* Root vowels → Domain & Aspect.
* PoS suffix → base **HeadKind**:

```text
-M / -R / -T  → Entity<Domain,Aspect>
-N            → Event<Domain,Aspect>
-S            → Property<Domain,Aspect>
-L            → Manner<Domain,Aspect>
```

Optionally, you can use **series prefixes** in fixed templates:

* **Bi- + root + -M** → “abstract state/event of X” (using Logic series to reify a proposition).
* **Wa- + root + -M** → “typical doer of X” (using Group series for agent roles).
* **Mu- + root + -M** → “instrument/tool for X” (Voice series repurposed in derivation).

These derivations still respect the same prefix and suffix rules and use consonants in the allowed sets.

---

# 4. CV Codes for 00–99

We **strictly** follow the global consonant order and vowel order to define CV-codes:

* Consonants: **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**
* Numeric vowels: the **first 5** in the vowel order: **I  Y  E  A  O**

So we get 20 × 5 = 100 distinct CV syllables.

## 4.1 Indexing

**Consonant index (C_index, 0–19)**

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

**Vowel index (V_index, 0–4)**

0. I
1. Y
2. E
3. A
4. O

Both sequences follow the global ordering.

## 4.2 Number → CV

For integer **d** with 0 ≤ d ≤ 99:

```text
c_index = d // 5      # integer division → 0..19
v_index = d % 5       # remainder         → 0..4

CV(d) = C[c_index] + V[v_index]
```

### Examples

**Block 0** (C = P, c_index = 0):

* 00 → **PI**
* 01 → **PY**
* 02 → **PE**
* 03 → **PA**
* 04 → **PO**

**Block 1** (C = B, c_index = 1):

* 05 → **BI**
* 06 → **BY**
* 07 → **BE**
* 08 → **BA**
* 09 → **BO**

**Block 2** (C = M, c_index = 2):

* 10 → **MI**
* 11 → **MY**
* 12 → **ME**
* 13 → **MA**
* 14 → **MO**

…

**Last block** (C = H, c_index = 19):

* 95 → **HI**
* 96 → **HY**
* 97 → **HE**
* 98 → **HA**
* 99 → **HO**

## 4.3 CV → Number

Given a CV syllable with:

* C in {P, B, M, F, V, T, D, N, Q, S, Z, L, C, W, X, J, K, G, R, H},
* V in {I, Y, E, A, O},

we recover the number:

```text
d = 5 * c_index + v_index
```

where `c_index` and `v_index` are the positions of C and V in their canonical lists.

The **ordering is fully canonical**: no exceptions.

---

# 5. Atomic Series (C/V-ordered)

These are **atomic words** (mostly CV), not built from CVCV roots, but they still respect the global C/V orders internally.

## 5.1 Pronouns (T / D / N, with vowels I/A)

We choose three adjacent consonants from the canonical order:

* After V = index 4, the next consonants are **T (5), D (6), N (7)**.

Map:

* **T** → 1st person
* **D** → 2nd person
* **N** → 3rd person

Use vowels for number:

* **I** → singular
* **A** → plural

Pronouns:

| Form   | Person/Number | Meaning   |
| ------ | ------------- | --------- |
| **Ti** | 1sg           | I / me    |
| **Ta** | 1pl           | we / us   |
| **Di** | 2sg           | you (sg)  |
| **Da** | 2pl           | you (pl)  |
| **Ni** | 3sg           | he/she/it |
| **Na** | 3pl           | they      |

Order T D N is exactly consonant indices 5, 6, 7.

## 5.2 Demonstratives (K-series, number × distance)

Pick **K** from the velar region (index 16), and use vowels in order:

* I/Y/E = singular (near → mid → far)
* A/O/U = plural (near → mid → far)

| Form   | Features     | Meaning                    |
| ------ | ------------ | -------------------------- |
| **Ki** | sg, proximal | this (near speaker)        |
| **Ky** | sg, medial   | that (near hearer/context) |
| **Ke** | sg, distal   | that (far away)            |
| **Ka** | pl, proximal | these                      |
| **Ko** | pl, medial   | those (near hearer)        |
| **Ku** | pl, distal   | those (far away)           |

K+vowels are listed **Ki Ky Ke Ka Ko Ku**, respecting I Y E A O U.

## 5.3 Wh-words (F-series, atomic)

Use **F** (index 3) with vowels in order for wh-/relative roles, from concrete → abstract:

| Form   | Meaning              |
| ------ | -------------------- |
| **Fi** | what / which (thing) |
| **Fy** | who / which (person) |
| **Fe** | where / which place  |
| **Fa** | when / which time    |
| **Fo** | why / reason         |
| **Fu** | how / manner         |

Again Fi–Fy–Fe–Fa–Fo–Fu is in strict vowel order.

## 5.4 Prepositions (G-series, atomic)

Use **G** (index 17, after K) with vowels in order for NP roles:

| Form   | Core Role    | Meaning / Use              |
| ------ | ------------ | -------------------------- |
| **Gi** | LOCATION     | in, at, on                 |
| **Gy** | GOAL         | to, towards                |
| **Ge** | SOURCE       | from, out of               |
| **Ga** | PATH/MEDIUM  | via, along, through        |
| **Go** | INSTR/COMIT  | with, using, together with |
| **Gu** | CAUSE/REASON | because of, due to         |

Ordering is **Gi Gy Ge Ga Go Gu**, exactly matching I Y E A O U.

## 5.5 Particles & Auxiliaries (examples)

These can be somewhat arbitrary but still stay within the phonological system:

* **Ja** — and

* **Je** — or

* **Jo** — yes / yes–no question marker

* **Ju** — no

* **Ba** — be

* **Va** — have

* **Li** — want / intend

* **Le** — can / be able

* **La** — must / necessary

* **Lo** — that (complementizer)

* **Nu** — if (subordinator; uses N, index 7)

They are **atomic** and do not follow the prefix/root suffix template.

---

# 6. Syntax Skeleton (Ordering-neutral)

Syntax reuses your earlier design and is mostly independent of consonant order (so nothing to reorder here), but for completeness:

* **Canonical clause order**: SVO

  ```text
  [Frame Adv*] [Subject NP] [Aux*] [Verb] [Object NP*] [Adv(-L)*] [PP*]
  ```

* Roles via position + G-prepositions:

  * Subject = agent/experiencer by default.
  * Object = patient/theme.
  * Gi NP = location, Gy NP = goal, Ge NP = source, Ga NP = path, Go NP = instrument/comitative, Gu NP = cause.

* **NP structure**:

  ```text
  [Number/Quant] [Dem K-] [Head N-M/T (+ W-prefix if used)]
  [Adj-S*] [Genitive N-R?] [RelClause*] [PP*]
  ```

* **Questions**:

  * Wh: F-series word (Fi/Fy/Fe/Fa/Fo/Fu) at start.
  * Yes/no: Jo + clause.

* **Conditionals**:

  * Nu + protasis, followed by apodosis.

---

Everything that **depends on consonant order** now explicitly follows:

* The global consonant order **P B M F V T D N Q S Z L C W X J K G R H**.
* Series subsets (prefix consonants, pronoun consonants, etc.) are **subsequences** of that order, and all internal lists use that same order for vowels and consonants.
