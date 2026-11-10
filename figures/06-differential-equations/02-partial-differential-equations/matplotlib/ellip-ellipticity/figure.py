from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# level sets of the principal symbol xi^T A xi = 1.
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
panel(fig, left=.05, right=.985, top=.97, bottom=.2, wspace=.2)
A = np.array([[2, .6], [.6, 1]]); ev = np.linalg.eigvalsh(A)
g = np.linspace(-2.2, 2.2, 601); P, Q = np.meshgrid(g, g)
ax = axes[0]
ax.contour(P, Q, A[0,0]*P**2+2*A[0,1]*P*Q+A[1,1]*Q**2, [1], colors=BLUE, linewidths=1.4)
t = np.linspace(0, 2*np.pi, 300)
for k, c in zip(ev, (PURPLE, PURPLE)):
    ax.plot(np.cos(t)/np.sqrt(k), np.sin(t)/np.sqrt(k), color=c, lw=.85, ls=DASH)
ax = axes[1]
for s in (-1, 1): ax.plot([s, s], [-2, 2], color=BLUE, lw=1.4)
ax = axes[2]
ax.contour(P, Q, P**2-Q**2, [1], colors=BLUE, linewidths=1.4)
for ax in axes:
    ax.axhline(0, color=STROKE, lw=.6); ax.axvline(0, color=STROKE, lw=.6)
    ax.set_xlim(-2, 2); ax.set_ylim(-2, 2); ax.set_aspect('equal'); ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values(): s.set_visible(False)
    lab(ax, 1.98, .1, r'$\xi_1$', MUTED, ha='right'); lab(ax, .1, 1.76, r'$\xi_2$', MUTED)
tags(fig, axes)
save(fig, HERE, 'figure', {'A': A.tolist(), 'eig': ev.tolist(), 'degenerate': 'diag(1,0)', 'indefinite': 'diag(1,-1)'})
