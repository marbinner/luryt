---
name: improve-luryt
description: Stress-test one narrowly scoped part of the Luryt constructed language, isolate a repeated failure, and propose or implement exactly one evidence-backed language change. Use when you are asked to improve, evolve, extend, challenge, or stress-test Luryt grammar, morphology, phonology, particles, roots, semantics, spatial constructions, questions, or numbers. Do not use for tooling-only bugs, ordinary code changes, or wording edits that do not alter the language.
---

# Improve Luryt

## Objective

Run an evidence-first language-design cycle:

    current rule -> adversarial corpus -> repeated failure -> one change -> holdout and regression test

Make one semantic design decision per run. Treat the documentation, data, examples, and tests needed to express that decision consistently as parts of the same change.

## Establish authority

Resolve the repository root before using the paths below. Preserve unrelated work in the
worktree. Prefer starting a run from a clean committed tree; when the tree carries prior
adopted-but-uncommitted work, say so in the snapshot label and record which paths it touches.

1. Read CONTRIBUTING.md in full.
2. Map the headings and cross-references in language/grammar/foundational.md. Read section 0, the complete section under test, and every section whose behavior directly interacts with it. Read the full spec only when the target is genuinely global or its dependencies cannot be bounded.
3. Inspect the relevant canonical files under language/data/. Generated JSON under src/ and docs/ is consumer output, not an editing target.
4. Inspect the relevant parser and tests. Remember that the current parser establishes word-form validity, not sentence-level grammaticality or meaning.
5. Inspect docs/index.html only when it contains target facts or examples, or when implementation is authorized. Treat archive/ as historical evidence only. Do not restore an older rule merely because it existed before.
6. Record git status and content hashes for every authoritative target file. Give this source set one snapshot label and use it throughout the run.

Recompute the hashes before failure clustering, before opening the holdout, and before any repository edit. If a target file changed:

- inspect the intervening diff;
- continue only when the drift is unrelated to the target, recording that fact;
- discard affected classifications and restart them against one coherent snapshot when target rules changed; and
- never combine evidence derived from different snapshots.

Determine the requested stopping point. An explicit request to implement or make an improvement authorizes the complete cycle. A request only to investigate, recommend, or draft a proposal stops at the proposal checkpoint unless the user later accepts implementation.

## 1. Frame one target

Choose the part named by the user. If none is named, derive a target from a deliberately open or underspecified point in the current spec.

Before inventing any solution, write down:

- one sentence naming the surface under test;
- the current rule, with exact spec evidence;
- the meanings or constructions that surface is expected to support;
- invariants that must remain true;
- observable failure criteria; and
- explicit non-goals.

Keep the scope narrow enough that one rule, contrast, root, or coherent six-form series could address it. Do not preselect the desired change.

## 2. Stress-test the current language

Read [the stress-test playbook](references/stress-test-playbook.md) in full before building the corpus.

Construct 24–40 meaningful cases by default. Use fewer only when the target cannot support that many independent contrasts, and explain the reduced coverage. Reserve at least 20 percent as a frozen holdout set: write those prompts before considering fixes, but do not analyze them until a candidate has been selected, frozen, and passed the pre-holdout reruns in step 5.

Freeze the coverage plan with the prompts. Give every manifest row a stable ID, partition, intended task, pressure lens, and contrast or coverage cell. For a holdout, record what dimension it covers without recording an expression, derivation, desired answer, or expected result. This makes coverage auditable without leaking the test.

Treat the 24–40 cases as the semantic corpus, not as a ceiling on generated checks. When the target is finite or algorithmic, predeclare useful properties and equivalence classes, then add bounded exhaustive or reproducibly sampled checks. Record the oracle, range, count, and random seed where applicable. Generated checks supplement the meaningful cases; their raw count does not turn one structural defect into many independent failures.

Before analysis, create the auditable artifact defined in the playbook. Store it outside the repository for proposal-only work, report its path, and hash the frozen prompt manifest. If no temporary filesystem is available, include the complete artifact in the final response. Do not keep the only copy in private working notes.

