# Foundational Spec

## 0\. Scope

**Fixed now:**

  - Consonant inventory **and canonical order**
  - Vowel inventory **and canonical order**
  - Syllable structure & stress
  - Two word types: **atomic CV** vs **content words**
  - Content-word template: **(CV prefixes) + CVCV root + final suffix**
  - Final suffix system: **M T N S L R**
  - Principle that **CV series use one consonant + vowels in I Y E A O U order**
  - Root semantics: **6 Domains × 6 Aspects** (semantic matrix)
  - Numeric **00–99 → CV** system
  - Particle series defined:
      - **P** (Phase), **M** (Degree), **T** (Time), **D** (Demonstrative), **N** (Polarity)
      - **Q** (Quantifier), **S** (Space), **C** (Comparative), **W** (Wh-word), **J** (Pronoun)
      - **K** (Configuration), **R** (Role), **H** (Frequency)
      - **NEW: V** (Modality), **NEW: L** (Logic/Connective)
  - First derivational prefix series: **K, V, L** (and generally any particle series)
  - A core lexicon: **one root per semantic cell (36 roots)**

**Still open:**

  - Additional derivational prefix series (Voice, Evidentiality, etc.)
  - Larger lexicon beyond the 36 core roots
  - Full complex sentence syntax (subordination strategies beyond basic conjunctions)

Design principle:

> Wherever natural, **CV particles double as prefixes** with parallel semantics
> (phrasal vs lexical level).

-----

## 1\. Phonology

### 1.1 Consonants

Canonical consonant order (for indexing, sorting, numeric codes, series labels):

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

| Letter | IPA | Description |
| :--- | :--- | :--- |
| P | /p/ | bilabial voiceless stop |
| B | /b/ | bilabial voiced stop |
| M | /m/ | bilabial nasal |
| F | /f/ | labiodental voiceless fricative |
| V | /v/ | labiodental voiced fricative |
| T | /t/ | alveolar voiceless stop |
| D | /d/ | alveolar voiced stop |
| N | /n/ | alveolar nasal |
| Q | /ts/ | alveolar voiceless affricate |
| S | /s/ | alveolar voiceless fricative |
| Z | /z/ | alveolar voiced fricative |
| L | /l/ | alveolar lateral approximant |
| C | /tʃ/ | postalveolar voiceless affricate (“ch”) |
| W | /dʒ/ | postalveolar voiced affricate (“j”) |
| X | /ʃ/ | postalveolar voiceless fricative (“sh”) |
| J | /j/ | palatal approximant (“y”) |
| K | /k/ | velar voiceless stop |
| G | /g/ | velar voiced stop |
| R | /ʀ/ | uvular trill (or [ʁ]) |
| H | /h/ | glottal voiceless fricative |

**Final consonant pool (for content words):**

> **M  T  N  S  L  R**

Only these six may appear as the final consonant of a **content word**.

-----

### 1.2 Vowels

Canonical vowel order:

> **I  Y  E  A  O  U**

| Letter | IPA | Description |
| :--- | :--- | :--- |
| I | /i/ | high front unrounded |
| Y | /y/ | high front rounded |
| E | /e/ | mid front unrounded |
| A | /a/ | low (front/central) |
| O | /o/ | mid back rounded |
| U | /u/ | high back rounded |

-----

### 1.3 Syllable Structure & Stress

  - Allowed syllables: **CV** or **CVC**
  - No onsetless syllables; no consonant clusters
  - Stress: always on the **penultimate syllable**

Example: `ka.pi.ri-m` → stress on **pi**.

-----

## 2\. Word Structure

### 2.1 Two Word Types

1.  **Atomic words (particles)**

      * Shape: typically **CV**; a few longer fixed forms allowed.
      * Used for: pronouns, TAM, quantifiers, roles, wh-words, connectors.
      * No productive morphology on these forms.

2.  **Content words**

      * Exactly one **CVCV root**.
      * Optional prefix block of one or more **CV prefixes**.
      * Exactly one final consonant suffix from {**M, T, N, S, L, R**}.
      * Template: `(CV prefix)* + CVCV(root) + final suffix`
      * Open-class items: entities, events, properties, manners, relations.

