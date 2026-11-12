"""Geom(0.2): (a) mass function; (b) tail P(T>k) and the conditional tail after m=5 failures."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

p, m = .2, 5
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
k = np.arange(1, 21)
bars(ax, k, p*(1-p)**(k-1), width=.6)
ax.plot([1/p], [-.008], marker='^', ms=6, color=RED, mew=0, clip_on=False, zorder=6)
lab(ax, 1/p+.3, .1, '均值 5', RED)
ax.set_xlim(0, 20.7); ax.set_ylim(0, .22); ax.set_xticks([1, 5, 10, 15, 20]); ax.set_yticks([0, .1, .2])
ax.set_xlabel('$k$', labelpad=1); ax.set_ylabel('$P(T=k)$', labelpad=1)
ax = axes[1]; style(ax)
kk = np.arange(0, 16)
G = (1-p)**kk
ax.plot(kk, G, color=BLUE, lw=1.4, marker='o', ms=3.2, mfc='white', mec=BLUE, mew=.9)
Gc = (1-p)**(m+kk)/(1-p)**m
ax.plot(kk, Gc, ls='none', marker='o', ms=1.8, color=GREEN)
lab(ax, 3.2, .62, r'$P(T>k)$', BLUE); lab(ax, 6.4, .3, r'$P(T>5+k\mid T>5)$', GREEN)
ax.set_xlim(0, 15); ax.set_ylim(0, 1.05); ax.set_xticks([0, 5, 10, 15]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$k$', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'P(T>5)': (1-p)**5, 'mean': 1/p, 'var': (1-p)/p**2})