Make the audit machine-checkable. Read [the audit-integrity reference](references/audit-integrity.md)
in full, initialize `audit-state.json` with `scripts/check_audit.py`, populate it, and pass the
`manifest --seal` gate before classifying any case. Treat a gate failure as a workflow failure;
repair the artifact, not the evidence, before continuing.

Test the current language without editing authoritative files. Include ordinary controls, minimal pairs, boundary cases, interactions with other systems, scope or attachment traps, productive novel examples, and realistic translation pressure. Reuse existing vocabulary where possible so a missing root is not mistaken for a grammar failure.

For every discovery case, record:

- intended meaning or communicative task;
- best expression licensed by the current spec;
- derivation or parse;
- exact rule evidence;
- result: PASS, STRAINED, AMBIGUOUS, GAP, or CONFLICT; and
- severity and confidence.

Try the strongest charitable analysis permitted by the written rules. Do not silently add a convention to make a case pass. Separate language-design failures from missing vocabulary, documentation ambiguity, and tooling limitations.

Write every result row to the audit artifact, not only totals or representative cases. Freeze the completed discovery results before designing a fix.

## 3. Extract the failure, not the anecdote

Cluster the non-passing cases by cause. Require one repeated failure pattern supported by at least three independent cases before changing the language. Rank clusters by communicative severity, breadth, confidence, and damage to Luryt's design invariants.

If the target survives, select one adjacent underspecified surface and repeat the test. Do not manufacture a change to satisfy the workflow. Stop without mutation if no evidence-backed failure can be found within the authorized scope.

State the selected failure as a falsifiable claim:

    Under rule X, construction Y cannot reliably distinguish meanings A and B when condition Z holds.

## 4. Select exactly one change

Compare at least two plausible remedies plus the null option of clarification or no change. Prefer the remedy that:

- resolves the largest share of the selected cluster;
- preserves unique word parsing and existing contrasts;
- follows the domain-by-aspect matrix and i y e a o u series principle where applicable;
- introduces the fewest new forms or exceptions;
- composes predictably with existing operators, roles, heads, and prefixes;
- minimizes breakage of valid examples; and
- can be stated and taught precisely.

Define the chosen change in one normative sentence, followed by its non-goals. One new root is one change. One syntax rule is one change. One complete six-form particle family may be one change when the family expresses one coherent scale. Do not bundle unrelated roots, cleanup, or syntax decisions.

Count semantic commitments, not sentences. Add an atomicity ledger to the audit artifact listing every newly licensed or prohibited form, interpretation, boundary rule, precedence rule, and exception. Tie each commitment either to the selected failure cluster or to an invariant required to make the remedy deterministic. Defer any commitment that instead settles an adjacent surface or repairs a separate failure cluster.

Before testing the chosen change, freeze its exact normative text, non-goals, atomicity ledger, and predicted discovery coverage under a candidate version ID. Store the canonical record as immutable UTF-8 bytes in a separate temporary file or a clearly delimited byte-stable artifact block, report its location, and hash those exact bytes before inspecting any holdout analysis.

## 5. Try to break the candidate

Apply the candidate hypothetically before editing the repository.

1. Recheck the authority snapshot and resolve any drift.
2. Re-run every failing discovery case.
3. Verify that passing controls still pass.
4. Re-run every predeclared property or generated check that applies to the candidate.
5. Populate the machine-readable candidate, ledger, rerun, and generated-check records. Pass the
   `pre-holdout --seal` audit gate. Do not inspect any holdout outcome until it passes.
6. If the candidate changes before holdout analysis, preserve the superseded version and its results, classify the edit as editorial or semantic, freeze and hash a new version, and repeat steps 2–5. Any edit that changes a licensed form, reading, boundary, precedence, or exception is semantic even if described as a refinement.
7. Open and analyze the frozen holdout set without altering its prompt text.
8. Generate fresh counterexamples aimed specifically at ambiguity, overgeneration, scope leaks, collisions, and irregularity.
9. Compare the result with the unchanged language.

