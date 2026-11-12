"""(a) Exp(lambda) densities; (b) Exp(0.5) survival vs discretised geometric waits with step h."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent/"cdist-common"))
from cdist_fig import *

fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, left=.08, bottom=.27, wspace=.3)
ax = axes[0]; style(ax)
t = np.linspace(0, 6, 601)
for lam, c, ls in ((.5, BLUE, '-'), (1, YELLOW, '--'), (2, PURPLE, '-.')):
    ax.plot(t, lam*np.exp(-lam*t), color=c, lw=1.4, ls=ls)
lab(ax, 2.2, .26, r'$\lambda=0.5$', BLUE); lab(ax, .9, .5, r'$\lambda=1$', YELLOW); lab(ax, .45, 1.55, r'$\lambda=2$', PURPLE)
ax.set_xlim(0, 6); ax.set_ylim(0, 2.05); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, 1, 2])
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('$f_T(t)$', labelpad=1)
ax = axes[1]; style(ax)
lam = .5
for h, c, ls in ((1, YELLOW, '-'), (.25, PURPLE, '-')):
    tt = np.arange(0, 6+h, h); G = (1-lam*h)**np.arange(len(tt))
    for i in range(len(tt)-1):
        ax.plot([tt[i], tt[i+1]], [G[i], G[i]], color=c, lw=1.1)
t = np.linspace(0, 6, 601); ax.plot(t, np.exp(-lam*t), color=BLUE, lw=1.4)
lab(ax, 3.2, .52, r'$\mathrm{e}^{-0.5t}$', BLUE); lab(ax, 1.15, .28, '$h=1$', YELLOW); lab(ax, .3, .14, '$h=0.25$', PURPLE)
ax.set_xlim(0, 6); ax.set_ylim(0, 1.05); ax.set_xticks([0, 2, 4, 6]); ax.set_yticks([0, .5, 1])
ax.set_xlabel('$t$', labelpad=1); ax.set_ylabel('生存概率', labelpad=1)
tags(fig, axes)
save(fig, here(__file__), 'figure', {'lambda': lam, 'P(T>3)': float(np.exp(-1.5)), 'note': 'steps: (1-lambda h)^floor(t/h)'})
