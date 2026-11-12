"""Triangle model: P(X>=3/4, Y<=1/2) = int_0^{1/2} K(y,[3/4,1]) f_Y(y) dy = 1/4.
(a) rectangle in the triangle; (b) integrand K(y,A)f_Y(y) = 1/2 (y<=3/4), 2(1-y) (y>3/4)."""
from pathlib import Path
import sys, math
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=104, height_mm=48, ncols=2)
a.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE, lw=1.1)
a.fill([0.75, 1, 1, 0.75], [0, 0, 0.5, 0.5], color=BLUE_FILL, lw=0)
a.plot([0.75, 1, 1, 0.75, 0.75], [0, 0, 0.5, 0.5, 0], color=BLUE, lw=0.8)
a.set_aspect('equal'); a.set_xlim(-0.02, 1.04); a.set_ylim(-0.02, 1.04)
a.set_xticks([0, 0.75, 1]); a.set_yticks([0, 0.5, 1]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$y$', rotation=0)
y = np.linspace(0, 0.999, 600)
g = tri_kernel(y, 0.75, 1)*2*(1 - y)
yy = np.linspace(0, 0.5, 100)
b.fill_between(yy, 0, tri_kernel(yy, 0.75, 1)*2*(1 - yy), color=BLUE_FILL, lw=0)
b.plot(y, g, color=BLUE, lw=1.4)
b.text(0.12, 0.22, '面积 1/4', fontsize=7.5)
b.set_xlim(0, 1); b.set_ylim(0, 0.62); b.set_xticks([0, 0.5, 0.75, 1]); b.set_yticks([0, 0.25, 0.5])
b.set_xlabel('$y$', labelpad=1); b.set_ylabel('$K(y,A)\\,f_Y(y)$')

area = float(np.trapezoid(tri_kernel(yy, 0.75, 1)*2*(1 - yy), yy))
tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'A': '[3/4,1]', 'B': '[0,1/2]', 'area_numeric': area, 'exact': 0.25})
