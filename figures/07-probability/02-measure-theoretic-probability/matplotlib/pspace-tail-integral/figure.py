from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: E[W] computed two ways for the running waiting time W = Q_W(U) on Omega=[0,1).
# (a) region {(u,t): 0 <= t < Q_W(u)}; integrating over t first gives Q_W(u), over u first gives P(W>t).
# (b) survival P(W>t) = 0.7 e^{-t} for t >= 0; both areas equal E[W] = 0.7.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
for ax in (a, b): style(ax)
u = np.linspace(0, 0.999, 3000)
q = Q_W(u)
a.fill_between(u, 0, q, color=BLUE_FILL, lw=0)
a.plot(u, q, color=BLUE, lw=1.4)
t0 = 1.0; u0 = 1-0.7*np.exp(-t0)
a.plot([u0, 1], [t0, t0], color=RED, lw=2.0, solid_capstyle='butt')
a.text(0.02, t0+0.08, '$t=1$', fontsize=7.5, color=INK)
a.set_xlim(0, 1); a.set_ylim(0, 3.2); a.set_xticks([0, 0.3, 1]); a.set_yticks([0, 1, 2, 3])
a.set_ylabel('$t$'); sub(a, 'a', '$u$')
t = np.linspace(0, 4, 400)
s = 0.7*np.exp(-t)
b.fill_between(t, 0, s, color=BLUE_FILL, lw=0)
b.plot(t, s, color=BLUE, lw=1.4)
b.plot([-0.5, 0], [1, 1], color=BLUE, lw=1.4)
b.plot([0], [1], 'o', ms=3.2, mfc='white', mec=BLUE, mew=.9, zorder=5); b.plot([0], [0.7], 'o', ms=3.2, color=BLUE, zorder=5)
b.plot([1, 1], [0, 0.7*np.exp(-1)], color=RED, lw=2.0, solid_capstyle='butt')
b.set_xlim(-0.5, 4); b.set_ylim(0, 1.08); b.set_xticks([0, 1, 2, 3, 4]); b.set_yticks([0, 0.7, 1])
b.set_ylabel(r'$P(W>t)$'); sub(b, 'b', '$t$')
area = float(np.trapezoid(s, t)) + 0.7*np.exp(-4)
assert abs(area-0.7) < 1e-3
save(fig, HERE(__file__), 'figure', {'E[W]': 0.7, 'P(W>1)': 0.7*np.exp(-1)})
