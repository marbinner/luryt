"""End-to-end exit-code contracts for the command-line interface."""

import os
import subprocess
import sys


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "conlang_tools.cli", *args],
        check=False,
        capture_output=True,
        text=True,
    )


def test_successful_commands_exit_zero():
    assert run_cli("parse", "kapirim").returncode == 0
    result = run_cli("num", "--to-cv", "42", "100", "12345678")
    assert result.returncode == 0
    assert "42 -> qe" in result.stdout
    assert "100 -> py pi" in result.stdout
    assert "12345678 -> me do ly ja" in result.stdout

    result = run_cli("num", "--to-num", "py pi")
    assert result.returncode == 0
    assert "py pi -> 100" in result.stdout


def test_invalid_words_exit_nonzero():
    assert run_cli("parse", "piri").returncode == 1
    assert run_cli("validate", "piri").returncode == 1


def test_undefined_prefixes_exit_nonzero():
    result = run_cli("validate", "--verbose", "xupirim", "papirim", "bipirim")
    assert result.returncode == 1
    assert result.stdout.count("INVALID") == 3
    assert result.stdout.count("not standardized") == 3


def test_number_conversion_error_exits_nonzero_on_stderr():
    result = run_cli("num", "--to-cv", "-1")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Number must be a nonnegative integer" in result.stderr

    result = run_cli("num", "--to-num", "pi py")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "cannot begin with the zero block" in result.stderr


def test_number_command_requires_a_direction():
    result = run_cli("num")
    assert result.returncode == 2
    assert "at least one of --to-cv or --to-num is required" in result.stderr


def test_number_command_supports_unbounded_numeral_runs():
    decimal = "9" * 4400
    numeric_cv = " ".join(["ho"] * 2200)

    encoded = run_cli("num", "--to-cv", decimal)
    assert encoded.returncode == 0
    assert encoded.stderr == ""
    assert encoded.stdout == f"{decimal} -> {numeric_cv}\n"

    decoded = run_cli("num", "--to-num", numeric_cv)
    assert decoded.returncode == 0
    assert decoded.stderr == ""
    assert decoded.stdout == f"{numeric_cv} -> {decimal}\n"


def test_unicode_lookalikes_exit_nonzero():
    result = run_cli("validate", "pı", "ſi")
    assert result.returncode == 1
    assert result.stdout.count("INVALID") == 2


def test_commands_work_with_cp1252_output():
    env = os.environ.copy()
    env["PYTHONIOENCODING"] = "cp1252"

    commands = (
        ("parse", "kapirim"),
        ("validate", "kapirim"),
        ("num", "--to-cv", "42"),
    )
    for command in commands:
        result = subprocess.run(
            [sys.executable, "-m", "conlang_tools.cli", *command],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 0, result.stderr
        assert "Traceback" not in result.stderr

    invalid_commands = (
        ("parse", "pı"),
        ("validate", "pı"),
    )
    for command in invalid_commands:
        result = subprocess.run(
            [sys.executable, "-m", "conlang_tools.cli", *command],
            check=False,
            capture_output=True,
            text=True,
            env=env,
        )
        assert result.returncode == 1
        assert "Traceback" not in result.stderr
        assert "\\u0131" in result.stdout
