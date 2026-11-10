from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：logistic，x0=1/4，T=ln3，J=x(T)。前向 S、反向 lambda 及乘积恒等于 4/3；lambda*x(1-x) 恒为 1/4。RK4 计算。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .07, .985, .955, .28, .24)
T = np.log(3); ts = np.linspace(0, T, 1001)
Z = rk4(lambda t, z: np.array([z[0]*(1-z[0]), (1-2*z[0])*z[1]]), [.25, 1.], ts); x, S = Z[:, 0], Z[:, 1]
rev = ts[::-1]
def xat(t): return logistic(t, .25)
lam = rk4(lambda t, l: -(1-2*xat(t))*l, 1., rev)[::-1]
ax = axes[0]; ax.plot(ts, S, color=GREEN, lw=1.4); ax.plot(ts, lam, color=PURPLE, lw=1.4); ax.plot(ts, S*lam, color=MUTED, lw=1.1, ls=(0, (4, 2)))
ax.plot([0], [lam[0]], 'o', ms=4.2, color=RED, mew=0, zorder=5, clip_on=False); ax.plot([T], [S[-1]], 'o', ms=4.2, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(.22, 1.0, '$z(t)$', color=GREEN, fontsize=7.5, ha='left', va='top'); ax.text(.82, 1.06, '$\\lambda(t)$', color=PURPLE, fontsize=7.5, ha='left', va='bottom'); ax.text(.55, 1.36, '$\\lambda z=4/3$', color=MUTED, fontsize=7.5, ha='left', va='bottom')
ax.set_xlim(0, T); ax.set_ylim(.85, 1.5); ax.set_xticks([0, T/2, T]); ax.set_xticklabels(['0', '$T/2$', '$T$']); ax.set_yticks([1, 4/3]); ax.set_yticklabels(['1', '4/3']); ax.set_xlabel('$t$', labelpad=0)
ax = axes[1]; f = x*(1-x); ax.plot(ts, f, color=BLUE, lw=1.4); ax.plot(ts, lam, color=PURPLE, lw=1.4); ax.plot(ts, lam*f, color=GREEN, lw=1.4)
ax.text(.15, 1.12, '$\\lambda$', color=PURPLE, fontsize=7.5, va='top'); ax.text(.55, .07, '$x(1-x)$', color=BLUE, fontsize=7.5); ax.text(.45, .31, '$\\lambda x(1-x)=1/4$', color=GREEN, fontsize=7.5)
ax.set_xlim(0, T); ax.set_ylim(0, 1.45); ax.set_xticks([0, T/2, T]); ax.set_xticklabels(['0', '$T/2$', '$T$']); ax.set_yticks([0, .25, 1]); ax.set_yticklabels(['0', '1/4', '1']); ax.set_xlabel('$t$', labelpad=0)
tags(fig, axes)
print('lam0', lam[0], 'S', S[-1], 'x at T/2', xat(T/2), lam[500], 'int', np.trapezoid(lam*f, ts), T/4)
save(fig, HERE, 'figure', {'x0': .25, 'T': 'ln 3', 'J': 'x(T)'})
