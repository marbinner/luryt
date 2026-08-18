<!-- Generated from language/grammar/foundational.md; do not edit. -->

# Foundational Spec (v2)

> **v2 — August 2026.** First revision, driven by an external stress test of the language.
> Summary of changes: **-t** referential vs **-m** descriptive; a **pivot-and-role** clause rule;
> three distinct spatial constructions with the new **G-series** (path orientation) and **ru** as
> the path-phrase closer; linear **operator scope**; a clause-final **ROOT-l event-manner slot**;
> a zero-copula **simple property clause** with broad N-series polarity and narrow **na** scope;
> the numeral marker **num** with productive base-100
> cardinal runs; stress restated as root-anchored (equivalent to the old penultimate rule).
> The prior version is preserved as
> `archive/doc_v15.md`. Details in §9.

## 0. Scope

**Fixed now:**

- Consonant inventory **and canonical order**
- Vowel inventory **and canonical order**
- Syllable structure & stress
- Two word types: **atomic CV** vs **content words**
- Content-word template: **(CV prefixes) + CVCV root + final suffix**
- Final suffix system: **M T N S L R** and what each means
- Principle that **CV series use one consonant + vowels in I Y E A O U order**
- Root semantics: **6 Domains × 6 Aspects** (semantic matrix)
- Numeric **00–99 → CV block** system and canonical base-100 cardinal composition
- Particle series defined so far: **P, M, F, T, D, N, Q, S, C, W, J, K, G, R, H**
- First derivational prefix series: **K-series** (configuration / collectivity)
- A core lexicon: **one root per semantic cell (36 roots)**
- The numeral marker **num** (§8.1)
- Clause **pivot rule** and linear **operator scope** (§7.1)
- Clause-final event-modifying **ROOT-l manner slot** (§7.1)
- Zero-copula simple **ROOT-s property clause** with broad N-series and narrow **na** polarity
  scope (§7.5)
- Free K-series noun-phrase order and scope before Q/D/NUM (§7.2)
- Exact-cardinal noun-phrase slot and scope with K/Q/D (§7.2)
- Attributive **ROOT-s** property modifiers in the noun-phrase slot before the entity head
  (§7.2)
- **F-series coordination**: same-kind infix coordination of noun phrases and clauses,
  sentence-initial discourse linkage, and the low-attachment rule (§7.6)
- Symmetric C-scale with superlative-low **ci**, and a single front N-series polarity
  position on comparative and superlative clauses (§7.5)
- Monotone Q-scale with **qi** “few”; empty-set claims are compositional (front N over an
  existential, §4.8/§7.1)

**Still open (deliberately):**

- Numeric expressions beyond nonnegative exact cardinals: negative numbers, fractions, decimals, and ordinals, and scalar bounds over cardinals (“at least three”)
- Additional derivational prefix series (Time, Voice, Valence, etc.)
- More closed-class items (focus particles, further clause-linkers, etc.)
- The earmarked series **B** (mood / clause force),
  **X** (subordinate-clause delimiters), **Z** (reflexive / reciprocal / discourse reference):
  functions reserved, forms not yet specified. **V** and **L** remain unallocated.
- Layers on top of coordination: emphatic/exclusive correlatives (“both … and”,
  “either … or”), K-configuration scoping over a whole coordination, ellipsis and gapping
  across conjuncts, and coordination of bare numerals (an open payload run absorbs a
  numeric-vowel F form; use counted heads or separate sentences)
- Causal subordination (“because”-clauses): X-series work; until then, put the cause first
  and link with **fo** (§7.6)
- Larger lexicon beyond the 36 core roots
- Full syntax for complex clauses, subordination, focus, etc.
- Direct event-level use and ordering of free K-series modifiers relative to the event-operator track
- Distribution and scope of T/P/H/M operators in property clauses
- Non-event distribution of manner (`ROOT-l`) heads and general distribution of relational
  (`ROOT-r`) heads
- Property restriction of pronoun-headed noun phrases; non-restrictive (appositive)
  modification; and degree (M) or comparison (C) operators inside noun phrases
- W-extraction from inside static-location and oriented-path phrases

Design principle:

> Wherever natural, **CV particles double as prefixes** with parallel semantics
> (phrasal vs lexical level). K-series is the first fully specified example of this.

---

## 1. Phonology

### 1.1 Consonants

Canonical consonant order (for indexing, sorting, numeric codes, series labels):

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

| Letter | IPA  | Description                             |
|--------|------|-----------------------------------------|
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

**Final consonant pool (for content words):**

> **M  T  N  S  L  R**

Only these six may appear as the final consonant of a **content word**.

---

### 1.2 Vowels

Canonical vowel order:

> **I  Y  E  A  O  U**

| Letter | IPA | Description          |
|--------|-----|----------------------|
| I      | /i/ | high front unrounded |
| Y      | /y/ | high front rounded   |
| E      | /e/ | mid front unrounded  |
| A      | /a/ | low (front/central)  |
| O      | /o/ | mid back rounded     |
| U      | /u/ | high back rounded    |

Used for:

- semantic series (particles, prefixes),
- root matrix coordinates (V₁, V₂),
- numeric CV block system (I/Y/E/A/O; U unused in the 00–99 block inventory).

---

### 1.3 Syllable Structure & Stress

- Allowed syllables: **CV** or **CVC**
- No onsetless syllables; no consonant clusters
- Stress: on the **first syllable of the root** — which, given the content-word template, is
  always the **penultimate syllable**. The two statements are equivalent; the root-anchored one
  is primary (v2).
- Free atomic particles are separate prosodic words, each carrying its own stress.

Examples: `pi.rim` → **pi**rim; `ka.pi.rim` → ka**pi**rim.

Because prefixes are unstressed but free particles are stressed, `ka pirim` (**ka** **pi**rim,
“people, as a group”) is audibly distinct from `kapirim` (ka**pi**rim, “a crowd”).

---

## 2. Word Structure

### 2.1 Two Word Types

1. **Atomic words (particles)**
   - Shape: typically **CV**; a few longer fixed forms allowed
     (currently one exists: **num**, the numeral marker — §8.1).
   - Used for: pronouns, TAM, quantifiers, roles, wh-words, etc.
   - No productive morphology (no prefixes/suffixes) on these forms.

2. **Content words**
   - Exactly one **CVCV root**.
   - Optional prefix block of one or more **CV prefixes**.
   - Exactly one final consonant suffix from {**M, T, N, S, L, R**}.
   - Template:

     ```text
     (CV prefix)* + CVCV(root) + final suffix
     ```

   - Open-class items: entities, events, properties, manners, relations.

In running text:

- bare **CV** → atomic word (particle, numeral, etc.).
- **CVCV + suffix** (+ optional CV prefixes) → content word.

---

### 2.2 Final Suffix System (Head Kinds)

Final suffixes (in canonical order):

