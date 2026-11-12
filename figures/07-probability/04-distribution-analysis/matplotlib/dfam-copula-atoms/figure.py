"""Two independent fair coins: Ran F x Ran F = {0,1/2,1}^2. Contours of Pi(u,v)=uv and C2=(M+W)/2 at 0.1,0.25,0.5,0.75; they agree on grid points."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

g = np.linspace(0, 1, 401)
U, V = np.meshgrid(g, g)
Pi = U*V
C2 = 0.5*np.minimum(U, V)+0.5*np.maximum(U+V-1, 0)
lv = [0.1, 0.25, 0.5, 0.75]
fig, ax = figure(width_mm=72, height_mm=64)
cs1 = ax.contour(U, V, Pi, levels=lv, colors=BLUE, linewidths=1.1)
cs2 = ax.contour(U, V, C2, levels=lv, colors=YELLOW, linewidths=1.3, linestyles='--')
ax.clabel(cs1, fmt='%.2f', fontsize=6.5, inline_spacing=2, manual=[(0.85, 0.118), (0.85, 0.294), (0.8, 0.625), (0.9, 0.833)])
gp = [0, 0.5, 1]
P = [(a, b) for a in gp for b in gp]
ax.scatter([p[0] for p in P], [p[1] for p in P], s=16, color=RED, zorder=5, clip_on=False)
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([0, 0.5, 1]); ax.set_yticks([0, 0.5, 1])
ax.set_xlabel('$u$', labelpad=1); ax.set_ylabel('$v$', labelpad=1); ax.set_box_aspect(1)
agree = {f'{a},{b}': [a*b, 0.5*min(a, b)+0.5*max(a+b-1, 0)] for a, b in P}
save(fig, HERE, 'figure', {'grid_values_Pi_C2': agree, 'at_quarter': [1/16, 1/8]})
