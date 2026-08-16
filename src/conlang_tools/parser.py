"""Word parser and validator for the conlang."""

from dataclasses import dataclass
from typing import List, Optional
from .constants import (
    ATOMIC_WORDS, CONSONANTS, VOWELS, FINAL_CONSONANTS, PARTICLE_SERIES,
    DOMAINS, ASPECTS, HEAD_KINDS, cv_to_number
)


@dataclass
class ParseResult:
    """Result of parsing a word."""
    original: str
    word_type: str  # 'atomic' or 'content'
    is_valid: bool
    errors: List[str]

    # For atomic words
    particle_series: Optional[str] = None
    particle_meaning: Optional[tuple] = None
    numeric_value: Optional[int] = None

    # For content words
    prefixes: List[str] = None
    root: Optional[str] = None
    suffix: Optional[str] = None
    head_kind: Optional[str] = None

    # Root analysis
    domain: Optional[str] = None
    aspect: Optional[str] = None
    domain_name: Optional[str] = None
    aspect_name: Optional[str] = None

    def __post_init__(self):
        if self.prefixes is None:
            self.prefixes = []

    def __str__(self) -> str:
        """Human-readable representation of the parse result."""
        lines = [f"Word: {self.original}"]
        lines.append(f"Type: {self.word_type}")
        lines.append(f"Valid: {'✓' if self.is_valid else '✗'}")

        if self.errors:
            lines.append("Errors:")
            for error in self.errors:
                lines.append(f"  - {error}")

        if self.word_type == 'atomic':
            if self.particle_series:
                meaning, gloss = self.particle_meaning
                lines.append(f"Particle: {self.particle_series}-series ({meaning})")
                lines.append(f"Gloss: \"{gloss}\"")
            elif self.particle_meaning:
                meaning, gloss = self.particle_meaning
                lines.append(f"Fixed form: {meaning}")
                lines.append(f"Gloss: \"{gloss}\"")
            if self.numeric_value is not None:
                lines.append(f"Numeric value: {self.numeric_value}")

        elif self.word_type == 'content':
            if self.prefixes:
                lines.append(f"Prefixes: {'-'.join(self.prefixes)}")
            if self.root:
                lines.append(f"Root: {self.root}")
                if self.domain and self.aspect:
                    lines.append(f"  Domain: {self.domain} ({self.domain_name})")
                    lines.append(f"  Aspect: {self.aspect} ({self.aspect_name})")
            if self.suffix:
                head_kind, description = HEAD_KINDS[self.suffix]
                lines.append(f"Suffix: -{self.suffix} ({head_kind})")
                lines.append(f"  {description}")

        return '\n'.join(lines)


