"""FastAPI web server for conlang tools."""

from pathlib import Path
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse
from pydantic import BaseModel

from .parser import WordParser, ParseResult
from .lexicon import Lexicon, LexiconEntry
from .constants import (
    PARTICLE_SERIES, CORE_ROOTS, HEAD_KINDS, DOMAINS, ASPECTS,
    CONSONANTS, VOWELS, number_to_cv, cv_to_number
)

# Initialize app
app = FastAPI(title="Conlang Tools API", version="0.1.0")

# Initialize services
parser = WordParser()
lexicon = Lexicon()

# Load core content into lexicon
lexicon.load_core_roots()
lexicon.load_particles()


# Request/Response models
class ParseRequest(BaseModel):
    word: str


class ParseResponse(BaseModel):
    original: str
    word_type: str
    is_valid: bool
    errors: List[str]
    particle_series: Optional[str] = None
    particle_meaning: Optional[tuple] = None
    numeric_value: Optional[int] = None
    prefixes: List[str] = []
    root: Optional[str] = None
    suffix: Optional[str] = None
    head_kind: Optional[str] = None
    domain: Optional[str] = None
    aspect: Optional[str] = None
    domain_name: Optional[str] = None
    aspect_name: Optional[str] = None


class NumberRequest(BaseModel):
    value: int


class CVRequest(BaseModel):
    cv: str


class SearchRequest(BaseModel):
    query: str
    field: str = "all"


class AddWordRequest(BaseModel):
    word: str
    gloss: str
    notes: str = ""
    examples: List[str] = []


# API Endpoints

@app.get("/")
async def root():
    """Serve the main HTML page."""
    html_file = Path(__file__).parent / "static" / "index.html"
    if html_file.exists():
        return FileResponse(html_file)
    return {"message": "Conlang Tools API"}


@app.post("/api/parse", response_model=ParseResponse)
async def parse_word(request: ParseRequest):
    """Parse a word and return detailed analysis."""
    result = parser.parse(request.word)

    return ParseResponse(
        original=result.original,
        word_type=result.word_type,
        is_valid=result.is_valid,
        errors=result.errors,
        particle_series=result.particle_series,
        particle_meaning=result.particle_meaning,
        numeric_value=result.numeric_value,
        prefixes=result.prefixes or [],
        root=result.root,
        suffix=result.suffix,
        head_kind=result.head_kind,
        domain=result.domain,
        aspect=result.aspect,
        domain_name=result.domain_name,
        aspect_name=result.aspect_name
    )


@app.get("/api/particles")
async def get_particles():
    """Get all particle series."""
    result = {}
    for series_name, particles in PARTICLE_SERIES.items():
        result[series_name] = {
            particle: {"meaning": meaning, "gloss": gloss}
            for particle, (meaning, gloss) in particles.items()
        }
    return result


@app.get("/api/particles/{series}")
async def get_particle_series(series: str):
    """Get a specific particle series."""
    series = series.upper()
    if series not in PARTICLE_SERIES:
        raise HTTPException(status_code=404, detail=f"Series {series} not found")

    particles = PARTICLE_SERIES[series]
    return {
        "series": series,
        "particles": {
            particle: {"meaning": meaning, "gloss": gloss}
            for particle, (meaning, gloss) in particles.items()
        }
    }


@app.get("/api/roots")
async def get_roots():
    """Get all core roots."""
    return {
        root: {
            "domain": info["domain"],
            "aspect": info["aspect"],
            "gloss": info["gloss"],
            "domain_name": DOMAINS[info["domain"]][0],
            "aspect_name": ASPECTS[info["aspect"]][0]
        }
        for root, info in CORE_ROOTS.items()
    }


@app.get("/api/suffixes")
async def get_suffixes():
    """Get all final suffixes."""
    return {
        suffix: {"kind": kind, "description": desc}
        for suffix, (kind, desc) in HEAD_KINDS.items()
    }


