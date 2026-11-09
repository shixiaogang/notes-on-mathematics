from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# (a) cobweb of T(x)=(x+2)/3 from x0=0; (b) T=cos x on [0,1], x0=0, q=sin 1: true error, a priori and a posteriori bounds.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2, width_ratios=[.82, 1])
fig.set_layout_engine(None)
fig.subplots_adjust(left=.055, right=.985, top=.97, bottom=.2, wspace=.2)
a = axes[0]
T = lambda x: (x+2)/3
xx = np.array([0, 1.25])
a.plot(xx, xx, color=MUTED, lw=.9, zorder=2)
a.plot(xx, T(xx), color=BLUE, lw=1.4, zorder=3)
px, py = [0.0], [0.0]; v = 0.0
for k in range(6):
    w = T(v); px += [v, w]; py += [w, w]; v = w
a.plot(px, py, color=RED, lw=.9, zorder=4)
for k, val in enumerate([0, 2/3, 8/9, 26/27]):
    a.plot([val], [0], 'o', ms=2.8, color=INK, mew=0, zorder=5, clip_on=False)
a.plot([1], [1], 'o', ms=3.6, color=INK, mew=0, zorder=5)
a.set_xlim(0, 1.25); a.set_ylim(0, 1.25); a.set_xticks([0, 2/3, 1]); a.set_xticklabels(['$0$', r'$\frac{2}{3}$', '$1$']); a.set_yticks([0, 1])
a.text(.32, .9, '$T$', color=INK, ha='center'); a.text(.4, .28, '$y=x$', color=INK, ha='left')
b = axes[1]
q = np.sin(1); N = 30
it = [0.0]
for k in range(200): it.append(np.cos(it[-1]))
star = it[-1]; it = np.array(it[:N+1])
k = np.arange(1, N+1)
err = np.abs(it[1:]-star)
pri = q**k/(1-q)*abs(it[1]-it[0])
post = q/(1-q)*np.abs(it[1:]-it[:-1])
b.semilogy(k, pri, color=GREEN, lw=1.3)
b.semilogy(k, post, color=BLUE, lw=1.3)
b.semilogy(k, err, color=RED, lw=1.3)
b.text(21, pri[20]*1.9, '先验', color=INK, ha='left', va='bottom')
b.text(13.5, post[13]*2.4, '后验', color=INK, ha='left', va='bottom')
b.text(5, err[5]*.13, '真实误差', color=INK, ha='left', va='top')
b.set_xlim(1, 30); b.set_ylim(1e-7, 10); b.set_xticks([1, 10, 20, 30]); b.set_yticks([1e-6, 1e-4, 1e-2, 1]); b.minorticks_off()
for ax, s in zip(axes, '(a) (b)'.split()):
    ax.spines['left'].set_linewidth(.95); ax.spines['bottom'].set_linewidth(.95)
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .03, s, ha='center', va='bottom')
fig.text((axes[1].get_position().x0+axes[1].get_position().x1)/2, .115, '$k$', ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'T=(x+2)/3 cobweb; cos iteration x0=0, q=sin 1, bounds q^k/(1-q)|x1-x0|, q/(1-q)|x_k-x_{k-1}|'})
