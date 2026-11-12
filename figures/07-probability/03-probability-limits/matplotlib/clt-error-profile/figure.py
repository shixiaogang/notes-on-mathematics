from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Signed error P(Z_n <= z) - Phi(z) of the standardized sum, as a function of the threshold z.
# (a) Exp(1) steps, n = 10 (exact Erlang distribution function): smooth, skewness-driven;
# (b) Bern(1/2) steps, n = 20 (exact binomial): saw-tooth, jumps at the lattice points.
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.13, right=.97, bottom=.28, wspace=.3)
z = np.linspace(-4, 4, 3201)
n = 10; ea = erlang_cdf(n, n+z*math.sqrt(n)) - Phi(z)
a.plot(z, ea, color=RED, lw=1.3)
i = int(np.argmax(np.abs(ea))); dot(a, z[i], ea[i], RED, ms=3.8)
m = 20; pm = binpmf(m); F = np.cumsum(pm)
k = np.floor(m/2 + z*math.sqrt(m)/2).astype(int)
Fz = np.where(k < 0, 0.0, F[np.clip(k, 0, m)])
eb = Fz - Phi(z)
b.plot(z, eb, color=RED, lw=1.0)
j = int(np.argmax(np.abs(eb)))
for ax in (a, b):
    ax.axhline(0, color=STROKE, lw=.6); ax.set_xlim(-4, 4); ax.set_xticks([-4, -2, 0, 2, 4])
a.set_ylim(-.06, .06); b.set_ylim(-.11, .11)
axlab(a, '$z$', r'$F_{Z_n}(z)-\Phi(z)$'); axlab(b, '$z$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'exp_n10_max': float(abs(ea[i])), 'exp_argmax': float(z[i]),
     'bin_n20_max': bin_sup_error(20, .5)})
