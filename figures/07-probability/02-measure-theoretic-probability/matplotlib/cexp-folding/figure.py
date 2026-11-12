"""Folding example: Omega=(-1,1) with uniform probability, X(w)=w, Y=|X|; sigma(Y) groups {w,-w}.
E[g(X)|Y] = (g(Y)+g(-Y))/2. (a) g(x)=x^+ (blue) and E[X^+|Y]=|X|/2 (green); red pair w=+-0.6, average 0.3.
(b) g(x)=e^x (blue) and E[e^X|Y]=cosh|X| (green); red pair w=+-0.6, average cosh 0.6 = 1.1855."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

w = np.linspace(-1, 1, 401)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
for ax, g, h, lab in [(a, lambda x: np.maximum(x, 0), lambda x: np.abs(x)/2, 'a'),
                      (b, np.exp, lambda x: np.cosh(x), 'b')]:
    ax.plot(w, g(w), color=BLUE, lw=1.4)
    ax.plot(w, h(w), color=GREEN, lw=1.4)
    s = 0.6
    ax.plot([-s, s], [g(-s), g(s)], color=RED, lw=0.8, ls='--')
    ax.scatter([-s, s], [g(-s), g(s)], s=14, color=RED, zorder=4)
    ax.scatter([-s, s], [h(s), h(s)], s=14, color=GREEN, zorder=4)
    for x in (-s, s):
        ax.plot([x, x], [ax.get_ylim()[0] if False else (0 if lab == 'a' else 0.3), h(s)], color=STROKE, lw=0.6, ls=':')
    ax.set_xlim(-1, 1); ax.set_xticks([-1, -0.6, 0, 0.6, 1]); ax.set_xticklabels(['-1', '-0.6', '0', '0.6', '1'])
    ax.set_xlabel(r'$\omega$', labelpad=1)
    tag(ax, f'({lab})', y=-0.27)
a.set_ylim(0, 1.02); b.set_ylim(0.3, 2.8)
a.text(0.97, 0.93, '$X^{+}$', color=BLUE, ha='right'); a.text(-0.97, 0.56, r'$|X|/2$', color=GREEN)
b.text(0.62, 2.2, r'$\mathrm{e}^{X}$', color=BLUE, ha='right'); b.text(-0.95, 1.75, r'$\cosh|X|$', color=GREEN)
save(fig, Path(__file__).resolve().parent, 'figure', {'pair': 0.6, 'avg_xplus': 0.3, 'cosh06': float(np.cosh(0.6))})
