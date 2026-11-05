"""Replay only real-font text composition over the retained final background."""
from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/mathematical-generators/generated/typography'))
from render_labels import render
render(str(Path(__file__).resolve().parent))
