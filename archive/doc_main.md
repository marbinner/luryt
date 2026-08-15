
# Foundational Spec

## 0. Scope

**Fixed now:**

- Consonant inventory **and canonical order**
- Vowel inventory **and canonical order**
- Syllable structure & stress
- Two word types: **atomic CV** vs **content words**
- Content-word template: **(CV prefixes) + CVCV root + final suffix**
- Final suffix system: **M T N S L R** and what each means
- Principle that **CV series use one consonant + vowels in I Y E A O U order**
- Root semantics: **6 Domains × 6 Aspects** (semantic matrix below)
- Numeric **00–99 → CV** system
- Particle series defined so far: **P, M, T, D, N, Q, S, C, W, J, R, H**
- A first **core lexicon**: one root per semantic cell

**Still open (deliberately):**

- Which consonants are used as **productive prefix series** (Time, Scale, Logic, Voice, derivation, etc.)
- Additional closed-class items (conjunctions, clause-linkers, etc.)
- Larger lexicon beyond the 36 core roots
- Detailed syntax (subordination, relative clauses, focus constructions, etc.)

---

## 1. Phonology

### 1.1 Consonants

**Canonical consonant order** (for indexing, numeric codes, series labels):

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

Only these six may appear as the final consonant of a content word.

---

### 1.2 Vowels

**Canonical vowel order:**

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

- semantic series (particles, future prefixes),
- root matrix coordinates (V₁, V₂),
- numeric CV system (I/Y/E/A/O; U unused for 00–99).

---

### 1.3 Syllable Structure & Stress

- Allowed syllables: **CV** or **CVC**
- No onsetless syllables; no consonant clusters
- Stress: **penultimate syllable** in every word

---

## 2. Word Structure

### 2.1 Two Word Types

1. **Atomic words (particles)**  
   - Shape: typically **CV** (some longer fixed forms allowed)  
   - Used for: pronouns, TAM particles, quantifiers, roles, wh-words, etc.  
   - No productive morphology (no regular prefixes/suffixes).

2. **Content words**  
   - Exactly one **CVCV root**  
   - Optional prefix block of one or more **CV** prefixes  
   - Exactly one final consonant suffix from {**M, T, N, S, L, R**}  
   - Template:

     ```text
     (CV prefix)* + CVCV(root) + final suffix
     ```

---

### 2.2 Final Suffix System (Head Kinds)

Final suffix set:

> **-M  -T  -N  -S  -L  -R**

| Suffix | Head kind      | Typical use                                         |
|--------|----------------|-----------------------------------------------------|
| **-M** | Entity head    | generic noun: “an X-thing / X-entity”              |
| **-T** | Specific head  | specific entity: “that/the X”                      |
| **-N** | Event head     | verb: “to X / X happens”                           |
| **-S** | Property head  | adjective: “X-like, having X-property”             |
| **-L** | Manner head    | adverb: “in an X way, X-ly”                        |
| **-R** | Relational head| relational NP: “of X, X’s, from X, related-by-X”   |

No further head classes will be added; derivation is handled by prefixes + these six.

---

### 2.3 Parsing Content Words

Given a token:

1. If length = 2 and shape is CV → **atomic** word (particle/numeral).
2. Else:
   - If final char ∉ `{m,t,n,s,l,r}` → not a well-formed content word.
   - Else:
     - final char = suffix
     - preceding 4 characters must be **CVCV** = root
     - any remaining left characters must form a sequence of **CV** prefixes.

If this holds, segmentation is unique:

```text
(CV prefix)* + CVCV(root) + suffix
```

---

### 2.4 Series Principle (for Particles & Future Prefixes)

Any productive CV series uses:

* a single **consonant**, and
* all six **vowels** in order **I Y E A O U**,
* with a semantic progression across the six members.

Example:

* **T-series**: ti/ty/te/ta/to/tu for remote past → recent past → present → near future → far future → timeless.

---

## 3. Semantic Matrix (Domains × Aspects)

### 3.1 Domains (V₁)

V₁ = first vowel of the root (C₁ V₁ C₂ V₂):

* **I = PERSON** – individual humans: body, mind, experience
* **Y = SOCIETY** – families, groups, institutions, culture
* **E = LIFE** – non-human life: animals, plants, ecosystems
* **A = PHYSICAL** – non-living world: matter, space, energy, weather
* **O = ARTEFACT** – tools, objects, machines, infrastructure
* **U = ABSTRACT** – ideas, language, math, logic, information

### 3.2 Aspects (V₂)

V₂ = second vowel of the root:

