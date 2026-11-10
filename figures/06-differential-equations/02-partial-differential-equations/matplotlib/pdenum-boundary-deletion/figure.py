from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Correct lifted system vs dropping the boundary column on the running example, h=1/4.
n = 4; h = 1/n; x = np.linspace(0, 1, n+1); X = np.linspace(0, 1, 401); xi = x[1:-1]
K = (2*np.eye(3)-np.eye(3, k=1)-np.eye(3, k=-1))/h; b = 2*(1-np.cos(PI*h))/h*np.sin(PI*xi)
good = np.linalg.solve(K, b+np.array([0, 0, 1/h])); bad = np.linalg.solve(K, b)
fig, ax = figure(width_mm=88, height_mm=50)
ax.plot(X, uex(X), color=BLUE, lw=1.4)
ax.plot(x, np.r_[0, good, 1], color=GREEN, lw=1.3, marker='o', ms=3.8, mew=0)
ax.plot(x, np.r_[0, bad, 0], color=RED, lw=1.3, marker='o', ms=3.8, mew=0)
ax.plot([0, 1], [0, 1], 'o', ms=4.8, color=RED, mew=0, zorder=6, clip_on=False)
ax.set_xlim(-.02, 1.02); ax.set_ylim(0, 1.75); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$u$', labelpad=1)
save(fig, HERE, 'figure', {'correct': good.tolist(), 'dropped': bad.tolist()}); print(good, bad)
