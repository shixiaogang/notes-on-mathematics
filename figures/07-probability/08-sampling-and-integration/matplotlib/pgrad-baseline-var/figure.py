from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X ~ N(theta,1), theta = 1, f = x^2.  Single-sample estimator (f(X) - b)(X - theta) with a constant baseline b:
# Var(b) = E[f^2 s^2] - 2b E[f s^2] + b^2 E[s^2] - J'^2 = 34 - 8b + b^2 - 4.
# Dots: b = 0 (30), b = J(1) = 2 (18), b* = E[f s^2]/E[s^2] = 4 (14).  Purple dashed: reparameterization variance 4.
b = np.linspace(-1, 7, 300); V = b**2-8*b+30
fig, ax = figure(width_mm=80, height_mm=50)
panel(fig, left=.13, right=.97, bottom=.19, top=.96)
ax.plot(b, V, color=BLUE, lw=1.4)
ax.axhline(4, color=PURPLE, lw=.9, ls=DASH)
for bb, c, s, dx, dy in [(0, BLUE, '30', .2, 1.0), (2, GREEN, '18', .2, 1.0), (4, RED, '14', -.25, -4.0)]:
    dot(ax, bb, bb*bb-8*bb+30, c); lab(ax, bb+dx, bb*bb-8*bb+30+dy, s, c)
lab(ax, 4.7, 5.2, '重参数化 4', PURPLE)
ax.set_xlim(-1, 7); ax.set_ylim(0, 42); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, 10, 20, 30, 40])
axlab(ax, r'$b$')
save(fig, HERE, 'figure', {'var_b0': 30, 'var_bJ': 18, 'var_bstar': 14, 'b_star': 4, 'var_reparam': 4})
