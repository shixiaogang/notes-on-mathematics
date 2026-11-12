"""Joint laws without a planar density. (a) X=Y~Unif(0,1), kernel delta_y (red point at y=0.3);
(b) random coin n=3: mass of (U,N) on lines N=k with densities C(3,k)u^k(1-u)^(3-k) drawn as ridges (scale 0.8)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=104, height_mm=48, ncols=2)
a.plot([0, 1, 1, 0, 0], [0, 0, 1, 1, 0], color=STROKE, lw=0.6)
a.plot([0, 1], [0, 1], color=BLUE, lw=2.0)
a.plot([0.3, 0.3], [0, 0.3], color=STROKE, lw=0.7, ls=DASH)
a.scatter([0.3], [0.3], s=18, color=RED, zorder=4)
a.set_aspect('equal'); a.set_xlim(-0.03, 1.03); a.set_ylim(-0.03, 1.03)
a.set_xticks([0, 0.3, 1]); a.set_yticks([0, 0.3, 1]); a.set_xlabel('$y$', labelpad=1); a.set_ylabel('$x$', rotation=0)
u = np.linspace(0, 1, 300)
cols = [BLUE, YELLOW, PURPLE, GREEN]
for k in range(4):
    d = math.comb(3, k)*u**k*(1 - u)**(3 - k)
    b.plot([0, 1], [k, k], color=STROKE, lw=0.6)
    b.plot(u, k + 0.8*d, color=cols[k], lw=1.4)
b.set_xlim(0, 1); b.set_ylim(-0.2, 3.95); b.set_xticks([0, 0.5, 1]); b.set_yticks([0, 1, 2, 3])
b.set_xlabel('$u$', labelpad=1); b.set_ylabel('$k$', rotation=0)

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'ridge_scale': 0.8, 'n': 3})
