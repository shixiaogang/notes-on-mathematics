from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# mixed problem -u''=1, u(0)=0, u'(1)=0; residual R(v)=int u'v'-int f v.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.085, wspace=.3, bottom=.27)
ax = axes[0]
ax.plot(X, X-X**2/2, color=BLUE, lw=1.4); ax.plot(X, X*(1-X)/2, color=YELLOW, lw=1.5)
dot(ax, 0, 0)
lab(ax, .62, .49, '$u_{*}$', BLUE, va='top', ha='left'); lab(ax, .5, .15, r'$\tilde{u}$', YELLOW, ha='center', va='bottom')
ax.set_xlim(-.02, 1.04); ax.set_ylim(-.02, .56); ax.set_xticks([0, 1]); ax.set_yticks([0, .5]); hat01(ax, yl='$u$')
ax = axes[1]
vs = [('x', 1.), ('x(1-x)', 0.), ('2x', 2.), ('x^2', 1.)]
s = np.linspace(-.1, 2.2, 3)
ax.plot(s, 0*s, color=BLUE, lw=1.4); ax.plot(s, -s/2, color=YELLOW, lw=1.5)
for name, b in vs:
    dot(ax, b, -b/2, RED, 3.8)
lab(ax, 2.2, .04, 'R(v) 对 $u_*$'.replace('R(v) 对 $u_*$', '$u_{*}$'), BLUE, ha='right', va='bottom'); lab(ax, 1.55, -.83, r'$\tilde{u}$', YELLOW, ha='right', va='top')
ax.set_xlim(-.1, 2.25); ax.set_ylim(-1.2, .25); ax.set_xticks([0, 1, 2]); ax.set_yticks([-1, -.5, 0]); hat01(ax, '$v(1)$', r'$R(v)$')
tags(fig, axes)
def R(du, dv, v):
    return float(np.trapezoid(du*dv-v, X))
ut = .5-X
print([R(ut, 1+0*X, X), R(ut, 1-2*X, X*(1-X)), R(ut, 2*X, X**2), R(1-X, 1+0*X, X), R(1-X, 2*X, X**2)])
save(fig, HERE, 'figure', {'R_wrong(x)': R(ut, 1+0*X, X), 'R_wrong(x^2)': R(ut, 2*X, X**2), 'R_true(x)': R(1-X, 1+0*X, X)})
