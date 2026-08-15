# Foundational Spec (Updated)

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
- Particle series defined so far: **P, M, T, D, N, Q, S, C, W, J, K, R, H**
- First derivational prefix series: **K-series** (configuration / collectivity)
- A core lexicon: **one root per semantic cell (36 roots)**

**Still open (deliberately):**

- Additional derivational prefix series (Time, Voice, Valence, etc.)
- More closed-class items (conjunctions, clause-linkers, etc.)
- Larger lexicon beyond the 36 core roots
- Full syntax for complex clauses, subordination, focus, etc.

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
- Stress: always on the **penultimate syllable**

Example: `ka.piri.m` → stress on **pi**.

---

## 2. Word Structure

### 2.1 Two Word Types

1. **Atomic words (particles)**  
   - Shape: typically **CV**; a few longer fixed forms allowed.
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
| **-m** | Entity head      | generic noun: “an X-thing / X-entity”                |
| **-t** | Specific head    | specific entity: “that/the X”                        |
| **-n** | Event head       | verb: “to X / X happens”                             |
| **-s** | Property head    | adjective: “X-like, having X-property”               |
| **-l** | Manner head      | adverb: “in an X way, X-ly”                          |
| **-r** | Relational head  | relational NP: “of X, X’s, from X, related-by-X”     |

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

*(unused / reserved)*

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

*(unused / reserved)*

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
Dynamic: with motion verbs (`pase-n` “go/move”) → path relative to ground.

---

### 10 – Z

*(unused / reserved)*

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

*(unused / reserved)*

---

### 15 – J (Personal Pronouns)

| Form   | Person / number | Gloss         |
| ------ | --------------- | ------------- |
| **ji** | 1st singular    | I             |
| **jy** | 2nd singular    | you (sg)      |
| **je** | 3rd singular    | he / she / it |
| **ja** | 1st plural      | we            |
| **jo** | 2nd plural      | you (pl)      |
| **ju** | 3rd plural      | they          |

---

### 16 – K (Configuration / Collectivity: Particle + Prefix)

**K-series** expresses how many units and how they are **grouped**.
Each form functions as:

* a **particle** (phrasal modifier), and
* a **prefix** `kV-` on roots, deriving “group-of-X” nouns (and optionally other heads).

| **Form** | **Config type**         | **Particle gloss**                 | **Prefix gloss (kV-ROOT-m)**                  |
| -------- | ----------------------- | ---------------------------------- | --------------------------------------------- |
| **ki**   | singled, atomic         | “as a single unit, alone, singly”  | “one specific X, singled-out unit”            |
| **ky**   | pair / dual             | “in pairs, as a pair”              | “a pair of X”                                 |
| **ke**   | small group             | “in a small group, a few together” | “a small group of X (a few Xs)”               |
| **ka**   | generic group / crowd   | “as a group, together, in a crowd” | “a group / crowd / community of X”            |
| **ko**   | large collective / mass | “en masse, as a large crowd/mass”  | “a large collective / mass / population of X” |
| **ku**   | scattered / distributed | “scattered, spread out, all over”  | “X scattered / distributed (many Xs)”         |

Examples of **prefix** use:

* `piri-m` = a person → `kapiri-m` = a group/crowd/community of people
* `feni-m` = an animal → `kefeni-m` = a small group of animals (if you choose that reading)
* `kory-m` = a house → `kakory-m` = a group of houses (neighborhood/block)

As a **particle**:

* `ka piri-m pase-n sa sary-m.` – “People go as a group around the region.”

---

### 17 – G

*(unused / reserved)*

---

### 18 – R (Roles / Case-like Particles)

| **Form** | **Role**                   | **Gloss**                                  |
| -------- | -------------------------- | ------------------------------------------ |
| **ri**   | agent / controller         | “by (agent), as doer”                      |
| **ry**   | experiencer / beneficiary  | “to / for (person)”                        |
| **re**   | patient / theme / standard | “object of, about; ‘than’ in comparatives” |
| **ra**   | instrument / means         | “with, using, by means of”                 |
| **ro**   | location / setting         | “at, in, on (place/time)”                  |
| **ru**   | source/goal / path edge    | “from, to, into/out of (generic DIR)”      |

`NP + R` pattern: R acts like a postposition.

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

Other series (M, T, etc.) may later get parallel **prefix roles** (e.g. degree prefixes on adjectives, tense-aspect prefixes on verbs).

---

## 6. Core Roots (Matrix-Aligned Lexicon)

Each root is **CVCV**. Actual words add a suffix:

* `ROOT-m` – entity
* `ROOT-t` – specific entity
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

### 7.1 Default Clause Template

A useful canonical word order:

```text
[W?] [T] [P] [H] [M] [N] SUBJECT [other NPs + R/S] VERB
```

Where:

* **W** – wh-word (wi/wy/we/wa/wo/wu)
* **T** – time (ti/ty/te/ta/to/tu)
* **P** – phase/aspect (pi/py/pe/pa/po/pu)
* **H** – frequency (hi/hy/he/ha/ho/hu)
* **M** – degree (mi/my/me/ma/mo/mu)
* **N** – polarity (ni/ny/ne/na/no/nu)
* **SUBJECT** – pronoun (J) or NP
* **other NPs + R/S** – arguments and spatial phrases
* **VERB** – root + `-n`

Many slots are optional; the minimal clause is **SUBJECT + VERB**.

Example:

* `ji zife-n.` – “I speak.”
* `te py ji zife-n.` – “Now I am speaking.”

---

### 7.2 Noun Phrase Template

```text
[Q] [D] [ROOT-m]
```

* **Q** – quantifier (qi/qy/qe/qa/q o/qu)
* **D** – demonstrative (di/de/do/dy/da/du)

Examples:

* `qy piri-m` – a person / some person
* `qa piri-m` – most people
* `qe da feni-m` – some of those animals (here)
* `qo du kory-m` – all those houses (over there)

Pronouns (`ji, jy, je, ja, jo, ju`) behave as NPs.

---

### 7.3 Roles & Space

Role particles (R-series):

* `NP ri` – agent/doer
* `NP re` – patient/theme; also “than NP” in comparatives
* `NP ry` – experiencer/beneficiary (“to/for NP”)
* `NP ra` – instrument/means (“with, using NP”)
* `NP ro` – location/setting (“at/in/on NP”)
* `NP ru` – path edge (“from/to/into/out-of NP”)

Spatial S-series:

* Static: `FIGURE S GROUND`
* Dynamic with motion: `FIGURE VERB S GROUND`

Examples:

* `di piri-t si di kory-m.` – “This person is inside this house.”
* `ji pase-n sa sary-m.` – “I go around the region.”

Combine with `ru` for directional:

* `ji ru si di kory-m pase-n.` – “I go into this house.”

---

### 7.4 Questions

**Wh-questions**: use W-series.

* `wo zife-n?` – “Who speaks?”
* `wa ji nife-n?` – “What do I eat?”
* `wi ju pase-n?` – “When do they go?”
* `wy je guse-n?` – “Why does he/she think?”
* `we je nife-n?` – “Where does he/she eat?”
* `wu je zife-n?` – “How does he/she speak?”

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

* `ji ca gusa-s de piri-m re.`
  → “I am more knowledgeable than that person.”

* `ji ce gusa-s de piri-m re.`
  → “I am as knowledgeable as that person.”

* `ji cy gusa-s de piri-m re.`
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

Numeric CVs can function as:

* atomic numerals,
* labels/codes,
* and, where sensible, also as particles (disambiguated by context).