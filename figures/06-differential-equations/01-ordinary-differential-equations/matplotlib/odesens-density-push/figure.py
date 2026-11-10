from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：logistic，T=ln3，x0 在 [0.1,0.4] 上均匀，推前密度 p_T(y)=p_0/S，样本（种子 7）直方对照。
fig, axes = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, .115, .985, .955, .28, .26)
T = np.log(3); phi = lambda s: logistic(T, s)
S = lambda s: np.exp(T)/(1-s+s*np.exp(T))**2
ax = axes[0]; s = np.linspace(0, .6, 300); ax.plot(s, phi(s), color=BLUE, lw=1.4); ax.fill_between([.1, .4], 0, .02, color=YELLOW, lw=0)
for a in (.1, .25, .4):
    ax.plot([a, a], [0, phi(a)], color=MUTED, lw=.85, ls=(0, (2, 2))); ax.plot([0, a], [phi(a), phi(a)], color=MUTED, lw=.85, ls=(0, (2, 2)))
ax.set_xlim(0, .6); ax.set_ylim(0, .9); ax.set_xticks([.1, .25, .4]); ax.set_yticks([phi(.1), phi(.25), phi(.4)]); ax.set_yticklabels(['0.25', '0.5', '0.667']); ax.set_xlabel('$x_0$', labelpad=0); ax.set_ylabel('$\\varphi_T(x_0)$', labelpad=1)
ax = axes[1]; rng = np.random.default_rng(7); xs = phi(rng.uniform(.1, .4, 40000))
s = np.linspace(.1, .4, 400); p0 = 1/.3
h, e = np.histogram(xs, bins=26, range=(.2, .7), density=True)
ax.bar(e[:-1], h, width=e[1]-e[0], align='edge', color=GREEN_FILL, edgecolor='none')
ax.plot([.1, .1, .4, .4], [0, p0, p0, 0], color=YELLOW, lw=1.4); ax.plot(phi(s), p0/S(s), color=BLUE, lw=1.4)
ax.text(.13, 3.5, '$p_0$', color=YELLOW, fontsize=7.5, va='bottom'); ax.text(.6, 2.6, '$p_T$', color=BLUE, fontsize=7.5)
ax.set_xlim(0, .75); ax.set_ylim(0, 4.2); ax.set_xticks([.1, .4, .667]); ax.set_xticklabels(['0.1', '0.4', '0.667']); ax.set_yticks([0, 2, 4]); ax.set_xlabel('状态', labelpad=0); ax.set_ylabel('密度', labelpad=1)
tags(fig, axes)
print('p_T at x=.5', p0/S(.25), S(.25))
save(fig, HERE, 'figure', {'x0': 'U[.1,.4]', 'T': 'ln 3', 'seed': 7, 'n': 40000})
