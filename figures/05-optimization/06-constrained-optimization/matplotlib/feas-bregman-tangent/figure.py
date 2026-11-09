from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax = axs[0]; h = lambda t: .5*t**2; dh = lambda t: t; X_ = np.linspace(0, 1.25, 300); x, u = .3, 1.
ax.plot(X_, h(X_), color=BLUE, lw=1.4); 
for p, c in ((x, GREEN), (u, YELLOW)): ax.plot(X_, h(p)+dh(p)*(X_-p), color=c, lw=1.2)
ax.plot([u, u], [h(x)+dh(x)*(u-x), h(u)], color=GREEN, lw=1.8); ax.plot([x, x], [h(u)+dh(u)*(x-u), h(x)], color=YELLOW, lw=1.8)
ax.text(u+.03, .25, '$D_h(u,x)$', fontsize=7.5, color=INK, va='center', ha='left'); ax.text(x+.03, -.05, '$D_h(x,u)$', fontsize=7.5, va='center')
setup(ax, (0, 1.55), (-.5, .8), [.3, 1.], [0, .5]); ax.set_xticklabels(['$x$', '$u$'])
ax = axs[1]; h = lambda t: t*np.log(t); dh = lambda t: np.log(t)+1; X_ = np.linspace(.004, 1.15, 400); x, u = .1, .8
ax.plot(X_, h(X_), color=BLUE, lw=1.4)
for p, c in ((x, GREEN), (u, YELLOW)): ax.plot(X_, h(p)+dh(p)*(X_-p), color=c, lw=1.2)
ax.plot([u, u], [h(x)+dh(x)*(u-x), h(u)], color=GREEN, lw=1.8); ax.plot([x, x], [h(u)+dh(u)*(x-u), h(x)], color=YELLOW, lw=1.8)
ax.text(u+.03, -.6, '$D_h(u,x)$', fontsize=7.5, va='center'); ax.text(x+.03, -1.0, '$D_h(x,u)$', fontsize=7.5, va='center')
setup(ax, (0, 1.4), (-1.5, .3), [.1, .8], [-1, 0]); ax.set_xticklabels(['$x$', '$u$'])
panels(fig, .06, .985, .98, .2, .2); tags(fig, axs)
save(fig, HERE, 'figure', {'left': 'h=t^2/2', 'right': 'h=t log t', 'points_right': [.1, .8]})
