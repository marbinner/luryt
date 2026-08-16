# Luryt Stress-Test Playbook

Use this playbook to build adversarial evidence before proposing a language change.

## Contents

- Case design
- Audit artifact
- Target-specific pressure
- Discovery matrix
- Useful adversarial methods
- Candidate scorecard
- Holdout protocol
- Evidence standard

## Case design

Start from communicative tasks, not desired forms. Include the intended meaning before attempting a Luryt expression. Prefer small cases whose variables can be changed one at a time.

Use as many of these lenses as apply:

| Lens | Questions to test |
| --- | --- |
| Baseline | Do canonical examples and ordinary uses work exactly as specified? |
| Contrast | Can minimal pairs express every distinction the rule claims to encode? |
| Boundary | What happens at semantic endpoints, empty values, extremes, and category edges? |
| Composition | What happens when the target combines with suffixes, prefixes, particles, roles, quantifiers, demonstratives, or numerals? |
| Scope and attachment | Can different operator orders, role frames, and phrase boundaries be interpreted uniquely? |
| Productivity | Can a speaker handle novel but regular words and sentences without memorized exceptions? |
| Collision | Does a new or existing form collide with a particle, numeral, root boundary, or competing analysis? |
| Discourse | Can the construction survive short connected contexts rather than isolated glosses? |
| Compatibility | Do current valid examples retain their meaning? Can old material be migrated mechanically? |
| Learnability | Can the rule be inferred from its paradigm, explained compactly, and applied without hidden conventions? |

Depth comes from independent contrasts and interactions, not repeated paraphrases.

## Audit artifact

Create one reviewable Markdown or CSV artifact before classifying any case. For proposal-only work, place it under a temporary directory rather than in the repository and report the exact path.

Include:

- target, non-goals, and authority-snapshot file hashes;
- every discovery and holdout prompt with stable IDs, pressure lenses, and intended contrast or coverage cells;
- the discovery/holdout partition;
- a SHA-256 hash of the frozen prompt manifest;
- every discovery result row;
- failure clusters and candidate scorecard;
- an atomicity ledger plus each frozen candidate version, its predicted discovery coverage, canonical-record location, and SHA-256;
- holdout analyses appended only after candidate freeze and the pre-holdout reruns; and
- fresh regression cases kept separate from the frozen corpus.

Also maintain the machine-readable `audit-state.json` described in
[audit-integrity.md](audit-integrity.md). Pass and seal its manifest, pre-holdout, and final gates
at the corresponding workflow boundaries. The checker validates IDs, hashes, summaries, holdout
separation, generated-case arithmetic, the atomicity ledger, and implementation traceability; it
does not decide whether a semantic analysis is correct.

The frozen manifest should contain the task and coverage intent, not a desired Luryt expression or expected PASS/failure label. Do not alter prompt wording, coverage fields, or partition after hashing. If a correction is unavoidable, preserve the old manifest, create a new version and hash, and explain why the run restarted. A summary is not a substitute for the full matrix.

## Target-specific pressure

### Particle or prefix series

- Exercise all six vowels, not only the endpoints.
- Compare every adjacent pair and both endpoints.
- Check whether the order i y e a o u forms a coherent progression.
- Test standalone particle behavior and prefix behavior separately when both are proposed.
- Stack the series with time, phase, frequency, degree, polarity, quantification, roles, and spatial operators where meaningful.
- Check numeric homophony and whether context or num resolves it.
- Search for a gap in the middle of the scale and overlap between neighboring values.

### Syntax or semantic rule

- Cover intransitive, transitive, and multi-argument frames when relevant.
- Vary pivot presence, fully role-marked clauses, pronouns, descriptive heads, and referential heads.
- Test questions, negation, quantifiers, comparison, static space, event settings, and oriented paths when they interact.
- Reverse noun-phrase order and operator order to expose attachment or scope dependence.
- Test ellipsis and omitted arguments only when the current spec licenses them.
- Treat labels such as particle, modifier, and phrasal as semantic descriptions unless the spec separately defines constituent boundaries, position, attachment, and scope. Test each unstated property instead of assuming it.
- Use minimal contexts that force each competing reading instead of accepting an English gloss that hides ambiguity.

### Root or lexical proposal

- Confirm that the first root vowel matches the intended domain and the second matches the intended aspect.
- Compare nearby core roots and explain why ordinary derivation or composition cannot supply the meaning.
- Exercise all six final heads where they yield coherent meanings.
- Exercise K-prefix configurations and relevant particles.
- Check phonological shape, existing root collisions, likely segmentation, and semantic overbreadth.
- Test several unrelated sentences so the proposal is not tailored to one translation.

### Phonology, morphology, or word structure

- Check every legal word boundary affected by the proposal.
- Test zero, one, and multiple prefixes.
- Test stress and prosodic contrast between free particles and prefixes.
- Search for ambiguous suffix, root, and prefix segmentation.
- Verify case normalization and written punctuation separately from phonological claims.
- Preserve the guarantee of unique structural parsing unless the proposal explicitly reopens that invariant.

### Numerals or quantitative expressions

- Test zero, one, transition points, maximum values, and out-of-range values.
- Test numeral/particle homophones in weak and strong contexts.
- Combine numerals with descriptive and referential noun phrases.
- Test counting, labels, arithmetic readings, approximate quantities, and distributive readings separately.
- Require a unique composition rule for multi-syllable numbers.
- For positional or recursive rules, test canonicality, round trips, aliases, leading and internal zeroes, run termination, and adjacent particle boundaries.

