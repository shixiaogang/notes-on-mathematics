from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: quantile transform W = Q_W(U) for the running waiting time W.
# u = 0.2 lies inside the jump of F_W at 0, so Q_W(0.2) = 0; u = 0.37 gives Q_W(0.37) = ln(0.7/0.63) = ln(10/9).
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
for ax in (a, b): style(ax)
t = np.linspace(0, 2.5, 400)
a.plot([-0.5, 0], [0, 0], color=BLUE, lw=1.4, solid_capstyle='butt')
a.plot(t, F_W(t), color=BLUE, lw=1.4)
a.plot([0], [0], 'o', ms=3.4, mfc='white', mec=BLUE, mew=.9, zorder=5)
a.plot([0], [0.3], 'o', ms=3.4, color=BLUE, zorder=5)
q = float(np.log(0.7/0.63))
for u, x in ((0.2, 0.0), (0.37, q)):
    a.plot([-0.5, x], [u, u], color=GREEN, lw=1.0, ls='--')
    a.plot([x, x], [u, 0], color=GREEN, lw=1.0, ls='--')
    a.plot([x], [u], 'o', ms=3.6, color=RED, zorder=6)
a.text(-0.45, 0.2+0.025, '$u=0.2$', fontsize=7.5, color=INK)
a.text(-0.45, 0.37+0.025, '$u=0.37$', fontsize=7.5, color=INK)
a.set_xlim(-0.5, 2.5); a.set_ylim(-0.02, 1.02)
a.set_xticks([0, 1, 2]); a.set_yticks([0, 0.3, 0.6, 0.9])
a.set_ylabel('$F_W(t)$'); sub(a, 'a', '$t$')
u = np.linspace(0, 0.95, 500)
b.plot(u, Q_W(u), color=BLUE, lw=1.4)
b.plot([0.2, 0.37], [0, q], 'o', ms=3.6, color=RED, zorder=6)
b.annotate(r'$\ln(10/9)\approx0.105$', (0.37, q), (0.45, 0.75), fontsize=7.5, color=INK,
           arrowprops=dict(arrowstyle='-', color=LINE, lw=.7))
b.set_xlim(0, 1); b.set_ylim(-0.05, 3.0)
b.set_xticks([0, 0.3, 0.6, 0.9]); b.set_yticks([0, 1, 2, 3])
b.set_ylabel('$Q_W(u)$'); sub(b, 'b', '$u$')
assert abs(q-0.10536) < 1e-4
save(fig, HERE(__file__), 'figure', {'Q_W(0.2)': 0.0, 'Q_W(0.37)': q})
