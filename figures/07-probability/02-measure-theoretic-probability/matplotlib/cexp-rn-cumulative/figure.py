"""Existence via Radon-Nikodym on Omega=[0,1), X(w)=w^2, G=G_2 (quarters).
nu(A)=E[X 1_A]. Blue: t -> nu([0,t)) = t^3/3 (known for all intervals, i.e. on F).
Green: on G only nu of the quarters is known; the polygon through (k/4, (k/4)^3/3) has slopes
nu(A_k)/P(A_k) = 1/48, 7/48, 19/48, 37/48 = E[X|G] on A_k. (b) masses P(A_k)=1/4 vs nu(A_k)=(1,7,19,37)/192."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

t = np.linspace(0, 1, 300)
e, m = dyadic_means(2)
fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
for x in e[1:-1]:
    a.axvline(x, color=STROKE, lw=0.7, ls=':')
a.plot(t, t**3/3, color=BLUE, lw=1.4)
a.plot(e, e**3/3, color=GREEN, lw=1.3, marker='o', ms=3.2)
for k, lab in enumerate(['1/48', '7/48', '19/48', '37/48']):
    xm = (e[k]+e[k+1])/2; ym = (e[k]**3+e[k+1]**3)/6
    if k == 3:
        a.text(0.985, 0.15, f'${lab}$', ha='right', fontsize=7.5, color=GREEN)
    else:
        a.text(xm-0.02, ym+0.025, f'${lab}$', ha='center', fontsize=7.5, color=GREEN)
a.text(0.97, 0.335, r'$\nu([0,t))=t^3/3$', ha='right', va='top', fontsize=7.5, color=BLUE)
a.set_xlim(0, 1); a.set_ylim(0, 0.36); a.set_xticks(e); a.set_xticklabels(['0', '1/4', '1/2', '3/4', '1'])
a.set_xlabel('$t$', labelpad=1)
nu = np.diff(e**3)/3
k = np.arange(4)
b.bar(k-0.18, np.full(4, 0.25), width=0.34, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
b.bar(k+0.18, nu, width=0.34, color=GREEN_FILL, edgecolor=GREEN, lw=0.8)
b.text(-0.18, 0.262, r'$\mathrm{P}$', ha='center', fontsize=7.5, color=BLUE)
b.text(3.18, nu[3]+0.012, r'$\nu$', ha='center', fontsize=7.5, color=GREEN)
b.set_xticks(k); b.set_xticklabels(['$A_1$', '$A_2$', '$A_3$', '$A_4$']); b.set_ylim(0, 0.3)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, Path(__file__).resolve().parent, 'figure', {'nu_quarters': list(nu), 'slopes': list(m)})
