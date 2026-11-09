from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# Price example: min .5(x1-1-th)^2+.5(x2-1)^2, th*x1+x2<=2, x>=0. Exact piecewise solution vs first-order prediction at th=1.
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
def exact(th):
    if th > 2: return np.array([2/th, 0.])  # x2=0 active
    lam = (th**2+th-1)/(1+th**2)
    if lam < 0: return np.array([1+th, 1.])
    return np.array([1+th-lam*th, 1-lam])
x0 = exact(1.); d = np.array([-.5, -1.])
ax = axs[0]
T = np.linspace(.45, 3, 500); E2 = np.array([exact(t)[1] for t in T])
ax.axvspan((np.sqrt(5)-1)/2, 2, facecolor=GREEN_FILL, edgecolor='none', zorder=0)
ax.plot(T, E2, color=BLUE, lw=1.4, zorder=3); ax.plot(T, x0[1]+d[1]*(T-1), color=YELLOW, lw=1.3, zorder=2)
opt_point(ax, (1, x0[1]))
ax.text(.73, 1.02, '$x_2$', fontsize=8, color=BLUE); ax.text(1.62, -.82, '预测', fontsize=7.5, color=YELLOW, va='center')
clean(ax, (.45, 3), (-1.1, 1.2), xlabel=r'$\theta$', sub='(a)', ylabel='$x_2$'); ax.set_xticks([1, 2, 3]); ax.set_yticks([-1, 0, 1])
ax = axs[1]
H = np.geomspace(1e-3, 3, 120)
err = np.array([np.linalg.norm(exact(1+h)-x0-h*d) for h in H])
ax.loglog(H, err, color=BLUE, lw=1.4, zorder=3)
ax.loglog(H[H < .3], 1.2*H[H < .3]**2, color=MUTED, lw=.85, ls=':', zorder=2)
ax.axvline(1, color=ACTIVE, lw=.85, ls='--', zorder=1)
ax.text(.02, 2.2e-3, '$h^2$', fontsize=8, color=MUTED, ha='right', va='bottom')
ax.text(.9, 2e-6, r'换活动集', fontsize=7.5, ha='right', color=INK)
clean(ax, None, None, xlabel='$h$', sub='(b)', ylabel='预测误差')
ax.minorticks_off()
save(fig, Path(__file__).resolve().parent, 'figure', {'x0': list(x0), 'dx': list(d), 'err@.1': float(np.linalg.norm(exact(1.1)-x0-.1*d))})
for h in (.1, .01): print(h, exact(1+h), x0+h*d, np.linalg.norm(exact(1+h)-x0-h*d))
