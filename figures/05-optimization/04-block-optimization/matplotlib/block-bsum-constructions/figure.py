from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) phi(z)=sqrt(1+z^2)-z/2 at x=2: quadratic bound (L=1) and proximal bound (beta=1). (b) phi(z)=(z^2-1)^2 at x=0.3: proximal term beta=10 makes the model strongly convex.
phi = lambda z: np.sqrt(1+z*z)-z/2; dphi = lambda z: z/np.sqrt(1+z*z)-.5
fig, (a, b) = figure(width_mm=112, height_mm=56, ncols=2)
panel(fig, .075, .985, .97, .25, wspace=.25)
z = np.linspace(-2, 4, 500); x = 2.; g = dphi(x); p0 = phi(x)
qu = p0+g*(z-x)+.5*(z-x)**2; pr = phi(z)+.5*(z-x)**2
a.plot(z, phi(z), color=BLUE, lw=1.4); a.plot(z, qu, color=GREEN, lw=1.4); a.plot(z, pr, color=YELLOW, lw=1.6)
pm = z[np.argmin(pr)]; a.plot([x], [p0], 'o', color=GREEN, ms=4.5, mew=0, zorder=5); a.plot([x-g], [p0+g*(-g)+.5*g*g], 'o', mfc='white', mec=GREEN, ms=4.5, zorder=5); a.plot([pm], [pr.min()], 'o', mfc='white', mec=YELLOW, ms=4.5, zorder=5)
a.text(-1.75, 1.5, r'$\varphi$', fontsize=8, color=INK); a.text(-.2, 3.05, '二次上界', fontsize=7.5, color=INK); a.text(-1.15, 4.1, '距离上界', fontsize=7.5, color=INK)
a.set_xlim(-2, 4); a.set_ylim(.4, 4.6); a.set_xlabel('$z$', labelpad=1)
z = np.linspace(-1.6, 1.6, 500); x = .3; ph = (z*z-1)**2; u = ph+5*(z-x)**2
b.plot(z, ph, color=BLUE, lw=1.4); b.plot(z, u, color=YELLOW, lw=1.6)
um = z[np.argmin(u)]; b.plot([x], [(x*x-1)**2], 'o', color=GREEN, ms=4.5, mew=0, zorder=5); b.plot([um], [u.min()], 'o', mfc='white', mec=YELLOW, ms=4.5, zorder=5); opt(b, -1, 0); opt(b, 1, 0)
b.text(-1.5, 2.8, r'$\varphi$', fontsize=8, color=INK); b.text(.72, 3.1, '距离上界', fontsize=7.5, color=INK)
b.set_xlim(-1.6, 1.6); b.set_ylim(-.15, 4); b.set_xlabel('$z$', labelpad=1)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'prox_min': float(pm), 'nonconvex_prox_min': float(um)})
print(pm, um)