@app.get("/api/domains")
async def get_domains():
    """Get all semantic domains."""
    return {
        vowel: {"name": name, "description": desc}
        for vowel, (name, desc) in DOMAINS.items()
    }


@app.get("/api/aspects")
async def get_aspects():
    """Get all semantic aspects."""
    return {
        vowel: {"name": name, "description": desc}
        for vowel, (name, desc) in ASPECTS.items()
    }


@app.post("/api/number-to-cv")
async def convert_number_to_cv(request: NumberRequest):
    """Convert a number to CV syllable."""
    try:
        cv = number_to_cv(request.value)
        return {"number": request.value, "cv": cv}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/cv-to-number")
async def convert_cv_to_number(request: CVRequest):
    """Convert a CV syllable to number."""
    try:
        number = cv_to_number(request.cv)
        return {"cv": request.cv.upper(), "number": number}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/dictionary")
async def get_dictionary(sort_by: str = "word", limit: int = 100):
    """Get dictionary entries."""
    entries = lexicon.list_all(sort_by=sort_by)

    # Limit results
    entries = entries[:limit]

    return {
        "total": len(lexicon),
        "returned": len(entries),
        "entries": [
            {
                "word": entry.word,
                "gloss": entry.gloss,
                "root": entry.root,
                "word_type": entry.word_type,
                "notes": entry.notes,
                "examples": entry.examples
            }
            for entry in entries
        ]
    }


@app.post("/api/dictionary/search")
async def search_dictionary(request: SearchRequest):
    """Search the dictionary."""
    results = lexicon.search(request.query, field=request.field)

    return {
        "query": request.query,
        "field": request.field,
        "count": len(results),
        "results": [
            {
                "word": entry.word,
                "gloss": entry.gloss,
                "root": entry.root,
                "word_type": entry.word_type,
                "notes": entry.notes,
                "examples": entry.examples
            }
            for entry in results
        ]
    }


@app.get("/api/dictionary/{word}")
async def get_dictionary_entry(word: str):
    """Get a specific dictionary entry."""
    entry = lexicon.get(word)
    if not entry:
        raise HTTPException(status_code=404, detail=f"Word '{word}' not found")

    return {
        "word": entry.word,
        "gloss": entry.gloss,
        "root": entry.root,
        "word_type": entry.word_type,
        "notes": entry.notes,
        "examples": entry.examples
    }


@app.post("/api/dictionary")
async def add_dictionary_entry(request: AddWordRequest):
    """Add a word to the dictionary."""
    success = lexicon.add_word(
        word=request.word,
        gloss=request.gloss,
        notes=request.notes,
        examples=request.examples,
        overwrite=False
    )

    if not success:
        raise HTTPException(
            status_code=409,
            detail=f"Word '{request.word}' already exists"
        )

    return {"success": True, "word": request.word.upper()}


@app.get("/api/stats")
async def get_stats():
    """Get dictionary and language statistics."""
    stats = lexicon.stats()

    return {
        "dictionary": stats,
        "phonology": {
            "consonants": len(CONSONANTS),
            "vowels": len(VOWELS),
            "particle_series": len(PARTICLE_SERIES),
            "core_roots": len(CORE_ROOTS)
        }
    }


@app.get("/api/random-word")
async def get_random_word():
    """Get a random word from the dictionary."""
    import random

    if len(lexicon) == 0:
        raise HTTPException(status_code=404, detail="Dictionary is empty")

    entries = list(lexicon.entries.values())
    entry = random.choice(entries)

    return {
        "word": entry.word,
        "gloss": entry.gloss,
        "root": entry.root,
        "word_type": entry.word_type,
        "notes": entry.notes,
        "examples": entry.examples
    }


# Mount static files
static_dir = Path(__file__).parent / "static"
if static_dir.exists():
    app.mount("/static", StaticFiles(directory=str(static_dir)), name="static")


def run_server(host: str = "127.0.0.1", port: int = 8000):
    """Run the web server."""
    import uvicorn
    uvicorn.run(app, host=host, port=port)


if __name__ == "__main__":
    run_server()
