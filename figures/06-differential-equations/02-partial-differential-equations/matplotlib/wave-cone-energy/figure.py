from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: local energy of the tent solution inside the backward cone of (0,3), c=1.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
ax = axs[0]; style(ax); xs = np.linspace(-4, 4, 801); ts = np.linspace(0, 3, 481); X, TT = np.meshgrid(xs, ts)
field(ax, wave_tent(X, TT), [-4, 4, 0, 3], vmax=1.)
ax.plot([-3, 0, 3], [0, 3, 0], color=LINE, lw=1.7)
ax.plot([-3, 3], [0, 0], color=RED, lw=2.2, clip_on=False, zorder=5)
ax.plot([0], [3], 'o', ms=4, color=RED, zorder=5)
ax.set_xlim(-4, 4); ax.set_ylim(0, 3); ax.set_xticks([-3, 0, 3]); ax.set_yticks([0, 1, 2, 3]); ax.set_ylabel('$t$'); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax); t = np.linspace(0, 3, 601); x = np.linspace(-3.2, 3.2, 25601); dx = x[1]-x[0]
e = []
for tt in t:
    ut = .5*(-tent_d(x-tt)+tent_d(x+tt)); ux = .5*(tent_d(x-tt)+tent_d(x+tt)); m = np.abs(x) <= 3-tt
    e.append(.5*np.sum((ut[m]**2+ux[m]**2))*dx)
e = np.array(e)
ax.plot(t, e, color=BLUE, lw=1.5)
ax.plot([1, 2], [1, 0], 'o', ms=3.4, color=RED, clip_on=False, zorder=5)
ax.set_xlim(0, 3); ax.set_ylim(0, 1.2); ax.set_xticks([0, 1, 2, 3]); ax.set_ylabel('$e(t)$'); sub(ax, 'b', '$t$')
print('e(0),e(1),e(1.5),e(2)=', e[0], e[200], e[300], e[400])
save(fig, HERE(__file__), 'figure', {'formula': 'e(t)=(1/2) int_{|x|<=3-t}(u_t^2+u_x^2) dx by quadrature; equals 1, then 2-t, then 0'})
