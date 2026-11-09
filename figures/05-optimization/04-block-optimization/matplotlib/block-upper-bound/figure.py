from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) phi(z)=sqrt(1+z^2)-z/2, block constant L=1, current z=2. (b) coordinate gradient on x1^2+x1x2+x2^2, steps 1/L_j=1/2 and 1/L=1/3.
fig, (a, b) = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .085, .985, .97, .23, wspace=.27)
phi = lambda z: np.sqrt(1+z*z)-z/2; dphi = lambda z: z/np.sqrt(1+z*z)-.5
z = np.linspace(-2.2, 4, 400); x = 2.; g = dphi(x); u = phi(x)+g*(z-x)+.5*(z-x)**2
a.plot(z, phi(z), color=BLUE, lw=1.4); a.plot(z, u, color=GREEN, lw=1.4)
zp = x-g; zs = 1/np.sqrt(3)
a.plot([x], [phi(x)], 'o', color=GREEN, ms=4.5, mew=0, zorder=5); a.plot([zp], [phi(zp)+g*(zp-x)+.5*(zp-x)**2], 'o', color=GREEN, ms=4.5, mew=0, zorder=5, mfc='white', mec=GREEN)
a.plot([zp], [phi(zp)], 's', color=GREEN, ms=3.8, mew=0, zorder=5); opt(a, zs, phi(zs))
a.text(-1.9, 3.1, r'$\varphi$', fontsize=8, color=INK); a.text(-.05, 3.05, '$u$', fontsize=7.5, color=INK); a.text(2.14, 1.08, '$z$', fontsize=7.5, color=INK); a.text(1.42, .84, '$z^+$', fontsize=7.5, color=INK)
a.set_xlabel('$z$', labelpad=1); a.set_xlim(-2.2, 4); a.set_ylim(.4, 3.5)
contour_c(b, (-3.2, 4.2), (-2.6, 4.8), [.75, 3, 12, 22, 37])
def bcgd(al, K=6):
    x = np.array([3., 4.]); P = [x.copy()]
    for k in range(K):
        i = k % 2; x[i] -= al*(2*x[i]+x[1-i]); P.append(x.copy())
    return np.array(P)
Py, Pg = bcgd(1/3), bcgd(1/2); path(b, Py, YELLOW, lw=1.6); path(b, Pg, GREEN); opt(b)
b.text(-2.9, 4.3, r'$\alpha=\frac{1}{2}$', fontsize=7.5, color=INK); b.text(.1, 3.05, r'$\alpha=\frac{1}{3}$', fontsize=7.5, color=INK)
b.set_xlabel('$x_1$', labelpad=1); b.set_ylabel('$x_2$', labelpad=1); b.set_aspect('equal'); b.set_xlim(-3.2, 4.2); b.set_ylim(-2.6, 4.8)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'z_plus': float(zp), 'Py': Py.tolist()})
print(zp, phi(2), phi(zp), Py)
