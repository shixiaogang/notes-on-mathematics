"""Y~Unif(0,1), X|Y=y ~ Exp(rate y): conditional mean 1/y finite for each y but E X = int_0^1 dy/y = inf.
(a) 1/y with area on [eps,1], eps=0.05; (b) ln(1/eps) against eps on a log axis."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=104, height_mm=44, ncols=2)
y = np.linspace(0.04, 1, 400)
eps = 0.05
ys = np.linspace(eps, 1, 300)
a.fill_between(ys, 0, 1/ys, color=BLUE_FILL, lw=0)
a.plot(y, 1/y, color=BLUE, lw=1.4)
a.set_xlim(0, 1); a.set_ylim(0, 25); a.set_xticks([0, eps, 0.5, 1]); a.set_xticklabels(['0', '$\\varepsilon$', '0.5', '1'])
a.set_yticks([0, 10, 20]); a.set_xlabel('$y$', labelpad=1); a.set_ylabel('$1/y$')
e = np.logspace(-6, 0, 200)
b.plot(e, np.log(1/e), color=BLUE, lw=1.4)
b.set_xscale('log'); b.set_xlim(1e-6, 1); b.set_ylim(0, 15); b.set_yticks([0, 5, 10, 15])
b.set_xlabel('$\\varepsilon$', labelpad=1); b.set_ylabel('$\\ln(1/\\varepsilon)$')

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'eps': eps, 'area_eps': math.log(1/eps)})
