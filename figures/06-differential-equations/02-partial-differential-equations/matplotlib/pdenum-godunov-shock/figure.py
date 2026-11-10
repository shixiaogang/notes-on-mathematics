from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Burgers ul=1, ur=0.2, x0=0.5, T=1, h=0.01, lam=0.5: Godunov conservative vs non-conservative upwind.
n = 200; h = 2/n; x = (np.arange(n)+.5)*h; lam = .5; T = 1.; N = round(T/(lam*h))
U = np.where(x < .5, 1., .2); W = U.copy()
for _ in range(N):
    U = fv_step(U, lam, godunov); V = W.copy(); V[1:] = W[1:]-lam*W[1:]*(W[1:]-W[:-1]); W = V
X = np.linspace(0, 2, 2001); sex = .5+.6*T
fig, ax = figure(width_mm=88, height_mm=50)
ax.plot(X, np.where(X < sex, 1., .2), color=BLUE, lw=1.4); ax.plot(x, U, color=GREEN, lw=1.3); ax.plot(x, W, color=RED, lw=1.3)
ax.set_xlim(.4, 1.6); ax.set_ylim(0, 1.2); ax.set_xticks([.5, 1.1]); ax.set_yticks([.2, 1]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=1)
crossU = x[np.argmax(U < .6)]; crossW = x[np.argmax(W < .6)]
save(fig, HERE, 'figure', {'exact': sex, 'godunov_half_height': float(crossU), 'nonconservative_half_height': float(crossW)}); print(sex, crossU, crossW)
