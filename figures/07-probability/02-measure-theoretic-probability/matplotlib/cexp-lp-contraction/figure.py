"""L^p contraction on Omega=[0,1) uniform, X(w)=w^2-1/3, G_n dyadic.
(a) ||E[X|G_n]||_p for n=0..7 and p=1 (circles), 2 (squares), 4 (triangles), green; ||X||_p purple dashed.
Norms by midpoint rule on 2^16 cells. (b) n=1: |X| (blue) and |E[X|G_1]| (green, values 1/4 on both halves);
red fill where |E[X|G_1]| > |X|."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

K = 2**16
w = (np.arange(K) + 0.5)/K
X = w**2 - 1/3
def cond(n):
    N = 2**n
    return X.reshape(N, -1).mean(axis=1).repeat(K//N)
ns = np.arange(8)
fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
facts = {}
for p, mk in [(1, 'o'), (2, 's'), (4, '^')]:
    vals = [np.mean(np.abs(cond(n))**p)**(1/p) for n in ns]
    full = np.mean(np.abs(X)**p)**(1/p)
    a.plot(ns, vals, color=GREEN, lw=1.1, marker=mk, ms=3.2)
    a.axhline(full, color=PURPLE, lw=1.0, ls='--')
    a.text(7.6, full + (0.012 if p == 4 else (-0.012 if p == 1 else 0)), f'$p={p}$', va='center', fontsize=7.5)
    facts[f'p{p}'] = {'cond_norms': vals, 'norm_X': full}
a.set_xlim(-0.3, 9.2); a.set_ylim(0, 0.5); a.set_xticks(range(0, 8)); a.set_xlabel('$n$', labelpad=1)
cm = np.abs(cond(1)); ax = np.abs(X)
b.fill_between(w, ax, cm, where=cm > ax, color=RED_FILL, lw=0)
b.plot(w, ax, color=BLUE, lw=1.4)
b.plot(w, cm, color=GREEN, lw=1.5)
b.axvline(0.5, color=STROKE, lw=0.7, ls=':')
b.text(0.97, 0.66, r'$|X|$', color=BLUE, ha='right')
b.text(0.03, 0.04, r'$|\mathrm{E}[X\mid\mathcal{G}_1]|$', color=GREEN, fontsize=7.5)
b.set_xlim(0, 1); b.set_ylim(0, 0.72); b.set_xticks([0, 0.5, 1]); b.set_xticklabels(['0', '1/2', '1'])
b.set_xlabel(r'$\omega$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
facts['n1_values'] = [float(cond(1)[0]), float(cond(1)[-1])]
save(fig, Path(__file__).resolve().parent, 'figure', facts)
