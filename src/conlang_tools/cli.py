"""Command-line interface for conlang tools."""

import argparse
import sys

from .parser import WordParser
from .constants import PARTICLE_SERIES, CORE_ROOTS, number_to_cv, cv_to_number


def _configure_output_streams() -> None:
    """Keep CLI diagnostics printable on non-UTF-8 text streams."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if callable(reconfigure):
            reconfigure(errors="backslashreplace")


def cmd_parse(args):
    """Parse and analyze words."""
    parser = WordParser()
    all_valid = True

    for word in args.words:
        result = parser.parse(word)
        all_valid = all_valid and result.is_valid
        print(result)
        print()

    return 0 if all_valid else 1


def cmd_validate(args):
    """Validate words."""
    parser = WordParser()
    all_valid = True

    for word in args.words:
        result = parser.parse(word)
        all_valid = all_valid and result.is_valid
        status = "VALID" if result.is_valid else "INVALID"
        print(f"{word}: {status}")
        if result.errors and args.verbose:
            for error in result.errors:
                print(f"  - {error}")

    return 0 if all_valid else 1


def cmd_reference(args):
    """Show reference information."""
    if args.type == 'particles':
        print("Particle Series Reference\n")
        for series_name, particles in PARTICLE_SERIES.items():
            print(f"{series_name}-series:")
            for particle, (meaning, gloss) in particles.items():
                print(f"  {particle.lower()} - {gloss}")
            print()

    elif args.type == 'roots':
        print("Core Roots (36 from semantic matrix)\n")
        for root, info in sorted(CORE_ROOTS.items()):
            print(f"{root.lower()} ({info['domain']}{info['aspect']}) - {info['gloss']}")

    elif args.type == 'suffixes':
        from .constants import HEAD_KINDS
        print("Final Suffixes (Head Kinds)\n")
        for suffix, (kind, description) in HEAD_KINDS.items():
            print(f"-{suffix.lower()} : {kind}")
            print(f"    {description}")
            print()

    return 0


def cmd_number(args):
    """Convert between numbers and canonical numeric-CV runs."""
    status = 0

    if args.to_cv:
        # Convert numbers to canonical CV runs
        for num in args.to_cv:
            try:
                cv = number_to_cv(num)
            except ValueError as e:
                print(f"Error for {num}: {e}", file=sys.stderr)
                status = 1
            else:
                print(f"{num} -> {cv.lower()}")

    if args.to_num:
        # Convert canonical CV runs to numbers
        for cv in args.to_num:
            try:
                num = cv_to_number(cv)
            except ValueError as e:
                print(f"Error for {cv}: {e}", file=sys.stderr)
                status = 1
            else:
                print(f"{cv.lower()} -> {num}")

    return status


def main() -> int:
    """Main CLI entry point."""
    _configure_output_streams()

    parser = argparse.ArgumentParser(
        description='Luryt parsing and reference tools',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # Parse command
    parse_parser = subparsers.add_parser('parse', help='Parse and analyze words')
    parse_parser.add_argument('words', nargs='+', help='Words to parse')
    parse_parser.set_defaults(func=cmd_parse)

    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate word structure')
    validate_parser.add_argument('words', nargs='+', help='Words to validate')
    validate_parser.add_argument('-v', '--verbose', action='store_true',
                                help='Show error details')
    validate_parser.set_defaults(func=cmd_validate)

    # Reference command
    ref_parser = subparsers.add_parser('ref', help='Show reference information')
    ref_parser.add_argument('type', choices=['particles', 'roots', 'suffixes'],
                           help='Type of reference to show')
    ref_parser.set_defaults(func=cmd_reference)

    # Number conversion command
    num_parser = subparsers.add_parser(
        'num', help='Convert between numbers and numeric-CV runs'
    )
    num_parser.add_argument('--to-cv', type=int, nargs='+',
                           help='Convert nonnegative integers to canonical CV runs')
    num_parser.add_argument('--to-num', nargs='+',
                           help='Convert CV runs to integers (quote multi-block runs)')
    num_parser.set_defaults(func=cmd_number)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 1

    if args.command == 'num' and not args.to_cv and not args.to_num:
        num_parser.error("at least one of --to-cv or --to-num is required")

    if hasattr(args, 'func'):
        return args.func(args)

    parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
