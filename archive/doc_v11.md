Here’s a cleaned-up, fully-integrated spec with all your current decisions folded in and lightly stitched together. I’ll keep your content but organize and clarify a bit, especially around **how the particles are used**.

---

# 0. Scope

**Fixed now:**

* Phonology (consonants, vowels, canonical order)
* Syllable structure & stress
* Two word types: **atomic CV** vs **content words**
* Content-word template: **(CV prefixes) + CVCV root + final suffix**
* Final suffix system: **M T N S L R** and their functions
* Principle that **CV series use one consonant + vowels in I Y E A O U order**
* Root semantics: **6 Domains × 6 Aspects** (matrix)
* Numeric **00–99 → CV** system
* **Particle series** defined so far:
  **P, M, T, D, N, Q, S, C, W, J, R, H** (with semantics & tables below)

**Still open:**

* Which consonants will be used as **prefix series** (Time, Scale, Logic, Voice, derivation, etc.)
* Exact closed-class inventory beyond these series (e.g. conjunctions, clause-linkers)
* Concrete lexical roots (CVCV) beyond illustrative examples
* Precise syntax / word order beyond current recommendations

---

# 1. Phonology

## 1.1 Consonants

Canonical consonant order (for indexing, numeric codes, series labels):

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

**Final-consonant (suffix) pool** (only for content words):

> **M  T  N  S  L  R**

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

Used for:

* semantic series (particles & prefixes),
* root matrix indices (V₁, V₂),
* numeric CV system (I Y E A O; U unused for 00–99).

---

## 1.3 Syllable Structure & Stress

* Allowed syllables: **CV** or **CVC**
* No onsetless syllables; no consonant clusters
* Stress: **penultimate syllable** of the word

---

# 2. Word Structure

## 2.1 Two Word Types

1. **Atomic words (particles)**

   * Shape: typically **CV** (sometimes longer fixed forms if needed)
   * Used for: pronouns, demonstratives, quantifiers, prepositions/roles, TAM particles, wh-words, etc.
   * **No productive morphology** in the core system.

2. **Content words**

   * Exactly one **CVCV root**

   * Optional **prefix block**: one or more **CV** prefixes

   * Exactly one **final suffix** from {M, T, N, S, L, R}

   * Template:

     ```text
     (CV prefix)* + CVCV (root) + final suffix (M/T/N/S/L/R)
     ```

   * All open-class lexemes (entities, events, properties, relations, quantities).

In running text:

* bare **CV** → atomic word (particle or numeral)
* **CVCV + suffix** → content word

---

## 2.2 Final Suffixes (Head Kinds)

> **-M -T -N -S -L -R**

| Suffix | Head kind       | Function / typical use                                 |
| ------ | --------------- | ------------------------------------------------------ |
| **-M** | Entity head     | generic noun: “an X-thing / X-entity”                  |
| **-T** | Specific head   | specific entity: “that/the X”                          |
| **-N** | Event head      | verb: “to X / X happens”                               |
| **-S** | Property head   | adjective: “X-like, having X-property”                 |
| **-L** | Manner head     | adverb: “X-ly, in an X way”                            |
| **-R** | Relational head | relational NP: “of X, X’s, from X, related-by-X, etc.” |

No additional suffix classes will be added; derivational distinctions are handled by prefixes and particles plus these six head-kinds.

---

## 2.3 Parsing Content Words

Given a token:

1. If `len = 2` and shape = CV → **atomic** (particle/number).
2. Else:

   * If final char ∉ `{m,t,n,s,l,r}` → not a valid content word.
   * Else:

     * final char = suffix ∈ {M,T,N,S,L,R}
     * preceding four characters must be **CVCV** = root
     * anything to the left must decompose into a sequence of **CV** prefixes.

If that holds, segmentation is unique:

```text
(CV prefix)* + CVCV(root) + suffix
```

---

## 2.4 Series Principle

Any productive CV series (particles or prefixes):

* uses **one consonant**,
* all six vowels in order **I Y E A O U**,
* encodes some semantic gradient or structured set.

Example: T-series for time, D-series for demonstratives, W-series for wh-words, etc.

---

# 3. Root Semantics: 6×6 Matrix

Every root = **C₁ V₁ C₂ V₂**.

* **V₁** (row) = **Domain**
* **V₂** (column) = **Aspect**

