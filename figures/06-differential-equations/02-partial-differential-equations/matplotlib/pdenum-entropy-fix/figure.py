from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Riemann data -1,1 at T=0.5: Godunov approaches the rarefaction; Roe keeps the expansion shock.
n = 100; h = 2/n; x = -1+(np.arange(n)+.5)*h; lam = .5; T = .5; N = round(T/(lam*h)); U0 = np.where(x < 0, -1., 1.)
A = U0.copy(); B = U0.copy()
for _ in range(N): A = fv_step(A, lam, godunov); B = fv_step(B, lam, roe)
X = np.linspace(-1, 1, 1001); ex = np.clip(X/T, -1, 1)
fig, axes = figure(width_mm=112, height_mm=48, ncols=2, sharey=True)
panel(fig, left=.075, wspace=.1, bottom=.28)
for ax, U, c in zip(axes, (A, B), (GREEN, RED)):
    ax.plot(X, ex, color=BLUE, lw=1.4); ax.plot(x, U, color=c, lw=1.3); ax.axhline(0, color=STROKE, lw=.5)
    ax.set_xlim(-1, 1); ax.set_xticks([-.5, 0, .5]); ax.set_xlabel('$x$', labelpad=1)
axes[0].set_ylim(-1.2, 1.2); axes[0].set_yticks([-1, 0, 1]); axes[0].set_ylabel('$u$', labelpad=1); tags(fig, axes)
save(fig, HERE, 'figure', {'T': T, 'godunov_L1': float(h*np.sum(np.abs(A-np.clip(x/T, -1, 1)))), 'roe_L1': float(h*np.sum(np.abs(B-np.clip(x/T, -1, 1))))})
print(h*np.sum(np.abs(A-np.clip(x/T, -1, 1))), h*np.sum(np.abs(B-np.clip(x/T, -1, 1))))
