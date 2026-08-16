"""Ensure every local asset used by the guide is present in the repository tree."""

import re
from pathlib import Path


DOCS = Path(__file__).parent.parent / "docs"
GUIDE = (DOCS / "index.html").read_text(encoding="utf-8")
ILLUSTRATIONS = DOCS / "assets" / "illustrations"


def test_static_guide_asset_references_exist():
    refs = re.findall(
        r'(?:src|href)="([^"#]+\.(?:webp|png|jpg|svg))"',
        GUIDE,
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
