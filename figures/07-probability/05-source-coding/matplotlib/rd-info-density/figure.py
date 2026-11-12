"""Per-symbol information density (1/n) sum log2 q(Xh_i|X_i)/r(Xh_i) under the optimal joint law
for Bern(0.3), Hamming, D=0.1 (r=(0.75,0.25)). Monte Carlo, seed SEED, 20000 blocks per n.
Concentrates at I=0.4123 bit (red)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

p, D = P_SRC, .1
r1 = (p-D)/(1-2*D)
# joint law of (X, Xh): X = Xh xor Z, Xh~Bern(r1), Z~Bern(D)
J = np.array([[(1-r1)*(1-D), r1*D], [(1-r1)*D, r1*(1-D)]])   # J[x, xh]
px = J.sum(1); r = J.sum(0)
dens = np.log2(J/(px[:, None]*r[None, :]))
I = float(np.sum(J*dens))
rng = np.random.default_rng(SEED)
fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.07, right=.99, top=.95, bottom=.33, wspace=.3)
flat = J.ravel(); vals = dens.ravel()
out = {}
for ax, n in zip(axs, (10, 100, 1000)):
    cnt = rng.multinomial(n, flat, size=20000)
    m = cnt @ vals / n
    ax.hist(m, bins=np.linspace(-1.4, 1.6, 61), color=GREEN_FILL, edgecolor=GREEN, lw=.5, density=True)
    ax.axvline(I, color=RED, lw=1.1)
    ax.set_xlim(-1.4, 1.6); ax.set_yticks([])
    ax.set_xlabel('$\\frac{1}{n}\\imath_n$ (bit)', labelpad=1)
    lab(ax, -1.3, ax.get_ylim()[1]*.85, f'$n={n}$', INK)
    out[n] = [float(m.mean()), float(m.std()), float(np.mean(m > I+.1))]
tags(fig, axs)
save(fig, HERE, 'figure', {'I': I, 'values': vals.tolist(), 'mean_std_P(>I+0.1)': out})
