"""Shared helpers for chapter 5.19 figures: the budget quadratic and plotting conventions.
Budget example: min 0.5*||x-c||^2  s.t. x1+x2<=tau, x>=0 with default c=(2,1)."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, STROKE, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
C0 = np.array([2., 1.])
ACTIVE = '#4C4D4F'

def budget(tau, c=C0):
    """Exact solution for the 2-D budget problem. Returns x, (lam1, lam2, lam3)."""
    c = np.asarray(c, float)
    p = np.maximum(c, 0.0)
    if p.sum() <= tau:
        return p, (0.0, max(-c[0], 0.0), max(-c[1], 0.0))
    # project onto x1+x2=tau, x>=0
    lam = (c.sum()-tau)/2
    x = c-lam
    if x[1] < 0:
        x = np.array([tau, 0.]); lam = c[0]-tau
    elif x[0] < 0:
        x = np.array([0., tau]); lam = c[1]-tau
    return x, (lam, x[0]-c[0]+lam, x[1]-c[1]+lam)

def value(tau, c=C0):
    x, _ = budget(tau, c)
    return 0.5*np.sum((x-np.asarray(c))**2)

def opt_point(ax, p, ms=4.4, z=8):
    ax.plot([p[0]], [p[1]], 'o', color=RED, ms=ms, zorder=z)

def clean(ax, xlim=None, ylim=None, xlabel=None, ylabel=None, sub=None):
    if xlim: ax.set_xlim(*xlim)
    if ylim: ax.set_ylim(*ylim)
    x = xlabel or ''
    if sub:
        x = (x+'\n'+sub) if x else sub
    if x: ax.set_xlabel(x, labelpad=1)
    if ylabel: ax.set_ylabel(ylabel, labelpad=1)

def triangle(ax, tau, active=(), lw=1.6):
    """Draw the budget triangle with the listed active edges (1 budget, 2 x1=0, 3 x2=0)."""
    ax.fill([0, tau, 0], [0, 0, tau], facecolor=BLUE_FILL, edgecolor=BLUE, lw=0.9, zorder=1)
    if 1 in active: ax.plot([tau, 0], [0, tau], color=ACTIVE, lw=lw, zorder=4)
    if 2 in active: ax.plot([0, 0], [0, tau], color=ACTIVE, lw=lw, zorder=4)
    if 3 in active: ax.plot([0, tau], [0, 0], color=ACTIVE, lw=lw, zorder=4)

def circles(ax, c=C0, radii=(.5, 1, 1.5, 2, 2.5), lw=.7, zorder=2):
    t = np.linspace(0, 2*np.pi, 241)
    for r in radii:
        ax.plot(c[0]+r*np.cos(t), c[1]+r*np.sin(t), color=BLUE, lw=lw, zorder=zorder)
