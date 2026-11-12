from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lln-common"))
from lln_fig import *
# Kronecker's lemma with b_n = n on the deterministic sequence x_k = (-1)^{k+1} sqrt(k).
# (a) s_n = sum_{k<=n} x_k/k = sum (-1)^{k+1}/sqrt(k) (blue) and its average (1/n) sum_{k<n} s_k (yellow);
#     both tend to s = (1 - sqrt 2) zeta(1/2) ~ 0.6049.
# (b) their difference (1/n) sum_{k<=n} x_k (green) with the envelope +-1/(2 sqrt n) (purple).
N = 10**4
k = np.arange(1, N+1)
x = (-1.0)**(k+1)*np.sqrt(k)
s = np.cumsum(x/k)
w = np.concatenate([[0.], np.cumsum(s)[:-1]])/k
avg = np.cumsum(x)/k
lim = (1-np.sqrt(2))*(-1.4603545088095868)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.97, bottom=.28, wspace=.32)
a.plot(k, s, color=BLUE, lw=1.0); a.plot(k, w, color=YELLOW, lw=1.5)
a.axhline(lim, color=STROKE, lw=.6, ls=DOT)
lab(a, 300, .82, '$s_n$', BLUE); lab(a, 300, .4, r'$\frac{1}{n}\sum_{k<n}s_k$', YELLOW)
a.set_ylim(0, 1.05)
b.plot(k, avg, color=GREEN, lw=1.0)
b.plot(k, 1/(2*np.sqrt(k)), color=PURPLE, lw=1.1, ls=DASH); b.plot(k, -1/(2*np.sqrt(k)), color=PURPLE, lw=1.1, ls=DASH)
b.axhline(0, color=STROKE, lw=.6); b.set_ylim(-.6, 1.05)
lab(b, 200, .2, r'$\pm\frac{1}{2\sqrt{n}}$', PURPLE)
for ax in (a, b): ax.set_xscale('log'); ax.set_xlim(1, N); logticks(ax, [0, 1, 2, 3, 4], 'x'); axlab(ax, '$n$')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'limit': float(lim), 'avg_100': float(avg[99]), 'avg_1000': float(avg[999]), 'avg_10000': float(avg[-1]),
     's_10000': float(s[-1])})
