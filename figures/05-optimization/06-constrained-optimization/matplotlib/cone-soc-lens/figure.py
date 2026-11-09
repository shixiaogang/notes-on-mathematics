from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cone-common"))
from cone_fig import *
HERE = Path(__file__).resolve().parent
# SOCP: min x2 s.t. ||x||<=5, ||x-(6,0)||<=5. Optimum (3,-4); dual u1=(-3/8,1/2), u2=(3/8,1/2), tau=5/8.
fig, ax = figure(width_mm=88, height_mm=70)
xl, yl = (-1.5, 7.9), (-5.6, 3.6)
X, Y = grid2(xl, yl, 700)
mask = (X**2+Y**2 <= 25) & ((X-6)**2+Y**2 <= 25)
ax.contourf(X, Y, mask.astype(float), levels=[.5, 1.5], colors=[BLUE_FILL], zorder=1)
th = np.linspace(0, 2*np.pi, 400)
for cx in (0, 6): ax.plot(cx+5*np.cos(th), 5*np.sin(th), color=BLUE, lw=.95, zorder=2)
for v in (-3, -2, -1, 0): pass
for lev in (-4, -2.5, -1):
    ax.plot(xl, [lev, lev], color=BLUE, lw=.7, ls=(0, (4, 2)), zorder=2)
x = np.array([3., -4.]); s = 3.2
u1 = np.array([-3/8, .5]); u2 = np.array([3/8, .5])
arrow(ax, x, x+s*u1, color=PURPLE, lw=1.3); arrow(ax, x, x+s*u2, color=PURPLE, lw=1.3)
arrow(ax, x, x+s*(u1+u2), color=BLUE, lw=1.5, z=6)
dot(ax, x); dot(ax, (0, 0), INK, ms=3); dot(ax, (6, 0), INK, ms=3)
setup(ax, xl, yl, [0, 2, 4, 6], [-4, -2, 0, 2])
ax.text(.12, .22, '$a_1$', fontsize=8); ax.text(6.12, .22, '$a_2$', fontsize=8)
ax.text(3, -5.35, '$x^*=(3,-4)$', color=RED, fontsize=7.5, ha='center', va='center')
ax.text(2.45, -2.8, '$u_1$', color=PURPLE, fontsize=8, ha='center'); ax.text(3.55, -2.8, '$u_2$', color=PURPLE, fontsize=8, ha='center')
ax.text(3.12, -.45, '$q$', color=BLUE, fontsize=8)
save(fig, HERE, 'figure', {'p*': -4, 'u1': u1.tolist(), 'u2': u2.tolist(), 'tau': .625, 'arrow_scale': s})
