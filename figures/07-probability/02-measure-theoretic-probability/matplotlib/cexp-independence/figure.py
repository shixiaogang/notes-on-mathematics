"""Constant conditional mean does not imply independence. Simulation, seed 7, n=300 points (green).
(a) X~Unif(-1,1), Y=|X|: points (Y, X) lie on x=+-y; E[X|Y]=0 (red line), yet given Y=y, X=+-y.
(b) X~Unif(-1,1) independent of Z~Unif(0,1): points (Z, X) fill the rectangle; E[X|Z]=0 (red line)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

rng = np.random.default_rng(7)
n = 300
X = rng.uniform(-1, 1, n); Z = rng.uniform(0, 1, n)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2, sharey=True)
a.scatter(np.abs(X), X, s=2.5, color=GREEN, lw=0)
b.scatter(Z, X, s=2.5, color=GREEN, lw=0)
for ax in (a, b):
    ax.axhline(0, color=RED, lw=1.6)
    ax.set_xlim(0, 1); ax.set_ylim(-1.05, 1.05)
s = 0.7
a.plot([s, s], [-s, s], color=STROKE, lw=0.7, ls=':')
a.scatter([s, s], [-s, s], s=14, color=BLUE, zorder=4)
a.set_xlabel('$Y=|X|$', labelpad=1); a.set_ylabel('$X$')
b.set_xlabel('$Z$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'seed': 7, 'n': n, 'sample_mean_X': float(X.mean())})
