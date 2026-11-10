from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：x'=-x+g，g 分 20 段常值，J=x(T)^2/2，一次反向积分给出全部 20 个偏导；与差分（每个分量两次前向）对照。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .06, .985, .955, .28, .36)
T = 4.; N = 20; sub = 40; ts = np.linspace(0, T, N*sub+1); tj = np.linspace(0, T, N+1); theta = 1+.6*np.sin(1.5*tj[:-1])
def forward(th):
    x = [0.]; g = np.repeat(th, sub); h = T/(N*sub)
    for gk in g:
        f = lambda v: -v+gk; v = x[-1]; k1 = f(v); k2 = f(v+h/2*k1); k3 = f(v+h/2*k2); k4 = f(v+h*k3); x.append(v+h/6*(k1+2*k2+2*k3+k4))
    return np.array(x)
x = forward(theta); lam = x[-1]*np.exp(ts-T)
grad = np.array([np.trapezoid(lam[j*sub:(j+1)*sub+1], ts[j*sub:(j+1)*sub+1]) for j in range(N)])
eps = 1e-5; fd = []
for j in range(N):
    d = np.zeros(N); d[j] = eps; fd.append((forward(theta+d)[-1]**2-forward(theta-d)[-1]**2)/2/(2*eps))
fd = np.array(fd)
ax = axes[0]; ax.step(np.r_[tj[:-1], T], np.r_[theta, theta[-1]], where='post', color=YELLOW, lw=1.2); ax.plot(ts, x, color=BLUE, lw=1.4); ax.plot(ts, lam, color=PURPLE, lw=1.4)
ax.plot([T], [x[-1]], 'o', ms=4.2, color=RED, mew=0, zorder=5, clip_on=False)
ax.text(1.0, 1.72, '$g$', color=YELLOW, fontsize=7.5); ax.text(1.2, .72, '$x$', color=BLUE, fontsize=7.5, va='top'); ax.text(3.1, .12, '$\\lambda$', color=PURPLE, fontsize=7.5, va='top', ha='left')
ax.set_xlim(0, T); ax.set_ylim(0, 1.9); ax.set_xticks([0, 2, 4]); ax.set_yticks([0, 1]); ax.set_xlabel('$t$', labelpad=0)
ax = axes[1]; c = (tj[:-1]+tj[1:])/2; ax.bar(c, grad, width=.13, color=GREEN, edgecolor='none'); ax.plot(c, fd, 'o', ms=3, color=RED, mew=0, zorder=4)
ax.set_xlim(0, T); ax.set_ylim(0, grad.max()*1.1); ax.set_xticks([0, 2, 4]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel(r'$\partial J/\partial\theta_j$', labelpad=1)
tags(fig, axes)
print('max diff', np.max(np.abs(grad-fd)), grad[-1], fd[-1], x[-1])
save(fig, HERE, 'figure', {'N': N, 'T': T, 'theta': '1+.6 sin(1.5 t_j)', 'max_diff': float(np.max(np.abs(grad-fd)))})
