from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
from types_exact import types, class_prob
# Typical set A = {x_{1:n}: | -(1/n) log2 p(x_{1:n}) - H | < eps}, eps = 0.1, p = (0.4,0.3,0.2,0.1), exact via types.
# (a) P(A) against n (blue) with the Chebyshev lower bound 1 - sigma^2/(n eps^2) (purple dashed), sigma^2 = Var(-log2 p(X)).
# (b) (1/n) log2 |A| (blue) with H +- eps (gray dotted), H (red) and log2 4 = 2 (purple).
eps = .1
sig2 = float((P*(-np.log2(P)-H)**2).sum())
ns = np.arange(5, 251, 5); PA, LA = [], []
for n in ns:
    K, lc, si = types(n); pr = class_prob(lc, si); m = np.abs(si/n-H) < eps
    PA.append(pr[m].sum()); mx = lc[m].max(); LA.append((mx + np.log2(np.exp2(lc[m]-mx).sum()))/n)
PA, LA = np.array(PA), np.array(LA)
fig, (a1, a2) = figure(width_mm=110, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.3)
nn = np.linspace(5, 250, 400)
a1.plot(nn, np.maximum(0, 1-sig2/(nn*eps**2)), color=PURPLE, lw=1.1, ls=DASH)
a1.plot(ns, PA, color=BLUE, lw=1.4)
a1.set_xlim(0, 250); a1.set_ylim(0, 1.12)
lab(a1, 150, .55, 'Chebyshev', PURPLE); lab(a1, 150, 1.01, "典型集的概率", BLUE, va='bottom')
a1.set_xlabel('$n$', labelpad=1)
a2.axhline(2, color=PURPLE, lw=1.1); a2.axhline(H, color=RED, lw=1.0)
for s in (-eps, eps):
    a2.axhline(H+s, color=STROKE, lw=.85, ls=DOT)
a2.plot(ns, LA, color=BLUE, lw=1.4)
a2.set_xlim(0, 250); a2.set_ylim(1.6, 2.1)
lab(a2, 245, 2.01, r'$\log_2 4$', PURPLE, ha='right'); lab(a2, 245, H+eps+.008, r'$H+\varepsilon$', STROKE, ha='right')
lab(a2, 245, H-eps+.008, r'$H-\varepsilon$', STROKE, ha='right'); lab(a2, 245, H+.008, r'$H$', RED, ha='right')
lab(a2, 22, 1.63, r'$\frac{1}{n}\log_2|A_{\varepsilon}^{(n)}|$', BLUE)
a2.set_xlabel('$n$', labelpad=1)
tags(fig, (a1, a2))
save(fig, HERE, 'figure', {'eps': eps, 'sigma2': sig2, 'P_A': dict(zip(map(int, ns[::5]), map(float, PA[::5]))),
     'log2A_over_n': dict(zip(map(int, ns[::5]), map(float, LA[::5])))})
