from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Explicit Euler for heat equation, h=1/20: r=0.4 and r=0.55, u0=sin(pi x)+0.1 sin(3 pi x), t up to 0.04.
n = 20; h = 1/n; x = np.linspace(0, 1, n+1); X = np.linspace(0, 1, 401); A = lap1d(n)
def exact(s, t): return np.exp(-PI**2*t)*np.sin(PI*s)+.1*np.exp(-9*PI**2*t)*np.sin(3*PI*s)
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.24, bottom=.27)
rec = {}
for ax, r, c in zip(axes, (.4, .55), (GREEN, RED)):
    tau = r*h*h; N = round(.08/tau); tau = .08/N; U = exact(x[1:-1], 0)+2e-5*np.sin(19*PI*x[1:-1])
    for k in range(N): U = U-tau*A@U
    ax.plot(X, exact(X, .08), color=BLUE, lw=1.4); ax.plot(x, np.r_[0, U, 0], color=c, lw=1.1, marker='o', ms=2.6, mew=0)
    ax.set_xlim(-.02, 1.02); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_xlabel('$x$', labelpad=1)
    rec[r] = {'steps': N, 'max': float(np.max(np.abs(U)))}; ax.set_ylim(-.9, 1.3); ax.set_yticks([-.5, 0, .5, 1])
axes[0].set_ylabel('$u$', labelpad=1)
tags(fig, axes); save(fig, HERE, 'figure', rec); print(rec)
