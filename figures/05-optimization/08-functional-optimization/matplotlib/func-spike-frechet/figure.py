from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'func-common'))
from func_fig import *
# J(u)=int sin u，u=0，spike eta_k=pi 1_[0,1/k]，固定方向 t*1。
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.075, wspace=.26, bottom=.28)
ax = axes[0]
for k, c in ((2, YELLOW), (4, BLUE), (16, GREEN)):
    ax.plot([0, 0, 1/k, 1/k, 1], [0, np.pi, np.pi, 0, 0], color=c, lw=1.4)
    ax.text(1/k+.02, np.pi-.25*(1+(k==16)*0), f'$k={k}$', color=c, fontsize=7.5, va='top')
for t in (.5,):
    ax.plot([0, 1], [t, t], color=PURPLE, lw=1.4)
ax.text(.98, .6, r'$t\cdot 1$', color=PURPLE, fontsize=7.5, ha='right')
ax.set_xlim(-.02, 1); ax.set_ylim(-.1, 3.9); ax.set_xticks([0, 1]); ax.set_yticks([0, np.pi]); ax.set_yticklabels(['0', r'$\pi$']); ax.set_xlabel('$x$', labelpad=-4); ax.set_ylabel(r'$\eta$', labelpad=0)
ax = axes[1]
k = 2.0**np.arange(0, 11)
d = 1/k
ratio_l1 = np.abs(np.sin(np.pi)-np.pi)*d/(np.pi*d)
ratio_l2 = np.abs(np.sin(np.pi)-np.pi)*d/(np.pi*np.sqrt(d))
t = np.pi*d
ratio_fix = (t-np.sin(t))/t
ax.loglog(d, ratio_l1, color=RED, lw=1.4)
ax.loglog(d, ratio_l2, color=BLUE, lw=1.4)
ax.loglog(d, ratio_fix, color=PURPLE, lw=1.4)
ax.text(.0012, 2.0, '尖峰，L¹ 范数', color=RED, fontsize=7.5)
ax.text(.0035, .012, '尖峰，L² 范数', color=BLUE, fontsize=7.5)
ax.text(.012, .000042, r'固定方向', color=PURPLE, fontsize=7.5)
ax.set_xlim(8e-4, 1.2); ax.set_ylim(1e-6, 12); ax.set_xlabel(r'$\Vert\eta\Vert_1/\pi$', labelpad=0); ax.set_ylabel('余项 / 范数', labelpad=0)
ax.set_yticks([1e-5, 1e-3, 1e-1]); ax.minorticks_off(); ax.set_xticks([1e-3, 1e-2, 1e-1, 1])
tags(fig, axes)
save(fig, HERE, 'figure', {'R': 'int(eta-sin eta)', 'spike': 'pi on [0,1/k]', 'ratio_L1': ratio_l1.tolist()[:3], 'ratio_L2': ratio_l2.tolist()[:3]})
