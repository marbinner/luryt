"""Dictionary and lexicon management for the conlang."""

import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import List, Optional, Dict, Set
from .constants import CORE_ROOTS, PARTICLE_SERIES
from .parser import WordParser, ParseResult


@dataclass
class LexiconEntry:
    """An entry in the lexicon."""
    word: str  # The full word form
    gloss: str  # English translation/meaning
    root: Optional[str] = None  # The CVCV root (for content words)
    word_type: str = 'content'  # 'content' or 'atomic'
    notes: str = ''  # Additional notes
    examples: List[str] = None  # Example sentences

    def __post_init__(self):
        if self.examples is None:
            self.examples = []
        self.word = self.word.upper()
        if self.root:
            self.root = self.root.upper()

    def to_dict(self) -> Dict:
        """Convert to dictionary for JSON serialization."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict) -> 'LexiconEntry':
        """Create entry from dictionary."""
        return cls(**data)


class Lexicon:
    """Manages the vocabulary/dictionary."""

    def __init__(self, filepath: Optional[Path] = None):
        """Initialize lexicon.

        Args:
            filepath: Optional path to JSON file for persistent storage
        """
        self.filepath = filepath
        self.entries: Dict[str, LexiconEntry] = {}
        self.parser = WordParser()

        # Load from file if it exists
        if filepath and filepath.exists():
            self.load()

    def add(self, entry: LexiconEntry, overwrite: bool = False) -> bool:
        """Add an entry to the lexicon.

        Args:
            entry: The entry to add
            overwrite: If True, overwrite existing entry with same word

        Returns:
            True if added successfully, False if word already exists and overwrite=False
        """
        if entry.word in self.entries and not overwrite:
            return False

        self.entries[entry.word] = entry
        return True

    def add_word(self, word: str, gloss: str, notes: str = '',
                 examples: Optional[List[str]] = None, overwrite: bool = False) -> bool:
        """Convenience method to add a word.

        Args:
            word: The word form
            gloss: English translation
            notes: Additional notes
            examples: Example sentences
            overwrite: If True, overwrite existing entry

        Returns:
            True if added successfully
        """
        # Parse the word to extract root
        parse_result = self.parser.parse(word)

        entry = LexiconEntry(
            word=word,
            gloss=gloss,
            root=parse_result.root,
            word_type=parse_result.word_type,
            notes=notes,
            examples=examples or []
        )

        return self.add(entry, overwrite=overwrite)

    def get(self, word: str) -> Optional[LexiconEntry]:
        """Get an entry by word.

        Args:
            word: The word to look up (case-insensitive)

        Returns:
            The entry if found, None otherwise
        """
        return self.entries.get(word.upper())

    def search(self, query: str, field: str = 'all') -> List[LexiconEntry]:
        """Search the lexicon.

        Args:
            query: Search query (case-insensitive)
            field: Which field to search ('word', 'gloss', 'root', 'notes', or 'all')

        Returns:
            List of matching entries
        """
        query = query.lower()
        results = []

        for entry in self.entries.values():
            match = False

            if field in ('word', 'all'):
                if query in entry.word.lower():
                    match = True

            if field in ('gloss', 'all'):
                if query in entry.gloss.lower():
                    match = True

            if field in ('root', 'all') and entry.root:
                if query in entry.root.lower():
                    match = True

            if field in ('notes', 'all'):
                if query in entry.notes.lower():
                    match = True

            if match:
                results.append(entry)

        return results

    def get_by_root(self, root: str) -> List[LexiconEntry]:
        """Get all entries derived from a specific root.

        Args:
            root: The CVCV root (case-insensitive)

        Returns:
            List of entries with that root
        """
        root = root.upper()
        return [entry for entry in self.entries.values()
                if entry.root == root]

    def list_all(self, sort_by: str = 'word') -> List[LexiconEntry]:
        """Get all entries, sorted.

        Args:
            sort_by: Field to sort by ('word', 'gloss', or 'root')

        Returns:
            Sorted list of all entries
        """
        entries = list(self.entries.values())

        if sort_by == 'word':
            return sorted(entries, key=lambda e: e.word)
        elif sort_by == 'gloss':
            return sorted(entries, key=lambda e: e.gloss.lower())
        elif sort_by == 'root':
            return sorted(entries, key=lambda e: e.root or '')
        else:
            return entries

    def remove(self, word: str) -> bool:
        """Remove an entry.

        Args:
            word: The word to remove (case-insensitive)

        Returns:
            True if removed, False if not found
        """
        word = word.upper()
        if word in self.entries:
            del self.entries[word]
            return True
        return False

    def load_core_roots(self, suffixes: Optional[List[str]] = None) -> int:
        """Load core roots from the spec as lexicon entries.

        Args:
            suffixes: List of suffixes to generate (default: ['M', 'N', 'S'])

        Returns:
            Number of entries added
        """
        if suffixes is None:
            suffixes = ['M', 'N', 'S']  # Entity, Event, Property

        count = 0
        for root, info in CORE_ROOTS.items():
            for suffix in suffixes:
                word = root + suffix
                self.add_word(
                    word=word,
                    gloss=info['gloss'],
                    notes=f"Core root - Domain: {info['domain']}, Aspect: {info['aspect']}",
                    overwrite=False
                )
                count += 1

        return count

    def load_particles(self) -> int:
        """Load all particle series as lexicon entries.

        Returns:
            Number of entries added
        """
        count = 0
        for series_name, particles in PARTICLE_SERIES.items():
            for particle, (meaning, gloss) in particles.items():
                self.add_word(
                    word=particle,
                    gloss=gloss,
                    notes=f"{series_name}-series: {meaning}",
                    overwrite=False
                )
                count += 1

        return count

    def save(self, filepath: Optional[Path] = None) -> None:
        """Save lexicon to JSON file.

        Args:
            filepath: Path to save to (uses self.filepath if not provided)
        """
        filepath = filepath or self.filepath
        if not filepath:
            raise ValueError("No filepath specified for saving")

        filepath = Path(filepath)
        filepath.parent.mkdir(parents=True, exist_ok=True)

        data = {
            'entries': [entry.to_dict() for entry in self.entries.values()]
        }

        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load(self, filepath: Optional[Path] = None) -> None:
        """Load lexicon from JSON file.

        Args:
            filepath: Path to load from (uses self.filepath if not provided)
        """
        filepath = filepath or self.filepath
        if not filepath:
            raise ValueError("No filepath specified for loading")

        filepath = Path(filepath)
        if not filepath.exists():
            return

        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.entries = {}
        for entry_dict in data.get('entries', []):
            entry = LexiconEntry.from_dict(entry_dict)
            self.entries[entry.word] = entry

    def export_csv(self, filepath: Path) -> None:
        """Export lexicon to CSV file.

        Args:
            filepath: Path to save CSV file
        """
        import csv

        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Word', 'Gloss', 'Root', 'Type', 'Notes', 'Examples'])

            for entry in self.list_all():
                writer.writerow([
                    entry.word,
                    entry.gloss,
                    entry.root or '',
                    entry.word_type,
                    entry.notes,
                    ' | '.join(entry.examples)
                ])

    def import_csv(self, filepath: Path, overwrite: bool = False) -> int:
        """Import lexicon from CSV file.

        Args:
            filepath: Path to CSV file
            overwrite: Whether to overwrite existing entries

        Returns:
            Number of entries imported
        """
        import csv

        count = 0
        with open(filepath, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                examples = row.get('Examples', '').split(' | ') if row.get('Examples') else []
                examples = [ex for ex in examples if ex]  # Filter empty strings

                entry = LexiconEntry(
                    word=row['Word'],
                    gloss=row['Gloss'],
                    root=row.get('Root') or None,
                    word_type=row.get('Type', 'content'),
                    notes=row.get('Notes', ''),
                    examples=examples
                )

                if self.add(entry, overwrite=overwrite):
                    count += 1

        return count

    def stats(self) -> Dict:
        """Get statistics about the lexicon.

        Returns:
            Dictionary with various stats
        """
        total = len(self.entries)
        content_words = sum(1 for e in self.entries.values() if e.word_type == 'content')
        atomic_words = sum(1 for e in self.entries.values() if e.word_type == 'atomic')

        roots: Set[str] = set()
        for entry in self.entries.values():
            if entry.root:
                roots.add(entry.root)

        return {
            'total_entries': total,
            'content_words': content_words,
            'atomic_words': atomic_words,
            'unique_roots': len(roots),
            'entries_with_examples': sum(1 for e in self.entries.values() if e.examples)
        }

    def __len__(self) -> int:
        """Return number of entries."""
        return len(self.entries)

    def __contains__(self, word: str) -> bool:
        """Check if word is in lexicon."""
        return word.upper() in self.entries
