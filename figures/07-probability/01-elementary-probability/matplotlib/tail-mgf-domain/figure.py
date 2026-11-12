from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"tail-common"))
from tail_fig import *
# Moment generating functions M(lam)=E[e^{lam X}]: N(0,1) e^{lam^2/2} (all lam), Exp(1) 1/(1-lam) (lam<1), Laplace(0,1) 1/(1-lam^2) (|lam|<1).
fig, ax = figure(width_mm=90, height_mm=52)
lam = np.linspace(-2, 2, 801)
ax.plot(lam, np.exp(lam**2/2), color=BLUE, lw=1.4)
le = lam[lam < .985]; ax.plot(le, 1/(1-le), color=YELLOW, lw=1.6)
ll = lam[np.abs(lam) < .985]; ax.plot(ll, 1/(1-ll**2), color=PURPLE, lw=1.4)
for v in (-1, 1): ax.axvline(v, color=STROKE, lw=.85, ls=DOT)
dot(ax, 0, 1, RED, ms=3.6)
lab(ax, 1.95, 1.9, r'$\mathcal{N}(0,1)$', BLUE, ha='right', va='top')
lab(ax, .62, 6.5, r'$\operatorname{Exp}(1)$', YELLOW, ha='right')
lab(ax, -.72, 5.2, 'Laplace', PURPLE, ha='left')
ax.set_xlim(-2, 2); ax.set_ylim(0, 8); ax.set_xticks([-2, -1, 0, 1, 2]); ax.set_yticks([0, 1, 2, 4, 6, 8])
axlab(ax, r'$\lambda$', r'$M_X(\lambda)$')
save(fig, HERE, 'figure', {'domains': {'normal': 'R', 'exp': 'lam<1', 'laplace': '|lam|<1'}})
