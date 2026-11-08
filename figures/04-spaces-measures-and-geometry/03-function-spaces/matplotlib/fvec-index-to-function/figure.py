from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

# 同一构造的三种输入集合：X={1,2,3,4}，X=N+，X=[0,1]。
fig, axes = figure(width_mm=112, height_mm=48, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.075, right=.985, top=.95, bottom=.3, wspace=.42)
def stem(ax, x, y, c=BLUE):
    ax.vlines(x, 0, y, color=c, lw=1.1)
    ax.plot(x, y, 'o', ms=3.4, color=c, mew=0)
a = axes[0]
k = np.arange(1, 5); v = np.array([1.5, .5, 2.0, 1.0])
stem(a, k, v); a.set_xlim(.4, 4.6); a.set_ylim(0, 2.45); a.set_xticks(k); a.set_yticks([0, 1, 2])
a.set_xlabel('$k$', labelpad=1); a.set_ylabel('$a_k$', labelpad=2)
b = axes[1]
k = np.arange(1, 14); v = 2/k**.8
stem(b, k, v); b.set_xlim(.2, 15.6); b.set_ylim(0, 2.45); b.set_xticks([1, 5, 10]); b.set_yticks([0, 1, 2])
b.text(14.75, .22, r'$\cdots$', ha='center', va='center', color=MUTED)
b.set_xlabel('$k$', labelpad=1); b.set_ylabel('$a_k$', labelpad=2)
c = axes[2]
x = np.linspace(0, 1, 400); f = lambda t: 1.15 + .75*np.sin(2*np.pi*t)
c.plot(x, f(x), color=BLUE, lw=1.4)
x0 = .62
c.vlines(x0, 0, f(x0), color=BLUE, lw=1.1); c.plot([x0], [f(x0)], 'o', ms=3.4, color=BLUE, mew=0)
c.text(x0+.04, f(x0)+.14, '$f(x)$', va='bottom', ha='left')
c.set_xlim(0, 1.03); c.set_ylim(0, 2.45); c.set_xticks([0, x0, 1]); c.set_xticklabels(['0', '$x$', '1']); c.set_yticks([0, 1, 2])
c.set_xlabel(' ', labelpad=1); c.set_ylabel('$f$', labelpad=2)
for ax, s in zip(axes, '(a) (b) (c)'.split()):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, .02, s, ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': '(a) [1.5,0.5,2,1]; (b) a_k=2/k^0.8; (c) f(x)=1.15+0.75 sin(2 pi x)'})
