"""Borel-Kolmogorov paradox on the unit square. (a) band |Y-X|<=h, (b) wedge |Y/X-1|<=h, h=0.1 (drawn);
(c) simulation (seed 7, n=400000, h=0.02): histograms of X in band (green) and wedge (yellow); limits 1 and 2x."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
fig, (a, b, c) = figure(width_mm=112, height_mm=42, ncols=3)
h = 0.1
x = np.linspace(0, 1, 400)
a.fill_between(x, np.clip(x - h, 0, 1), np.clip(x + h, 0, 1), color=BLUE_FILL, lw=0)
b.fill_between(x, np.clip(x*(1 - h), 0, 1), np.clip(x*(1 + h), 0, 1), color=BLUE_FILL, lw=0)
for ax in (a, b):
    ax.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=0.85)
    ax.plot([0, 1], [0, 1], color=BLUE, lw=1.0)
    for sp in ax.spines.values(): sp.set_visible(False)
    ax.set_aspect('equal'); ax.set_xlim(-0.03, 1.03); ax.set_ylim(-0.03, 1.03)
    ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
a.set_ylabel('$y$', rotation=0, labelpad=2)
rng = np.random.default_rng(7)
n = 400000; hs = 0.02
P = rng.random((n, 2)); X, Y = P[:, 0], P[:, 1]
band = np.abs(Y - X) <= hs
wedge = np.abs(Y/X - 1) <= hs
bins = np.linspace(0, 1, 21)
c.hist(X[band], bins=bins, density=True, color=GREEN_FILL, edgecolor=GREEN, lw=0.6)
c.hist(X[wedge], bins=bins, density=True, histtype='step', color=YELLOW, lw=1.0)
c.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
c.plot([0, 1], [0, 2], color=YELLOW, lw=1.6)
c.set_xlim(0, 1); c.set_ylim(0, 2.2); c.set_xticks([0, 0.5, 1]); c.set_yticks([0, 1, 2]); c.set_xlabel('$x$', labelpad=0)
tags(fig, (a, b, c), ('(a)', '(b)', '(c)'))
save(fig, HERE, 'figure', {'h_drawn': h, 'seed': 7, 'n': n, 'h_sim': hs, 'band_count': int(band.sum()), 'wedge_count': int(wedge.sum())})
