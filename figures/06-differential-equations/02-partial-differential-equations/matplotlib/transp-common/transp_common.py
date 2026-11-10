"""Shared helpers for the transport-equation chapter figures (values computed from closed forms)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, configure, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, to_rgb
CHAR = '#4C4D4F'
CMAP = LinearSegmentedColormap.from_list('whiteblue', ['#FFFFFF', BLUE_FILL, BLUE])
DIV = LinearSegmentedColormap.from_list('redwhiteblue', [RED, '#FFFFFF', BLUE])
def tent(x, c=1.0, w=1.0):
    return np.maximum(0.0, 1.0-np.abs(x-c)/w)
def shades(n):
    a, b = np.array(to_rgb('#B7C4D3')), np.array(to_rgb('#4F6785'))
    return [tuple(a+(b-a)*(k/(max(n-1, 1)))) for k in range(n)]
def heat(ax, Z, xlim, tlim, vmin=0.0, vmax=1.0, cmap=CMAP):
    return ax.imshow(Z, extent=[xlim[0], xlim[1], tlim[0], tlim[1]], origin='lower', aspect='auto', cmap=cmap, vmin=vmin, vmax=vmax, interpolation='bilinear')
def tail(ax, xlabel, tag=None, ylabel=None):
    ax.set_xlabel(xlabel+('\n'+tag if tag else ''))
    if ylabel: ax.set_ylabel(ylabel)
