from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Event frequency as Monte Carlo area: U, V independent Unif(0,1); event A = {U^2 + V^2 <= 1}, P(A) = pi/4.
# (a) first 400 points of one sample (seed 31): inside A green, outside grey; quarter circle blue.
# (b) 4 x frequency of A for five independent runs (seeds 31..35), n <= 10^4, log x-axis; pi as blue line.
N = 10**4
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2, gridspec_kw={'width_ratios': [1, 1.5]})
panel(fig, left=.06, right=.97, bottom=.26, wspace=.25)
runs = []
for sd in range(31, 36):
    r = np.random.default_rng(sd); U = r.random((N, 2)); ins = (U**2).sum(1) <= 1; runs.append((U, ins))
U, ins = runs[0]
a.plot(U[:400][ins[:400], 0], U[:400][ins[:400], 1], 'o', ms=1.8, color=GREEN, mew=0)
a.plot(U[:400][~ins[:400], 0], U[:400][~ins[:400], 1], 'o', ms=1.8, color=MUTED, mew=0)
t = np.linspace(0, np.pi/2, 200); a.plot(np.cos(t), np.sin(t), color=BLUE, lw=1.3)
a.set_xlim(0, 1); a.set_ylim(0, 1); a.set_aspect('equal'); a.set_xticks([0, 1]); a.set_yticks([0, 1])
n = np.arange(1, N+1)
for U_, ins_ in runs: b.plot(n, 4*np.cumsum(ins_)/n, color=GREEN, lw=.8)
b.axhline(np.pi, color=BLUE, lw=1.2); lab(b, 3e3, 2.95, r'$\pi$', BLUE)
b.set_xscale('log'); b.set_xlim(1, N); logticks(b, [0, 1, 2, 3, 4], 'x'); b.set_ylim(2.4, 4.05); axlab(b, '$n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'inside_first_400': int(ins[:400].sum()), 'est_400': float(4*ins[:400].mean()),
     'final_estimates': [float(4*i.mean()) for _, i in runs]})
