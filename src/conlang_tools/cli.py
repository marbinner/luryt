"""Command-line interface for conlang tools."""

import argparse
import sys
from pathlib import Path
from typing import Optional

from .parser import WordParser
from .lexicon import Lexicon, LexiconEntry
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


def cmd_dict_init(args):
    """Initialize a new dictionary."""
    lexicon = Lexicon(filepath=Path(args.file))

    # Load core content if requested
    added = 0
    if args.load_roots:
        added += lexicon.load_core_roots()
        print(f"Loaded {added} core root entries")

    if args.load_particles:
        p_added = lexicon.load_particles()
        added += p_added
        print(f"Loaded {p_added} particle entries")

    lexicon.save()
    print(f"Dictionary initialized at {args.file}")
    print(f"Total entries: {len(lexicon)}")


def cmd_dict_add(args):
    """Add word to dictionary."""
    lexicon = Lexicon(filepath=Path(args.file))

    examples = args.examples if args.examples else []

    success = lexicon.add_word(
        word=args.word,
        gloss=args.gloss,
        notes=args.notes or '',
        examples=examples,
        overwrite=args.overwrite
    )

    if success:
        lexicon.save()
        print(f"Added '{args.word}' to dictionary")
    else:
        print(f"Word '{args.word}' already exists (use --overwrite to replace)")
        sys.exit(1)


def cmd_dict_lookup(args):
    """Look up word in dictionary."""
    lexicon = Lexicon(filepath=Path(args.file))

    if not lexicon.filepath.exists():
        print(f"Dictionary file not found: {args.file}")
        sys.exit(1)

    entry = lexicon.get(args.word)

    if entry:
        print(f"Word: {entry.word}")
        print(f"Gloss: {entry.gloss}")
        if entry.root:
            print(f"Root: {entry.root}")
        print(f"Type: {entry.word_type}")
        if entry.notes:
            print(f"Notes: {entry.notes}")
        if entry.examples:
            print("Examples:")
            for ex in entry.examples:
                print(f"  - {ex}")
    else:
        print(f"Word '{args.word}' not found in dictionary")
        sys.exit(1)


def cmd_dict_search(args):
    """Search dictionary."""
    lexicon = Lexicon(filepath=Path(args.file))

    if not lexicon.filepath.exists():
        print(f"Dictionary file not found: {args.file}")
        sys.exit(1)

    results = lexicon.search(args.query, field=args.field)

    if results:
        print(f"Found {len(results)} result(s):\n")
        for entry in results:
            print(f"{entry.word} - {entry.gloss}")
            if args.verbose and entry.notes:
                print(f"  Notes: {entry.notes}")
            if args.verbose and entry.root:
                print(f"  Root: {entry.root}")
            print()
    else:
        print(f"No results found for '{args.query}'")


def cmd_dict_list(args):
    """List all dictionary entries."""
    lexicon = Lexicon(filepath=Path(args.file))

    if not lexicon.filepath.exists():
        print(f"Dictionary file not found: {args.file}")
        sys.exit(1)

    entries = lexicon.list_all(sort_by=args.sort)

    if entries:
        print(f"Dictionary contains {len(entries)} entries:\n")
        for entry in entries:
            print(f"{entry.word} - {entry.gloss}")
            if args.verbose:
                if entry.root:
                    print(f"  Root: {entry.root}")
                if entry.notes:
                    print(f"  Notes: {entry.notes}")
                print()
    else:
        print("Dictionary is empty")


def cmd_dict_stats(args):
    """Show dictionary statistics."""
    lexicon = Lexicon(filepath=Path(args.file))

    if not lexicon.filepath.exists():
        print(f"Dictionary file not found: {args.file}")
        sys.exit(1)

    stats = lexicon.stats()

    print("Dictionary Statistics:")
    print(f"  Total entries: {stats['total_entries']}")
    print(f"  Content words: {stats['content_words']}")
    print(f"  Atomic words: {stats['atomic_words']}")
    print(f"  Unique roots: {stats['unique_roots']}")
    print(f"  Entries with examples: {stats['entries_with_examples']}")


def cmd_dict_export(args):
    """Export dictionary to CSV."""
    lexicon = Lexicon(filepath=Path(args.file))

    if not lexicon.filepath.exists():
        print(f"Dictionary file not found: {args.file}")
        sys.exit(1)

    lexicon.export_csv(Path(args.output))
    print(f"Exported {len(lexicon)} entries to {args.output}")


