from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# f=sqrt on [0,1], piecewise constants with midrange values on N=6 cells: uniform i/6 and optimal (i/6)^2. (c) uniform error 1/(2 sqrt N), greedy dyadic bisection, optimal 1/(2N).
import heapq
def staircase(ax, t):
    r = np.sqrt(t)
    for i in range(len(t)-1):
        c = (r[i]+r[i+1])/2
        ax.plot([t[i], t[i+1]], [c, c], color=GREEN, lw=1.3)
        ax.plot([t[i]], [0], '|', color=MUTED, ms=4, mew=.8)
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.058, right=.985, top=.97, bottom=.27, wspace=.3)
x = np.linspace(0, 1, 3001); N = 6
for ax, t in zip(axes[:2], (np.arange(N+1)/N, (np.arange(N+1)/N)**2)):
    ax.plot(x, np.sqrt(x), color=BLUE, lw=1.4); staircase(ax, t)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1.08); ax.set_xticks([0, .5, 1]); ax.set_xticklabels(['0', '1/2', '1']); ax.set_yticks([0, .5, 1]); ax.set_yticklabels(['0', '.5', '1']); ax.set_xlabel('$x$', labelpad=0)
def greedy(N):
    h = [(-1.0, 0.0, 1.0)]
    while len(h) < N:
        o, a, b = heapq.heappop(h); m = (a+b)/2
        heapq.heappush(h, (-(np.sqrt(m)-np.sqrt(a)), a, m)); heapq.heappush(h, (-(np.sqrt(b)-np.sqrt(m)), m, b))
    return -min(h)[0]/2
ns = np.array([2, 4, 8, 16, 32, 64, 128, 256, 512, 1024])
print([greedy(int(n)) for n in (4, 16, 64)])
ax = axes[2]
ax.loglog(ns, 1/(2*np.sqrt(ns)), color=RED, lw=1.3, marker='s', ms=2.6, mew=0)
ax.loglog(ns, [greedy(int(n)) for n in ns], color=YELLOW, lw=1.3, marker='^', ms=3, mew=0)
ax.loglog(ns, 1/(2*ns), color=GREEN, lw=1.3, marker='o', ms=2.8, mew=0)
ax.text(40, .12, '等距', ha='left'); ax.text(4, .017, '最优', ha='left'); ax.text(30, .025, '贪心', ha='left')
ax.set_xlim(1.6, 1300); ax.set_ylim(3e-4, 1); ax.set_xlabel('$N$', labelpad=0); ax.set_xticks([10, 100, 1000])
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'E=osc/2; uniform 1/(2 sqrt N); optimal (i/N)^2 gives 1/(2N); greedy dyadic bisection by largest oscillation'})