Both use vowel order: **I Y E A O U**

So: 6 Domains × 6 Aspects = **36 semantic buckets**.

## 3.1 Domains (V₁)

| V₁ | Domain   | World layer                                 |
| -- | -------- | ------------------------------------------- |
| I  | PERSON   | human individual: body, mind, experience    |
| Y  | SOCIETY  | families, groups, institutions, culture     |
| E  | LIFE     | non-human life: animals, plants, ecosystems |
| A  | PHYSICAL | non-living: matter, space, energy, weather  |
| O  | ARTEFACT | tools, objects, machines, infrastructure    |
| U  | ABSTRACT | ideas, language, math, logic, information   |

## 3.2 Aspects (V₂)

| V₂ | Aspect     | Intuition                                    |
| -- | ---------- | -------------------------------------------- |
| I  | INDIVIDUAL | basic “thing/actor” in that domain           |
| Y  | CONFIG     | wholes, structures, groups, systems          |
| E  | PROCESS    | activities, processes, changes               |
| A  | STATE      | relatively stable states/qualities           |
| O  | RELATION   | relational links (X-of, in, above, equal-to) |
| U  | QUANTITY   | amounts, magnitudes, measures, degrees       |

(Content of the full matrix is unchanged from your draft; not repeating all examples here.)

---

## 3.3 Head-Kind Interaction

For a root **R = C₁ V₁ C₂ V₂** in some Domain×Aspect cell:

* **R-m**: “an R-entity”
* **R-t**: “that/the R-entity”
* **R-n**: “to R / R-happens”
* **R-s**: “R-like, having R-property”
* **R-l**: “in an R way”
* **R-r**: “of R, R’s, related-by-R”

(Your **syro-** friend example still applies.)

---

# 4. Particle System (CV Series)

This section collects all current **atomic CV series**, their semantics, and basic usage.

Consonant order reminder:

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

Series defined so far:

* **0 – P**: Aspect / Event Phase
* **2 – M**: Degree / Intensity
* **5 – T**: Time / Tense
* **6 – D**: Demonstratives
* **7 – N**: Polarity
* **8 – Q**: Quantifier type
* **9 – S**: Spatial topology
* **12 – C**: Comparatives
* **13 – W**: Wh-/interrogatives
* **15 – J**: Personal pronouns
* **18 – R**: Semantic roles / case
* **19 – H**: Frequency / habituality

Slots **1 (B), 3 (F), 4 (V), 10 (Z), 11 (L), 14 (X), 16 (K), 17 (G)** are currently **unused/reserved**.

---

## 4.1 P-series (Aspect / Event Phase)

**Usage:** clause particle, usually before the verb (can combine with T, H, M, N).

| **Form** | **Phase value**                       | **Gloss**                        |
| -------- | ------------------------------------- | -------------------------------- |
| **pi**   | inceptive / just starting             | “just, just now start to”        |
| **py**   | progressive / in progress             | “currently, be -ing”             |
| **pe**   | resumptive / back again               | “again, back (to doing it)”      |
| **pa**   | continuative / still ongoing          | “still, keep (on)”               |
| **po**   | completive / through to the end       | “completely, all the way”        |
| **pu**   | perfect / already done / result state | “already, (has) done / finished” |

Example:

```text
te py ji nife-n.
now PROG I eat
“I am eating now.”

pu ty je pase-n.
PRF recent 3SG go
“He/she has already gone (recently).”
```

---

## 4.2 M-series (Degree / Intensity)

**Usage:** modifies properties (`-s`) and events (`-n`), often pre-verbal or pre-adjectival.

| **Form** | **Degree value**               | **Gloss**                 |
| -------- | ------------------------------ | ------------------------- |
| **mi**   | minimal presence               | “slightly, a bit, barely” |
| **my**   | low / below-typical            | “somewhat, rather low”    |
| **me**   | neutral / typical degree       | “moderately, normally”    |
| **ma**   | above-typical                  | “quite, pretty, fairly”   |
| **mo**   | strong / high degree           | “very, strongly”          |
| **mu**   | maximal / excessive / too much | “extremely, too, overly”  |

Example (with a property root `gusa-s` = “knowledgeable”):

