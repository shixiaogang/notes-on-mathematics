from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Step initial data, h=1/40, tau=0.02 (r=32), t=0.06: BE vs CN against a fine reference.
n = 40; h = 1/n; x = np.linspace(0, 1, n+1); xi = x[1:-1]; A = lap1d(n); I = np.eye(n-1)
U0 = np.where(abs(xi-.5) < .25, 1., 0.); tau = .02; N = 3
BE = np.linalg.inv(I+tau*A); CN = np.linalg.solve(I+tau/2*A, I-tau/2*A)
Ub = U0.copy(); Uc = U0.copy()
for _ in range(N): Ub = BE@Ub; Uc = CN@Uc
# reference: eigen expansion of the semi-discrete system
w, V = np.linalg.eigh(A); ref = V@(np.exp(-w*tau*N)*(V.T@U0))
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, sharey=True)
panel(fig, left=.075, wspace=.1, bottom=.27)
for ax, U, c in zip(axes, (Ub, Uc), (GREEN, YELLOW)):
    ax.plot(x, np.r_[0, ref, 0], color=BLUE, lw=1.4); ax.plot(x, np.r_[0, U, 0], color=c, lw=1.3, marker='o', ms=2.4, mew=0)
    ax.axhline(0, color=STROKE, lw=.6); ax.set_xlim(-.02, 1.02); ax.set_xticks([0, .25, .75, 1]); ax.set_xticklabels(['0', '1/4', '3/4', '1']); ax.set_xlabel('$x$', labelpad=1)
axes[0].set_ylim(-.25, .85); axes[0].set_yticks([0, .4, .8]); axes[0].set_ylabel('$u$', labelpad=1)
tags(fig, axes)
Rmin = float((1-tau/2*w.max())/(1+tau/2*w.max()))
save(fig, HERE, 'figure', {'r': tau/h**2, 'CN_factor_top_mode': Rmin, 'min_BE': float(Ub.min()), 'min_CN': float(Uc.min())})
print(Rmin, Ub.min(), Uc.min(), tau*w.max())