* **I = INDIVIDUAL** – basic “things/actors” in that domain
* **Y = CONFIG** – parts, wholes, groups, layouts, structures, systems
* **E = PROCESS** – activities, processes, changes, doing
* **A = STATE** – relatively stable conditions/qualities
* **O = RELATION** – links/roles between things
* **U = QUANTITY** – measures, magnitudes, degrees

### 3.3 Cells (V₁ × V₂)

#### I PERSON (V₁ = I)

* **II – INDIVIDUAL**: person, self, individual human
* **IY – CONFIG**: body, hand, heart, family (parts/wholes of a person)
* **IE – PROCESS**: act, speak, eat, see, move (personal actions)
* **IA – STATE**: hungry, tired, sad, happy, healthy (personal states)
* **IO – RELATION**: friend-of, parent-of, sibling-of, lover-of
* **IU – QUANTITY**: age, strength, personal habit frequency

#### Y SOCIETY (V₁ = Y)

* **YI – INDIVIDUAL**: group, tribe, clan, city (as a single social unit)
* **YY – CONFIG**: institution, hierarchy, government, organization
* **YE – PROCESS**: trade, talk, fight, negotiate, vote, cooperate
* **YA – STATE**: peace, war, crisis, stability, trust
* **YO – RELATION**: citizen-of, member-of, boss-of, rule-over
* **YU – QUANTITY**: money, price, wealth, budget, GDP

#### E LIFE (V₁ = E)

* **EI – INDIVIDUAL**: animal, plant, fungus, organism
* **EY – CONFIG**: forest, herd, swarm, ecosystem
* **EE – PROCESS**: grow, hunt, migrate, bloom, reproduce
* **EA – STATE**: alive, dead, sick, healthy, poisonous
* **EO – RELATION**: predator-of, prey-of, host-of, symbiont-of
* **EU – QUANTITY**: population size, biomass, crop yield

#### A PHYSICAL (V₁ = A)

* **AI – INDIVIDUAL**: rock, river, mountain, planet, object of matter
* **AY – CONFIG**: landscape, region, terrain, field, cluster
* **AE – PROCESS**: flow, fall, rain, blow, melt, freeze
* **AA – STATE**: hot, cold, solid, liquid, gas, wet, dry
* **AO – RELATION**: in, on, under, near, around, between (spatial relations)
* **AU – QUANTITY**: length, mass, time, energy, temperature

#### O ARTEFACT (V₁ = O)

* **OI – INDIVIDUAL**: tool, knife, cup, phone, vehicle, device
* **OY – CONFIG**: house, road, bridge, network, city plan
* **OE – PROCESS**: cut, build, drive, send, print, compute
* **OA – STATE**: broken, fixed, open, closed, on, off
* **OO – RELATION**: key-of, lock-for, plug-into, port-of, interface-with
* **OU – QUANTITY**: size, capacity, speed, power, storage, bandwidth

#### U ABSTRACT (V₁ = U)

* **UI – INDIVIDUAL**: idea, concept, proposition, word, symbol
* **UY – CONFIG**: theory, language, model, formal system, taxonomy
* **UE – PROCESS**: think, learn, compute, imagine, infer
* **UA – STATE**: know, believe, remember, doubt, forget
* **UO – RELATION**: cause-of, equal-to, implies, means-of, part-of (abstract)
* **UU – QUANTITY**: number, amount, probability, measure, degree

---

## 4. Particle Mappings (Atomic CV Series)

**Consonant order:**

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

**Vowel order:**

> **I  Y  E  A  O  U**


### 0 – P (Aspect / Event Phase)

| **Form** | **Phase value**                       | **Gloss**                        |
| -------- | ------------------------------------- | -------------------------------- |
| **pi**   | inceptive / just starting             | “just, just now start to”        |
| **py**   | progressive / in progress             | “currently, be -ing”             |
| **pe**   | resumptive / back again               | “again, back (to doing it)”      |
| **pa**   | continuative / still ongoing          | “still, keep (on)”               |
| **po**   | completive / through to the end       | “completely, all the way”        |
| **pu**   | perfect / already done / result state | “already, (has) done / finished” |

Used as clause particles, usually before the verb.

---

### 1 – B

*(currently unused / reserved)*

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

*(currently unused / reserved)*

---

### 4 – V

*(currently unused / reserved)*

---

### 5 – T (Time / Tense)

| **Form** | **Time value**    | **Gloss**              |
| -------- | ----------------- | ---------------------- |
| **ti**   | remote past       | “long ago”             |
| **ty**   | recent past       | “recently / just now”  |
| **te**   | present           | “now / currently”      |
| **ta**   | near future       | “soon / about to”      |
| **to**   | far future        | “later / someday”      |
| **tu**   | gnomic / timeless | “generally / whenever” |

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