```text
ji mi gusa-s.   “I’m a bit knowledgeable.”
ji ma gusa-s.   “I’m quite knowledgeable.”
ji mu gusa-s.   “I’m too knowledgeable / excessively so.”
```

---

## 4.3 T-series (Time / Tense)

**Usage:** clause particle; may stack with P/H/etc.

| **Form** | **Time value**    | **Gloss**              |
| -------- | ----------------- | ---------------------- |
| **ti**   | remote past       | “long ago”             |
| **ty**   | recent past       | “recently / just now”  |
| **te**   | present           | “now / currently”      |
| **ta**   | near future       | “soon / about to”      |
| **to**   | far future        | “later / someday”      |
| **tu**   | gnomic / timeless | “generally / whenever” |

Example:

```text
ty ji nife-n.
recent I eat
“I ate recently / just now.”

tu ju nife-n.
GNOM they eat
“They (generally) eat / they eat whenever (habitually).”
```

---

## 4.4 D-series (Demonstratives)

**Usage:** determiners or demonstrative pronouns.

| **Form** | **Distance / number**     | **Gloss**                |
| -------- | ------------------------- | ------------------------ |
| **di**   | near, singular            | “this”                   |
| **de**   | medial/local, singular    | “that (here / in view)”  |
| **do**   | far / elsewhere, singular | “that (elsewhere)”       |
| **dy**   | near, plural              | “these”                  |
| **da**   | medial/local, plural      | “those (here / in view)” |
| **du**   | far / elsewhere, plural   | “those (elsewhere)”      |

NP example:

```text
di reyi-m   = this person
da kory-t   = those houses (around here)
du beyo-m   = those forests (elsewhere)
```

As pronouns:

```text
di nife-n.  “This (one) eats.”
du pase-n.  “Those (ones) go.”
```

---

## 4.5 N-series (Polarity)

**Usage:** clause-level polarity; often pre-verbal, but may appear in answers.

| **Form** | **Polarity type**               | **Gloss / force**                  |
| -------- | ------------------------------- | ---------------------------------- |
| **ni**   | explicit affirmation            | “yes, indeed, it *is* so”          |
| **ny**   | partial / mixed presence        | “sort of, partly, more or less”    |
| **ne**   | neutral / no polarity focus     | “(no polarity focus / ‘meh’)”      |
| **na**   | simple negation                 | “not, no, it isn’t so”             |
| **no**   | contrary / opposite / anti-     | “on the contrary, anti-, opposite” |
| **nu**   | strong negation / impossibility | “never, absolutely not, cannot”    |

Example:

```text
na ji nife-n.   “I do not eat.”
nu ju pase-n.   “They must never / cannot go.”
ni.             “Yes.” (short answer)
na.             “No.”
```

---

## 4.6 Q-series (Quantifier Type)

**Usage:** NP-level, typically **Q – D – NOUN**.

| Form   | Type                       | Short gloss                       |
| ------ | -------------------------- | --------------------------------- |
| **qi** | empty set                  | “no, none of”                     |
| **qy** | existential, non-partitive | “a / some (there exists)”         |
| **qe** | partitive, not-all         | “some of (them), not all”         |
| **qa** | large subset               | “most (of)”                       |
| **qo** | universal, collective      | “all (of), the whole X”           |
| **qu** | universal, distributive    | “every / each / any (one by one)” |

Examples:

```text
qi reyi-m      = “no person / nobody”
qy reyi-m      = “a person / some (person/people)”
qe reyi-m      = “some of the people (not all)”
qa reyi-m      = “most people”
qo reyi-m      = “all the people (as a group)”
qu reyi-m      = “every person / each person”
```

With D:

```text
qe de reyi-m   = “some of those people (here)”
qa du kory-t   = “most of those houses (elsewhere)”
```

---

## 4.7 S-series (Spatial Topology: static & path)

**Usage:**

* Static: `FIGURE S GROUND` → “X is in/on/around Y”
* Dynamic with a motion verb (`pase-n` “go/move”): same S encodes path relative to ground.

| **Form** | **Topological relation (static)** | **Static gloss**              |
| -------- | --------------------------------- | ----------------------------- |
| **si**   | interior / within boundary        | “in, inside (within X)”       |
| **sy**   | surface / contact                 | “on, on top of, touching X”   |
| **se**   | adjacency / side-by-side          | “next to, beside X”           |
| **sa**   | surrounding area / vicinity       | “around X, in X’s area”       |
| **so**   | exterior / beyond boundary        | “outside X, beyond X”         |
| **su**   | among multiple / spread through   | “among X, amidst, throughout” |

