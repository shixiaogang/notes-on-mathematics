"""Shared helpers for the chapter 6.11 (scalar conservation laws) figures."""
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
HERE = lambda f: Path(f).resolve().parent
TSTAR = 8*np.sqrt(3)/9
XSTAR = np.sqrt(3)
def style(ax):
    for s in ax.spines.values():
        s.set_linewidth(.95)
    ax.tick_params(width=.85, length=2.5)
def sub(ax, letter, xlabel=None):
    """Set the x label with the panel letter underneath it."""
    ax.set_xlabel((xlabel+'\n' if xlabel else '')+f'({letter})', linespacing=1.5)
def bump(x):
    return 1/(1+x**2)
def dbump(x):
    return -2*x/(1+x**2)**2
def ramp(x):
    return np.where(x < 0, 1.0, np.where(x > 1, 0.0, 1-x))

GRID0 = np.concatenate([np.linspace(-60, -6, 3000, endpoint=False), np.linspace(-6, 8, 60000, endpoint=False), np.linspace(8, 400, 12000)])
def branches(t):
    """Return grid indices (il, ir) that bound the folded part of x0 -> x0+t u0(x0) for the bump datum."""
    G1 = 1+t*dbump(GRID0)
    neg = np.where(G1 < 0)[0]
    if len(neg) == 0:
        return None
    return neg[0], neg[-1]
def bump_shock(tmax, dt=2e-3):
    """Track the shock of Burgers with the bump datum by integrating s=(u_-+u_+)/2 from the break point."""
    t = TSTAR+1e-5
    g = XSTAR+.75*1e-5
    T, Xs, UL, UR = [TSTAR], [XSTAR], [.75], [.75]
    def state(t, g):
        il, ir = branches(t)
        X = GRID0+t*bump(GRID0)
        xl = np.interp(g, X[:il+1], GRID0[:il+1]) if g >= X[0] else GRID0[0]
        xr = np.interp(g, X[ir:], GRID0[ir:])
        return xl, xr
    while t < tmax:
        def rhs(t, g):
            xl, xr = state(t, g)
            return .5*(bump(xl)+bump(xr))
        k1 = rhs(t, g); k2 = rhs(t+dt/2, g+dt/2*k1); k3 = rhs(t+dt/2, g+dt/2*k2); k4 = rhs(t+dt, g+dt*k3)
        g += dt*(k1+2*k2+2*k3+k4)/6
        t += dt
        xl, xr = state(t, g)
        T.append(t); Xs.append(g); UL.append(bump(xl)); UR.append(bump(xr))
    return np.array(T), np.array(Xs), np.array(UL), np.array(UR)
def bump_profile(x, t, T, Xs):
    """Single-valued entropy profile of the bump datum at time t (x an increasing array)."""
    X = GRID0+t*bump(GRID0)
    br = branches(t)
    if br is None:
        return bump(np.interp(x, X, GRID0))
    il, ir = br
    g = np.interp(t, T, Xs)
    return np.where(x < g, bump(np.interp(x, X[:il+1], GRID0[:il+1])), bump(np.interp(x, X[ir:], GRID0[ir:])))
def godunov_step(u, h, tau, flux):
    uL, uR = u[:-1], u[1:]
    F = flux(uL, uR)
    v = u.copy()
    v[1:-1] -= tau/h*(F[1:]-F[:-1])
    return v
def godunov_burgers_flux(a, b):
    return np.maximum(.5*np.maximum(a, 0)**2, .5*np.minimum(b, 0)**2)
