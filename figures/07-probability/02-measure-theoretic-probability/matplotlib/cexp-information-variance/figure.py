"""Total variance under growing information.
(a) Sensor table, Var(Y)=0.6 split into E[Var(Y|G)] (blue fill) + Var(E[Y|G]) (green fill) for
G = trivial, H=sigma(1{X=2}), sigma(X), sigma(X,Y): (0.6,0), (43/105, 4/21), (1/3, 4/15), (0, 0.6).
(b) Omega=[0,1), X=w^2, G_n dyadic: E[Var(X|G_n)] (blue) decreases, Var(E[X|G_n]) (green) increases,
their sum is Var(X)=4/45 (purple dashed). Exact interval formulas."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

cells = [(x, y) for x in range(3) for y in range(3)]
Yv = np.array([[y for y in range(3)] for x in range(3)], float)
keys = [lambda x, y: 0, lambda x, y: x == 2, lambda x, y: x, lambda x, y: (x, y)]
within, between = [], []
for k in keys:
    m = cond_mean(Yv, k)
    mm = np.where(P > 0, m, 0)
    within.append(float((P*(Yv - mm)**2).sum())); between.append(float((P*(mm - 1)**2).sum()))
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
xs = np.arange(4)
a.bar(xs, within, width=0.55, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
a.bar(xs, between, bottom=within, width=0.55, color=GREEN_FILL, edgecolor=GREEN, lw=0.8)
for i in range(4):
    if within[i] > 0.02:
        a.text(i, within[i]/2, f'{within[i]:.3f}', ha='center', va='center', fontsize=7, color=INK)
    if between[i] > 0.02:
        a.text(i, within[i] + between[i]/2, f'{between[i]:.3f}', ha='center', va='center', fontsize=7, color=INK)
a.set_xticks(xs); a.set_xticklabels([r'$\{\emptyset,\Omega\}$', r'$\mathcal{H}$', r'$\sigma(X)$', r'$\sigma(X,Y)$'], fontsize=7.5)
a.set_ylim(0, 0.68)
ns = np.arange(0, 8)
Vm = []
for n in ns:
    e, m = dyadic_means(n)
    Vm.append(float(np.mean(m**2) - 1/9))
Vm = np.array(Vm); EV = 4/45 - Vm
b.plot(ns, EV, color=BLUE, lw=1.3, marker='o', ms=3)
b.plot(ns, Vm, color=GREEN, lw=1.3, marker='s', ms=3)
b.axhline(4/45, color=PURPLE, lw=1.0, ls='--')
b.text(7, 4/45 + 0.004, r'$\mathrm{Var}(X)=4/45$', ha='right', fontsize=7.5, color=PURPLE)
b.text(7, Vm[-1] - 0.006, r'$\mathrm{Var}(\mathrm{E}[X\mid\mathcal{G}_n])$', ha='right', va='top', fontsize=7.5, color=GREEN)
b.text(7, EV[-1] + 0.006, r'$\mathrm{E}[\mathrm{Var}(X\mid\mathcal{G}_n)]$', ha='right', va='bottom', fontsize=7.5, color=BLUE)
b.set_xlim(-0.3, 7.3); b.set_ylim(0, 0.105); b.set_xlabel('$n$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'within': within, 'between': between, 'dyadic_Vm': list(Vm)})
