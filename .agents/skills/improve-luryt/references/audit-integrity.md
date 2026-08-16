# Audit Integrity Gate

Use `scripts/check_audit.py` to make bookkeeping and holdout chronology machine-checkable. The
checker is not a semantic oracle; it verifies that the evidence claimed in prose is complete,
arithmetically consistent, hashed, and traceable to the frozen candidate.

## Lifecycle

Create the state template beside the audit artifacts:

```bash
python .agents/skills/improve-luryt/scripts/check_audit.py init AUDIT_DIR --mode proposal
```

Use `--mode implementation` only when the user authorized repository edits. Populate
`audit-state.json`, then pass and seal these gates in order:

```bash
python .agents/skills/improve-luryt/scripts/check_audit.py check manifest AUDIT_DIR/audit-state.json --seal
python .agents/skills/improve-luryt/scripts/check_audit.py check pre-holdout AUDIT_DIR/audit-state.json --seal
python .agents/skills/improve-luryt/scripts/check_audit.py check final AUDIT_DIR/audit-state.json --seal
```

The manifest gate requires all later artifacts to remain `null`. The pre-holdout gate requires a
complete discovery matrix, candidate record, atomicity ledger, pre-holdout rerun, and generated
checks while holdout results remain `null`. Its seal fingerprints the candidate record. The final
gate refuses an adopted candidate if that fingerprint changed after the holdout opened.

Seals live in `AUDIT_DIR/.audit-gates/`. The checker never overwrites a different seal; start a
new versioned audit run when a frozen artifact legitimately changes.

## CSV contracts

| Artifact | Required columns |
| --- | --- |
| Manifest | `id,partition,intended_task,pressure_lens,coverage_cell` |
| Discovery | `id,result` |
| Pre-holdout rerun | `id,candidate_result` |
| Holdout | `id,baseline_result,candidate_result` |
| Fresh regressions | `id,result,severity` |

Every result artifact records the corresponding summary in the state file. Include all five keys
even when zero: `PASS`, `STRAINED`, `AMBIGUOUS`, `GAP`, and `CONFLICT`.

Each artifact record has a path relative to `audit-state.json` and its lowercase SHA-256:

```json
{"path": "discovery-results-v1.csv", "sha256": "...", "summary": {"PASS": 0, "STRAINED": 0, "AMBIGUOUS": 0, "GAP": 0, "CONFLICT": 0}}
```

## Candidate and atomicity record

Record the canonical candidate file, selected and predicted failure IDs, non-goals, and every
semantic commitment:

```json
{
  "version": "TARGET-R1-v1",
  "path": "candidate-TARGET-R1-v1.txt",
  "sha256": "...",
  "selected_failure_ids": ["D07", "D08", "D09"],
  "predicted_fixed_ids": ["D07", "D08", "D09"],
  "non_goals": ["adjacent construction remains open"],
  "atomicity_ledger": [{
    "id": "A01",
    "kind": "license",
    "commitment": "License the selected construction.",
    "basis": [{"type": "failure", "ids": ["D07", "D08", "D09"]}]
  }]
}
```

Allowed commitment kinds are `license`, `prohibition`, `interpretation`, `boundary`,
`precedence`, and `exception`. Tie each item to selected failure IDs or to a named invariant.

## Generated checks and implementation traceability

For every generated check, record `planned_cases`, `executed_cases`, `passed`, `failed`, and
`applies_to_candidate`. The checker computes their aggregate and compares it with
`generated_summary`; use the printed totals in the final report.

In implementation mode, list the paths authorized for the run, the paths actually attributed to
it, and map every atomicity ID to its normative files plus tests. If a commitment cannot be tested,
provide `test_limit` instead:

```json
{
  "authorized_paths": ["language/grammar/foundational.md", "tests/test_v2_contracts.py"],
  "changed_paths": ["language/grammar/foundational.md", "tests/test_v2_contracts.py"],
  "traceability": [{
    "commitment_id": "A01",
    "paths": ["language/grammar/foundational.md", "tests/test_v2_contracts.py"],
    "tests": ["tests/test_v2_contracts.py::test_target_rule"]
  }]
}
```

For a final `no-change` decision, supply a nonempty `decision_rationale` and leave implementation
records `null`. A candidate rejected before or after holdout may remain recorded for auditability.
