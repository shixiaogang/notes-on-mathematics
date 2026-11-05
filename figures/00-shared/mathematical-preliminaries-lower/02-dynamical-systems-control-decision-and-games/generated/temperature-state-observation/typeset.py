from pathlib import Path
import sys
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/mathematical-generators/generated/typography'))
import typeset_common
# Explicit STIX alias covers individually tagged mathcal 𝒞/ℋ/𝒦/ℰ/ℳ missing from the actual Fira Math cmap.
# Current temperature labels contain none of these; retain the alias for shared renderer cmap initialization.
typeset_common.FONT_FILES['stix-missing']='STIXTwoMath-Regular.otf'
from render_labels import render
render(Path(__file__).resolve().parent)
