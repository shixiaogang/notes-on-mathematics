from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# f(x,theta)=(x^2-1)^2+theta*x: wells at theta=0.3, stationary branches, branch values and global value.
fig, axs = figure(width_mm=112, height_mm=46, ncols=3)
F = lambda x, t: (x**2-1)**2+t*x
ax = axs[0]
X = np.linspace(-1.55, 1.55, 400)
ax.plot(X, F(X, .3), color=BLUE, lw=1.4)
th = .3
r = np.sort(np.roots([4, 0, -4, th]).real)
ax.plot([r[2]], [F(r[2], th)], 'o', mfc='white', mec=GREEN, mew=1.1, ms=4.4, zorder=7)
opt_point(ax, (r[0], F(r[0], th)))
clean(ax, (-1.6, 1.6), (-.6, 2.2), xlabel='$x$', sub='(a)')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([0, 1, 2]); ax.text(-.46, 1.95, r'$\theta=0.3$', fontsize=8)
T = np.linspace(-1.9, 1.9, 761)
lo, hi, mid = [], [], []
tc = 8/(3*np.sqrt(3))
TP = T[(T > -tc) & (T < tc)]
# branch tracking inside (-tc, tc): three real roots
R = np.array([np.sort(np.roots([4, 0, -4, t]).real) for t in TP])
Tneg = np.linspace(-tc+1e-6, 1.9, 500); Tpos = np.linspace(-1.9, tc-1e-6, 500)
xp = np.array([max(np.roots([4, 0, -4, t])[abs(np.roots([4, 0, -4, t]).imag) < 1e-7].real) for t in Tpos])
xm = np.array([min(np.roots([4, 0, -4, t])[abs(np.roots([4, 0, -4, t]).imag) < 1e-7].real) for t in Tneg])
ax = axs[1]
ax.plot(Tpos, xp, color=GREEN, lw=1.1, ls='--', dashes=(3, 1.6)); ax.plot(Tneg, xm, color=GREEN, lw=1.1, ls='--', dashes=(3, 1.6))
ax.plot(TP, R[:, 1], color=MUTED, lw=.85, ls=':')
ax.plot(Tpos[Tpos < 0], xp[Tpos < 0], color=RED, lw=1.6)
ax.plot(Tneg[Tneg > 0], xm[Tneg > 0], color=RED, lw=1.6)
clean(ax, (-1.9, 1.9), (-1.75, 1.75), xlabel=r'$\theta$', sub='(b)')
ax.set_ylabel('$x$', labelpad=1); ax.set_xticks([-1, 0, 1]); ax.set_yticks([-1, 0, 1])
ax = axs[2]
vp, vm = F(xp, Tpos), F(xm, Tneg)
ax.plot(Tpos, vp, color=GREEN, lw=1.1, ls='--', dashes=(3, 1.6)); ax.plot(Tneg, vm, color=GREEN, lw=1.1, ls='--', dashes=(3, 1.6))
V = np.minimum(np.interp(T, Tpos, vp, left=np.inf, right=np.inf), np.interp(T, Tneg, vm, left=np.inf, right=np.inf))
ax.plot(T, V, color=RED, lw=1.5)
clean(ax, (-1.9, 1.9), (-2.1, .75), xlabel=r'$\theta$', sub='(c)')
ax.set_xticks([-1, 0, 1]); ax.set_yticks([-2, -1, 0])
save(fig, Path(__file__).resolve().parent, 'figure', {'objective': '(x^2-1)^2+theta*x', 'fold_theta': float(tc)})
