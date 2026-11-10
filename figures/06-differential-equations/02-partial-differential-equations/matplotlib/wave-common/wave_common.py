"""Shared imports, data and small helpers for the wave figures (chapter 6.9)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
from matplotlib.colors import LinearSegmentedColormap, TwoSlopeNorm
LINE = '#4C4D4F'
SHADES = ['#C3CEDA', '#9AACC0', '#7188A3', '#4F6580']
FIELD = LinearSegmentedColormap.from_list('field', ['#FFFFFF', BLUE_FILL, BLUE])
SIGNED = LinearSegmentedColormap.from_list('signed', [RED, RED_FILL, '#FFFFFF', BLUE_FILL, BLUE])
HERE = lambda f: Path(f).resolve().parent
def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)
def sub(ax, letter, xlabel=None):
    """Set the x label with the panel letter underneath it."""
    ax.set_xlabel((xlabel+'\n' if xlabel else '')+f'({letter})', linespacing=1.5)
def tent(x):
    """Running initial displacement T(x)=max(1-|x|,0)."""
    return np.maximum(1-np.abs(x), 0.)
def tent_d(x):
    """Derivative of the tent, 0 outside (-1,1)."""
    return np.where(np.abs(x)<1, -np.sign(x), 0.)
def box(x):
    """Running initial velocity, the indicator of (-1,1)."""
    return np.where(np.abs(x)<1, 1., 0.)
def wave_tent(x, t):
    return .5*(tent(x-t)+tent(x+t))
def wave_box(x, t):
    """Velocity contribution of d'Alembert's formula for the box with c=1."""
    return .5*(np.clip(x+t, -1, 1)-np.clip(x-t, -1, 1))
def pluck(x):
    return np.minimum(x, 1-x)
def pluck_ext(x):
    """Odd 2-periodic extension of the plucked shape min(x,1-x) on (0,1)."""
    y = np.mod(x, 2.)
    return np.where(y<=1, pluck(y), -pluck(y-1))
def pluck_wave(x, t):
    return .5*(pluck_ext(x-t)+pluck_ext(x+t))
def heat_tent(x, t):
    """Convolution of the tent with the heat kernel, by quadrature (diffusivity 1)."""
    y = np.linspace(-1, 1, 4001)
    x = np.asarray(x, float)
    t = np.asarray(t, float)[..., None]
    k = np.exp(-(x[..., None]-y)**2/(4*t))/np.sqrt(4*np.pi*t)
    return np.trapezoid(k*tent(y), y, axis=-1) if hasattr(np, 'trapezoid') else np.trapz(k*tent(y), y, axis=-1)
def field(ax, Z, ext, signed=False, vmax=None):
    v = vmax if vmax is not None else float(np.abs(Z).max())
    if signed:
        return ax.imshow(Z, origin='lower', extent=ext, aspect='auto', cmap=SIGNED, norm=TwoSlopeNorm(0, -v, v), interpolation='bilinear')
    return ax.imshow(Z, origin='lower', extent=ext, aspect='auto', cmap=FIELD, vmin=0, vmax=v, interpolation='bilinear')