Static examples:

```text
reyi-m si kory-t.    “The person is in the house.”
feni-m sy kory-t.    “The animal is on the house.”
reyi-m se kory-t.    “The person is next to the house.”
reyi-m sa kory-t.    “The person is around the house.”
reyi-m so kory-t.    “The person is outside the house.”
reyi-m su beyo-m.    “The person is among the forest / amidst the trees.”
```

Dynamic with `pase-n` “go/move”:

```text
ji pase-n di kory-t si.   “I go into this house.”
ji pase-n di kory-t sy.   “I go onto this house (roof).”
ji pase-n di kory-t se.   “I go to stand next to this house.”
ji pase-n di kory-t sa.   “I go around this house (into its area).”
ji pase-n di kory-t so.   “I go out of / past this house.”
ji pase-n beyo-m su.      “I go through the forest / along/among the trees.”
```

---

## 4.8 C-series (Comparison / Scalar Relations)

**Usage:** modifies a property `X-s` (or intensity), often with a **standard marked by `re`** (“than NP”).

Pattern for basic comparatives:

```text
[Subject NP]  [C-form] [PROPERTY-s]  [Standard NP] re
→ “Subject is (less/as/more/most/etc.) PROPERTY than Standard.”
```

| **Form** | **Comparative role**  | **Gloss**          |
| -------- | --------------------- | ------------------ |
| **ci**   | minimal bound         | “at least”         |
| **cy**   | less-than             | “less, not as ~”   |
| **ce**   | equal                 | “as ~ as, equally” |
| **ca**   | more-than             | “more, -er”        |
| **co**   | maximal / superlative | “most, at most”    |
| **cu**   | extremal limit        | “as ~ as possible” |

Examples with `gusa-s` = knowledgeable, `reyi-m` = person, `kory-t` = house:

```text
ji ca gusa-s de reyi-m re.
I more knowledgeable that person than
“I am more knowledgeable than that person.”

ji cy gusa-s de reyi-m re.
“I am less knowledgeable than that person.”

ji ce gusa-s de reyi-m re.
“I am as knowledgeable as that person.”

di kory-t ca hoti-s do kory-t re.
this house more hot that.far house than
“This house is hotter than that (far) house.”

ji co gusa-s.
“I am the most knowledgeable (in context).”

ji cu gusa-s.
“I am as knowledgeable as possible.”
```

`re` thus has a special additional use:

* **in comparatives with C**: marks **standard-of-comparison = “than NP”**.

---

## 4.9 W-series (Wh-/Interrogatives)

**Usage:** wh-words; they usually signal interrogativity by themselves. “Which” is expressed compositionally via **wa + NP** (“what thing/person”) plus context.

| **Form** | **Question type** | **Gloss**                 |
| -------- | ----------------- | ------------------------- |
| **wi**   | time              | “when?”                   |
| **wy**   | reason            | “why? (for what reason?)” |
| **we**   | place             | “where?”                  |
| **wa**   | thing             | “what? / what thing?”     |
| **wo**   | person            | “who? / which person?”    |
| **wu**   | manner            | “how? / in what way?”     |

Examples:

```text
wi je nife-n?
when 3SG eat
“When does he/she eat?”

wy je nife-n?
why 3SG eat
“Why does he/she eat?”

we je nife-n?
where 3SG eat
“Where does he/she eat?”

wa ji nife-n?
what I eat
“What do I eat?”

wo nife-n?
who eat
“Who eats?”

wu je nife-n?
how 3SG eat
“How does he/she eat?”
```

“Which X?” is done via **wa/wo + NP (+ D/Q)**:

```text
wo dy reyi-m nife-n?
who these people eat
“Which of these people eats?”

wa dy kory-t ji pase-n so?
what these houses I go past
“Past which of these houses do I go?”
```

---

## 4.10 J-series (Personal Pronouns)

**Usage:** core pronouns; number built in.