> **-M  -T  -N  -S  -L  -R**

| Suffix | Head kind        | Typical use                                           |
|--------|------------------|-------------------------------------------------------|
| **-m** | Entity head      | descriptive noun: “an X / X-things” (no particular one) |
| **-t** | Referential head | identifiable entity or set: “the X (we can identify)”  |
| **-n** | Event head       | verb: “to X / X happens”                             |
| **-s** | Property head    | adjective: “X-like, having X-property”               |
| **-l** | Manner head      | adverb: “in an X way, X-ly”                          |
| **-r** | Relational head  | relational NP: “of X, X’s, from X, related-by-X”     |

These six head meanings and their word formation are fixed. The basic syntax below specifies
entity, event, and property constructions, including event-modifying `ROOT-l` manner heads
(§7.1) and attributive `ROOT-s` modifiers inside noun phrases (§7.2). Non-event placement of
`ROOT-l` and the general placement and attachment rules for `ROOT-r` relational heads remain
deliberately open.

**-m** vs **-t** (v2): **-t** picks out a referent the hearer can identify — a specific
individual *or* an identifiable plural set (`kory-t` “the house / those houses, you know which”).
**-m** is descriptive and non-anchored: a class or an unidentified instance (`kory-m` “a house,
houses in general”). **-t** marks *identifiability*, not distance — pointing is the D-series’ job,
and demonstratives therefore normally combine with **-t** (§7.2).

Hyphens (`piri-m`) are just glossing; in orthography it’s written as one word (`pirim`).

---

### 2.3 Parsing Content Words

Given a token:

1. If length = 2 and shape = CV → treat as **atomic word**.
2. Else:
   - If final char ∉ `{m,t,n,s,l,r}` → not a well-formed content word.
   - Else:
     - final char = suffix.
     - preceding 4 characters must be **CVCV** = root.
     - any remaining left characters must form a sequence of **CV** prefixes.

If this holds, segmentation is unique:

