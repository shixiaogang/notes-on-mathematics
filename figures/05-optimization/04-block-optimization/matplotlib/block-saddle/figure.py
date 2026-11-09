from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# Phi(u,v)=1/2(uv-1)^2+rho/2(u^2+v^2), rho=0.36. Alternating exact updates: u=v/(v^2+rho), v=u/(u^2+rho).
rho = .36; Phi = lambda u, v: .5*(u*v-1)**2+rho/2*(u*u+v*v)
fig, ax = figure(width_mm=88, height_mm=70)
panel(fig, .1, .98, .985, .12)
U, V = np.meshgrid(np.linspace(-1.5, 2.4, 700), np.linspace(-1.5, 2.2, 700))
ax.contour(U, V, Phi(U, V), levels=[.31, .36, .42, .5, .62, .85, 1.3, 2.], colors=[BLUE], linewidths=.65)
ax.contour(U, V, Phi(U, V), levels=[.5], colors=[BLUE], linewidths=1.05)
v = .15; u = 2.2; P = [(u, v)]
for k in range(7):
    u = v/(v*v+rho); P.append((u, v)); v = u/(u*u+rho); P.append((u, v))
path(ax, P, GREEN, ms=2.8); opt(ax, .8, .8); opt(ax, -.8, -.8)
ax.plot([0], [0], 'o', ms=5, mfc='white', mec=RED, mew=1.1, zorder=6)
ax.text(.09, -.28, '原点', fontsize=7.5, color=INK); ax.text(.92, 1.0, '$(0.8,0.8)$', fontsize=7.5, color=INK, bbox=dict(fc='white', ec='none', pad=.6)); ax.text(-1.4, -1.12, '$(-0.8,-0.8)$', fontsize=7.5, color=INK); ax.text(2.0, .25, '起点', fontsize=7.5, color=INK)
ax.set_xlabel('$u$', labelpad=1); ax.set_ylabel('$v$', labelpad=1); ax.set_aspect('equal'); ax.set_xlim(-1.5, 2.4); ax.set_ylim(-1.5, 2.2)
save(fig, HERE, 'figure', {'rho': rho, 'path': [list(map(float, p)) for p in P]})
print(P)
