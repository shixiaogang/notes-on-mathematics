from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# Source mu = N(0, diag(1,0)) on the horizontal axis; target nu = N(0, I).
# Unique optimal coupling: Y = (X_1, Z), Z ~ N(0,1) independent; cost E Z^2 = 1 = W_2^2.
# 40 coupled pairs drawn with seed 729: source points (blue, on the axis), targets (green), vertical moves (gray).
rng = np.random.default_rng(SEED)
x1 = rng.standard_normal(40); z = rng.standard_normal(40)
fig, ax = figure(width_mm=56, height_mm=52)
panel(fig, left=.14, right=.97, top=.97, bottom=.12)
ax.plot([-3, 3], [0, 0], color=BLUE, lw=1.4)
for s, t in zip(x1, z):
    ax.plot([s, s], [0, t], color=STROKE, lw=.6)
ax.plot(x1, z, 'o', ms=2.6, color=GREEN, mew=0)
ax.plot(x1, 0*x1, 'o', ms=2.6, color=BLUE, mew=0)
ax.set_xlim(-3, 3); ax.set_ylim(-3, 3); ax.set_aspect('equal')
ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
save(fig, HERE, 'figure', {'seed': SEED, 'n': 40, 'mean_sq_move_sample': float(np.mean(z**2)), 'W2sq_exact': 1.0})