In running text:

  - bare **CV** → atomic word (particle, numeral, etc.).
  - **CVCV + suffix** (+ optional CV prefixes) → content word.

-----

### 2.2 Final Suffix System (Head Kinds)

Final suffixes (in canonical order):

> **-M  -T  -N  -S  -L  -R**

| Suffix | Head kind | Typical use |
| :--- | :--- | :--- |
| **-m** | Entity head | generic noun: “an X-thing / X-entity” |
| **-t** | Specific head | specific entity: “that/the X” |
| **-n** | Event head | verb: “to X / X happens” |
| **-s** | Property head | adjective: “X-like, having X-property” |
| **-l** | Manner head | adverb: “in an X way, X-ly” |
| **-r** | Relational head | relational NP: “of X, X’s, from X, related-by-X” |

-----

### 2.3 Parsing Content Words

Given a token:

1.  If length = 2 and shape = CV → treat as **atomic word**.
2.  Else:
      * If final char ∉ `{m,t,n,s,l,r}` → not a well-formed content word.
      * Else:
          * final char = suffix.
          * preceding 4 characters must be **CVCV** = root.
          * any remaining left characters must form a sequence of **CV** prefixes.

-----

### 2.4 Series Principle (Particles & Prefixes)

Any systematic CV series uses:

  * **one consonant**, and
  * all six **vowels** in canonical order **I Y E A O U**,
  * mapping that vowel order to a consistent semantic progression.

Many CV series serve as:

  * **free particles** (clausal/phrasal operators), and
  * **prefixes** (lexical operators) with parallel semantics.

-----

## 3\. Semantic Matrix (Domains × Aspects)

Every root is **C₁ V₁ C₂ V₂**.

### 3.1 Domains (V₁)

  * **I = PERSON** – individual humans
  * **Y = SOCIETY** – families, groups, institutions
  * **E = LIFE** – non-human life: animals, plants
  * **A = PHYSICAL** – non-living world: matter, energy
  * **O = ARTEFACT** – tools, objects, machines
  * **U = ABSTRACT** – ideas, logic, information

### 3.2 Aspects (V₂)

  * **I = INDIVIDUAL** – basic “things/actors”
  * **Y = CONFIG** – parts, wholes, layouts
  * **E = PROCESS** – activities, changes
  * **A = STATE** – conditions, qualities
  * **O = RELATION** – links, roles
  * **U = QUANTITY** – measures, degrees

*(See Section 6 for the 36 Core Roots)*

-----

## 4\. Particle Mappings (Atomic CV Series)

**Consonant order:**

> **P  B  M  F  V  T  D  N  Q  S  Z  L  C  W  X  J  K  G  R  H**

### 0 – P (Phase / Event Aspect)

| Form | Phase value | Gloss |
| :--- | :--- | :--- |
| **pi** | inceptive | “just now start to” |
| **py** | progressive | “currently, be -ing” |
| **pe** | resumptive | “again, back to doing it” |
| **pa** | continuative | “still, keep (on)” |
| **po** | completive | “completely, all the way” |
| **pu** | perfect | “already, (has) done/finished” |

-----

### 1 – B

*(unused / reserved – potential Voice/Valence)*

-----

### 2 – M (Degree / Intensity)

| Form | Degree value | Gloss |
| :--- | :--- | :--- |
| **mi** | minimal | “slightly, a bit, barely” |
| **my** | low | “somewhat, rather low” |
| **me** | neutral | “moderately, normally” |
| **ma** | above-typical | “quite, pretty, fairly” |
| **mo** | strong | “very, strongly” |
| **mu** | maximal | “extremely, too, overly” |

-----

### 3 – F

*(unused / reserved – potential Evidentiality)*

-----

### 4 – V (Modality / Mood) [NEW]

Expresses the speaker’s attitude toward the reality or necessity of the event.

| Form | Modal Type | Particle Gloss | Prefix Gloss (Derivational) |
| :--- | :--- | :--- | :--- |
| **vi** | Potential | “might, could (maybe)” | “potential-X” |
| **vy** | Ability | “can, able to” | “able-X, capable-X” |
| **ve** | Permission | “may, allowed to” | “permissible-X, licit-X” |
| **va** | Volition | “want to, desire to” | “desired-X, favorite-X” |
| **vo** | Obligation | “should, ought to” | “required-X, duty-X” |
| **vu** | Necessity | “must, have to” | “essential-X, mandatory-X” |

