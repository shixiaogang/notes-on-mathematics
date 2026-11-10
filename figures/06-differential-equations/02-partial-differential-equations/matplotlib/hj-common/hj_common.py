"""Shared imports and exact formulas for the Hamilton-Jacobi figures (chapter 6.12)."""
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
DIVERGE = LinearSegmentedColormap.from_list('div', [RED, RED_FILL, '#FFFFFF', BLUE_FILL, BLUE])
def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)
def sub(ax, letter, xlabel=None):
    ax.set_xlabel((xlabel+'\n' if xlabel else '')+f'({letter})', linespacing=1.5)
def hopf_lax(x, t, u0, ys):
    """Hopf-Lax for H=p^2/2: min_y u0(y)+(x-y)^2/(2t); returns value and minimiser."""
    x = np.atleast_1d(x)
    F = u0(ys)[None, :] + (x[:, None]-ys[None, :])**2/(2*t)
    return F.min(1), ys[F.argmin(1)]
def cole_hopf(x, t, eps, u0, ys):
    """Exact viscous solution of u_t+u_x^2/2=eps u_xx via the Cole-Hopf integral."""
    x = np.atleast_1d(x)
    F = u0(ys)[None, :] + (x[:, None]-ys[None, :])**2/(2*t)
    m = F.min(1)
    dy = ys[1]-ys[0]
    return m - 2*eps*np.log(np.exp(-(F-m[:, None])/(2*eps)).sum(1)*dy/np.sqrt(4*np.pi*eps*t))