| Form   | Person / number | Gloss           |
| ------ | --------------- | --------------- |
| **ji** | 1st singular    | “I”             |
| **jy** | 2nd singular    | “you (sg)”      |
| **je** | 3rd singular    | “he / she / it” |
| **ja** | 1st plural      | “we”            |
| **jo** | 2nd plural      | “you (pl)”      |
| **ju** | 3rd plural      | “they”          |

Examples:

```text
ji nife-n.   “I eat.”
jy zune-n.   “You (sg) speak.”
je pase-n.   “He/she/it goes.”
ja nife-n.   “We eat.”
jo zune-n.   “You (pl) speak.”
ju pase-n.   “They go.”
```

These pronouns combine naturally with T/P/H/M, etc.

---

## 4.11 R-series (Semantic Roles / Case-like Particles)

**Usage:** **NP + R** (postposition-like). Provides core roles: agent, patient, experiencer, instrument, setting, source/goal. Also used in comparatives (`re` = “than NP”).

| **Form** | **Role**                   | **Gloss**                              |
| -------- | -------------------------- | -------------------------------------- |
| **ri**   | agent / controller         | “by (agent), as doer”                  |
| **ry**   | experiencer / beneficiary  | “to / for (person)”                    |
| **re**   | patient / theme / standard | “(object of), about, concerning; than” |
| **ra**   | instrument / means         | “with, using, by means of”             |
| **ro**   | location / setting         | “at, in, on (place/time)”              |
| **ru**   | source/goal / path edge    | “from, to, into/out of (generic DIR)”  |

Examples with `reyi-m` (person), `feni-m` (animal), `kory-t` (house), `rufi-m` (idea), `nife-n`, `zune-n`, `pase-n`:

```text
qi reyi-m ri   qi feni-m re   nife-n.
one person AGT one animal PAT eat
“One person eats one animal.”

qi feni-m re   qi reyi-m ry   zune-n.
one animal PAT one person EXP speak
“The animal speaks to/for one person.”

qi reyi-m ri   de rufi-m ra   zune-n.
one person AGT that idea INST speak
“One person speaks using that idea.”

reyi-m ro kory-t nife-n.
person LOC house eat
“The person eats at the house.”
```

With S for directional path:

```text
reyi-m ru si kory-t pase-n.
person DIR in house go
“The person goes into the house.”

reyi-m ru so kory-t pase-n.
person DIR outside house go
“The person goes out of / past the house.”

reyi-m ru su beyo-m pase-n.
person DIR among forest go
“The person goes through the forest / among the trees.”
```

With C for comparison (as above), **re** marks “than NP”.

---

## 4.12 H-series (Frequency / Habituality)

**Usage:** clause-level particle indicating how often an event occurs.

| **Form** | **Frequency value** | **Gloss**            |
| -------- | ------------------- | -------------------- |
| **hi**   | single occurrence   | “once, one time”     |
| **hy**   | low frequency       | “rarely, seldom”     |
| **he**   | intermittent        | “sometimes”          |
| **ha**   | frequent            | “often, frequently”  |
| **ho**   | typical / habitual  | “usually, normally”  |
| **hu**   | maximal frequency   | “always, constantly” |

Examples:

```text
hi ji nife-n.
once I eat
“I eat once / I ate once.”

hy ju zune-n.
rarely they speak
“They rarely speak.”

he reyi-m nife-n.
sometimes person eat
“Sometimes the person eats.”

ha ju nife-n.
often they eat
“They often eat.”

ho ji zune-n.
usually I speak
“I usually speak.”

hu ji nife-n.
always I eat
“I always eat.”
```

Combines with T/P/M/N/Q etc.

---

# 5. Numeric CV System (00–99)

As in your original spec:

* Consonants in canonical order indexed 0–19.
* Vowels for numerals: I/Y/E/A/O indexed 0–4.
* `CV(d)` with `d = 5*c_index + v_index`, 0 ≤ d ≤ 99.
* U not used for numerals.

Numeric CVs can also function as atomic words in context (digits, labels, codes).

---

That’s your **current full spec** with all defined series, root-matrix, morphology, and particle semantics integrated and lightly cross-linked. If you want, next step could be:

* a **“mini grammar”** page showing recommended default word order (e.g. `[Topic] [Q/W] [T] [P] [H] [M] [N] [Subject] [Other NPs+R/S] [Verb]`), or
* a small **sample text** (like 3–5 sentences) annotated with all these series in action.