Once any holdout outcome has been inspected, do not tune the candidate against it and continue calling that set a holdout. A semantic revision after opening it turns those rows into discovery evidence; either evaluate the revision on a newly frozen untouched holdout of adequate size or reject it for this run.

Reject or revise the candidate if it merely moves the ambiguity, needs unstated exceptions, breaks a core invariant, or causes a severe regression. Accept it only when it fixes the repeated failure and survives the holdout with no comparably serious new problem.

## 6. Pass the design checkpoint

Respect the language-design process in CONTRIBUTING.md.

For a proposal-only task, produce one issue-ready proposal containing:

- target and current rule;
- authority snapshot and any drift resolution;
- stress-test method and coverage;
- audit-artifact path or complete appendix plus frozen-manifest hash;
- frozen candidate version and hash, including any superseded versions;
- representative failures and controls;
- the single proposed rule;
- alternatives considered;
- holdout and regression results;
- examples and minimal pairs;
- compatibility impact; and
- non-goals.

Do not edit the language in proposal-only mode.

For an implementation task, treat the user's explicit implementation request or an already accepted proposal as the checkpoint approval, then implement only the selected change.

## 7. Synchronize an accepted change

Update canonical sources first, then regenerate every affected consumer:

- language/data/*.json for structured facts;
- language/grammar/foundational.md for normative prose and examples;
- docs/index.html or docs/assets/js/guide.mjs for teaching presentation, only when needed;
- tests/ for machine-checkable invariants and representative forms; and
- README.md only when the public overview changes.

For a prose-only syntax decision that has no JSON representation, make language/grammar/foundational.md the normative edit and add the strongest feasible regression coverage. Do not claim that token-level corpus parsing proves sentence semantics; preserve semantic contrasts as explicit spec examples when no sentence parser can assert them.

When a change adds, removes, or renames a series, root, family, or fixed atom, sweep every
consumer that hardcodes membership or counts. Presentation registries (for example
`SERIES_ORDER` and `SERIES_UI` in docs/assets/js/guide.mjs) fail no check when an entry is
missing — a data-driven page can still have a hand-maintained layout map — and spelled-out
counts ("fourteen families", "seventy of the hundred", "four already earmarked") live in the
spec, the guide, README.md, and CONTRIBUTING.md. Grep for both kinds before declaring the
sync complete.

In implementation mode, record the paths authorized and changed by this run. Map every atomicity
ledger ID to its normative representation and regression coverage; explain any untestable semantic
claim rather than silently omitting it.

Use the established orthography and formatting. Keep roots and particles bolded where the sync tests expect them. Do not change version numbers or historical files unless the accepted change includes a release decision.

## 8. Validate and report

For proposal-only work, run only the targeted read-only checks needed to support factual compatibility claims. Label results from the unchanged repository as baselines; they do not validate the candidate's sentence semantics. Skip the complete repository suite unless a specific proposal claim requires it or the user requests it.

For implementation work, run the relevant focused checks, then run the complete repository checks:

    uv run python scripts/language.py generate
    uv run python scripts/language.py check
    uv run pytest -q
    node --check docs/assets/js/guide.mjs
    node --check docs/assets/js/dictionary.mjs
    git diff --check

Inspect the final diff for scope creep and stale examples; for additive changes, confirm the
new material actually appears on every consumer surface — green checks prove consistency of
what exists, not the presence of what should. Report:

- what was stress-tested and how many cases were used;
- the repeated failure found;
- the one rule adopted or proposed;
- holdout and regression outcomes;
- files changed, if any;
- validation results; and
- important limitations that remain outside scope.

Before reporting, populate the final holdout, regression, generated-summary, decision, and optional
implementation records, then pass `check_audit.py check final ... --seal`. Use its computed counts
instead of manually adding totals. A final `no-change` run must also pass this gate, with a recorded
rationale and no implementation record.
