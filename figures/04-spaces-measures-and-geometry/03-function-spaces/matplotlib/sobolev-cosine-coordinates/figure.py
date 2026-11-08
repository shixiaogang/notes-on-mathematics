from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Cosine coordinates a_n=sqrt2*int_0^1 f cos(pi n x)dx. kink |x-1/2|: a_{2m}=sqrt2/(pi^2 m^2), m odd, others 0.
# step 1_[1/2,1): |a_n|=sqrt2/(pi n), n odd. Weighted sums S_N=sum_{n<=N} pi^2 n^2 a_n^2.
N = 40; n = np.arange(1, N+1)
kink = np.zeros(N); step = np.zeros(N)
for k in n:
    if k % 2 == 0 and (k//2) % 2 == 1: kink[k-1] = 2**.5/(np.pi**2*(k//2)**2)
    if k % 2 == 1: step[k-1] = 2**.5/(np.pi*k)
# numerical check of the closed forms
t = (np.arange(400000)+.5)/400000
for k in (1, 2, 3, 6):
    a = 2**.5*np.mean(np.abs(t-.5)*np.cos(np.pi*k*t)); assert abs(abs(a)-kink[k-1]) < 1e-6
    b = 2**.5*np.mean((t >= .5)*np.cos(np.pi*k*t)); assert abs(abs(b)-step[k-1]) < 1e-5
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
fig.set_layout_engine(None); fig.subplots_adjust(left=.095, right=.98, top=.97, bottom=.25, wspace=.3)
ax = axes[0]; m = n <= 20
for nn, v, c, dx in [(n[m], step[m], YELLOW, .16), (n[m], kink[m], BLUE, -.16)]:
    keep = v > 0
    ax.vlines(nn[keep]+dx, 0, v[keep], color=c, lw=1.4); ax.plot(nn[keep]+dx, v[keep], 'o', color=c, ms=3)
ax.text(3.5, .36, '阶跃', va='center'); ax.text(5.5, .17, '折点', va='center')
ax.set_xlim(0, 20.8); ax.set_ylim(0, .52); ax.set_xticks([1, 5, 10, 15, 20]); ax.set_yticks([0, .2, .4]); ax.set_xlabel('$n$', labelpad=0); ax.set_ylabel(r'$|a_n|$', labelpad=1)
ax = axes[1]
Sk = np.cumsum(np.pi**2*n**2*kink**2); Ss = np.cumsum(np.pi**2*n**2*step**2)
ax.plot(n, Ss, color=YELLOW, lw=1.4, drawstyle='steps-post'); ax.plot(n, Sk, color=BLUE, lw=1.4, drawstyle='steps-post')
ax.axhline(1, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.text(36, 28, '阶跃', ha='right', va='center'); ax.text(38, 3.6, '折点', ha='right', va='center')
ax.set_xlim(1, 40); ax.set_ylim(0, 42); ax.set_xticks([1, 10, 20, 30, 40]); ax.set_yticks([0, 20, 40]); ax.set_xlabel('$N$', labelpad=0); ax.set_ylabel(r'$S_N$', labelpad=1)
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'cosine coordinates of kink and step; S_N=sum pi^2 n^2 a_n^2'})