```text
(CV prefix)* + CVCV(root) + suffix
````

---

### 2.4 Series Principle (Particles & Prefixes)

Any systematic CV series uses:

* **one consonant**, and
* all six **vowels** in canonical order **I Y E A O U**,
* mapping that vowel order to a consistent semantic progression.

Example:

* **T-series**: ti/ty/te/ta/to/tu for time: remote past → recent past → present → near future → far future → timeless.

Many CV series serve as:

* **free particles** (clausal/phrasal operators), and
* **prefixes** (lexical operators) with parallel semantics.

K-series (configuration) is the first fully specified particle+prefix series.

Note (categorical series): when one series crosses two categories (distance × number in D,
person × number in J), the vowels interleave **major–minor** — `di`/`dy` “this/these”,
`ji`/`jy` “I/we”. Future series must not place a participant-, polarity-, or
direction-flipping contrast on the acoustically weakest vowel pairs **i/y** and **o/u**;
those pairs should differ only in the minor category or by one step of the scale.

---

## 3. Semantic Matrix (Domains × Aspects)

Every root is **C₁ V₁ C₂ V₂**.

* **V₁** (first vowel) = **Domain** (row)
* **V₂** (second vowel) = **Aspect** (column)

### 3.1 Domains (V₁)

* **I = PERSON** – individual humans: body, mind, experience
* **Y = SOCIETY** – families, groups, institutions, culture
* **E = LIFE** – non-human life: animals, plants, ecosystems
* **A = PHYSICAL** – non-living world: matter, space, energy, weather
* **O = ARTEFACT** – tools, objects, machines, buildings, infrastructure
* **U = ABSTRACT** – ideas, language, math, logic, information

### 3.2 Aspects (V₂)

* **I = INDIVIDUAL** – basic “things/actors” in that domain
* **Y = CONFIG** – parts, wholes, groups, layouts, structures, systems
* **E = PROCESS** – activities, processes, changes, doing
* **A = STATE** – relatively stable conditions/qualities
* **O = RELATION** – links/roles between things
* **U = QUANTITY** – measures, magnitudes, degrees

### 3.3 Cells (V₁ × V₂) – Concept Zones

#### I PERSON (V₁ = I)

* **II** – person, self
* **IY** – body, hand, heart, family
* **IE** – act, speak, eat, see, move
* **IA** – hungry, tired, sad, happy, healthy
* **IO** – friend-of, parent-of, sibling-of, lover-of
* **IU** – age, strength, personal habit frequency

#### Y SOCIETY (V₁ = Y)

* **YI** – group, tribe, clan, city (as social unit)
* **YY** – institution, hierarchy, government, organization
* **YE** – trade, talk, fight, negotiate, vote, cooperate
* **YA** – peace, war, crisis, stability, trust
* **YO** – citizen-of, member-of, boss-of, rule-over
* **YU** – money, price, wealth, budget, GDP

#### E LIFE (V₁ = E)

* **EI** – animal, plant, fungus, organism
* **EY** – forest, herd, swarm, ecosystem
* **EE** – grow, hunt, migrate, bloom, reproduce
* **EA** – alive, dead, sick, healthy, poisonous
* **EO** – predator-of, prey-of, host-of, symbiont-of
* **EU** – population size, biomass, crop yield

#### A PHYSICAL (V₁ = A)

* **AI** – rock, river, mountain, planet, physical object
* **AY** – landscape, region, terrain, field, cluster
* **AE** – flow, fall, rain, blow, melt, freeze
* **AA** – hot, cold, solid, liquid, gas, wet, dry
* **AO** – in, on, under, near, around, between
* **AU** – length, mass, time, energy, temperature

#### O ARTEFACT (V₁ = O)

* **OI** – tool, knife, cup, phone, vehicle, device
* **OY** – house, road, bridge, network, city plan
* **OE** – cut, build, drive, send, compute
* **OA** – broken, fixed, open, closed, on, off
* **OO** – key-of, lock-for, plug-into, port-of, interface-with
* **OU** – size, capacity, speed, power, storage, bandwidth

#### U ABSTRACT (V₁ = U)

* **UI** – idea, concept, word, symbol
* **UY** – theory, language, model, formal system, taxonomy
* **UE** – think, learn, compute, imagine, infer
* **UA** – know, believe, remember, doubt, forget
* **UO** – cause-of, equal-to, implies, means-of, part-of
* **UU** – number, amount, probability, measure, degree

---

## 4. Particle Mappings (Atomic CV Series)

**Consonant order:**

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

**Vowel order:**

> **I  Y  E  A  O  U**

### 0 – P (Phase / Event Aspect)

| **Form** | **Phase value**                       | **Gloss**                      |
| -------- | ------------------------------------- | ------------------------------ |
| **pi**   | inceptive / just starting             | “just now start to”            |
| **py**   | progressive / in progress             | “currently, be -ing”           |
| **pe**   | resumptive / back again               | “again, back to doing it”      |
| **pa**   | continuative / still ongoing          | “still, keep (on)”             |
| **po**   | completive / through to the end       | “completely, all the way”      |
| **pu**   | perfect / already done / result state | “already, (has) done/finished” |

Used as clause particles, typically before the verb.

---

### 1 – B

*(reserved — earmarked for mood / clause force)*

---

### 2 – M (Degree / Intensity)

| **Form** | **Degree value**               | **Gloss**                 |
| -------- | ------------------------------ | ------------------------- |
| **mi**   | minimal presence               | “slightly, a bit, barely” |
| **my**   | low / below-typical            | “somewhat, rather low”    |
| **me**   | neutral / typical degree       | “moderately, normally”    |
| **ma**   | above-typical                  | “quite, pretty, fairly”   |
| **mo**   | strong / high degree           | “very, strongly”          |
| **mu**   | maximal / excessive / too much | “extremely, too, overly”  |

---

### 3 – F (Coordination & Logical Linkage)

| **Form** | **Relation**                        | **Gloss**            |
| -------- | ----------------------------------- | -------------------- |
| **fi**   | additive                            | “and”                |
| **fy**   | sequential                          | “and then”           |
| **fe**   | alternative (inclusive)             | “or”                 |
| **fa**   | adversative                         | “but, yet”           |
| **fo**   | consecutive                         | “so, therefore”      |
| **fu**   | preventive / alternative consequence | “or else, otherwise” |

The scale runs from symmetric addition to conditional consequence: additive → sequential →
alternative → adversative → consecutive → preventive. A free F particle joins two constituents
of the same kind — complete noun phrases or complete clauses — and may open a sentence as a
discourse connective. Syntax and attachment in §7.6.

Note (safety): **fi/fy** differ only in sequence, and **fo/fu** are both forward-looking
consequence links, so a misheard vowel keeps the discourse move. “Because” is deliberately
*not* an F form — backward-looking grounds are future X-series subordination; until then, put
the cause first and link with **fo** (§7.6).

---

### 4 – V

*(unused / reserved)*

---

### 5 – T (Time / Tense-like)

| **Form** | **Time value**    | **Gloss**             |
| -------- | ----------------- | --------------------- |
| **ti**   | remote past       | “long ago”            |
| **ty**   | recent past       | “recently, just now”  |
| **te**   | present           | “now, currently”      |
| **ta**   | near future       | “soon, about to”      |
| **to**   | far future        | “later, someday”      |
| **tu**   | gnomic / timeless | “generally, whenever” |

---

### 6 – D (Demonstratives)

| **Form** | **Distance / number**     | **Gloss**                |
| -------- | ------------------------- | ------------------------ |
| **di**   | near, singular            | “this”                   |
| **de**   | medial/local, singular    | “that (here / in view)”  |
| **do**   | far / elsewhere, singular | “that (elsewhere)”       |
| **dy**   | near, plural              | “these”                  |
| **da**   | medial/local, plural      | “those (here / in view)” |
| **du**   | far / elsewhere, plural   | “those (elsewhere)”      |

---

### 7 – N (Polarity)

| **Form** | **Polarity type**               | **Gloss / core force**          |
| -------- | ------------------------------- | ------------------------------- |
| **ni**   | explicit affirmation            | “yes, indeed, it is so”         |
| **ny**   | partial / mixed presence        | “sort of, partly, more or less” |
| **ne**   | neutral / unmarked polarity     | “(no special polarity)”         |
| **na**   | simple negation                 | “not, no, it isn’t so”          |
| **no**   | contrary / opposite / anti-     | “on the contrary, anti-”        |
| **nu**   | strong negation / impossibility | “never, absolutely not, cannot” |

---

### 8 – Q (Quantifiers)

| Form   | Type                       | Short gloss                       |
| ------ | -------------------------- | --------------------------------- |
| **qi** | few / small subset         | “few, a small number of”          |
| **qy** | existential, non-partitive | “a / some (there exists)”         |
| **qe** | partitive, not-all         | “some of (them), not all”         |
| **qa** | large subset               | “most (of)”                       |
| **qo** | universal, collective      | “all (of), the whole X”           |
| **qu** | universal, distributive    | “every / each / any (one by one)” |

The scale is a monotone positive quantity progression: few → some → some of → most → all →
every. There is no negative quantifier: an empty-set claim is compositional, with a front
N-series particle over an existential — `na qy piri-m pase-n.` “no person goes” (¬∃),
`nu qy piri-m pase-n.` “absolutely no one goes” — exactly as linear operator scope (§7.1)
already provides. Quantity is not configuration: `qi piri-m` “few people” (proportion)
contrasts with `ke piri-m` “people in a small group” (K-series grouping).

---

### 9 – S (Spatial Topology, Static/Dynamic)

| **Form** | **Topological relation (static)** | **Gloss**                     |
| -------- | --------------------------------- | ----------------------------- |
| **si**   | interior / within boundary        | “in, inside (within X)”       |
| **sy**   | surface / contact                 | “on, on top of, touching X”   |
| **se**   | adjacency / side-by-side          | “next to, beside X”           |
| **sa**   | surrounding area / vicinity       | “around X, in X’s area”       |
| **so**   | exterior / beyond boundary        | “outside X, beyond X”         |
| **su**   | among multiple / spread through   | “among X, amidst, throughout” |

Static pattern: `FIGURE S GROUND`
Path-neutral motion: `FIGURE S GROUND MOTION-VERB`; the S-relation describes the path topology.

---

### 10 – Z

*(reserved — earmarked for reflexive, reciprocal & discourse reference)*

---

### 11 – L

*(unused / reserved)*

---

### 12 – C (Comparatives / Scalar Relations)

| **Form** | **Comparative role**  | **Gloss**              |
| -------- | --------------------- | ---------------------- |
| **ci**   | superlative-low       | “least, the least ~”   |
| **cy**   | less-than             | “less, not as ~”       |
| **ce**   | equal                 | “as ~ as, equally”     |
| **ca**   | more-than             | “more, -er”            |
| **co**   | superlative           | “most, the most ~”     |
| **cu**   | extremal limit        | “as ~ as possible”     |

The scale is symmetric and monotone: least → less → equal → more → most → as-possible.

Pattern with property `PROP-s`:

```text
A cy/ce/ca PROP-s B re
= “A is less/as/more PROP than B”
```

`re` (R-series) marks **standard-of-comparison** (“than B”). The superlatives `ci` and `co`
take the standard-less frame `A ci/co PROP-s` (§7.5). Scalar bounds are compositional, not
lexical: front `na` over a comparative gives “at least” (`na … cy`, not-less) and “at most”
(`na … ca`, not-more) — see §7.5. No C form encodes a bound.

---

### 13 – W (Wh-/Interrogatives)

| **Form** | **Question type** | **Gloss**                 |
| -------- | ----------------- | ------------------------- |
| **wi**   | time              | “when?”                   |
| **wy**   | reason            | “why? (for what reason?)” |
| **we**   | place             | “where?”                  |
| **wa**   | thing             | “what? / what thing?”     |
| **wo**   | person            | “who? / which person?”    |
| **wu**   | manner            | “how? / in what way?”     |

---

### 14 – X

*(reserved — earmarked for subordinate-clause delimiters)*

---

### 15 – J (Personal Pronouns)

| Form   | Person / number | Gloss         |
| ------ | --------------- | ------------- |
| **ji** | 1sg             | I             |
| **jy** | 1pl             | we            |
| **je** | 2sg             | you (sg)      |
| **ja** | 2pl             | you (pl)      |
| **jo** | 3sg             | he / she / it |
| **ju** | 3pl             | they          |

The mapping is person-major, number-minor — the same major–minor interleave as the D-series
(`di`/`dy` “this/these”), so the acoustically closest pairs `ji`/`jy` and `jo`/`ju` differ
only in number (“I/we”, “he-she-it/they”), never in discourse participant.

---

### 16 – K (Configuration / Collectivity: Particle + Prefix)

**K-series** expresses how many units and how they are **grouped**.
Each form functions as:

* a **particle** (phrasal modifier), and
* a **prefix** `kV-` on roots, deriving “group-of-X” nouns (and optionally other heads).

| **Form** | **Config type**         | **Particle gloss**                 | **Prefix gloss (kV-ROOT-m)**                  |
| -------- | ----------------------- | ---------------------------------- | --------------------------------------------- |
| **ki**   | singled, atomic         | “as a single unit, alone, singly”  | “one singled-out X, an atomic unit”            |
| **ky**   | pair / dual             | “in pairs, as a pair”              | “a pair of X”                                 |
| **ke**   | small group             | “in a small group, a few together” | “a small group of X (a few Xs)”               |
| **ka**   | generic group / crowd   | “as a group, together, in a crowd” | “a group / crowd / community of X”            |
| **ko**   | large collective / mass | “en masse, as a large crowd/mass”  | “a large collective / mass / population of X” |
| **ku**   | scattered / distributed | “scattered, spread out, all over”  | “X scattered / distributed (many Xs)”         |

Examples of **prefix** use:

* `piri-m` = a person → `kapiri-m` = a group/crowd/community of people
* `feni-m` = an animal → `kefeni-m` = a small group of animals (if you choose that reading)
* `kory-m` = a house → `kakory-m` = a group of houses (neighborhood/block)

As a **particle before an NP**, K occupies the outermost NP slot:

```text
[K] [Q] [D] [NUM] [ROOT-s]* [ROOT-{m|t}]
```

The free K-particle configures the participants selected by the complete following Q/D/NUM/head
phrase. At most one free K-particle fills this slot. **NUM** is the optional exact-cardinal
constituent defined in §7.2.

* `ka piri-m sa sary-m pase-n.` – “People, configured as a group, go around the region.”
* `ky qe da feni-t` – “some of those animals, configured in pairs”

A bound `kV-` remains lexical inside the entity head, so Q and D select configuration entities
instead. Compare:

* `ka qa piri-m` – “most people, configured together”
* `qa ka-piri-m` – “most crowds”
* `ky qe da feni-t` – “some of those animals, configured in pairs”
* `qe da ky-feni-t` – “some of those identifiable animal pairs”

Direct event-level use of free K, and its order among the front operators, remain open (§7.1).

---

### 17 – G (Path Orientation)

Orients a motion event relative to its path. The path phrase is closed by **ru** (§7.3).

| **Form** | **Orientation** | **Gloss**                  |
| -------- | --------------- | -------------------------- |
| **gi**   | origin          | “from, starting at”        |
| **gy**   | departure       | “away from, leaving”       |
| **ge**   | route           | “along, via, through”      |
| **ga**   | approach        | “toward, nearing”          |
| **go**   | endpoint        | “into / onto, arriving at” |
| **gu**   | return          | “back to, returning”       |

Pattern: `FIGURE  G  (S)  GROUND  ru  MOTION-VERB` — see §7.3.

---

### 18 – R (Roles / Case-like Particles)

| **Form** | **Role**                   | **Gloss**                                  |
| -------- | -------------------------- | ------------------------------------------ |
| **ri**   | agent / controller         | “by (agent), as doer”                      |
| **ry**   | experiencer / beneficiary  | “to / for (person)”                        |
| **re**   | patient / theme / standard | “object of, about; ‘than’ in comparatives” |
| **ra**   | instrument / means         | “with, using, by means of”                 |
| **ro**   | location / setting         | “at, in, on (place/time)”                  |
| **ru**   | path-frame closer          | closes a G-oriented path phrase; not directional by itself |

`NP + R` pattern: R normally acts like a postposition. In the path construction, **ru** closes
the complete `G (S) GROUND` frame; the G-series supplies its orientation (§7.3).

---

### 19 – H (Frequency / Habituality)

| **Form** | **Frequency value** | **Gloss**            |
| -------- | ------------------- | -------------------- |
| **hi**   | single occurrence   | “once, one time”     |
| **hy**   | low frequency       | “rarely, seldom”     |
| **he**   | intermittent        | “sometimes”          |
| **ha**   | frequent            | “often, frequently”  |
| **ho**   | typical / habitual  | “usually, normally”  |
| **hu**   | maximal frequency   | “always, constantly” |

---

## 5. Derivational Prefixes

Content words:

```text
(CV prefix)* + CVCV(root) + suffix
```

Some CV series can serve **both** as:

* **particles** (independent CV words), and
* **derivational prefixes** on content roots.

When used as a prefix, they apply their semantics **lexically**, inside the word, rather than phrasally.

### 5.1 K-series as derivational prefix (configuration)

For a root **R = C₁V₁C₂V₂**, entity head **R-m**:

* `R-m`  – “an X (individual)”
* `kiR-m` – “a single, singled-out X”
* `kyR-m` – “a pair of X”
* `keR-m` – “a small group of X (a few)”
* `kaR-m` – “a group/crowd/community of X”
* `koR-m` – “a large collective/mass/population of X”
* `kuR-m` – “X scattered/distributed all over”

Example:

* `piri-m` = person
* `kapiri-m` = (one) group of people, a crowd/community

This **does not change** the Domain×Aspect classification of the root; it only modifies **internal configuration**.

Note (v2): **ki-** singles out one unit from a configuration (“one of the group”). It does not
mark identifiability (that is **-t**) nor pointing (that is the D-series): `kipiri-m` “a lone
individual”, `kipiri-t` “the lone individual (we can identify)”.

Other series (M, T, etc.) may later get parallel **prefix roles** (e.g. degree prefixes on adjectives, tense-aspect prefixes on verbs).

---

## 6. Core Roots (Matrix-Aligned Lexicon)

Each root is **CVCV**. Actual words add a suffix:

* `ROOT-m` – entity
* `ROOT-t` – referential entity or set (identifiable in context)
* `ROOT-n` – event/verb
* `ROOT-s` – property
* `ROOT-l` – manner
* `ROOT-r` – relational

### I I

* **piri** – person, human individual

### I Y

* **mily** – body, physical self

### I E

* **zife** – to speak, talk (personal act)

### I A

* **hisa** – to be well, healthy

### I O

* **siro** – friend relation, friend-of

### I U

* **tinu** – age of a person (years lived)

---

### Y I

* **rydi** – group, crowd, people-as-unit

### Y Y

* **syry** – institution, organized structure

### Y E

* **gyfe** – to interact socially, mingle

### Y A

* **vyra** – social peace, order, stability

### Y O

* **tyro** – rule/authority relation, boss-of

### Y U

* **byru** – wealth, money amount

---

### E I

* **feni** – animal (non-human)

### E Y

* **bely** – forest / herd / ecosystem cluster

### E E

* **kefe** – to grow, develop (biological)

### E A

* **mela** – to be alive, living

### E O

* **sevo** – ecological relation (predator-of, symbiont-of, etc.)

### E U

* **benu** – population, biomass, ecological quantity

---

### A I

* **kati** – rock, stone, lump of matter

### A Y

* **sary** – region, landscape, area

### A E

* **pase** – to move, go, travel, flow

### A A

* **hata** – hot/warm (physical temperature)

### A O

* **sako** – physical relation (contact/inclusion/proximity)

### A U

* **daru** – distance, spatial extent, length

---

### O I

* **toki** – tool, implement, usable object

### O Y

* **kory** – house, building, constructed structure

### O E

* **gose** – to build, construct, make artefact

### O A

* **vosa** – broken, out of order

### O O

* **zoro** – functional relation (fit, plug, compatibility)

### O U

* **komu** – capacity, size, volume (of artefacts)

---

### U I

* **rufi** – idea, concept

### U Y

* **lury** – language, system, theory

### U E

* **guse** – to think, compute, reason

### U A

* **gusa** – to know, be knowledgeable

### U O

* **kuro** – cause-of, reason relation

### U U

* **nunu** – number, amount, abstract quantity

*(Examples sometimes use an extra root `nife` ≈ “eat”; this is a **provisional** IE root not yet in the core 36 list.)*

---

## 7. Basic Syntax (Provisional)

### 7.1 Default Event-Clause Template

A useful canonical order for a clause headed by an event word (`ROOT-n`):

```text
[W (+R)?] [T] [P] [H] [M] [N] [PIVOT] [other NPs + R/S] [MANNER] [na] VERB
```

Where:

* **W (+R)** – wh-word, optionally followed by the role it questions (§7.4)
* **T** – time (ti/ty/te/ta/to/tu)
* **P** – phase/aspect (pi/py/pe/pa/po/pu)
* **H** – frequency (hi/hy/he/ha/ho/hu)
* **M** – degree (mi/my/me/ma/mo/mu)
* **N** – polarity (ni/ny/ne/na/no/nu)
* **PIVOT** – optional unmarked pronoun (J) or NP
* **other NPs + R/S** – arguments and spatial phrases
* **MANNER** – optional single event-modifying `ROOT-l` manner head
* **na** – optional narrow-scope polarity immediately before the verb
* **VERB** – root + `-n`

The smallest pivoted event clause is **PIVOT + VERB**. The pivot may be absent in a fully
role-marked clause. Static-location and property-predicate clauses use their own patterns below
and do not require an event word.

The track covers the fixed event operators. A free K-particle that introduces an NP belongs to
that NP and precedes its Q, D, and NUM slots (§§4.16, 7.2). Direct event-level K scope and order
relative to this track remain open.

An event clause may contain one event-modifying `ROOT-l` manner head in a clause-final MANNER
slot after the pivot and every role-marked or spatial phrase but before the existing
immediately-preverbal narrow `na` (if present) and final `ROOT-n`; the manner modifies that final
event predicate, while W/T/P/H/M/N front operators retain their existing order and rightward
scope. The slot is optional and single: multiple event-manner heads are not licensed.

Example:

* `ji zife-n.` – “I speak.”
* `te py ji zife-n.` – “Now I am speaking.”

**Pivot and roles (v2).** An event clause has at most one *unmarked* noun phrase: the **pivot**, in
the pivot slot, read as the most agent-like argument of the verb. Every other argument carries an
R-series role particle (§7.3), including a questioned argument (§7.4). A clause may also be
*fully role-marked*, with no pivot at all — which is how the agent is omitted, with no passive
morphology:

* `ji kory-t re toki-m ra gose-n.` – “I build the house with a tool.”
* `ji je ry qy rufi-m re zife-n.` – “I tell you an idea.”
* `ty di kory-t re gose-n.` – “This house was built recently.” (patient marked, agent omitted)

**Event manner.** The MANNER slot stays adjacent to the clause-final event tail even when the
clause contains arguments or spatial frames:

* `ji guse-l zife-n.` – “I speak thoughtfully.”
* `ji kory-t re toki-m ra guse-l gose-n.` – “I build the house thoughtfully, with a tool.”
* `ji si di kory-t ro guse-l zife-n.` – “I speak thoughtfully inside this house.”
* `ji go si di kory-t ru vyra-l pase-n.` – “I move peacefully into this house.”
* `ji guse-l na zife-n.` – the fixed narrow-polarity tail is `MANNER na VERB`

**Operator scope (v2).** The front operators ([T] [P] [H] [M] [N]) take scope over everything to
their right, in linear order. Polarity **na** may also stand immediately before the verb for
narrow scope:

* `na qo piri-m pase-n.` – “Not all people go.” (¬∀)
* `qo piri-m na pase-n.` – “All the people don’t go — none of them go.” (∀¬)

---

### 7.2 Noun Phrase Template

```text
[K] [Q] [D] [NUM] [ROOT-s]* [ROOT-{m|t}]
```

* **K** – configuration of the selected participants (ki/ky/ke/ka/ko/ku)
* **Q** – quantifier (qi/qy/qe/qa/qo/qu)
* **D** – demonstrative (di/de/do/dy/da/du)
* **NUM** – optional exact nonnegative cardinal, with the fixed form `num numeric-CV+`
* **ROOT-s*** – zero or more attributive property modifiers, each restricting the head
* **ROOT-m / ROOT-t** – descriptive or referential entity head

Examples:

* `qi piri-m` – few people
* `qy piri-m` – a person / some person
* `qa piri-m` – most people
* `qe da feni-t` – some of those animals (here)
* `qo du kory-t` – all those houses (over there)
* `ka qa piri-m` – most people, configured together
* `ky qe da feni-t` – some of those animals, configured in pairs
* `ki qu dy kory-t re gose-n.` – each of these houses, configured singly, was built
* `dy num pa piri-t` – these three people / exactly three of these people
* `qe da num bi feni-t` – some but not all of those five animals
* `qu dy num pa kory-t re gose-n.` – each of these three houses was built

Free K takes scope over the participants selected by the following Q/D/NUM/head phrase. Bound K
is part of the head instead: `ka num pa piri-m` means “exactly three people, together,” while
`num pa ka-piri-m` means “exactly three crowds.” Likewise, `ky qe da feni-t` configures some
animals as pairs, whereas `qe da ky-feni-t` selects some identifiable animal-pair entities. Only
one free K occupies the optional outer slot. A following R-series role marks the complete NP,
including its K/Q/D/NUM scope.

A NUM constituent contains the marker followed by a maximal run of one or more numeric CV blocks:

```text
NUM = num numeric-CV+
```

Each block keeps its 0–99 value from §8. With block values *d₁ … dₖ*, the run is read
most-significant first in base 100:

```text
value = d₁ × 100^(k-1) + d₂ × 100^(k-2) + … + dₖ
```

A one-block run therefore retains every existing 0–99 expression. In a run of two or more blocks,
the first block must be nonzero; zero blocks may occur internally or finally. `num pi` is the sole
form of zero. There is no maximum block count.

NUM gives the exact cardinality of the entity head — as restricted by any attributive block —
inside any restriction supplied by D. An overt
Q scopes over the following D/NUM/head cardinal frame, so `qe da num bi feni-t` selects some but
not all of an identified five-animal set. All K/Q/D particles precede NUM, and the attributive
block follows NUM. After `num`, successive
numeric CVs belong to its payload until the first structurally distinct content word — an
attributive modifier or the entity head — ends the run;
no K/Q/D or other particle can intervene. Outside an entity NP, the numeral-phrase boundary ends
a standalone NUM. A later `num` begins a separate NUM constituent, not another block of the same
integer. These boundaries preserve the particle/numeral distinction even when a CV has both uses:

* `num pa piri-m` – three people
* `qe num qe piri-t` – some but not all of an identifiable forty-two-person set
* `da num da piri-t` – thirty-three of those people (first `da` = demonstrative; second = 33)
* `ka num ka piri-m` – eighty-three people, configured together (first `ka` = K; second = 83)
* `num py pi piri-m` – one hundred people
* `num py pi pi kory-t` – ten thousand identifiable houses
* `ka num pe pi piri-m` – two hundred people configured together
* `num pe pi ka-piri-m` – two hundred crowd entities

The rule adds no special agreement morphology: combinations whose existing D, Q, and numeral
meanings contradict one another remain semantically anomalous.

**Attributive properties.** An entity noun phrase may include an attributive block of one or
more property modifiers — each a bare `ROOT-s` content word — immediately before its entity
head. Each attributive `ROOT-s` restricts the head's referents intersectively to those having
the property; order among stacked attributives carries no semantic import. The surrounding
K/Q/D/NUM operators take scope over the restricted head: restriction applies before
configuration, quantification, pointing, and counting, so `qa vosa-s kory-m` quantifies over
broken houses, not houses. Attributive `ROOT-s` occurs only in this prenominal block — never
after the head, never on a pronoun head, and nowhere else in the clause — so clause-final
property predication (§7.5) keeps its unique parse. The positions form a minimal pair:
`vosa-s kory-m` “a broken house” is a noun phrase, while `kory-m vosa-s.` “a house is broken”
is a clause.

* `vosa-s kory-m` – a broken house / broken houses
* `di vosa-s kory-t` – this broken house
* `qa vosa-s kory-m` – most broken houses
* `qe da vosa-s kory-t` – some of those broken houses
* `dy num pa vosa-s kory-t` – these three broken houses
* `ka hisa-s piri-m` – healthy people, configured as a group
* `di hata-s vosa-s toki-t` – this hot, broken tool (equivalently `di vosa-s hata-s toki-t`)
* `tu hata-s kati-m pase-n.` – “Hot rocks move.” (gnomic claim about a restricted kind)
* `ti di vosa-s kory-t re gose-n.` – “This broken house was built long ago.”
* `di vosa-s kory-t hata-s.` – “This broken house is hot.” (attribution inside the subject,
  predication at the clause end)

Demonstratives point at identifiable referents, so they normally take **-t** heads; a **-m** head
after a demonstrative gives a kind reading (`da feni-m` ≈ “those sorts of animal”).

Pronouns (`ji, jy, je, ja, jo, ju`) behave as NPs.

---

### 7.3 Roles & Space

Role particles (R-series):

* `NP ri` – agent/doer
* `NP re` – patient/theme; also “than NP” in comparatives
* `NP ry` – experiencer/beneficiary (“to/for NP”)
* `NP ra` – instrument/means (“with, using NP”)
* `NP ro` – location/setting (“at/in/on NP”)
* `G (S) GROUND ru` – completed path frame; G supplies origin/route/goal orientation

Space (v2) distinguishes three constructions:

**1 · Static location** — no verb needed: `FIGURE  S  GROUND`

* `di piri-t si di kory-t.` – “This person is inside this house.”

**2 · Location adjunct of an event** — the spatial phrase is closed by `ro` (location role):

* `ji si di kory-t ro zife-n.` – “I speak inside this house.”

**3 · Motion path.** An S-phrase alone supplies path topology without choosing an orientation:

* `ji sa sary-m pase-n.` – “I wander around the region.” (path-neutral motion)

A G-series particle adds orientation, and `ru` closes the whole oriented path phrase:
`FIGURE  G  (S)  GROUND  ru  MOTION-VERB`

* `ji go si di kory-t ru pase-n.` – “I go into this house.” (endpoint + inside)
* `ji gi si di kory-t ru pase-n.` – “I come out of this house.” (origin + inside)
* `jy ge su bely-m ru pase-n.` – “We travel through the forest.” (route + among)
* `jo gu si di kory-t ru pase-n.` – “She returns into this house.”

`ru` no longer means “from” or “to” by itself: orientation lives in the G-series, and `ru` is the
role particle closing the completed path frame. (This fixes v1, where `ru` conflated source with
goal and the directional example placed `ru` *before* its NP, against the `NP + R` rule.)

---

### 7.4 Questions

**Wh-questions** use the W-series and keep the W-word clause-initial. A W-word that questions the
pivot is unmarked. If it questions any other event participant or setting, its ordinary
R-series marker follows it immediately; the W+R phrase remains ahead of T/P/H/M/N. W-words used
as non-role operators (time, reason, manner) remain unmarked.

* `wo zife-n?` – “Who speaks?”
* `wa re ji nife-n?` – “What do I eat?” (patient)
* `wo ry ji qy rufi-m re zife-n?` – “To whom do I tell an idea?” (beneficiary)
* `wa ra ji di kory-t re gose-n?` – “With what do I build this house?” (instrument)
* `wo ri di kory-t re gose-n?` – “By whom was this house built?” (explicit agent; no pivot)
* `wi ju pase-n?` – “When do they go?”
* `wy jo guse-n?` – “Why does he/she think?”
* `we ro jo nife-n?` – “Where does he/she eat?” (event setting)
* `wu jo zife-n?` – “How does he/she speak?”
  * `jo guse-l zife-n.` – “He/she speaks thoughtfully.”

This rule does not extract a W-word from inside a static S construction or an oriented G…`ru`
path frame; those question constructions remain open (§0).

**Yes/no questions**: same clause + question intonation / `?`.

* `jo zife-n?` – “Does he/she speak?”

Answers with N-series:

* `ni.` – yes
* `na.` – no
* `no.` – on the contrary
* `nu.` – absolutely not / never

---

### 7.5 Properties and Comparatives

Property from root + `-s`:

* `gusa` – know / be knowledgeable → `gusa-s` – knowledgeable

**Simple property clause.** An unmarked affirmative non-comparative property clause has the
zero-copula form `SUBJECT PROPERTY`: SUBJECT is exactly one pronoun or complete
`[K] [Q] [D] [NUM] ROOT-{m|t}` noun phrase, and PROPERTY is exactly one clause-final `ROOT-s`
whose property is asserted of that subject.

```text
SUBJECT PROPERTY
```

Examples:

* `ji gusa-s.` – “I am knowledgeable.”
* `di kory-t vosa-s.` – “This house is broken.”
* `kory-m vosa-s.` – “A house is broken / houses are broken.”
* `qa dy num pa kory-t vosa-s.` – “Most of these three houses are broken.”
* `ky qe da feni-t mela-s.` – “Some of those animals, configured in pairs, are alive.”
* `di toki-t vosa-s?` – “Is this tool broken?” (ordinary yes/no intonation)

**Property polarity.** A simple property proposition may contain at most one free N-series
particle in one of two mutually exclusive positions:

```text
[N] SUBJECT PROPERTY
SUBJECT na PROPERTY
```

Any N-series form (`ni/ny/ne/na/no/nu`) may occupy the front position and takes rightward scope
over the complete `SUBJECT PROPERTY` proposition. Only `na` may instead occur immediately before
PROPERTY; there, the complete SUBJECT noun phrase — including its K/Q/D/NUM scope — outscopes
negation. The two positions cannot co-occur, and N particles do not stack. With neither position,
the clause retains the unmarked affirmative reading.

Examples:

* `ni di kory-t vosa-s.` – “Indeed, this house is broken.”
* `ny di kory-t vosa-s.` – “This house is partly / mixedly broken.”
* `ne di kory-t vosa-s.` – overt neutral polarity: “This house is broken.”
* `na di kory-t vosa-s.` – “This house is not broken.”
* `no di kory-t vosa-s.` – “On the contrary, this house is not broken.” (corrective opposite)
* `nu di kory-t vosa-s.` – “This house absolutely cannot be broken.”
* `na qo dy kory-t vosa-s.` – “Not all these houses are broken.” (`¬∀`)
* `qo dy kory-t na vosa-s.` – “All these houses are not broken — none of them is broken.” (`∀¬`)
* `na di toki-t vosa-s?` – “Isn’t this tool broken?” (ordinary yes/no intonation)

No copula, event head, role marker, or agreement stands between the subject and property; local
`na` is the sole licensed intervening polarity particle.
The template licenses one property predicate; multiple or coordinated property predicates remain
open. Attributive `ROOT-s` inside a noun phrase is licensed by §7.2 and is not predication: in
`di vosa-s kory-t hata-s.` only hotness is predicated, of this broken house. Property polarity is
the only operator extension licensed here:
simple property clauses have no T/P/H/M operator track, and those event-clause positions in §7.1
do not extend to them by analogy. The two N patterns above likewise do not extend by analogy to
static-location clauses; a comparison licenses one front polarity position of its own (below).

Comparative pattern (C-series + `re`):

* `ji ca gusa-s de piri-t re.`
  → “I am more knowledgeable than that person.”

* `ji ce gusa-s de piri-t re.`
  → “I am as knowledgeable as that person.”

* `ji cy gusa-s de piri-t re.`
  → “I am less knowledgeable than that person.”

Superlatives (standard-less frame):

* `ji co gusa-s.`
  → “I am the most knowledgeable.”

* `ji ci gusa-s.`
  → “I am the least knowledgeable.”

**Comparative polarity.** A comparative or superlative clause may contain at most one front
N-series particle, taking scope over the whole comparison; the narrow pre-predicate position
does not extend to comparisons:

* `na ji ca gusa-s de piri-t re.` – “I am not more knowledgeable than that person” — that is,
  at most as knowledgeable.
* `na ji cy gusa-s de piri-t re.` – “I am not less knowledgeable than that person” — at least
  as knowledgeable.
* `na ji ce gusa-s de piri-t re.` – “I am not exactly as knowledgeable as that person.”
* `ni ji ca gusa-s de piri-t re.` – “Indeed, I am more knowledgeable than that person.”
* `nu ji ca gusa-s de piri-t re.` – “I absolutely cannot be more knowledgeable than that
  person.”
* `na ji co gusa-s.` – “I am not the most knowledgeable.”

Scalar bounds are therefore compositional — **na + cy** “at least”, **na + ca** “at most” —
and no C form encodes a bound.

An overt C-series form keeps the existing comparative or superlative construction; it is not an
optional part of the simple `SUBJECT PROPERTY` template.

---

### 7.6 Coordination (F-series)

A free F particle (§4.3) links **exactly two constituents of the same kind** as `X F Y`:

- **noun phrases**: each conjunct is one complete §7.2 noun phrase (pronouns included), and
  the coordinated noun phrase stands wherever the grammar licenses a noun phrase — pivot,
  role-marked argument, property-clause subject, spatial ground. A following role particle
  marks the **complete** coordination; every K/Q/D/NUM particle and attributive modifier
  scopes only inside its own conjunct.
- **clauses**: each conjunct is one complete clause (event, property, comparative, or static);
  front operators (§7.1) remain local to their own clause — an operator’s rightward scope ends
  at its clause’s F boundary.

Chains iterate left to right with the same construction: `A fi B fi C`; a mixed chain such as
`A fi B fe C` groups as `(A fi B) fe C`.

**Attachment (low attachment).** An F particle immediately preceded by a noun-phrase-final
word (an entity head or pronoun) and immediately followed by a noun-phrase-initial word (a
K/Q/D particle, `num`, an attributive `ROOT-s`, an entity head, or a pronoun) coordinates
noun phrases; clause coordination is available only otherwise. To chain a clause after one
that ends in a noun phrase (a static-location clause), give the next clause a non-NP-initial
start — a front operator — or use separate sentences.

**Discourse use.** A sentence may open with one F particle, linking the whole sentence to the
previous sentence with the same relation: `di koryt vosas. fo ji gosen.` — “The house is
broken. So, I build.” Cause-first order plus **fo** covers “because” until X-series
subordination exists.

**Not licensed:** linking constituents of different kinds; F inside an attributive block;
correlative doubling (“both … and”); and F directly inside an open numeral payload — a
numeric-vowel F form there is read as a payload block (§8.1), so bare numerals are not
coordinable (coordinate counted heads instead: `num pa kory-m fi num bi feni-m`).

Examples:

* `ji kory-t fi toki-m re gose-n.` – “I build the house and the tool.” (one event, one role)
* `piri-m fe feni-m pase-n.` – “A person or an animal goes.”
* `di kory-t vosa-s fa di toki-t na vosa-s.` – “The house is broken, but the tool is not.”
* `di kory-t vosa-s fo ji gose-n.` – “The house is broken, so I build.”
* `ty jo zife-n fy jo pase-n.` – “She spoke and then goes on.”
* `na qy piri-m fe qy feni-m pase-n.` – “Neither a person nor an animal goes.” (¬∃ over `fe`)
* `di toki-t vosa-s fe di toki-t hata-s?` – “Is this tool broken, or is it hot?”
* `ji go si di kory-t fi di sary-t ru pase-n.` – “I go into the house and the region.”
* `piri-m fi feni-m fi kati-m pase-n.` – “The person, the animal, and the rock move.”
* `qa kory-m fi qe toki-m vosa-s.` – “Most houses and some tools are broken.”
* `te ji zife-n fi to je zife-n.` – “Now I speak, and later you will speak.”
* `je zife-n fu ji pase-n.` – “You speak, or else I go.”

---

## 8. Numeric CV Blocks and Base-100 Cardinals

Consonant indices (canonical order):

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

Vowel indices for numerals (first five vowels):

0. I
1. Y
2. E
3. A
4. O

Each numeric CV is one base-100 block. For integer **d** with 0 ≤ d ≤ 99:

```text
c_index = d // 5      # 0..19
v_index = d % 5       # 0..4

