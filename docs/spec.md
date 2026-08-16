# Foundational Spec (v2)

> **v2 — August 2026.** First revision, driven by an external stress test of the language.
> Summary of changes: **-t** referential vs **-m** descriptive; a **pivot-and-role** clause rule;
> three distinct spatial constructions with the new **G-series** (path orientation) and **ru** as
> the path-phrase closer; linear **operator scope**; the numeral marker **num**; stress restated
> as root-anchored (equivalent to the old penultimate rule). The prior version is preserved as
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
- Numeric **00–99 → CV** system
- Particle series defined so far: **P, M, T, D, N, Q, S, C, W, J, K, G, R, H**
- First derivational prefix series: **K-series** (configuration / collectivity)
- A core lexicon: **one root per semantic cell (36 roots)**
- The numeral marker **num** (§8.1)
- Clause **pivot rule** and linear **operator scope** (§7.1)
- Free K-series noun-phrase order and scope before Q/D/NUM (§7.2)
- Exact-cardinal noun-phrase slot and scope with K/Q/D (§7.2)

**Still open (deliberately):**

- Additional derivational prefix series (Time, Voice, Valence, etc.)
- More closed-class items (conjunctions, clause-linkers, etc.)
- The earmarked series **B** (mood / clause force), **F** (coordination & logical linkage),
  **X** (subordinate-clause delimiters), **Z** (reflexive / reciprocal / discourse reference):
  functions reserved, forms not yet specified. **V** and **L** remain unallocated.
- Larger lexicon beyond the 36 core roots
- Full syntax for complex clauses, subordination, focus, etc.
- Direct event-level use and ordering of free K-series modifiers relative to the event-operator track
- General clause/phrase distribution of manner (`ROOT-l`) and relational (`ROOT-r`) heads
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
- numeric CV system (I/Y/E/A/O; U unused for 00–99).

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
entity, event, and property constructions; the general placement and attachment rules for
`ROOT-l` manner heads and `ROOT-r` relational heads remain deliberately open.

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

### 3 – F

*(reserved — earmarked for coordination & logical linkage)*

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
| **qi** | empty set                  | “no, none of”                     |
| **qy** | existential, non-partitive | “a / some (there exists)”         |
| **qe** | partitive, not-all         | “some of (them), not all”         |
| **qa** | large subset               | “most (of)”                       |
| **qo** | universal, collective      | “all (of), the whole X”           |
| **qu** | universal, distributive    | “every / each / any (one by one)” |

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

| **Form** | **Comparative role**  | **Gloss**          |
| -------- | --------------------- | ------------------ |
| **ci**   | minimal bound         | “at least”         |
| **cy**   | less-than             | “less, not as ~”   |
| **ce**   | equal                 | “as ~ as, equally” |
| **ca**   | more-than             | “more, -er”        |
| **co**   | maximal / superlative | “most, at most”    |
| **cu**   | extremal limit        | “as ~ as possible” |

Pattern with property `PROP-s`:

```text
A cy/ce/ca PROP-s B re
= “A is less/as/more PROP than B”
```

`re` (R-series) marks **standard-of-comparison** (“than B”).

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
| **jy** | 2sg             | you (sg)      |
| **je** | 3sg             | he / she / it |
| **ja** | 1pl             | we            |
| **jo** | 2pl             | you (pl)      |
| **ju** | 3pl             | they          |

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
[K] [Q] [D] [NUM] [ROOT-{m|t}]
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
[W (+R)?] [T] [P] [H] [M] [N] [PIVOT] [other NPs + R/S] VERB
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
* **VERB** – root + `-n`

The smallest pivoted event clause is **PIVOT + VERB**. The pivot may be absent in a fully
role-marked clause. Static-location and property-predicate clauses use their own patterns below
and do not require an event word.

The track covers the fixed event operators. A free K-particle that introduces an NP belongs to
that NP and precedes its Q, D, and NUM slots (§§4.16, 7.2). Direct event-level K scope and order
relative to this track remain open.

Example:

* `ji zife-n.` – “I speak.”
* `te py ji zife-n.` – “Now I am speaking.”

**Pivot and roles (v2).** An event clause has at most one *unmarked* noun phrase: the **pivot**, in
the pivot slot, read as the most agent-like argument of the verb. Every other argument carries an
R-series role particle (§7.3), including a questioned argument (§7.4). A clause may also be
*fully role-marked*, with no pivot at all — which is how the agent is omitted, with no passive
morphology:

* `ji kory-t re toki-m ra gose-n.` – “I build the house with a tool.”
* `ji jy ry qy rufi-m re zife-n.` – “I tell you an idea.”
* `ty di kory-t re gose-n.` – “This house was built recently.” (patient marked, agent omitted)

**Operator scope (v2).** The front operators ([T] [P] [H] [M] [N]) take scope over everything to
their right, in linear order. Polarity **na** may also stand immediately before the verb for
narrow scope:

