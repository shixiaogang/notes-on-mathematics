from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Second-order cone with one-dimensional u: barrier level sets and exact step to the boundary.
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
u, t = np.meshgrid(np.linspace(-3, 3, 600), np.linspace(.02, 3.2, 500)); om = t**2-u**2
with np.errstate(all='ignore'): Z = np.ma.masked_where(om <= 1e-6, -np.log(om))
a.fill([0, 3.2, -3.2], [0, 3.2, 3.2], color=BLUE_FILL, zorder=0)
a.contour(u, t, Z, levels=[-1.8, -1.2, -.6, 0, .8, 1.6], colors=BLUE, linewidths=.75, linestyles='solid', zorder=1)
a.plot([-3.2, 0, 3.2], [3.2, 0, 3.2], color=EDGE, lw=1.7, zorder=2)
x = np.array([1., 2.]); d = np.array([2., -1.]); am = 1/3
a.annotate('', xy=x+.9*am*d*1.1, xytext=x, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.3), zorder=5)
a.plot(*x, 'o', color=GREEN, ms=4.5, zorder=6); a.plot(*(x+am*d), 'o', color=RED, ms=4.5, zorder=6)
a.text(.86, 2.08, '$(1,2)$', fontsize=7.5, ha='right', zorder=7); a.text(1.85, 1.5, '$(5/3,5/3)$', fontsize=7.5, zorder=7)
a.set_xlim(-3.2, 3.2); a.set_ylim(0, 3.2); a.set_aspect('equal'); tag(a, '$u$', '(a)'); a.set_ylabel('$t$', labelpad=1)
al = np.linspace(-.05, am-1e-4, 500); w = 3-8*al-3*al**2
b.plot(al, -np.log(w), color=BLUE, lw=1.5); b.axvline(am, color=EDGE, lw=1.7)
dphi = 8/3; ddphi = (8/3)**2+2*3/3
qq = -np.log(3)+dphi*al+.5*ddphi*al**2; b.plot(al, qq, color=YELLOW, lw=1.6, ls='--')
b.set_xlim(-.05, .38); b.set_ylim(-1.3, 3.2); b.text(am-.006, 2.8, '$\\alpha_{\\max}=1/3$', fontsize=7.5, ha='right'); tag(b, '$\\alpha$', '(b)')
save(fig, OUT, 'figure', {'alpha_max': am, 'dphi': dphi, 'ddphi': ddphi})
