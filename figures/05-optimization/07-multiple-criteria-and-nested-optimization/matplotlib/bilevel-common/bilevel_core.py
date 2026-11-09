"""Shared helpers for chapter 5.28 (bilevel optimization).
Running example: inner g(x,y)=0.5(y-3)^2+0.5*x*y^2, outer F=0.5(y-1)^2, y*(x)=3/(1+x).
Inner gradient descent: alpha=1/2, y^(0)=0, so y^(T)=y*(1-q^T), q=(1-x)/2."""
from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, STROKE, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
ACTIVE = '#4C4D4F'
def ystar(x): return 3/(1+x)
def yT(x, T):
    q = (1-x)/2
    return ystar(x)*(1-q**T)
def Phi(x): return .5*(ystar(x)-1)**2
def clean(ax, xlim, ylim, xlabel=None, ylabel=None):
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    if xlabel: ax.set_xlabel(xlabel, labelpad=1.5)
    if ylabel: ax.set_ylabel(ylabel, labelpad=1.5)
    ax.tick_params(length=2.2, width=.7, pad=1.8)
    ax.grid(False)
def tag(ax, s, y=-.3):
    ax.text(.5, y, s, transform=ax.transAxes, ha='center', va='top', fontsize=8, color=INK)
