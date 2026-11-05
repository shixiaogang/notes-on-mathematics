"""Resolve outputs of generators that serve several book parts."""
from functools import lru_cache
import json
from pathlib import Path

ROOT = next(p for p in Path(__file__).resolve().parents
            if (p / "build.sh").is_file() and (p / "tex/book.tex").is_file())


@lru_cache(maxsize=None)
def _catalog(directory):
    file = directory / "assets.json"
    return json.loads(file.read_text(encoding="utf-8")) if file.is_file() else {}


def asset_path(directory, filename):
    """Use a group's declared path, retaining local metadata beside its script."""
    directory = Path(directory).resolve()
    target = _catalog(directory).get(str(filename))
    path = ROOT / target if target else directory / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    return path