## Discovery matrix

Use a table like this in working notes:

| ID | Intended meaning/task | Current expression | Derivation and rule | Lens | Result | Severity | Confidence |
| --- | --- | --- | --- | --- | --- | --- | --- |
| D01 | ... | ... | ... | contrast | AMBIGUOUS | high | high |

Use the result labels consistently:

- PASS: The written rules derive the intended reading compositionally and with adequate contrast.
- STRAINED: A reading is possible, but depends on an unformalized convention, unusual inference, or loss of a claimed distinction.
- AMBIGUOUS: Two relevant readings remain available and context cannot reliably recover the intended one.
- GAP: No expression is licensed without inventing a form or rule.
- CONFLICT: Two written rules require incompatible analyses. Use this when a normative general rule and a documented example directly disagree; reserve STRAINED for an analysis that is possible but depends on an unstated convention.

Record parser or guide behavior separately as TOOLING; it is evidence about implementation, not automatically evidence about the language.

## Useful adversarial methods

### Minimal pairs

Change one feature at a time: identifiable/descriptive, singular/plural, static/dynamic, source/goal, wide/narrow scope, pivot/role-marked, particle/prefix, or adjacent scale value. Confirm that only the intended interpretation changes.

### Cartesian coverage

Cross the target with small sets from an interacting system. For example, test each candidate question role against pivot present/absent, or each path orientation against relevant spatial topologies. Use a reduced pairwise matrix when the full product would add redundant cases.

### Property and generated checks

Use these when a rule is deterministic enough to have an independent oracle, especially for numerals, phonotactics, paradigms, and structural parsing. Freeze the properties before candidate selection where possible. Useful properties include round-trip identity, injectivity, canonical form, closure, boundary transitions, preservation of legacy mappings, and absence of forbidden collisions.

Exhaust a finite domain only when its bound and runtime are reasonable. Otherwise test declared equivalence classes, adversarial boundaries, and a fixed-seed sample. Record the property, oracle, range, seed, case count, and every counterexample. A candidate's own restatement is not an independent oracle, and a million generated instances of one defect still support one failure cause rather than a million independent failures. Machine checks establish formal behavior only; keep semantic evidence in the manual matrix.

### Round-trip paraphrase

Translate an intended meaning into Luryt, derive its meaning from Luryt using only the spec, and compare that derivation with the original. Count hidden English assumptions as failures of the analysis, not features of Luryt.

### Connected micro-contexts

Use two- or three-sentence situations that make deixis, identifiability, reference, temporal scope, or argument roles unavoidable. Keep vocabulary simple enough that the target remains the only variable.

### Counterexample search

After choosing a candidate, construct the shortest sentence that might receive an unwanted reading under it. Then search for an existing valid example whose derivation would change. A candidate is not ready merely because its motivating examples improve.

## Candidate scorecard

Compare each remedy qualitatively:

| Criterion | Questions |
| --- | --- |
| Coverage | How many independent failures disappear? |
| Economy | How many forms, rules, and exceptions are added? |
| Regularity | Does it follow existing matrices, series, word shapes, and scope rules? |
| Compatibility | Which valid words, sentences, data, or teaching examples change? |
| Compositionality | Can the resulting meaning be derived without pragmatic patchwork? |
| Atomicity | Which normative commitments are added, and does any one settle a separable surface or failure cluster? |
| Teachability | Can the rule and its contrasts be stated briefly and demonstrated by minimal pairs? |
| Testability | Which claims can be enforced by code, and which need normative examples? |

Prefer a clarification only when it makes an already entailed analysis explicit. If the clarification chooses among analyses that the current text genuinely permits, treat it as a language change.

Before holdout analysis, write a canonical candidate record containing the exact rule, non-goals, atomicity ledger, and predicted discovery coverage. Save it as immutable UTF-8 bytes in a separate file or a clearly delimited byte-stable artifact block; report its location, version ID, and SHA-256. Preserve every superseded record: changing a licensed form, reading, boundary, precedence rule, or exception creates a new semantic version even when the central idea stays the same.

## Holdout protocol

Write the holdout prompts at the same time as the discovery corpus, then leave them unanalyzed. After selecting and freezing a candidate:

1. Re-run the selected discovery failures, passing controls, and predeclared formal properties.
2. If they expose a semantic defect, preserve that candidate version, freeze the revision, and repeat step 1 before opening the holdout.
3. Derive each holdout case under the unchanged language.
4. Derive it again under the candidate rule.
5. Record improvements, unchanged failures, and regressions.
6. Reject a candidate that requires a second design decision to rescue the holdout.

Do not rewrite holdout prompts after seeing the result. Add new counterexamples as a separate regression set. If a holdout result motivates any semantic candidate revision, relabel that set as discovery evidence and use a newly frozen untouched holdout; otherwise stop without claiming holdout validation.

## Evidence standard

A language change should have:

- at least three independent failures with one root cause;
- exact evidence from the current specification;
- controls showing that neighboring constructions already work;
- a one-sentence normative remedy;
- better outcomes on both discovery and holdout cases;
- no comparably severe new ambiguity or invariant break; and
- explicit remaining limitations.

When that standard is not met, report what the stress test established and leave the language unchanged.
