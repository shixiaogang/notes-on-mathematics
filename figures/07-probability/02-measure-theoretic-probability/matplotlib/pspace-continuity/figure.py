from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common'))
from pspace_common import *
# Target: continuity of probability for the waiting time W (atom 0.3 at 0, density 0.7e^{-t} on t>0).
# Decreasing events {W <= 1/n} shrink to {W <= 0}: F_W(1/n) decreases to F_W(0) = 0.3.
# Increasing events {W <= -1/n} grow to {W < 0}: probabilities 0 increase to P(W < 0) = 0, the jump 0.3 is P(W = 0).
fig, (a, b) = plt_axes = figure(width_mm=112, height_mm=50, ncols=2)
for ax in (a, b): style(ax)
t = np.linspace(0.0, 1.6, 400)
a.plot([-0.6, 0], [0, 0], color=BLUE, lw=1.4, solid_capstyle='butt')
a.plot(t, F_W(t), color=BLUE, lw=1.4)
ns = np.arange(1, 9)
a.plot(1/ns, F_W(1/ns), 'o', ms=3.2, color=GREEN, zorder=4)
a.plot(-1/ns[:4], np.zeros(4), 'o', ms=3.2, color=GREEN, zorder=4)
a.plot([0], [0], 'o', ms=3.6, mfc='white', mec=BLUE, mew=.9, zorder=5)
a.plot([0], [0.3], 'o', ms=3.8, color=RED, zorder=5)
a.text(0.06, 0.3-0.02, '$F_W(0)=0.3$', fontsize=7.5, color=RED, va='top')
a.set_xlim(-0.6, 1.6); a.set_ylim(-0.03, 0.95)
a.set_xticks([-0.5, 0, 0.5, 1, 1.5]); a.set_yticks([0, 0.3, 0.6, 0.9])
a.set_ylabel('$F_W(t)$'); sub(a, 'a', '$t$')
vals = F_W(1/ns)
b.plot(ns, vals, 'o-', ms=3.2, color=GREEN, lw=1.0)
b.plot(ns, np.zeros_like(ns, float), 's-', ms=3.0, color=GREEN, lw=1.0, mfc='white')
b.axhline(0.3, color=PURPLE, lw=0.85, ls='--')
b.axhline(0.0, color=PURPLE, lw=0.85, ls='--')
b.text(8.15, vals[-1]+0.03, r'$P(W\leq 1/n)$', fontsize=7.5, color=INK, ha='right', va='bottom')
b.text(8.15, 0.04, r'$P(W\leq -1/n)$', fontsize=7.5, color=INK, ha='right', va='bottom')
b.set_xlim(0.5, 8.5); b.set_ylim(-0.03, 0.95)
b.set_xticks(ns); b.set_yticks([0, 0.3, 0.6, 0.9])
sub(b, 'b', '$n$')
assert abs(vals[0]-0.7425) < 1e-4 and abs(vals[-1]-0.3823) < 1e-4
save(fig, HERE(__file__), 'figure', {'F_W(1/n), n=1..8': [round(float(v), 4) for v in vals], 'limit': 0.3})
