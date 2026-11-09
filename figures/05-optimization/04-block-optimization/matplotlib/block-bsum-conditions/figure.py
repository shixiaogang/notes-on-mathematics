from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# phi(z)=sqrt(1+z^2)-z/2 at x=2. (a) valid quadratic upper bound. (b) Taylor model: not an upper bound. (c) upper bound with a kink: value matches, slope does not.
phi = lambda z: np.sqrt(1+z*z)-z/2; dphi = lambda z: z/np.sqrt(1+z*z)-.5; d2 = lambda z: (1+z*z)**(-1.5)
fig, ax = figure(width_mm=112, height_mm=50, ncols=3)
panel(fig, .05, .99, .97, .27, wspace=.14)
z = np.linspace(-4, 4.5, 500); x = 2.; g = dphi(x); h = d2(x); p0 = phi(x)
models = [p0+g*(z-x)+.5*(z-x)**2, p0+g*(z-x)+.5*h*(z-x)**2, p0+1.5*abs(z-x)]
zm = [x-g, x-g/h, x]
for a, m, zz, s in zip(ax, models, zm, '(a) (b) (c)'.split()):
    a.plot(z, phi(z), color=BLUE, lw=1.4); a.plot(z, m, color=GREEN, lw=1.4)
    a.plot([x], [p0], 'o', color=GREEN, ms=4.2, mew=0, zorder=5)
    a.plot([zz], [phi(zz)], 's', color=(RED if s == '(b)' else GREEN), ms=3.8, mew=0, zorder=6)
    a.set_xlim(-4, 4.5); a.set_ylim(0, 6); a.set_xlabel('$z$', labelpad=1); tag(fig, a, s)
ax[0].set_yticks([0, 2, 4, 6]); ax[1].set_yticklabels([]); ax[2].set_yticklabels([])
ax[1].text(-2.4, phi(-2.4)+.45, r'$\varphi(z^+)$', fontsize=7.5, color=INK, ha='center')
save(fig, HERE, 'figure', {'taylor_min': float(zm[1]), 'phi_at_taylor_min': float(phi(zm[1])), 'phi_x': float(p0)})
print(zm, phi(zm[1]), p0)