| **Form** | **Polarity type**               | **Gloss / core force**              |
| -------- | ------------------------------- | ----------------------------------- |
| **ni**   | explicit affirmation            | “yes, indeed, it *is* so”           |
| **ny**   | partial / mixed presence        | “sort of, partly, more or less”     |
| **ne**   | neutral / polarity-unmarked     | “(no polarity focus / ‘meh’)”       |
| **na**   | simple negation                 | “not, no, it isn’t so”              |
| **no**   | contrary / opposite / anti-     | “on the contrary, anti-R, opposite” |
| **nu**   | strong negation / impossibility | “never, absolutely not, cannot”     |

---

### 8 – Q (Quantifier Type)

| Form   | Type                       | Short gloss                       |
| ------ | -------------------------- | --------------------------------- |
| **qi** | empty set                  | “no, none of”                     |
| **qy** | existential, non-partitive | “a / some (there exists)”         |
| **qe** | partitive, not-all         | “some of (them), not all”         |
| **qa** | large subset               | “most (of)”                       |
| **qo** | universal, collective      | “all (of), the whole X”           |
| **qu** | universal, distributive    | “every / each / any (one by one)” |

---

### 9 – S (Spatial Topology)

| **Form** | **Topological relation (static)** | **Static gloss**              |
| -------- | --------------------------------- | ----------------------------- |
| **si**   | interior / within boundary        | “in, inside (within X)”       |
| **sy**   | surface / contact                 | “on, on top of, touching X”   |
| **se**   | adjacency / side-by-side          | “next to, beside X”           |
| **sa**   | surrounding area / vicinity       | “around X, in X’s area”       |
| **so**   | exterior / beyond boundary        | “outside X, beyond X”         |
| **su**   | among multiple / spread through   | “among X, amidst, throughout” |

Static: `FIGURE S GROUND` (“X is in/on/next-to Y”).
Dynamic: with motion verbs (e.g. `pase-n` “go/move”) → path type relative to ground.

---

### 10 – Z

*(currently unused / reserved)*

---

### 11 – L

*(currently unused / reserved)*

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

**Comparative pattern:**
For property `PROP-s`:

```text
A cy/ce/ca PROP-s B re
= “A is less/as/more PROP than B”
```

`re` (R-series) in this context marks the **standard-of-comparison** (“than NP”).

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

“Which” is expressed compositionally via **wa/wo + NP (+ Q/D)**.

---

### 14 – X

*(currently unused / reserved)*

---

### 15 – J (Personal Pronouns)

| Form   | Person / number | Gloss              |
| ------ | --------------- | ------------------ |
| **ji** | 1st singular    | I                  |
| **jy** | 2nd singular    | you (sg)           |
| **je** | 3rd singular    | he / she / it (sg) |
| **ja** | 1st plural      | we                 |
| **jo** | 2nd plural      | you (pl)           |
| **ju** | 3rd plural      | they               |

---

### 16 – K

| Form   | log-odds | Approx p | Intuitive gloss                                             |
| ------ | -------- | -------- | ----------------------------------------------------------- |
| **ki** | -3       | ≈ 0.05   | very strong belief *against* (“I’d almost never bet on it”) |
| **ky** | -1       | ≈ 0.27   | moderate belief against (“I think it’s unlikely”)           |
| **ke** | -0.3     | ≈ 0.43   | slight lean against (“weak tilt to no”)                     |
| **ka** | +0.3     | ≈ 0.57   | slight lean for (“weak tilt to yes”)                        |
| **ko** | +1       | ≈ 0.73   | moderate belief for (“I think it’s likely”)                 |
| **ku** | +3       | ≈ 0.95   | very strong belief for (“I’d confidently bet on it”)        |

---

### 17 – G

*(currently unused / reserved)*

---

### 18 – R (Roles / Case-like Particles)

| **Form** | **Role**                   | **Gloss**                              |
| -------- | -------------------------- | -------------------------------------- |
| **ri**   | agent / controller         | “by (agent), as doer”                  |
| **ry**   | experiencer / beneficiary  | “to / for (person)”                    |
| **re**   | patient / theme / standard | “object of, about, concerning; ‘than’” |
| **ra**   | instrument / means         | “with, using, by means of”             |
| **ro**   | location / setting         | “at, in, on (place/time)”              |
| **ru**   | source/goal / path edge    | “from, to, into/out of (generic DIR)”  |

`NP + R` is the usual pattern (postposition-like).
`re` has the special extra role “than NP” with C-series comparatives.
`ru` plus S can express more articulated paths (into/out of/through/etc.).

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

## 5. Core Roots (Matrix-aligned Lexicon)

Each root is **CVCV**; actual words add suffixes:

