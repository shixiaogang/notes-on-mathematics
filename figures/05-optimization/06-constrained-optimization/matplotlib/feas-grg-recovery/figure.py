from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
y0, z0, G = .8, .6, -.75; zc = .7875; yp = y0+G*(zc-z0); ys = [yp]
for _ in range(3): ys.append(ys[-1]-(ys[-1]**2+zc**2-1)/(2*ys[-1]))
ax = axs[0]; Z = np.linspace(.5, .9, 200); ax.plot(Z, np.sqrt(1-Z**2), color=EDGE, lw=1.8); ax.plot([.55, .86], [y0+G*(.55-z0), y0+G*(.86-z0)], color=YELLOW, lw=1.2)
dot(ax, (z0, y0), GREEN, ms=4.8); hollow(ax, (zc, yp), YELLOW, ms=4.8); arrow(ax, (zc, yp), (zc, ys[2]), GREEN, lw=1.2, ms=6); dot(ax, (zc, ys[3]), GREEN, ms=4.8)
ax.text(zc+.012, yp+.015, '切向预测', fontsize=7.5); ax.text(zc-.012, ys[3]-.022, '恢复点', fontsize=7.5, ha='right')
setup(ax, (.53, .9), (.42, .9), [.6, .75, .9], [.5, .7, .9], xl='$z$', yl='$y$')
ax = axs[1]
def newton(zc, y, it=8):
    r = []
    for _ in range(it):
        c = y*y+zc*zc-1; r.append(abs(c)); y = y-c/(2*y)
    return r
ax.semilogy(range(8), np.maximum(newton(.7875, yp), 1e-16), '-o', color=GREEN, lw=1.4, ms=3, mew=0)
yl = y0+G*(1.2-z0); ax.semilogy(range(8), newton(1.2, yl), '-o', color=RED, lw=1.4, ms=3, mew=0)
ax.text(1.4, 4, '$z=1.2$', color=RED, fontsize=8); ax.text(4.0, 1.2e-9, '$z=0.7875$', color=GREEN, fontsize=8)
setup(ax, (0, 7), (1e-15, 30), [0, 2, 4, 6], [1e-12, 1e-6, 1], xl='Newton 轮数', yl='$|c(y,z)|$')
panels(fig, .1, .985, .98, .2, .36); tags(fig, axs)
save(fig, HERE, 'figure', {'y_newton': ys, 'predicted': yp})
