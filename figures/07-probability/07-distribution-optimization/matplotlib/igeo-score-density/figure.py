"""Scores of N(mu,sigma^2) at (0,1). Col (a): mean, s=x, perturbed N(0.4,1). Col (b): scale sigma, s=x^2-1, perturbed N(0,1.4^2).
Rows: densities; score s(x); derivative dp/dtheta = p*s with positive (blue) / negative (red) areas equal."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, axs = figure(width_mm=104, height_mm=72, ncols=2, nrows=3)
x = np.linspace(-4, 4, 800); p = npdf(x)
cols = [(x, npdf(x, 0.4, 1.0), r'$s_{\mu}(x)=x$'), (x*x-1, npdf(x, 0, 1.96), r'$s_{\sigma}(x)=x^{2}-1$')]
facts = {}
for j, (s, pert, lab) in enumerate(cols):
    a0, a1, a2 = axs[0, j], axs[1, j], axs[2, j]
    a0.plot(x, p, color=BLUE, lw=1.4); a0.plot(x, pert, color=YELLOW, lw=1.5)
    a0.set_ylim(0, 0.45); a0.set_yticks([0, 0.4])
    a1.axhline(0, color=STROKE, lw=0.6)
    a1.plot(x, s, color=STROKE, lw=1.3)
    a1.set_ylim(-3, 4.2); a1.set_yticks([-2, 0, 2, 4])
    a1.text(0.97, 0.08, lab, transform=a1.transAxes, va='bottom', ha='right', fontsize=7.5)
    d = p*s
    a2.fill_between(x, d, 0, where=d >= 0, color=BLUE_FILL, lw=0)
    a2.fill_between(x, d, 0, where=d < 0, color=RED_FILL, lw=0)
    a2.plot(x, d, color=BLUE, lw=1.2); a2.axhline(0, color=STROKE, lw=0.6)
    a2.set_ylim(-0.45, 0.32); a2.set_yticks([-0.4, 0, 0.2])
    for a in (a0, a1, a2):
        a.set_xlim(-4, 4); a.set_xticks([-3, 0, 3])
    a2.set_xlabel(r'$x$', labelpad=1)
    pos = float(np.trapezoid(np.where(d > 0, d, 0), x)); facts[f'pos_area_{j}'] = pos
    facts[f'total_{j}'] = float(np.trapezoid(d, x))
axs[0, 0].set_ylabel(r'$p$', labelpad=1); axs[1, 0].set_ylabel(r'$s$', labelpad=1); axs[2, 0].set_ylabel(r'$p\,s$', labelpad=1)
tag(axs[2, 0], '(a)', y=-0.66); tag(axs[2, 1], '(b)', y=-0.66)
save(fig, HERE, 'figure', facts)
