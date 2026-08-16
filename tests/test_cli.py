"""End-to-end exit-code contracts for the command-line interface."""

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
    result = run_cli("num", "--to-cv", "42")
    assert result.returncode == 0
    assert "42 → qe" in result.stdout


def test_invalid_words_exit_nonzero():
    assert run_cli("parse", "piri").returncode == 1
    assert run_cli("validate", "piri").returncode == 1


def test_number_conversion_error_exits_nonzero_on_stderr():
    result = run_cli("num", "--to-cv", "100")
    assert result.returncode == 1
    assert result.stdout == ""
    assert "Number must be between 0 and 99" in result.stderr


def test_number_command_requires_a_direction():
    result = run_cli("num")
    assert result.returncode == 2
    assert "at least one of --to-cv or --to-num is required" in result.stderr
