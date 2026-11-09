from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# (a) LMI [[1+x1,x2],[x2,1-x1]]>=0 is the unit disc. (b) lambda_min of [[1,.8,rho],[.8,1,.8],[rho,.8,1]].
fig, axes = figure(width_mm=112, height_mm=58, ncols=2)
panels(fig, .075, .985, .985, .25, .26)
a, b = axes
th = np.linspace(0, 2*np.pi, 300)
a.fill(np.cos(th), np.sin(th), facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.0, zorder=1)
dot(a, (.6, .6), GREEN); dot(a, (.8, .8), RED)
setup(a, (-1.25, 1.25), (-1.25, 1.25), [-1, 0, 1], [-1, 0, 1])
a.text(.5, .62, '$(0.6,0.6)$', fontsize=7.5, ha='right', va='center'); a.text(.76, .98, '$(0.8,0.8)$', fontsize=7.5, ha='center')
r = np.linspace(-.25, 1.25, 400)
lm = np.array([np.linalg.eigvalsh(np.array([[1, .8, x], [.8, 1, .8], [x, .8, 1]]))[0] for x in r])
b.axhline(0, color=MUTED, lw=.85)
b.fill_between(r, -.42, .55, where=(r >= .28) & (r <= 1), facecolor=BLUE_FILL, edgecolor='none', zorder=0)
b.plot(r, lm, color=BLUE, lw=1.5, zorder=3)
for x in (0, .5):
    v = np.linalg.eigvalsh(np.array([[1, .8, x], [.8, 1, .8], [x, .8, 1]]))[0]; dot(b, (x, v), RED if v < 0 else GREEN)
setup(b, (-.25, 1.25), (-.42, .55), [0, .28, .5, 1], [-.25, 0, .25, .5], xl='$\\rho$', yl='$\\lambda_{\\min}$', equal=False)
tags(fig, axes, y=.012)
save(fig, HERE, 'figure', {'lambda_min(0)': float(lm[np.argmin(abs(r))]), 'feasible rho': [.28, 1]})
