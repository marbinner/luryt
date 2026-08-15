"""Conlang Tools - Development and practice tools for the constructed language."""

from .parser import WordParser, ParseResult
from .lexicon import Lexicon, LexiconEntry

__version__ = "0.1.0"

__all__ = ["WordParser", "ParseResult", "Lexicon", "LexiconEntry"]
