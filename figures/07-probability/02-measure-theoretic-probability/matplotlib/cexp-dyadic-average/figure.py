"""Omega=[0,1) uniform, X(w)=w^2 (blue). E[X|G_n] for the sigma-algebra G_n of 2^n dyadic intervals
is the step function of interval means (a^2+ab+b^2)/3.
(a) n=2: means 1/48, 7/48, 19/48, 37/48 (green), boundaries grey; (b) n=1 (yellow), n=3 (purple), n=5 (green)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

w = np.linspace(0, 1, 400)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2, sharey=True)
e, m = dyadic_means(2)
for k in range(4):
    a.fill_between(w[(w >= e[k]) & (w <= e[k+1])], w[(w >= e[k]) & (w <= e[k+1])]**2, m[k], color=BLUE_FILL, lw=0)
for x in e[1:-1]:
    a.axvline(x, color=STROKE, lw=0.7, ls=':')
a.plot(w, w**2, color=BLUE, lw=1.4)
a.hlines(m, e[:-1], e[1:], color=GREEN, lw=1.6)
for k, lab in enumerate(['1/48', '7/48', '19/48', '37/48']):
    a.text((e[k]+e[k+1])/2, m[k]+0.05, f'${lab}$', ha='center', fontsize=7.5, color=INK)
a.text(0.93, 0.98, '$X$', color=BLUE, ha='right', va='top')
a.set_xlim(0, 1); a.set_ylim(0, 1.05); a.set_xticks([0, .25, .5, .75, 1]); a.set_xticklabels(['0', '1/4', '1/2', '3/4', '1'])
a.set_xlabel(r'$\omega$', labelpad=1)
for n, c, lw in [(1, YELLOW, 1.6), (3, PURPLE, 1.3), (5, GREEN, 1.2)]:
    e, m = dyadic_means(n)
    b.step(np.r_[e[:-1], 1], np.r_[m, m[-1]], where='post', color=c, lw=lw)
b.plot(w, w**2, color=BLUE, lw=1.4)
b.text(0.04, 0.14, '$n=1$', color=YELLOW, fontsize=7.5)
b.text(0.62, 0.62, '$n=3$', color=PURPLE, fontsize=7.5, ha='right')
b.text(0.80, 0.50, '$n=5$', color=GREEN, fontsize=7.5)
b.set_xlim(0, 1); b.set_xticks([0, .5, 1]); b.set_xticklabels(['0', '1/2', '1']); b.set_xlabel(r'$\omega$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'X': 'w^2', 'means_n2': [1/48, 7/48, 19/48, 37/48], 'mean': 1/3})
