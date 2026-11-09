from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Circle h=x1^2+x2^2-1, xbar=(1,0), d=(0,1): straight step (1,t) corrected along grad h(xbar) back to the circle.
fig, ax = figure(width_mm=78, height_mm=66)
t = np.linspace(-.2, 1.05, 300); ax.plot(np.sqrt(np.maximum(1-t*t, 0)), t, color=BLUE, lw=1.4, zorder=2)
setup(ax, (.2, 1.42), (-.12, 1.0), [.4, .8, 1.2], [0, .5, 1])
ax.plot([1, 1], [-.12, 1.0], color=YELLOW, lw=1.3, ls=(0, (4, 2)), zorder=2)
for s in (.3, .55, .8):
    q = np.array([1., s]); r = np.array([np.sqrt(1-s*s), s]); arrow(ax, q, r, color=GREEN, ms=7); hollow(ax, q, YELLOW, ms=4.2); dot(ax, r, GREEN, ms=4.2)
dot(ax, (1, 0), INK, ms=4.5); ax.text(1.03, -.07, '$\\bar{x}$', fontsize=8)
ax.text(1.03, .8, '$\\bar{x}+t\\,d$', fontsize=8, color=INK); ax.text(.77, .66, '$x(t)$', fontsize=8, color=INK, ha='right')
ax.text(1.05, .42, '沿 ∇h 修正', color=INK, fontsize=7.5)
save(fig, HERE, 'figure', {'t': [.3, .55, .8], 'w(t)': [float((np.sqrt(1-s*s)-1)/2) for s in (.3, .55, .8)]})
