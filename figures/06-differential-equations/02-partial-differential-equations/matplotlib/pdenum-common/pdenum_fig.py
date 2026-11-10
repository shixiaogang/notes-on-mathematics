"""Shared helpers for chapter 6.13 figures: running examples and panel layout."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
STROKE = '#4C4D4F'
PI = np.pi
DASH = (0, (4, 2)); DOT = (0, (1.5, 1.8))
def panel(fig, left=.09, right=.985, top=.96, bottom=.26, wspace=.26):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def lab(ax, x, y, s, color=INK, **k):
    k.setdefault('fontsize', 7.5); ax.text(x, y, s, color=color, **k)
def uex(x):
    """Running Poisson example: -u''=pi^2 sin(pi x), u(0)=0, u(1)=1."""
    return np.sin(PI*x)+x
def lap1d(n):
    """Interior matrix tridiag(-1,2,-1)/h^2 on n cells of (0,1)."""
    h = 1/n
    return (2*np.eye(n-1)-np.eye(n-1, k=1)-np.eye(n-1, k=-1))/h**2
def burgers(u):
    return u*u/2
def godunov(a, b):
    if a <= b:
        return 0. if a <= 0 <= b else min(burgers(a), burgers(b))
    return max(burgers(a), burgers(b))
def roe(a, b):
    return burgers(a) if (a+b)/2 >= 0 else burgers(b)
def fv_step(U, lam, flux):
    """One conservative step with copied end states."""
    Up = np.r_[U[0], U, U[-1]]
    Fl = np.array([flux(Up[i], Up[i+1]) for i in range(len(Up)-1)])
    return U-lam*(Fl[1:]-Fl[:-1])
