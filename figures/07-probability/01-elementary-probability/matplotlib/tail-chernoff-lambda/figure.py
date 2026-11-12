from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Choosing lambda in the exponential-moment bound.
# (a) X ~ Bin(20,1/2), t=15: g(lam) = e^{-15 lam} ((1+e^lam)/2)^20, minimised at lam=ln 3 with value 2^20/3^15.
# (b) Z ~ N(0,1): e^{-lam t + lam^2/2} for t=1,2,3, minimised at lam=t with value e^{-t^2/2}.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.1, wspace=.34, bottom=.28)
ax = axes[0]; lam = np.linspace(0, 2.6, 600)
g = np.exp(-15*lam)*bin_mgf(lam)
ax.semilogy(lam, g, color=PURPLE, lw=1.4)
ax.axhline(bin_tail(15), color=BLUE, lw=1.0, ls=DASH)
l0 = np.log(3); dot(ax, l0, 2**20/3**15, RED)
lab(ax, l0, 2**20/3**15*.55, r'$\lambda=\ln 3$', RED, ha='center', va='top')
lab(ax, 2.55, bin_tail(15)*.8, '$0.0207$', BLUE, ha='right', va='top')
ax.set_xlim(0, 2.6); ax.set_ylim(8e-3, 1.5); logticks(ax, [0, -1, -2]); ax.set_xticks([0, .5, 1, 1.5, 2, 2.5])
axlab(ax, r'$\lambda$')
ax = axes[1]; lam = np.linspace(0, 4.2, 600)
for t, c in ((1, BLUE), (2, GREEN), (3, YELLOW)):
    ax.semilogy(lam, np.exp(-lam*t+lam**2/2), color=c, lw=1.4)
    dot(ax, t, np.exp(-t*t/2), RED, ms=3.8)
    lab(ax, *{1: (1.0, .45), 2: (3.9, .25), 3: (4.15, .009)}[t], '$t=%d$' % t, c, ha='center' if t == 1 else 'right', va='top')
ax.set_xlim(0, 4.2); ax.set_ylim(5e-3, 2); logticks(ax, [0, -1, -2]); ax.set_xticks([0, 1, 2, 3, 4])
axlab(ax, r'$\lambda$')
tags(fig, axes)
save(fig, HERE, 'figure', {'binomial_min': 2**20/3**15, 'binomial_argmin': float(l0), 'normal_min': [float(np.exp(-t*t/2)) for t in (1, 2, 3)]})
