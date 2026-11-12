"""Constrained steepest descent at N(1,4) in (mu,v) for L=D_KL(N(mu,v)||N(0,1)): g=(1,0.375), G=diag(1/4,1/32).
Blue ellipse (1/2) d^T G d = 0.05; gray dashed: level lines <g,d>=c; green: natural step -t G^{-1}g (t=0.1085);
yellow: Euclidean direction -g scaled to the same ellipse (t=0.627)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, ax = figure(width_mm=84, height_mm=60)
g = np.array([1.0, 0.375]); G = np.diag([0.25, 1/32]); eps = 0.05
nat = -np.linalg.solve(G, g); nat *= np.sqrt(2*eps/(nat@G@nat))
euc = -g*np.sqrt(2*eps/(g@G@g))
ang = np.linspace(0, 2*np.pi, 300); ra, rb = np.sqrt(2*eps/G[0, 0]), np.sqrt(2*eps/G[1, 1])
ax.fill(ra*np.cos(ang), rb*np.sin(ang), color=BLUE_FILL, lw=0); ax.plot(ra*np.cos(ang), rb*np.sin(ang), color=BLUE, lw=1.2)
xs = np.linspace(-1, 1, 10)
for c in np.linspace(-1.0, 0.8, 7):
    ax.plot(xs, (c-g[0]*xs)/g[1], color=STROKE, lw=0.6, ls=(0, (3, 2)))
cmin = g@nat
ax.plot(xs, (cmin-g[0]*xs)/g[1], color=RED, lw=1.0)
for v_, col in ((euc, YELLOW), (nat, GREEN)):
    ax.annotate('', xy=v_, xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=col, lw=1.6, mutation_scale=8))
ax.scatter([0], [0], s=12, color=STROKE, zorder=5)
ax.set_xlim(-1, 1); ax.set_ylim(-2.2, 2.2)
ax.set_xlabel(r'$\delta_{\mu}$', labelpad=1); ax.set_ylabel(r'$\delta_{v}$', labelpad=1)
save(fig, HERE, 'figure', {'nat_step': nat.tolist(), 'euc_step': euc.tolist(), 'lin_nat': float(g@nat), 'lin_euc': float(g@euc)})
