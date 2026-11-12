from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Truncation in the integrable weak law, Pareto(alpha = 1.5): density 1.5 x^{-2.5} on [1, inf), mean 3, infinite variance.
# (a) integrand x f(x) = 1.5 x^{-1.5} of the mean with truncation level c = 4: kept part x <= c (blue fill), cut part x > c (red fill, area tau(c));
#     tail mean tau(c) = E[X; X > c] = 3 c^{-1/2} = 1.5.
# (b) the two terms of the bound with eps = 1 (requires tau(c) < eps/3, i.e. c > 81):
#     total bound 27 (sqrt(c) - 1)/n + 9 c^{-1/2} for n = 10^4, 10^5, 10^6 (blue, solid/dash/dot), where the first term is 9 E[Y^2]/(n eps^2),
#     tail term 3 tau(c)/eps = 9 c^{-1/2} (purple); minimum of the sum marked red for each n.
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.97, bottom=.28, wspace=.3)
x = np.linspace(1, 25, 1200); f = 1.5*x**-1.5; c = 4
a.fill_between(x[x <= c], f[x <= c], color=BLUE_FILL, lw=0)
a.fill_between(x[x >= c], f[x >= c], color=RED_FILL, lw=0)
a.plot(x, f, color=BLUE, lw=1.4)
a.plot([c, c], [0, 1.5*c**-1.5], color=RED, lw=1.2); lab(a, c, -.12, '$c$', RED, ha='center', va='top')
a.plot([1, 1], [0, 1.5], color=BLUE, lw=1.4)
lab(a, 9, .25, r'$\tau(c)=3c^{-1/2}$', RED); lab(a, 2.6, 1.0, r'$xf(x)$', BLUE)
a.set_xlim(0, 25); a.set_ylim(0, 1.6); a.set_xticks([1, 4, 10, 20]); a.set_xticklabels(['1', '', '10', '20'])
axlab(a, '$x$')
cs = np.logspace(np.log10(81), 7, 400)
tail = 9/np.sqrt(cs)
b.plot(cs, tail, color=PURPLE, lw=1.4)
facts = {}
for n, ls in ((10**4, '-'), (10**5, DASH), (10**6, DOT)):
    var = 27*(np.sqrt(cs)-1)/n
    tot = var+tail
    b.plot(cs, tot, color=BLUE, lw=1.3, ls=ls); i = np.argmin(tot); dot(b, cs[i], tot[i], ms=3.6)
    facts[str(n)] = {'c_opt': float(cs[i]), 'bound_opt': float(tot[i])}
b.set_xscale('log'); b.set_yscale('log'); b.set_xlim(81, 1e7); b.set_ylim(1e-3, 3)
logticks(b, [2, 4, 6], 'x'); logticks(b, [-3, -2, -1, 0])
lab(b, 1e5, 3.5e-3, r'$9c^{-1/2}$', PURPLE)
lab(b, 1.2e6, .12, '$n=10^6$', BLUE, ha='center'); lab(b, 6e3, 1.3, '$n=10^4$', BLUE, ha='center')
axlab(b, '$c$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'tau_4': 1.5, **facts})
