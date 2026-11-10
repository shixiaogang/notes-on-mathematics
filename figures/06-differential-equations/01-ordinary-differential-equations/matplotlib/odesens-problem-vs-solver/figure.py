from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：Euler 折线的残差 r(s)（求解器）与放大权 exp(a(1-s))（问题）分开。a=+1 与 a=-1，h=1/4，T=1。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .1, .985, .955, .29, .44)
h = .25; res = {}
for a in (1., -1.):
    xk = [1.]
    for k in range(4): xk.append(xk[-1]*(1+a*h))
    xk = np.array(xk); s = np.linspace(0, 1-1e-9, 2001); k = np.floor(s/h).astype(int)
    y = xk[k]*(1+a*(s-k*h)); dy = a*xk[k]; r = dy-a*y
    x = np.exp(a*s); weight = np.exp(a*(1-s)); res[a] = (s, r, weight, np.abs(y-x), float(xk[-1]))
    # identity check: e(1) = int weight * r ds
    print(a, 'Euler', xk[-1], 'exact', np.exp(a), 'err', xk[-1]-np.exp(a), 'int', np.trapezoid(weight*r, s))
for a, c in ((1., GREEN), (-1., YELLOW)):
    s, r, wt, e, _ = res[a]
    axes[0].plot(s, np.abs(r), color=c, lw=1.2); axes[1].plot(s, wt, color=PURPLE if a > 0 else PURPLE, lw=1.4, ls='-' if a > 0 else (0, (3, 2))); axes[2].plot(s, e, color=c, lw=1.4)
axes[1].text(.3, 2.15, '$\\mathrm{e}^{1-s}$', color=PURPLE, fontsize=7.5); axes[1].text(.3, .28, '$\\mathrm{e}^{-(1-s)}$', color=PURPLE, fontsize=7.5)
axes[2].text(.62, .265, '$a=1$', color=GREEN, fontsize=7.5, ha='right'); axes[2].text(.7, .075, '$a=-1$', color=YELLOW, fontsize=7.5, ha='left', va='bottom')
axes[0].set_ylabel('$|r(s)|$', labelpad=1); axes[1].set_ylabel('放大权', labelpad=1); axes[2].set_ylabel('$|y-x|$', labelpad=1)
axes[0].set_ylim(0, .55); axes[0].set_yticks([0, .25, .5]); axes[1].set_ylim(0, 3); axes[1].set_yticks([0, 1, 2, 3]); axes[2].set_ylim(0, .32); axes[2].set_yticks([0, .15, .3])
for ax in axes: ax.set_xlim(0, 1); ax.set_xticks([0, .5, 1]); ax.set_xlabel('$s$' if ax is not axes[2] else '$t$', labelpad=0)
tags(fig, axes)
save(fig, HERE, 'figure', {'h': h, 'T': 1, 'finals': {str(a): res[a][4] for a in res}})