CV(d) = C[c_index] + V[v_index]
```

Examples:

* 00 → **pi**
* 01 → **py**
* 02 → **pe**
* 03 → **pa**
* 04 → **po**
* 05 → **bi**
* …
* 95 → **hi**
* 96 → **hy**
* 97 → **he**
* 98 → **ha**
* 99 → **ho**

Inverse, given CV (with vowel in {I,Y,E,A,O}):

```text
d = 5 * c_index + v_index
```

### 8.1 The numeral marker `num` and positional composition (v2)

Seventy-five of the hundred numeric CVs are homophonous with defined particles (`te` is both
“now” and 27). The remaining twenty-five use the five reserved or unallocated series consonants
and currently
have only a numeric reading. Because collisions are nevertheless systematic and common, ordinary
numeric expressions are announced uniformly by **num** — the language’s first fixed atomic form
longer than CV, a clipped entity form of **nunu** “number”:

* `num pi` – “zero”
* `num te` – “twenty-seven”
* `num py pi` – “one hundred” (blocks 1, 0)
* `num py py` – “one hundred one” (blocks 1, 1)
* `num py pi pi` – “ten thousand” (blocks 1, 0, 0)
* `num pa piri-m pase-n.` – “Three people go.”
* `pi ji zife-n.` – “I begin to speak.” (bare `pi` is still the phase particle)

Inside an entity NP, `num numeric-CV+` occupies the NUM slot after any K, Q, and D particles and
directly before the attributive block (if any) and entity head (§7.2).
The marker governs the maximal following run of numeric
CVs. For example, `da num da piri-t` keeps the first `da` demonstrative and reads the second as
33, while `da num py pi piri-t` reads the payload as 100.

For a payload of *k* block values *d₁ … dₖ*, composition is positional and
most-significant first:

```text
N = Σ dᵢ × 100^(k-i)    for i = 1 … k
```

Equivalently, start at zero and replace `N` with `100 × N + d` for each block from left to
right. The spelling is canonical:

* a payload contains at least one block;
* `num pi` is zero;
* a payload longer than one block cannot start with `pi`;
* internal and final `pi` blocks are retained; and
* the rule has no upper block-count limit.

Thus 9,999 is `num ho ho`, 10,001 is `num py pi py`, and 12,345,678 is
`num me do ly jy`. A following content word — attributive modifier or entity head — or the
boundary of a standalone numeral phrase
ends the run. A new `num` starts a separate numeral constituent: `num py pi` is the single
integer 100, whereas `num py / num pi` (with the slash only marking a phrase boundary here)
contains the separate integers 1 and 0.

A bare numeric CV remains available as a label or code where no clause competes for the reading
(list numbering, IDs, tables). A bare sequence such as `py pi` is correspondingly two code
elements, never an unmarked alias of `num py pi` “100.”

---

## 9. Version History

- **v1** — the original foundational spec, preserved as `archive/doc_v15.md`
  (earlier working drafts remain available in the repository’s Git history).
- **v2 (August 2026)** — first revision, prompted by an external stress test. The word-level
  architecture is unchanged (all 36 roots re-verified against the matrix). Adopted: referential
  **-t** / descriptive **-m**; the pivot-and-role clause rule with fully-role-marked
  (agent-omitting) clauses; three-way spatial constructions; the **G-series** with **ru** as path
  closer; linear operator scope; a clause-final event-modifying **ROOT-l** manner slot; a
  zero-copula simple **ROOT-s** property clause with broad N-series polarity and narrow **na**
  scope; the numeral marker **num** and canonical
  base-100 cardinal runs; root-anchored stress statement.
  Earmarked but *not* adopted sight-unseen from the stress-test proposal: the **B/F/X/Z** form
  tables and its provisional added roots.
- **v2 amendments (2026-08-18)** — five changes adopted through evidence-first stress-test
  cycles (frozen corpora with sealed holdouts; one design decision per cycle), each landed as
  its own commit:
  1. Attributive `ROOT-s` property modifiers in the noun phrase (§7.2).
  2. The **F-series** — coordination & logical linkage — with same-kind infix coordination,
     discourse-initial linkage, and the low-attachment rule (§4.3, §7.6).
  3. The **J-series** remapped person-major (`ji jy je ja jo ju` = I, we, you, you-pl,
     he/she/it, they), plus the §2.4 categorical-series design note.
  4. The symmetric **C-scale** (`ci` “least”), front N-series polarity on comparisons, and
     compositional bounds — `na … cy` “at least”, `na … ca` “at most” (§4.12, §7.5).
  5. The **Q-series** bottom slot: `qi` “few”; empty-set claims are compositional
     (`na qy …`) (§4.8).
  Numeric-particle homophones rose from seventy to seventy-five; word shapes, parsing, and
  the 36 core roots are unchanged throughout.