-----

### 5 – T (Time / Tense)

| Form | Time value | Gloss |
| :--- | :--- | :--- |
| **ti** | remote past | “long ago” |
| **ty** | recent past | “recently, just now” |
| **te** | present | “now, currently” |
| **ta** | near future | “soon, about to” |
| **to** | far future | “later, someday” |
| **tu** | gnomic | “generally, whenever” |

-----

### 6 – D (Demonstratives)

| Form | Distance / Number | Gloss |
| :--- | :--- | :--- |
| **di** | near, sg | “this” |
| **de** | medial, sg | “that (here)” |
| **do** | far, sg | “that (over there)” |
| **dy** | near, pl | “these” |
| **da** | medial, pl | “those (here)” |
| **du** | far, pl | “those (over there)” |

-----

### 7 – N (Polarity)

| Form | Polarity type | Gloss |
| :--- | :--- | :--- |
| **ni** | affirmation | “yes, indeed” |
| **ny** | partial | “sort of, partly” |
| **ne** | neutral | “(unmarked)” |
| **na** | negation | “not, no” |
| **no** | contrary | “on the contrary” |
| **nu** | strong negation | “never, absolutely not” |

-----

### 8 – Q (Quantifiers)

| Form | Type | Gloss |
| :--- | :--- | :--- |
| **qi** | empty set | “no, none of” |
| **qy** | existential | “a / some” |
| **qe** | partitive | “some of, not all” |
| **qa** | large subset | “most (of)” |
| **qo** | universal coll. | “all (of), the whole” |
| **qu** | universal dist. | “every / each / any” |

-----

### 9 – S (Spatial Topology)

| Form | Topology | Gloss |
| :--- | :--- | :--- |
| **si** | interior | “in, inside” |
| **sy** | surface | “on, touching” |
| **se** | adjacency | “next to, beside” |
| **sa** | vicinity | “around, near area” |
| **so** | exterior | “outside, beyond” |
| **su** | distributed | “among, throughout” |

-----

### 10 – Z

*(unused / reserved)*

-----

### 11 – L (Logic / Connection) [NEW]

Used to connect clauses or phrases.

| Form | Logic Type | Particle Gloss | Prefix Gloss (Derivational) |
| :--- | :--- | :--- | :--- |
| **li** | AND / Intersection | “and, also, plus” | “co-X, fellow-X” |
| **ly** | OR / Union | “or (inclusive)” | “alternative-X” |
| **le** | XOR / Exclusion | “either/or (exclusive)” | “rival-X, opposing-X” |
| **la** | IF / Condition | “if, assuming that” | “conditional-X” |
| **lo** | BUT / Contrast | “but, however, yet” | “inverse-X, counter-X” |
| **lu** | THEN / Result | “then, therefore, so” | “resultant-X” |

-----

### 12 – C (Comparatives)

| Form | Role | Gloss |
| :--- | :--- | :--- |
| **ci** | minimal | “at least” |
| **cy** | less-than | “less, not as” |
| **ce** | equal | “as \~ as” |
| **ca** | more-than | “more, -er” |
| **co** | superlative | “most” |
| **cu** | extremal | “maximally” |

-----

### 13 – W (Wh-Interrogatives)

| Form | Type | Gloss |
| :--- | :--- | :--- |
| **wi** | time | “when?” |
| **wy** | reason | “why?” |
| **we** | place | “where?” |
| **wa** | thing | “what?” |
| **wo** | person | “who?” |
| **wu** | manner | “how?” |

-----

### 14 – X

*(unused / reserved – potential Emotion)*

-----

### 15 – J (Personal Pronouns)

| Form | Person/Number | Gloss |
| :--- | :--- | :--- |
| **ji** | 1sg | I |
| **jy** | 2sg | you (sg) |
| **je** | 3sg | he / she / it |
| **ja** | 1pl | we |
| **jo** | 2pl | you (pl) |
| **ju** | 3pl | they |

-----

### 16 – K (Configuration)

