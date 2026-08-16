#!/usr/bin/env python3
"""Validate and seal improve-luryt audit checkpoints."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Any


RESULTS = ("PASS", "STRAINED", "AMBIGUOUS", "GAP", "CONFLICT")
NONPASS = set(RESULTS) - {"PASS"}
LEDGER_KINDS = {
    "license",
    "prohibition",
    "interpretation",
    "boundary",
    "precedence",
    "exception",
}
SEVERE = {"high", "critical"}
MANIFEST_COLUMNS = {
    "id",
    "partition",
    "intended_task",
    "pressure_lens",
    "coverage_cell",
}
HOLDOUT_LEAK_COLUMNS = {
    "expression",
    "luryt_expression",
    "derivation",
    "desired_answer",
    "expected_result",
    "result",
}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sha256_json(value: Any) -> str:
    payload = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def string_set(value: Any) -> tuple[set[str], bool]:
    """Return a set plus whether value is a list of nonempty strings."""
    valid = isinstance(value, list) and all(
        isinstance(item, str) and bool(item.strip()) for item in value
    )
    return (set(value) if valid else set(), valid)


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SystemExit(f"ERROR: cannot read {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SystemExit(f"ERROR: {path} must contain one JSON object")
    return value


class AuditValidator:
    def __init__(self, state_path: Path, state: dict[str, Any], gate: str):
        self.state_path = state_path.resolve()
        self.base = self.state_path.parent
        self.state = state
        self.gate = gate
        self.errors: list[str] = []
        self.metrics: dict[str, Any] = {}

    def require(self, condition: bool, message: str) -> bool:
        if not condition:
            self.errors.append(message)
        return condition

    def artifact(self, record: Any, label: str) -> Path | None:
        if not self.require(isinstance(record, dict), f"{label} must be an object"):
            return None
        raw_path = record.get("path")
        expected_hash = record.get("sha256")
        if not self.require(
            isinstance(raw_path, str) and bool(raw_path.strip()),
            f"{label}.path must be a nonempty relative path",
        ):
            return None
        path_value = Path(raw_path)
        if not self.require(
            not path_value.is_absolute() and ".." not in path_value.parts,
            f"{label}.path must stay inside the audit directory",
        ):
            return None
        path = (self.base / path_value).resolve()
        try:
            path.relative_to(self.base)
        except ValueError:
            self.errors.append(f"{label}.path escapes the audit directory")
            return None
        if not self.require(path.is_file(), f"{label} file does not exist: {path}"):
            return None
        if not self.require(
            isinstance(expected_hash, str)
            and len(expected_hash) == 64
            and all(c in "0123456789abcdef" for c in expected_hash),
            f"{label}.sha256 must be a lowercase SHA-256 digest",
        ):
            return path
        actual_hash = sha256_file(path)
        self.require(
            actual_hash == expected_hash,
            f"{label} hash mismatch: recorded {expected_hash}, actual {actual_hash}",
        )
        return path

    def csv_rows(
        self, path: Path | None, label: str, required_columns: set[str]
    ) -> tuple[list[dict[str, str]], set[str]]:
        if path is None:
            return [], set()
        try:
            with path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.DictReader(handle)
                headers = set(reader.fieldnames or [])
                rows = list(reader)
        except (OSError, csv.Error) as exc:
            self.errors.append(f"cannot read {label} CSV: {exc}")
            return [], set()
        missing = required_columns - headers
        self.require(not missing, f"{label} is missing columns: {sorted(missing)}")
        return rows, headers

    def exact_summary(
        self, supplied: Any, computed: Counter[str], label: str
    ) -> None:
        if not self.require(isinstance(supplied, dict), f"{label} must be an object"):
            return
        expected = {result: computed.get(result, 0) for result in RESULTS}
        actual = {key: supplied.get(key) for key in RESULTS}
        extras = set(supplied) - set(RESULTS)
        self.require(not extras, f"{label} has unknown keys: {sorted(extras)}")
        self.require(actual == expected, f"{label} is {actual}; computed {expected}")

    def validate_state_header(self) -> None:
        self.require(self.state.get("schema_version") == 1, "schema_version must be 1")
        self.require(
            self.state.get("mode") in {"proposal", "implementation"},
            "mode must be proposal or implementation",
        )
        self.require(
            isinstance(self.state.get("snapshot_label"), str)
            and bool(self.state["snapshot_label"].strip()),
            "snapshot_label must be nonempty",
        )
        self.require(
            self.state.get("decision") in {"pending", "adopt", "no-change"},
            "decision must be pending, adopt, or no-change",
        )

    def validate_manifest(self) -> tuple[set[str], set[str]]:
        record = self.state.get("manifest")
        path = self.artifact(record, "manifest")
        rows, headers = self.csv_rows(path, "manifest", MANIFEST_COLUMNS)
        discovery: set[str] = set()
        holdout: set[str] = set()
        seen: set[str] = set()
        for index, row in enumerate(rows, start=2):
            case_id = (row.get("id") or "").strip()
            partition = (row.get("partition") or "").strip().lower()
            self.require(bool(case_id), f"manifest row {index} has an empty id")
            self.require(case_id not in seen, f"manifest id is duplicated: {case_id}")
            seen.add(case_id)
            self.require(
                partition in {"discovery", "holdout"},
                f"manifest {case_id or index} has invalid partition {partition!r}",
            )
            for column in ("intended_task", "pressure_lens", "coverage_cell"):
                self.require(
                    bool((row.get(column) or "").strip()),
                    f"manifest {case_id or index} has empty {column}",
                )
            if partition == "discovery":
                discovery.add(case_id)
            elif partition == "holdout":
                holdout.add(case_id)
                for column in HOLDOUT_LEAK_COLUMNS & headers:
                    self.require(
                        not (row.get(column) or "").strip(),
                        f"holdout {case_id} leaks {column} before opening",
                    )

        total = len(rows)
        reason = self.state.get("reduced_corpus_reason")
        in_default_range = 24 <= total <= 40
        self.require(
            in_default_range or (isinstance(reason, str) and bool(reason.strip())),
            f"manifest has {total} cases; explain any count outside the default 24-40 range",
        )
        self.require(bool(discovery), "manifest must contain discovery cases")
        self.require(bool(holdout), "manifest must contain holdout cases")
        ratio = len(holdout) / total if total else 0.0
        self.require(ratio >= 0.20, f"holdout share is {ratio:.1%}; minimum is 20%")
        self.metrics.update(
            manifest_total=total,
            discovery_total=len(discovery),
            holdout_total=len(holdout),
            holdout_ratio=ratio,
        )
        return discovery, holdout

    def validate_result_file(
        self,
        record: Any,
        label: str,
        expected_ids: set[str],
        result_column: str,
    ) -> dict[str, str]:
        path = self.artifact(record, label)
        rows, _ = self.csv_rows(path, label, {"id", result_column})
        results: dict[str, str] = {}
        for index, row in enumerate(rows, start=2):
            case_id = (row.get("id") or "").strip()
            result = (row.get(result_column) or "").strip().upper()
            self.require(bool(case_id), f"{label} row {index} has an empty id")
            self.require(case_id not in results, f"{label} duplicates id {case_id}")
            self.require(result in RESULTS, f"{label} {case_id} has invalid result {result!r}")
            results[case_id] = result
        ids = set(results)
        self.require(
            ids == expected_ids,
            f"{label} ids differ: missing {sorted(expected_ids - ids)}, extra {sorted(ids - expected_ids)}",
        )
        self.exact_summary(
            record.get("summary") if isinstance(record, dict) else None,
            Counter(results.values()),
            f"{label}.summary",
        )
        return results

    def validate_discovery(self, discovery_ids: set[str]) -> dict[str, str]:
        results = self.validate_result_file(
            self.state.get("discovery_results"),
            "discovery_results",
            discovery_ids,
            "result",
        )
        self.metrics["discovery_summary"] = dict(Counter(results.values()))
        return results

    def validate_candidate(
        self, discovery: dict[str, str]
    ) -> tuple[dict[str, Any] | None, set[str], set[str], set[str]]:
        candidate = self.state.get("candidate")
        if not self.require(isinstance(candidate, dict), "candidate must be an object"):
            return None, set(), set(), set()
        self.artifact(candidate, "candidate")
        self.require(
            isinstance(candidate.get("version"), str) and bool(candidate["version"].strip()),
            "candidate.version must be nonempty",
        )
        non_goals = candidate.get("non_goals")
        self.require(
            isinstance(non_goals, list)
            and bool(non_goals)
            and all(isinstance(item, str) and item.strip() for item in non_goals),
            "candidate.non_goals must be a nonempty string list",
        )

        selected_list = candidate.get("selected_failure_ids")
        predicted_list = candidate.get("predicted_fixed_ids")
        selected, selected_valid = string_set(selected_list)
        predicted, predicted_valid = string_set(predicted_list)
        self.require(
            selected_valid and len(selected_list) == len(selected),
            "candidate.selected_failure_ids must be a unique nonempty-string list",
        )
        self.require(len(selected) >= 3, "candidate must select at least three failures")
        actual_nonpass = {case_id for case_id, result in discovery.items() if result in NONPASS}
        self.require(
            selected <= actual_nonpass,
            f"selected failures are not discovery non-passes: {sorted(selected - actual_nonpass)}",
        )
        self.require(
            predicted_valid
            and len(predicted_list) == len(predicted)
            and bool(predicted),
            "candidate.predicted_fixed_ids must be a nonempty unique list",
        )
        self.require(
            predicted <= selected,
            f"predicted fixes are outside the selected cluster: {sorted(predicted - selected)}",
        )

        ledger = candidate.get("atomicity_ledger")
        ledger_ids: set[str] = set()
        if not self.require(
            isinstance(ledger, list) and bool(ledger),
            "candidate.atomicity_ledger must be nonempty",
        ):
            ledger = []
        for index, item in enumerate(ledger, start=1):
            label = f"atomicity_ledger[{index}]"
            if not self.require(isinstance(item, dict), f"{label} must be an object"):
                continue
            item_id = item.get("id")
            self.require(
                isinstance(item_id, str) and bool(item_id.strip()),
                f"{label}.id must be nonempty",
            )
            if isinstance(item_id, str) and item_id.strip():
                self.require(item_id not in ledger_ids, f"atomicity id is duplicated: {item_id}")
                ledger_ids.add(item_id)
            self.require(item.get("kind") in LEDGER_KINDS, f"{label}.kind is invalid")
            self.require(
                isinstance(item.get("commitment"), str) and bool(item["commitment"].strip()),
                f"{label}.commitment must be nonempty",
            )
            bases = item.get("basis")
            if not self.require(
                isinstance(bases, list) and bool(bases), f"{label}.basis must be nonempty"
            ):
                continue
            for basis_index, basis in enumerate(bases, start=1):
                basis_label = f"{label}.basis[{basis_index}]"
                if not self.require(isinstance(basis, dict), f"{basis_label} must be an object"):
                    continue
                if basis.get("type") == "failure":
                    ids = basis.get("ids")
                    id_set, ids_valid = string_set(ids)
                    self.require(
                        ids_valid and bool(ids) and len(ids) == len(id_set),
                        f"{basis_label}.ids must be a nonempty unique list",
                    )
                    self.require(
                        id_set <= selected,
                        f"{basis_label} cites unselected failures: {sorted(id_set - selected)}",
                    )
                elif basis.get("type") == "invariant":
                    self.require(
                        isinstance(basis.get("name"), str) and bool(basis["name"].strip()),
                        f"{basis_label}.name must be nonempty",
                    )
                else:
                    self.errors.append(f"{basis_label}.type must be failure or invariant")
        self.metrics["selected_failures"] = len(selected)
        self.metrics["predicted_fixes"] = len(predicted)
        return candidate, selected, predicted, ledger_ids

    def validate_pre_holdout(
        self,
        discovery: dict[str, str],
        predicted: set[str],
        require_success: bool,
    ) -> dict[str, str]:
        results = self.validate_result_file(
            self.state.get("pre_holdout_results"),
            "pre_holdout_results",
            set(discovery),
            "candidate_result",
        )
        if require_success:
            missed = {case_id for case_id in predicted if results.get(case_id) != "PASS"}
            regressed = {
                case_id
                for case_id, baseline in discovery.items()
                if baseline == "PASS" and results.get(case_id) != "PASS"
            }
            self.require(not missed, f"predicted fixes did not pass: {sorted(missed)}")
            self.require(not regressed, f"passing discovery controls regressed: {sorted(regressed)}")
        self.metrics["pre_holdout_summary"] = dict(Counter(results.values()))
        return results

    def validate_holdout(
        self, record: Any, holdout_ids: set[str], require_acceptance: bool
    ) -> None:
        path = self.artifact(record, "holdout_results")
        rows, _ = self.csv_rows(
            path, "holdout_results", {"id", "baseline_result", "candidate_result"}
        )
        baseline: dict[str, str] = {}
        candidate: dict[str, str] = {}
        for index, row in enumerate(rows, start=2):
            case_id = (row.get("id") or "").strip()
            before = (row.get("baseline_result") or "").strip().upper()
            after = (row.get("candidate_result") or "").strip().upper()
            self.require(bool(case_id), f"holdout_results row {index} has an empty id")
            self.require(case_id not in baseline, f"holdout_results duplicates id {case_id}")
            self.require(before in RESULTS, f"holdout {case_id} has invalid baseline {before!r}")
            self.require(after in RESULTS, f"holdout {case_id} has invalid candidate {after!r}")
            baseline[case_id] = before
            candidate[case_id] = after
        ids = set(baseline)
        self.require(
            ids == holdout_ids,
            f"holdout_results ids differ: missing {sorted(holdout_ids - ids)}, extra {sorted(ids - holdout_ids)}",
        )
        if isinstance(record, dict):
            self.exact_summary(
                record.get("baseline_summary"),
                Counter(baseline.values()),
                "holdout_results.baseline_summary",
            )
            self.exact_summary(
                record.get("candidate_summary"),
                Counter(candidate.values()),
                "holdout_results.candidate_summary",
            )
        improvements = sum(
            1 for case_id in ids if baseline[case_id] != "PASS" and candidate[case_id] == "PASS"
        )
        regressions = sum(
            1 for case_id in ids if baseline[case_id] == "PASS" and candidate[case_id] != "PASS"
        )
        if require_acceptance:
            self.require(improvements > 0, "accepted candidate improves no failing holdout")
            self.require(regressions == 0, f"accepted candidate regresses {regressions} holdouts")
        self.metrics.update(holdout_improvements=improvements, holdout_regressions=regressions)

    def validate_fresh_regressions(self, record: Any, manifest_ids: set[str]) -> None:
        path = self.artifact(record, "fresh_regressions")
        rows, _ = self.csv_rows(path, "fresh_regressions", {"id", "result", "severity"})
        self.require(bool(rows), "fresh_regressions must contain at least one case")
        results: dict[str, str] = {}
        severe_nonpasses: list[str] = []
        for index, row in enumerate(rows, start=2):
            case_id = (row.get("id") or "").strip()
            result = (row.get("result") or "").strip().upper()
            severity = (row.get("severity") or "").strip().lower()
            self.require(bool(case_id), f"fresh_regressions row {index} has an empty id")
            self.require(case_id not in results, f"fresh_regressions duplicates id {case_id}")
            self.require(case_id not in manifest_ids, f"fresh regression reuses manifest id {case_id}")
            self.require(result in RESULTS, f"fresh regression {case_id} has invalid result {result!r}")
            self.require(
                severity in {"low", "medium", "high", "critical"},
                f"fresh regression {case_id} has invalid severity {severity!r}",
            )
            if result in NONPASS and severity in SEVERE:
                severe_nonpasses.append(case_id)
            results[case_id] = result
        if isinstance(record, dict):
            self.exact_summary(
                record.get("summary"),
                Counter(results.values()),
                "fresh_regressions.summary",
            )
        self.require(
            not severe_nonpasses,
            f"fresh regressions contain severe non-passes: {sorted(severe_nonpasses)}",
        )
        self.metrics["fresh_summary"] = dict(Counter(results.values()))

    def validate_generated(self, candidate_stage: bool) -> None:
        checks = self.state.get("generated_checks")
        if not self.require(isinstance(checks, list), "generated_checks must be a list"):
            return
        ids: set[str] = set()
        totals = Counter(planned_cases=0, executed_cases=0, passed=0, failed=0)
        for index, check in enumerate(checks, start=1):
            label = f"generated_checks[{index}]"
            if not self.require(isinstance(check, dict), f"{label} must be an object"):
                continue
            check_id = check.get("id")
            self.require(
                isinstance(check_id, str) and bool(check_id.strip()),
                f"{label}.id must be nonempty",
            )
            if isinstance(check_id, str):
                self.require(check_id not in ids, f"generated check id is duplicated: {check_id}")
                ids.add(check_id)
            self.require(
                isinstance(check.get("oracle"), str) and bool(check["oracle"].strip()),
                f"{label}.oracle must be nonempty",
            )
            numbers: dict[str, int] = {}
            for key in ("planned_cases", "executed_cases", "passed", "failed"):
                value = check.get(key)
                self.require(
                    isinstance(value, int) and not isinstance(value, bool) and value >= 0,
                    f"{label}.{key} must be a nonnegative integer",
                )
                numbers[key] = value if isinstance(value, int) and not isinstance(value, bool) else 0
                totals[key] += numbers[key]
            self.require(
                numbers["executed_cases"] == numbers["passed"] + numbers["failed"],
                f"{label}: executed_cases must equal passed + failed",
            )
            applies = check.get("applies_to_candidate")
            if candidate_stage:
                self.require(isinstance(applies, bool), f"{label}.applies_to_candidate must be boolean")
                if applies is True:
                    self.require(
                        numbers["executed_cases"] == numbers["planned_cases"],
                        f"{label}: execute every planned applicable case",
                    )
                elif applies is False:
                    self.require(
                        isinstance(check.get("not_applicable_reason"), str)
                        and bool(check["not_applicable_reason"].strip()),
                        f"{label}.not_applicable_reason must explain exclusion",
                    )
                    self.require(
                        numbers["executed_cases"] == 0,
                        f"{label}: a non-applicable check must execute zero cases",
                    )
            else:
                self.require(
                    numbers["executed_cases"] == 0,
                    f"{label}: do not record generated outcomes before analysis",
                )
        summary = self.state.get("generated_summary")
        if self.require(isinstance(summary, dict), "generated_summary must be an object"):
            actual = {key: summary.get(key) for key in totals}
            expected = dict(totals)
            self.require(actual == expected, f"generated_summary is {actual}; computed {expected}")
            extras = set(summary) - set(totals)
            self.require(not extras, f"generated_summary has unknown keys: {sorted(extras)}")
        self.metrics["generated_summary"] = dict(totals)

    def validate_implementation(self, ledger_ids: set[str]) -> None:
        implementation = self.state.get("implementation")
        mode = self.state.get("mode")
        if mode == "proposal":
            self.require(
                implementation is None,
                "proposal mode must not contain implementation records",
            )
            return
        if not self.require(
            isinstance(implementation, dict),
            "implementation mode requires an implementation object",
        ):
            return
        authorized = implementation.get("authorized_paths")
        changed = implementation.get("changed_paths")
        authorized_set, authorized_valid = string_set(authorized)
        changed_set, changed_valid = string_set(changed)
        self.require(
            authorized_valid and len(authorized) == len(authorized_set) and bool(authorized),
            "implementation.authorized_paths must be a nonempty unique list",
        )
        self.require(
            changed_valid and len(changed) == len(changed_set) and bool(changed),
            "implementation.changed_paths must be a nonempty unique list",
        )
        self.require(
            changed_set <= authorized_set,
            f"implementation changed unauthorized paths: {sorted(changed_set - authorized_set)}",
        )
        traceability = implementation.get("traceability")
        traced: set[str] = set()
        if not self.require(
            isinstance(traceability, list) and bool(traceability),
            "implementation.traceability must be nonempty",
        ):
            traceability = []
        for index, item in enumerate(traceability, start=1):
            label = f"implementation.traceability[{index}]"
            if not self.require(isinstance(item, dict), f"{label} must be an object"):
                continue
            commitment_id = item.get("commitment_id")
            self.require(
                isinstance(commitment_id, str) and commitment_id in ledger_ids,
                f"{label}.commitment_id must name an atomicity commitment",
            )
            if isinstance(commitment_id, str):
                self.require(commitment_id not in traced, f"traceability duplicates {commitment_id}")
                traced.add(commitment_id)
            paths = item.get("paths")
            path_set, paths_valid = string_set(paths)
            self.require(
                paths_valid and bool(paths) and len(paths) == len(path_set),
                f"{label}.paths must be a nonempty unique list",
            )
            self.require(
                path_set <= changed_set,
                f"{label} cites paths not attributed to this run: {sorted(path_set - changed_set)}",
            )
            tests = item.get("tests")
            test_limit = item.get("test_limit")
            has_tests = isinstance(tests, list) and bool(tests) and all(
                isinstance(test, str) and test.strip() for test in tests
            )
            has_limit = isinstance(test_limit, str) and bool(test_limit.strip())
            self.require(has_tests or has_limit, f"{label} needs tests or a test_limit explanation")
        self.require(
            traced == ledger_ids,
            f"traceability differs from atomicity ledger: missing {sorted(ledger_ids - traced)}, extra {sorted(traced - ledger_ids)}",
        )

    def seal_file(self, gate: str) -> Path:
        return self.base / ".audit-gates" / f"{gate}.json"

    def read_seal(self, gate: str) -> dict[str, Any] | None:
        path = self.seal_file(gate)
        if not self.require(path.is_file(), f"missing {gate} seal; run that gate with --seal first"):
            return None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            self.errors.append(f"cannot read {gate} seal: {exc}")
            return None
        if not self.require(isinstance(value, dict), f"{gate} seal must be a JSON object"):
            return None
        return value

    def manifest_seal_payload(self) -> dict[str, Any]:
        manifest = self.state.get("manifest") or {}
        return {
            "schema_version": 1,
            "gate": "manifest",
            "snapshot_label": self.state.get("snapshot_label"),
            "manifest_sha256": manifest.get("sha256"),
        }

    def pre_holdout_seal_payload(self) -> dict[str, Any]:
        manifest = self.state.get("manifest") or {}
        discovery = self.state.get("discovery_results") or {}
        candidate = self.state.get("candidate") or {}
        rerun = self.state.get("pre_holdout_results") or {}
        return {
            "schema_version": 1,
            "gate": "pre-holdout",
            "snapshot_label": self.state.get("snapshot_label"),
            "manifest_sha256": manifest.get("sha256"),
            "discovery_sha256": discovery.get("sha256"),
            "candidate_sha256": candidate.get("sha256"),
            "candidate_record_sha256": sha256_json(candidate),
            "pre_holdout_sha256": rerun.get("sha256"),
        }

    def verify_seal(self, gate: str, expected: dict[str, Any]) -> None:
        actual = self.read_seal(gate)
        if actual is not None:
            self.require(actual == expected, f"{gate} seal no longer matches frozen artifacts")

    def write_seal(self, gate: str, payload: dict[str, Any]) -> None:
        path = self.seal_file(gate)
        path.parent.mkdir(parents=True, exist_ok=True)
        if path.exists():
            existing = read_json(path)
            if existing != payload:
                raise SystemExit(
                    f"ERROR: refusing to overwrite changed seal {path}; start a new audit run"
                )
            print(f"seal unchanged: {path}")
            return
        path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"sealed: {path}")

    def run(self) -> tuple[dict[str, Any], dict[str, Any]]:
        self.validate_state_header()
        discovery_ids, holdout_ids = self.validate_manifest()
        decision = self.state.get("decision")

        if self.gate == "manifest":
            self.require(decision == "pending", "manifest gate requires decision=pending")
            for key in (
                "discovery_results",
                "candidate",
                "pre_holdout_results",
                "holdout_results",
                "fresh_regressions",
                "implementation",
            ):
                self.require(self.state.get(key) is None, f"manifest gate requires {key}=null")
            self.validate_generated(candidate_stage=False)
            payload = self.manifest_seal_payload()

        elif self.gate == "pre-holdout":
            self.require(decision == "pending", "pre-holdout gate requires decision=pending")
            self.verify_seal("manifest", self.manifest_seal_payload())
            discovery = self.validate_discovery(discovery_ids)
            candidate, _, predicted, _ = self.validate_candidate(discovery)
            self.validate_pre_holdout(discovery, predicted, require_success=True)
            self.validate_generated(candidate_stage=True)
            for key in ("holdout_results", "fresh_regressions", "implementation"):
                self.require(self.state.get(key) is None, f"pre-holdout gate requires {key}=null")
            self.require(candidate is not None, "pre-holdout gate requires a candidate")
            payload = self.pre_holdout_seal_payload()

        else:
            self.require(decision in {"adopt", "no-change"}, "final gate needs a final decision")
            self.verify_seal("manifest", self.manifest_seal_payload())
            discovery = self.validate_discovery(discovery_ids)
            candidate = None
            predicted: set[str] = set()
            ledger_ids: set[str] = set()
            if self.state.get("candidate") is not None:
                candidate, _, predicted, ledger_ids = self.validate_candidate(discovery)
            if self.state.get("pre_holdout_results") is not None:
                self.validate_pre_holdout(
                    discovery,
                    predicted,
                    require_success=decision == "adopt",
                )
            self.validate_generated(candidate_stage=candidate is not None)

            if decision == "adopt":
                self.require(candidate is not None, "adopt requires a candidate")
                self.require(
                    self.state.get("pre_holdout_results") is not None,
                    "adopt requires pre_holdout_results",
                )
                self.verify_seal("pre-holdout", self.pre_holdout_seal_payload())
                self.validate_holdout(
                    self.state.get("holdout_results"), holdout_ids, require_acceptance=True
                )
                self.validate_fresh_regressions(
                    self.state.get("fresh_regressions"), discovery_ids | holdout_ids
                )
                self.validate_implementation(ledger_ids)
            else:
                rationale = self.state.get("decision_rationale")
                self.require(
                    isinstance(rationale, str) and bool(rationale.strip()),
                    "no-change requires decision_rationale",
                )
                self.require(
                    self.state.get("implementation") is None,
                    "no-change must not contain implementation records",
                )
                if self.state.get("holdout_results") is not None:
                    self.require(candidate is not None, "holdout results require a candidate")
                    self.verify_seal("pre-holdout", self.pre_holdout_seal_payload())
                    self.validate_holdout(
                        self.state.get("holdout_results"), holdout_ids, require_acceptance=False
                    )
                if self.state.get("fresh_regressions") is not None:
                    self.validate_fresh_regressions(
                        self.state.get("fresh_regressions"), discovery_ids | holdout_ids
                    )
            payload = {
                "schema_version": 1,
                "gate": "final",
                "snapshot_label": self.state.get("snapshot_label"),
                "decision": decision,
                "manifest_sha256": (self.state.get("manifest") or {}).get("sha256"),
                "candidate_record_sha256": sha256_json(candidate) if candidate else None,
                "holdout_sha256": (self.state.get("holdout_results") or {}).get("sha256"),
                "fresh_regressions_sha256": (
                    self.state.get("fresh_regressions") or {}
                ).get("sha256"),
                "generated_summary": self.state.get("generated_summary"),
                "implementation_record_sha256": sha256_json(self.state.get("implementation")),
            }

        if self.errors:
            raise AuditFailure(self.errors)
        return payload, self.metrics


class AuditFailure(Exception):
    def __init__(self, errors: list[str]):
        self.errors = errors
        super().__init__("audit validation failed")


def initial_state(mode: str) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "mode": mode,
        "snapshot_label": "",
        "decision": "pending",
        "decision_rationale": "",
        "reduced_corpus_reason": "",
        "manifest": {"path": "prompt-manifest-v1.csv", "sha256": ""},
        "discovery_results": None,
        "candidate": None,
        "pre_holdout_results": None,
        "holdout_results": None,
        "fresh_regressions": None,
        "generated_checks": [],
        "generated_summary": {
            "planned_cases": 0,
            "executed_cases": 0,
            "passed": 0,
            "failed": 0,
        },
        "implementation": None,
    }


def command_init(args: argparse.Namespace) -> int:
    audit_dir = Path(args.audit_dir).resolve()
    audit_dir.mkdir(parents=True, exist_ok=True)
    state_path = audit_dir / "audit-state.json"
    if state_path.exists():
        print(f"ERROR: refusing to overwrite {state_path}", file=sys.stderr)
        return 1
    state_path.write_text(
        json.dumps(initial_state(args.mode), indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(state_path)
    return 0


def command_check(args: argparse.Namespace) -> int:
    state_path = Path(args.state).resolve()
    state = read_json(state_path)
    validator = AuditValidator(state_path, state, args.gate)
    try:
        payload, metrics = validator.run()
    except AuditFailure as exc:
        print(f"FAIL {args.gate} gate ({len(exc.errors)} errors):", file=sys.stderr)
        for error in exc.errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    manifest_line = (
        f"{metrics.get('manifest_total', 0)} prompts; "
        f"{metrics.get('discovery_total', 0)} discovery; "
        f"{metrics.get('holdout_total', 0)} holdout "
        f"({metrics.get('holdout_ratio', 0.0):.1%})"
    )
    generated = metrics.get("generated_summary", {})
    print(
        f"PASS {args.gate} gate: {manifest_line}; generated "
        f"{generated.get('executed_cases', 0)}/{generated.get('planned_cases', 0)} executed, "
        f"{generated.get('passed', 0)} passed, {generated.get('failed', 0)} failed"
    )
    if "holdout_improvements" in metrics:
        print(
            f"holdout: {metrics['holdout_improvements']} improvements, "
            f"{metrics['holdout_regressions']} regressions"
        )
    if args.seal:
        validator.write_seal(args.gate, payload)
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    init_parser = subparsers.add_parser("init", help="create an audit-state template")
    init_parser.add_argument("audit_dir")
    init_parser.add_argument("--mode", choices=("proposal", "implementation"), required=True)
    init_parser.set_defaults(func=command_init)

    check_parser = subparsers.add_parser("check", help="validate an audit checkpoint")
    check_parser.add_argument("gate", choices=("manifest", "pre-holdout", "final"))
    check_parser.add_argument("state")
    check_parser.add_argument("--seal", action="store_true", help="write an immutable gate seal")
    check_parser.set_defaults(func=command_check)
    return parser


def main() -> int:
    args = build_parser().parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
