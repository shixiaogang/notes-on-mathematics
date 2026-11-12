from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# Exp(1) steps, n = 10, Z = (S_10 - 10)/sqrt(10), S_10 ~ Gamma(10,1) exactly.
# (a) right tail P(Z >= z), exact (blue) vs normal 1 - Phi(z) (yellow), log scale;
# (b) left tail P(Z <= -z), exact (blue) vs Phi(-z) (yellow); the exact left tail is 0 for z >= sqrt(10).
n = 10; s = math.sqrt(n)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, right=.97, bottom=.28, wspace=.3)
z = np.linspace(0, 6, 601)
a.plot(z, erlang_sf(n, n+z*s), color=BLUE, lw=1.4)
a.plot(z, 1-Phi(z), color=YELLOW, lw=1.6, ls=DASH)
for zz in (3, 5):
    dot(a, zz, float(erlang_sf(n, n+zz*s)[0]), BLUE, ms=3.6); dot(a, zz, float(1-Phi(zz)), YELLOW, ms=3.6)
zl = np.linspace(0, s-1e-6, 2000)
b.plot(zl, erlang_cdf(n, n-zl*s), color=BLUE, lw=1.4)
zb = np.linspace(0, 4, 400)
b.plot(zb, Phi(-zb), color=YELLOW, lw=1.6, ls=DASH)
b.axvline(s, color=RED, lw=.8, ls=DOT)
lab(b, s+.08, 3e-2, r'$z=\sqrt{10}$', RED, ha='left')
for ax in (a, b):
    ax.set_yscale('log'); ax.set_ylim(1e-9, 1)
logticks(a, [-8, -6, -4, -2, 0]); logticks(b, [-8, -6, -4, -2, 0])
a.set_xlim(0, 6); b.set_xlim(0, 4)
axlab(a, '$z$', '尾概率'); axlab(b, '$z$')
tags(fig, (a, b))
facts = {str(zz): {'exact': float(erlang_sf(n, n+zz*s)[0]), 'normal': float(1-Phi(zz))} for zz in (2, 3, 4, 5)}
facts['left_normal_at_sqrt10'] = float(Phi(-s))
save(fig, HERE, 'figure', facts)