class WordParser:
    """Parser and validator for conlang words."""

    def __init__(self):
        self.consonants = set(CONSONANTS)
        self.vowels = set(VOWELS)
        self.final_consonants = set(FINAL_CONSONANTS)

    def parse(self, word: str) -> ParseResult:
        """Parse a word and return detailed analysis.

        Args:
            word: The word to parse (case-insensitive)

        Returns:
            ParseResult with complete analysis
        """
        original = word
        word = word.upper().strip()

        if not word:
            return ParseResult(
                original=original,
                word_type='unknown',
                is_valid=False,
                errors=['Empty word']
            )

        # Check if it's an atomic word (CV or known longer fixed form)
        if word in ATOMIC_WORDS:
            name, gloss = ATOMIC_WORDS[word]
            return ParseResult(
                original=original,
                word_type='atomic',
                is_valid=True,
                errors=[],
                particle_meaning=(name, gloss)
            )
        if len(word) == 2 and self._is_cv(word):
            return self._parse_atomic(word, original)

        # Otherwise try to parse as content word
        return self._parse_content(word, original)

    def _is_cv(self, s: str) -> bool:
        """Check if a string is a valid CV syllable."""
        return (len(s) == 2 and
                s[0] in self.consonants and
                s[1] in self.vowels)

    def _parse_atomic(self, word: str, original: str) -> ParseResult:
        """Parse an atomic (particle) word."""
        errors = []

        # Check if it's in a particle series
        particle_series = None
        particle_meaning = None
        for series_consonant, series_particles in PARTICLE_SERIES.items():
            if word in series_particles:
                particle_series = series_consonant
                particle_meaning = series_particles[word]
                break

        # Check if it's a numeric CV
        numeric_value = None
        try:
            numeric_value = cv_to_number(word)
        except ValueError:
            pass

        if not particle_series and numeric_value is None:
            errors.append(f"Unknown particle '{word}' (not in any defined series)")

        return ParseResult(
            original=original,
            word_type='atomic',
            is_valid=len(errors) == 0,
            errors=errors,
            particle_series=particle_series,
            particle_meaning=particle_meaning,
            numeric_value=numeric_value
        )

    def _parse_content(self, word: str, original: str) -> ParseResult:
        """Parse a content word."""
        errors = []

        # Check final character
        if word[-1] not in self.final_consonants:
            errors.append(
                f"Invalid final consonant '{word[-1]}'. "
                f"Must be one of: {', '.join(FINAL_CONSONANTS)}"
            )
            return ParseResult(
                original=original,
                word_type='content',
                is_valid=False,
                errors=errors
            )

        suffix = word[-1]

        # Extract root (must be exactly 4 characters: CVCV)
        if len(word) < 5:  # Need at least CVCV + suffix
            errors.append(f"Word too short. Need at least CVCV + suffix (5 chars)")
            return ParseResult(
                original=original,
                word_type='content',
                is_valid=False,
                errors=errors,
                suffix=suffix
            )

        root = word[-5:-1]  # 4 chars before suffix

        # Validate root structure: CVCV
        if not self._validate_root(root, errors):
            return ParseResult(
                original=original,
                word_type='content',
                is_valid=False,
                errors=errors,
                root=root,
                suffix=suffix
            )

        # Extract prefixes (everything before root)
        prefix_str = word[:-5]
        prefixes = []

        if prefix_str:
            # Parse prefixes (must be CV syllables)
            if len(prefix_str) % 2 != 0:
                errors.append(
                    f"Invalid prefix block '{prefix_str}': "
                    f"must be a sequence of CV syllables (even length)"
                )
            else:
                for i in range(0, len(prefix_str), 2):
                    prefix = prefix_str[i:i+2]
                    if not self._is_cv(prefix):
                        errors.append(
                            f"Invalid prefix '{prefix}': must be CV structure"
                        )
                    else:
                        prefixes.append(prefix)

        # Analyze root semantics
        v1, v2 = root[1], root[3]
        domain = v1
        aspect = v2
        domain_name = DOMAINS.get(domain, ('Unknown', ''))[0]
        aspect_name = ASPECTS.get(aspect, ('Unknown', ''))[0]

        return ParseResult(
            original=original,
            word_type='content',
            is_valid=len(errors) == 0,
            errors=errors,
            prefixes=prefixes,
            root=root,
            suffix=suffix,
            head_kind=HEAD_KINDS.get(suffix, ('Unknown', ''))[0],
            domain=domain,
            aspect=aspect,
            domain_name=domain_name,
            aspect_name=aspect_name
        )

    def _validate_root(self, root: str, errors: List[str]) -> bool:
        """Validate that root follows CVCV structure.

        Returns True if valid, False otherwise. Adds errors to the list.
        """
        if len(root) != 4:
            errors.append(f"Root must be exactly 4 characters (CVCV), got {len(root)}")
            return False

        c1, v1, c2, v2 = root

        valid = True
        if c1 not in self.consonants:
            errors.append(f"Root position 1: '{c1}' is not a valid consonant")
            valid = False
        if v1 not in self.vowels:
            errors.append(f"Root position 2: '{v1}' is not a valid vowel")
            valid = False
        if c2 not in self.consonants:
            errors.append(f"Root position 3: '{c2}' is not a valid consonant")
            valid = False
        if v2 not in self.vowels:
            errors.append(f"Root position 4: '{v2}' is not a valid vowel")
            valid = False

        return valid

    def validate(self, word: str) -> bool:
        """Quick validation check.

        Args:
            word: The word to validate

        Returns:
            True if the word is well-formed, False otherwise
        """
        result = self.parse(word)
        return result.is_valid

    def batch_parse(self, words: List[str]) -> List[ParseResult]:
        """Parse multiple words.

        Args:
            words: List of words to parse

        Returns:
            List of ParseResult objects
        """
        return [self.parse(word) for word in words]