def cmd_dict_import(args):
    """Import dictionary from CSV."""
    lexicon = Lexicon(filepath=Path(args.file))

    count = lexicon.import_csv(Path(args.input), overwrite=args.overwrite)
    lexicon.save()
    print(f"Imported {count} entries from {args.input}")


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


def cmd_web(args):
    """Start the web server."""
    from .web import run_server

    print(f"Starting Conlang Explorer web interface...")
    print(f"Server running at http://{args.host}:{args.port}")
    print(f"Press Ctrl+C to stop")

    try:
        run_server(host=args.host, port=args.port)
    except KeyboardInterrupt:
        print("\nServer stopped.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description='Conlang development and practice tools',
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

    # Dictionary commands
    dict_parser = subparsers.add_parser('dict', help='Dictionary management')
    dict_subparsers = dict_parser.add_subparsers(dest='dict_command')

    # dict init
    dict_init = dict_subparsers.add_parser('init', help='Initialize new dictionary')
    dict_init.add_argument('-f', '--file', default='lexicon.json',
                          help='Dictionary file path')
    dict_init.add_argument('--load-roots', action='store_true',
                          help='Load core roots')
    dict_init.add_argument('--load-particles', action='store_true',
                          help='Load particle series')
    dict_init.set_defaults(func=cmd_dict_init)

    # dict add
    dict_add = dict_subparsers.add_parser('add', help='Add word to dictionary')
    dict_add.add_argument('word', help='Word to add')
    dict_add.add_argument('gloss', help='English translation')
    dict_add.add_argument('-f', '--file', default='lexicon.json',
                         help='Dictionary file path')
    dict_add.add_argument('-n', '--notes', help='Additional notes')
    dict_add.add_argument('-e', '--examples', nargs='*',
                         help='Example sentences')
    dict_add.add_argument('--overwrite', action='store_true',
                         help='Overwrite existing entry')
    dict_add.set_defaults(func=cmd_dict_add)

    # dict lookup
    dict_lookup = dict_subparsers.add_parser('lookup', help='Look up word')
    dict_lookup.add_argument('word', help='Word to look up')
    dict_lookup.add_argument('-f', '--file', default='lexicon.json',
                            help='Dictionary file path')
    dict_lookup.set_defaults(func=cmd_dict_lookup)

    # dict search
    dict_search = dict_subparsers.add_parser('search', help='Search dictionary')
    dict_search.add_argument('query', help='Search query')
    dict_search.add_argument('-f', '--file', default='lexicon.json',
                            help='Dictionary file path')
    dict_search.add_argument('--field', choices=['word', 'gloss', 'root', 'notes', 'all'],
                            default='all', help='Field to search')
    dict_search.add_argument('-v', '--verbose', action='store_true',
                            help='Show detailed information')
    dict_search.set_defaults(func=cmd_dict_search)

    # dict list
    dict_list = dict_subparsers.add_parser('list', help='List all entries')
    dict_list.add_argument('-f', '--file', default='lexicon.json',
                          help='Dictionary file path')
    dict_list.add_argument('--sort', choices=['word', 'gloss', 'root'],
                          default='word', help='Sort order')
    dict_list.add_argument('-v', '--verbose', action='store_true',
                          help='Show detailed information')
    dict_list.set_defaults(func=cmd_dict_list)

    # dict stats
    dict_stats = dict_subparsers.add_parser('stats', help='Show statistics')
    dict_stats.add_argument('-f', '--file', default='lexicon.json',
                           help='Dictionary file path')
    dict_stats.set_defaults(func=cmd_dict_stats)

    # dict export
    dict_export = dict_subparsers.add_parser('export', help='Export to CSV')
    dict_export.add_argument('-f', '--file', default='lexicon.json',
                            help='Dictionary file path')
    dict_export.add_argument('-o', '--output', required=True,
                            help='Output CSV file')
    dict_export.set_defaults(func=cmd_dict_export)

    # dict import
    dict_import = dict_subparsers.add_parser('import', help='Import from CSV')
    dict_import.add_argument('-f', '--file', default='lexicon.json',
                            help='Dictionary file path')
    dict_import.add_argument('-i', '--input', required=True,
                            help='Input CSV file')
    dict_import.add_argument('--overwrite', action='store_true',
                            help='Overwrite existing entries')
    dict_import.set_defaults(func=cmd_dict_import)

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

    # Web server command
    web_parser = subparsers.add_parser('web', help='Start web interface')
    web_parser.add_argument('--host', default='127.0.0.1',
                           help='Host to bind to (default: 127.0.0.1)')
    web_parser.add_argument('--port', type=int, default=8000,
                           help='Port to bind to (default: 8000)')
    web_parser.set_defaults(func=cmd_web)

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
