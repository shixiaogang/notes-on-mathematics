from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
sys.path.insert(0, str(ROOT/"figures/05-optimization/02-smooth-optimization/matplotlib/qn-common"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
from qnlib import *
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = "#4C4D4F"

# f=x1^2+4x2^2，x0=(4,1)。绿：SR1，W0=I，单位步；黄：BFGS，W0=I，精确线搜索。
A = np.diag([2., 8.]); x = np.array([4., 1.]); W = np.eye(2); xs = [x.copy()]
for t in range(3):
    g = A@x
    if np.linalg.norm(g) < 1e-12: break
    s = -W@g; y = A@s; w = s-W@y
    den = float(w@y)
    if abs(den) > 1e-12: W = W+np.outer(w, w)/den
    x = x+s; xs.append(x.copy())
xs = np.array(xs)
xb = np.array([[4, 1], [2.4, -.6], [0, 0]])
fig, ax = figure(width_mm=78, height_mm=70)
X, Y = np.meshgrid(np.linspace(-5.4, 5.4, 500), np.linspace(-7.9, 2.2, 500))
ax.contour(X, Y, X*X+4*Y*Y, levels=[2, 10, 20, 40, 80, 200], colors=[BLUE], linewidths=.75)
ax.plot(xs[:, 0], xs[:, 1], '-o', color=GREEN, lw=1.4, ms=3.4, mew=0)
ax.plot(xb[:, 0], xb[:, 1], '-o', color=YELLOW, lw=1.3, ms=2.8, mew=0, zorder=5)
ax.plot([0], [0], 'o', ms=4, color=RED, mew=0, zorder=7)
ax.text(4.15, 1.2, '$x^{(0)}$', color=INK); ax.text(-3.75, -7.35, '$x^{(1)}$', color=INK); ax.text(-4.3, .9, '$x^{(2)}$', color=INK); ax.text(.3, .35, '$x^{(3)}$', color=INK)
ax.set_aspect('equal'); ax.set_xlim(-5.4, 5.4); ax.set_ylim(-7.9, 2.2); ax.set_xlabel('$x_1$', labelpad=1); ax.set_ylabel('$x_2$', labelpad=1)
save(fig, HERE, 'figure', {'sr1': xs.tolist(), 'W_final': W.tolist()})
