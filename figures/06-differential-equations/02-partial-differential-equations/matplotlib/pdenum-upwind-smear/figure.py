from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Square pulse on a periodic grid, a=1, h=1/100, lam=0.5, T=0.25: upwind vs modified equation; FTCS at T=0.05.
import math
n = 100; h = 1/n; x = (np.arange(n)+.5)*h; lam = .5
U0 = np.where((x > .2) & (x < .4), 1., 0.)
T = .25; N = round(T/(lam*h)); U = U0.copy()
for _ in range(N): U = U-lam*(U-np.roll(U, 1))
nu = h*(1-lam)/2; erf = np.vectorize(math.erf); X = np.linspace(0, 1, 1001); w = np.sqrt(4*nu*T)
mod = .5*(erf((X-.2-T)/w)-erf((X-.4-T)/w))
V = U0.copy(); Nf = 16
for _ in range(Nf): V = V-lam/2*(np.roll(V, -1)-np.roll(V, 1))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, wspace=.24, bottom=.27)
ax = axes[0]; ax.plot(X, np.where((X > .2+T) & (X < .4+T), 1., 0.), color=BLUE, lw=1.4); ax.plot(X, mod, color=PURPLE, lw=1.1, ls=DASH); ax.plot(x, U, color=GREEN, lw=1.3)
ax.set_xlim(.25, .9); ax.set_ylim(-.1, 1.15); ax.set_yticks([0, .5, 1]); ax.set_xticks([.45, .65]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=1)
ax = axes[1]; Tf = Nf*lam*h; ax.plot(X, np.where((X > .2+Tf) & (X < .4+Tf), 1., 0.), color=BLUE, lw=1.4); ax.plot(x, V, color=RED, lw=1.2)
ax.set_xlim(.15, .6); ax.set_xticks([.2+Tf, .4+Tf]); ax.set_xticklabels(['0.28', '0.48']); ax.set_xlabel('$x$', labelpad=1); ax.set_ylim(-1.3, 2.3); ax.set_yticks([0, 1])
tags(fig, axes); save(fig, HERE, 'figure', {'nu': nu, 'T': T, 'ftcs_T': Tf, 'ftcs_max': float(V.max()), 'upwind_mass': float(h*U.sum())}); print(nu, Tf, V.max(), V.min(), h*U.sum())
