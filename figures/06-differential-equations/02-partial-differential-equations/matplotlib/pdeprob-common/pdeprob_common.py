"""Shared imports and small helpers for the pdeprob figures (chapter 6.6)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap
LINE = '#4C4D4F'
SHADES = ['#C3CEDA', '#9AACC0', '#7188A3', '#4F6580']
FIELD = LinearSegmentedColormap.from_list('field', ['#FFFFFF', BLUE_FILL, BLUE])
def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)
def sub(ax, letter, xlabel=None):
    """Set the x label with the panel letter underneath it."""
    ax.set_xlabel((xlabel+'\n' if xlabel else '')+f'({letter})', linespacing=1.5)
