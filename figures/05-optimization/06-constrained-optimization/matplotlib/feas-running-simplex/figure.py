from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
# Running example on the simplex: contours of f, start x0, optimum x*, active edge x3=0.
fig, ax = figure(width_mm=78, height_mm=66); triangle(ax); contours(ax); off(ax, (-.14, 1.14), (-.12, .96))
active(ax, V[0], V[1]); dot(ax, bary(XS)); dot(ax, bary(X0), GREEN)
ax.text(bary(X0)[0]-.03, bary(X0)[1]+.01, '$x^{(0)}$', ha='right', fontsize=8)
ax.text(bary(XS)[0], bary(XS)[1]-.035, '$x^*=(\\frac{1}{2},\\frac{1}{2},0)$', ha='center', va='top', fontsize=8)
save(fig, HERE, 'figure', {'f': '((x1-1)^2+4(x2-5/8)^2+2x3^2)/2', 'x0': [.1, .2, .7], 'xstar': [.5, .5, 0]})
