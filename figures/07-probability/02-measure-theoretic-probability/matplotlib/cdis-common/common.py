"""Shared helpers for the conditional-distribution figures (chapter 7.11).

Running examples (all exact formulas, no hand-entered data):
- triangle model: (X,Y) uniform on {0<=y<=x<=1}; given Y=y, X ~ Unif(y,1); f_Y(y)=2(1-y);
- random coin: U ~ Unif(0,1), given U=u the flips are iid Bern(u).
"""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
DASH = (0, (4, 2))

def tag(ax, s, y=-0.30):
    ax.text(0.5, y, s, transform=ax.transAxes, ha='center', va='top')

def tri_kernel(y, a, b):
    """K(y,[a,b]) for the triangle model: length of [a,b] within [y,1] divided by 1-y."""
    y = np.asarray(y, dtype=float)
    lo = np.maximum(a, y); hi = np.minimum(b, 1.0)
    return np.clip(hi - lo, 0, None)/(1 - y)

def tags(fig, axes, labels, reserve_mm=5.2, pad_mm=0.8):
    """Place (a),(b),... centred under each axes on one common baseline near the bottom edge."""
    H = fig.get_figheight()*25.4
    fig.get_layout_engine().set(rect=(0, reserve_mm/H, 1, 1 - reserve_mm/H))
    fig.canvas.draw()
    for ax, s in zip(axes, labels):
        p = ax.get_position()
        fig.text((p.x0 + p.x1)/2, pad_mm/H, s, ha='center', va='bottom')
