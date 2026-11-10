from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：Gronwall 上界中初值、持续外力、可积放大率各自的作用；真实距离由 RK4 计算。
fig, axes = figure(width_mm=112, height_mm=46, ncols=3)
panel(fig, .105, .985, .955, .29, .38)
ts = np.linspace(0, 2, 801)
def dist(f, g, x0, y0): return np.abs(rk4(g, y0, ts)-rk4(f, x0, ts))
f = lambda t, x: np.sin(x)
# (a) initial difference only
d = dist(f, f, 1.0, 1.1); B = .1*np.exp(ts); axes[0].plot(ts, B, color=RED, lw=1.4); axes[0].plot(ts, d, color=BLUE, lw=1.4)
axes[0].set_ylabel(r'$\Vert \bm{e}(t)\Vert$'.replace(r'\bm{e}', 'e').replace(r'\Vert','|'), labelpad=1)
# (b) forcing only
d = dist(f, lambda t, x: np.sin(x)+.05, 1.0, 1.0); B = .05*(np.exp(ts)-1); axes[1].plot(ts, B, color=RED, lw=1.4); axes[1].plot(ts, d, color=BLUE, lw=1.4)
# (c) integrable rate: beta=1 on [0,1], 0 afterwards
beta = lambda t: 1.0 if t < 1 else 0.0
fb = lambda t, x: beta(t)*np.sin(x)
d = dist(fb, fb, 1.0, 1.1); B = .1*np.exp(np.minimum(ts, 1)); axes[2].plot(ts, B, color=RED, lw=1.4); axes[2].plot(ts, d, color=BLUE, lw=1.4)
axes[2].axvline(1, color=MUTED, lw=.85, ls=(0, (2, 2)))
for ax, top, (yt, lab) in zip(axes, (.85, .34, .34), (((0, .4, .8), None), ((0, .15, .3), None), ((0, .15, .3), None))):
    ax.set_xlim(0, 2); ax.set_ylim(0, top); ax.set_xticks([0, 1, 2]); ax.set_yticks(yt); ax.set_xlabel('$t$', labelpad=0)
axes[0].text(.95, .42, '上界', color=RED, fontsize=7.5, ha='right'); axes[0].text(1.0, .17, '真实距离', color=BLUE, fontsize=7.5)
tags(fig, axes)
save(fig, HERE, 'figure', {'field': 'sin x, Lipschitz 1', 'a': .1, 'b': .05, 'beta': '1 on [0,1], 0 after'})
