"""Ensure every local asset used by the guide is present in the repository tree."""

import re
from pathlib import Path


DOCS = Path(__file__).parent.parent / "docs"
GUIDE_HTML = (DOCS / "index.html").read_text(encoding="utf-8")
GUIDE_SCRIPT = (DOCS / "assets" / "js" / "guide.mjs").read_text(encoding="utf-8")
GUIDE = GUIDE_HTML + "\n" + GUIDE_SCRIPT
ILLUSTRATIONS = DOCS / "assets" / "illustrations"


def test_static_guide_asset_references_exist():
    refs = re.findall(
        r'(?:src|href)="([^"#]+\.(?:webp|png|jpg|svg))"',
        GUIDE_HTML,
        flags=re.IGNORECASE,
    )
    local_refs = [ref for ref in refs if not ref.startswith(("http://", "https://", "data:"))]
    missing = [ref for ref in local_refs if not (DOCS / ref).is_file()]
    assert local_refs
    assert not missing, f"guide references missing local assets: {missing}"


def test_javascript_generated_illustrations_exist():
    names = set(re.findall(r'([a-z][a-z0-9_-]+\.(?:webp|png|jpg))', GUIDE))
    if "scene-domain-${v}.webp" in GUIDE:
        names.update(f"scene-domain-{v}.webp" for v in "iyeaou")
    missing = sorted(name for name in names if not (ILLUSTRATIONS / name).is_file())
    assert names
    assert not missing, f"guide generates references to missing illustrations: {missing}"


def test_dictionary_local_assets_exist():
    page = DOCS / "dictionary" / "index.html"
    html = page.read_text(encoding="utf-8")
    refs = re.findall(
        r'(?:src|href)="([^"#]+\.(?:css|mjs|json|svg))"',
        html,
        flags=re.IGNORECASE,
    )
    local_refs = [ref for ref in refs if not ref.startswith(("http://", "https://", "data:"))]
    missing = [ref for ref in local_refs if not (page.parent / ref).resolve().is_file()]
    assert local_refs
    assert not missing, f"dictionary references missing local assets: {missing}"


def test_guide_particle_gallery_covers_every_series():
    """A data-defined series must render in the guide's particle chapter.

    The chapter's layout comes from the hand-maintained SERIES_ORDER and
    SERIES_UI maps in guide.mjs; nothing else fails when a newly adopted
    series is missing from them (the F-series was invisible until a docs
    pass caught it).
    """
    import json

    data = json.loads((DOCS / "data" / "language.json").read_text(encoding="utf-8"))
    defined = {c.lower() for c in data["particle_series"]}
    order = re.search(r'const SERIES_ORDER = "([a-z]+)";', GUIDE_SCRIPT).group(1)
    assert len(order) == len(set(order))
    assert set(order) == defined, (
        f"guide SERIES_ORDER covers {sorted(set(order))} but the language defines {sorted(defined)}"
    )
    for c in sorted(defined):
        assert re.search(rf"^  {c}:\{{grp:", GUIDE_SCRIPT, flags=re.M), (
            f"SERIES_UI has no entry for the {c.upper()}-series"
        )