| Form | Config type | Gloss | Prefix Gloss (kV-ROOT-m) |
| :--- | :--- | :--- | :--- |
| **ki** | singled | “singly” | “one specific X” |
| **ky** | pair | “in pairs” | “a pair of X” |
| **ke** | small group | “a few” | “a small group of X” |
| **ka** | crowd | “together” | “a group/crowd of X” |
| **ko** | mass | “en masse” | “a large mass of X” |
| **ku** | distributed | “scattered” | “X scattered all over” |

-----

### 17 – G

*(unused / reserved)*

-----

### 18 – R (Roles)

| Form | Role | Gloss |
| :--- | :--- | :--- |
| **ri** | agent | “by (doer)” |
| **ry** | experiencer | “to / for” |
| **re** | patient | “object of; than” |
| **ra** | instrument | “with / using” |
| **ro** | location | “at / in / on” |
| **ru** | source/goal | “from / to” |

-----

### 19 – H (Frequency)

| Form | Frequency | Gloss |
| :--- | :--- | :--- |
| **hi** | single | “once” |
| **hy** | low | “rarely” |
| **he** | intermittent | “sometimes” |
| **ha** | frequent | “often” |
| **ho** | habitual | “usually” |
| **hu** | maximal | “always” |

-----

## 5\. Derivational Prefixes

Content words: `(CV prefix)* + CVCV(root) + suffix`

New series added as prefixes:

### 5.1 V-series (Modality) as Prefix

Derives entities/actions characterized by ability, desire, or necessity.

  * **vy-** (Ability): `vy-pase-n` = "to be able to go / to be mobile"
  * **va-** (Desire): `va-feni-m` = "a desired animal" (e.g., a pet)
  * **vu-** (Necessity): `vu-toki-m` = "an essential tool"

### 5.2 L-series (Logic) as Prefix

Derives logical relationships between entities.

  * **li-** (AND): `li-piri-m` = "a fellow person / partner"
  * **lo-** (BUT): `lo-guse-n` = "to counter-think / to object / to rethink"

-----

## 6\. Core Roots (Matrix-Aligned Lexicon)

*(36 Roots – Identical to previous spec)*

  * **I (Person):** piri, mily, zife, hisa, siro, tinu
  * **Y (Society):** rydi, syry, gyfe, vyra, tyro, byru
  * **E (Life):** feni, bely, kefe, mela, sevo, benu
  * **A (Physical):** kati, sary, pase, hata, sako, daru
  * **O (Artefact):** toki, kory, gose, vosa, zoro, komu
  * **U (Abstract):** rufi, lury, guse, gusa, kuro, nunu

-----

## 7\. Basic Syntax (Updated)

### 7.1 Default Clause Template

Updated to include **L** (Clause connector) and **V** (Modality).

```text
[L] [W?] [T] [V] [P] [H] [M] [N] SUBJECT [other NPs] VERB
```

**Order Logic:**

1.  **L** (Connector) links this clause to the previous one.
2.  **T** (Time) sets the scene.
3.  **V** (Modality) sets the potential/desire (e.g., "wanted to").
4.  **P** (Phase) sets the internal timing (e.g., "start to").
5.  **H/M/N** modify the specific action.

Example:

  * `ji va zife-n.` – "I want to speak."
  * `ji va pi zife-n.` – "I want to start speaking."
  * `la ji pase-n, lu jy pase-n.` – "If I go, then you go."

-----

### 7.2 Noun Phrase Template

```text
[Q] [D] [ROOT-m]
```

*(Pronouns behave as NPs)*

-----

### 7.3 Roles & Space

  * `NP ri` (Agent), `NP re` (Patient), `NP ry` (Beneficiary)
  * `NP ro` (Loc), `NP ru` (Dir), `NP ra` (Instr)

-----

## 8\. Numeric CV System (00–99)

*(Unchanged)*
**Consonants:** P..H (0..19)
**Vowels:** I..O (0..4)
**Formula:** `Val = 5 * C_index + V_index`

*Note: Since P-series (00-04) overlaps with Phase particles (pi/py/pe...), context or a numeric marker (like `nunu`) may be required to disambiguate if a number appears in a verb slot.*