* `ROOT-m` – entity
* `ROOT-t` – specific entity
* `ROOT-n` – event/verb
* `ROOT-s` – property
* `ROOT-l` – manner
* `ROOT-r` – relational

### I I

piri – person, human individual

### I Y

mily – body, physical self

### I E

zife – to speak, talk

### I A

hisa – to be well, healthy

### I O

siro – friend relation, friend-of

### I U

tinu – age of a person (years lived)

---

### Y I

rydi – group, crowd, people-as-unit

### Y Y

syry – institution, organized structure

### Y E

gyfe – to interact socially, mingle

### Y A

vyra – social peace, order, stability

### Y O

tyro – rule/authority relation, boss-of

### Y U

byru – wealth, money amount

---

### E I

feni – animal (non-human)

### E Y

bely – forest / herd / ecosystem cluster

### E E

kefe – to grow, develop (biological)

### E A

mela – to be alive, living

keka - neutral (my first word!)


### E O

sevo – ecological relation (predator-of, symbiont-of, etc.)

### E U

benu – population, biomass, ecological quantity

---

### A I

kati – rock, stone, lump of matter

### A Y

sary – region, landscape, area

### A E

pase – to move, go, travel, flow

### A A

hata – hot/warm (physical temperature)

### A O

sako – physical relation (contact/inclusion/proximity)

### A U

daru – distance, spatial extent, length

---

### O I

toki – tool, implement, usable object

### O Y

kory – house, building, constructed structure

### O E

gose – to build, construct, make artefact

### O A

vosa – broken, out of order

### O O

zoro – functional relation (fit, plug, compatibility)

### O U

komu – capacity, size, volume (of artefacts)

---

### U I

rufi – idea, concept

### U Y

lury – language, system, theory

### U E

guse – to think, compute, reason

### U A

gusa – to know, be knowledgeable

### U O

kuro – cause-of, reason relation

### U U

nunu – number, amount, abstract quantity

---

## 6. Basic Syntax (Provisional)

### 6.1 Default clause template

A useful “vanilla” word order:

```text
[W?] [T] [P] [H] [M] [N]  SUBJECT  [other NPs + R/S]  VERB
```

Where:

* **W** = wh-word (wi/wy/we/wa/wo/wu) – only if needed
* **T** = tense/time (ti/ty/te/ta/to/tu)
* **P** = aspect/phase (pi/py/pe/pa/po/pu)
* **H** = frequency (hi/hy/he/ha/ho/hu)
* **M** = degree (mi/my/me/ma/mo/mu)
* **N** = polarity (ni/na/no/nu/etc.)
* **SUBJECT** = J pronoun or NP
* **other NPs + R/S** = arguments and spatial phrases
* **VERB** = root + `-n`

Many slots are optional; only **SUBJECT + VERB** are strictly necessary for a minimal clause.

---

### 6.2 NP template

```text
[Q] [D] [ROOT-m]
```

Examples:

* `qy piri-m` – a person / some person
* `qa piri-m` – most people
* `qo piri-m` – all the people (as a group)
* `qe da feni-m` – some of those animals (here)
* `qo du kory-m` – all those houses (elsewhere)

Pronouns:

* `ji, jy, je, ja, jo, ju` function as bare NPs.

---

### 6.3 Roles & Space

* `NP ri` – agent (“by X”)
* `NP re` – patient/theme (“X as object/about”), and **“than X”** with C-series
* `NP ry` – experiencer/beneficiary (“to/for X”)
* `NP ra` – instrument/means (“with, using X”)
* `NP ro` – location/setting (“at/in/on X”)
* `ru` – generic “along path linked to X”; often combined with S:

  * `ru si NP` – into NP
  * `ru so NP` – out of / past NP
  * `ru su NP` – through / along NP

Spatial S is normally `FIGURE S GROUND` (static) or `FIGURE VERB S GROUND` (dynamic).

---

### 6.4 Questions

**Wh-questions:** insert the appropriate W-word:

* `wo nife-n?` – “Who eats?”
* `wa ji nife-n?` – “What do I eat?”
* `we je nife-n?` – “Where does he/she eat?”
* `wi ju pase-n?` – “When do they go?”
* `wy je nife-n?` – “Why does he/she eat?”
* `wu je nife-n?` – “How does he/she eat?”

**Yes/no questions:** same clause + `?`; answers with N-series:

* `je nife-n?` – “Does he/she eat?”
* `ni.` – yes / indeed
* `na.` – no / not
* `no.` – on the contrary
* `nu.` – absolutely not / never

---

## 7. Numeric CV System (00–99)

Consonants indexed by canonical order:

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

Vowels for numerals: first five in order:

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

Numeric CVs can be used as:

* atomic numerals,
* labels/codes,
* and, where sensible, particles (disambiguated by context).
