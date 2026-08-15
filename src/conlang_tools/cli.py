"""Command-line interface for conlang tools."""

import argparse
import sys

from .parser import WordParser
from .constants import PARTICLE_SERIES, CORE_ROOTS, number_to_cv, cv_to_number


def cmd_parse(args):
    """Parse and analyze words."""
    parser = WordParser()

    for word in args.words:
        result = parser.parse(word)
        print(result)
        print()


def cmd_validate(args):
    """Validate words."""
    parser = WordParser()

    for word in args.words:
        result = parser.parse(word)
        status = "✓ VALID" if result.is_valid else "✗ INVALID"
        print(f"{word}: {status}")
        if result.errors and args.verbose:
            for error in result.errors:
                print(f"  - {error}")


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


def cmd_number(args):
    """Convert between numbers and CV syllables."""
    if args.to_cv:
        # Convert numbers to CV
        for num in args.to_cv:
            try:
                cv = number_to_cv(num)
                print(f"{num} → {cv.lower()}")
            except ValueError as e:
                print(f"Error for {num}: {e}")

    if args.to_num:
        # Convert CV to numbers
        for cv in args.to_num:
            try:
                num = cv_to_number(cv)
                print(f"{cv.lower()} → {num}")
            except ValueError as e:
                print(f"Error for {cv}: {e}")


def main():
    """Main CLI entry point."""
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
    num_parser = subparsers.add_parser('num', help='Convert between numbers and CV')
    num_parser.add_argument('--to-cv', type=int, nargs='+',
                           help='Convert numbers to CV')
    num_parser.add_argument('--to-num', nargs='+',
                           help='Convert CV to numbers')
    num_parser.set_defaults(func=cmd_number)

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