* `na qo piri-m pase-n.` – “Not all people go.” (¬∀)
* `qo piri-m na pase-n.` – “All the people don’t go — none of them go.” (∀¬)

---

### 7.2 Noun Phrase Template

```text
[K] [Q] [D] [NUM] [ROOT-{m|t}]
```

* **K** – configuration of the selected participants (ki/ky/ke/ka/ko/ku)
* **Q** – quantifier (qi/qy/qe/qa/qo/qu)
* **D** – demonstrative (di/de/do/dy/da/du)
* **NUM** – optional exact cardinal from 0 to 99, with the fixed form `num CV`
* **ROOT-m / ROOT-t** – descriptive or referential entity head

Examples:

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

The current NUM constituent is indivisible and contains exactly the marker plus one numeric CV:

```text
NUM = num CV
```

NUM gives the exact cardinality of the entity head inside any restriction supplied by D. An overt
Q scopes over the following D/NUM/head cardinal frame, so `qe da num bi feni-t` selects some but
not all of an identified five-animal set. All K/Q/D particles precede NUM; none can occur between
`num` and the entity head. This preserves the particle/numeral boundary even when the same CV has
both uses:

* `num pa piri-m` – three people
* `qe num qe piri-t` – some but not all of an identifiable forty-two-person set
* `da num da piri-t` – thirty-three of those people (first `da` = demonstrative; second = 33)
* `ka num ka piri-m` – eighty-three people, configured together (first `ka` = K; second = 83)

The rule adds no special agreement morphology: combinations whose existing D, Q, and numeral
meanings contradict one another remain semantically anomalous. Values above 99 remain open (§8).

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
* `ja ge su bely-m ru pase-n.` – “We travel through the forest.” (route + among)
* `je gu si di kory-t ru pase-n.` – “She returns into this house.”

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
* `wy je guse-n?` – “Why does he/she think?”
* `we ro je nife-n?` – “Where does he/she eat?” (event setting)
* `wu je zife-n?` – “How does he/she speak?”

This rule does not extract a W-word from inside a static S construction or an oriented G…`ru`
path frame; those question constructions remain open (§0).

**Yes/no questions**: same clause + question intonation / `?`.

* `je zife-n?` – “Does he/she speak?”

Answers with N-series:

* `ni.` – yes
* `na.` – no
* `no.` – on the contrary
* `nu.` – absolutely not / never

---

### 7.5 Comparatives

Property from root + `-s`:

* `gusa` – know / be knowledgeable → `gusa-s` – knowledgeable

Comparative pattern (C-series + `re`):

* `ji ca gusa-s de piri-t re.`
  → “I am more knowledgeable than that person.”

* `ji ce gusa-s de piri-t re.`
  → “I am as knowledgeable as that person.”

* `ji cy gusa-s de piri-t re.`
  → “I am less knowledgeable than that person.”

Superlative:

* `ji co gusa-s.`
  → “I am the most knowledgeable.”

---

## 8. Numeric CV System (00–99)

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

For integer **d** with 0 ≤ d ≤ 99:

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

### 8.1 The numeral marker `num` (v2)

Seventy of the hundred numeric CVs are homophonous with defined particles (`te` is both “now”
and 27). The remaining thirty use the six reserved or unallocated series consonants and currently
have only a numeric reading. Because collisions are nevertheless systematic and common, ordinary
numeric expressions are announced uniformly by **num** — the language’s first fixed atomic form
longer than CV, a clipped entity form of **nunu** “number”:

* `num pi` – “zero”
* `num te` – “twenty-seven”
* `num pa piri-m pase-n.` – “Three people go.”
* `pi ji zife-n.` – “I begin to speak.” (bare `pi` is still the phase particle)

Inside an entity NP, `num CV` occupies the NUM slot after any K, Q, and D particles and directly
before the entity head (§7.2). The marker governs exactly one numeric CV in the current 0–99
system. For example, `da num da piri-t` keeps the first `da` demonstrative and reads the second as
33. This order reserves a clear phrase boundary without defining any multi-CV value above 99.

A bare numeric CV remains available as a label or code where no clause competes for the reading
(list numbering, IDs, tables).

---

## 9. Version History

- **v1** — the original foundational spec, preserved as `archive/doc_v15.md`
  (earlier working drafts remain available in the repository’s Git history).
- **v2 (August 2026)** — first revision, prompted by an external stress test. The word-level
  architecture is unchanged (all 36 roots re-verified against the matrix). Adopted: referential
  **-t** / descriptive **-m**; the pivot-and-role clause rule with fully-role-marked
  (agent-omitting) clauses; three-way spatial constructions; the **G-series** with **ru** as path
  closer; linear operator scope; the numeral marker **num**; root-anchored stress statement.
  Earmarked but *not* adopted sight-unseen from the stress-test proposal: the **B/F/X/Z** form
  tables and its provisional added roots.
