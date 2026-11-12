from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# I = P(X>4), X ~ Exp(1).  (a) target density p(x)=e^{-x} (log scale), tail area shaded; five plain samples x=-ln u.
# (b) proposal q = Exp(1/4), q(x)=e^{-x/4}/4, with the same uniforms mapped by x=-4 ln u; samples beyond 4 carry
# weight w(x)=4 e^{-3x/4}.  Teaching uniforms u = 0.37, 0.81, 0.06, 0.52, 0.23.
x = np.linspace(0, 13, 600)
p = np.exp(-x); q = np.exp(-x/4)/4
xp = [-math.log(u) for u in U5]; xq = [-4*math.log(u) for u in U5]
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, right=.98, bottom=.26, top=.95, wspace=.22)
for ax in axs:
    ax.set_yscale('log'); ax.set_xlim(0, 13); ax.set_ylim(1e-5, 2); ax.set_xticks([0, 4, 8, 12])
    logticks(ax, [-4, -2, 0])
    m = x >= 4
    ax.fill_between(x[m], 1e-6, p[m], color=BLUE_FILL, lw=0)
    ax.plot(x, p, color=BLUE, lw=1.4)
    ax.axvline(4, color=RED, lw=1.2)
    axlab(ax, '$x$')
a, b = axs
tr = a.get_xaxis_transform()
for v in xp:
    a.plot([v, v], [0, .07], color=GREEN, lw=1.4, transform=tr)
lab(a, 0.5, 2e-3, r'$p(x)=\mathrm{e}^{-x}$', BLUE)
lab(a, 6.3, 5e-3, r'$I=\mathrm{e}^{-4}$', BLUE)
b.plot(x, q, color=YELLOW, lw=1.6)
tr = b.get_xaxis_transform()
for v in xq:
    hit = v > 4
    b.plot([v, v], [0, .07], color=GREEN if hit else MUTED, lw=1.4, transform=tr)
    if hit:
        b.text(v, .09, r'$%.3f$' % (4*math.exp(-.75*v)), color=GREEN, ha='center', fontsize=7.5, transform=tr)
lab(b, 0.5, 2e-3, r'$p$', BLUE)
lab(b, 6.0, .07, r'$q(x)=\frac{1}{4}\mathrm{e}^{-x/4}$', YELLOW)
tags(fig, axs)
save(fig, HERE, 'figure', {'plain_x': xp, 'is_x': xq, 'weights': [4*math.exp(-.75*v) for v in xq],
     'is_estimate_n5': sum(4*math.exp(-.75*v) for v in xq if v > 4)/5, 'I': math.exp(-4)})
