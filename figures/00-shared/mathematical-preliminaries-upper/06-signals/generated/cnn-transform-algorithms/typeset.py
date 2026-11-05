"""Replay actual-font labels over the archived model background only."""
from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file())
B=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'figures/00-shared/mathematical-generators/generated/typography'))
from render_labels import render
if __name__=='__main__': render(str(B))
