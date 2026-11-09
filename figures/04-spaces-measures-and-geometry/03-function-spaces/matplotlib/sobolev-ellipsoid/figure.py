from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c) (d)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# Unit ball of H^1(0,1) in cosine coordinates: semi-axis s_n=(1+pi^2 n^2)^(-1/2). s_1=.3033, s_2=.1572; tail below .1 from n=4.
s = lambda n: (1+np.pi**2*n**2)**-.5
fig, axes = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.55]})
fig.set_layout_engine(None); fig.subplots_adjust(left=.03, right=.98, top=.97, bottom=.24, wspace=.26)
ax = axes[0]; th = np.linspace(0, 2*np.pi, 400)
ax.fill(np.cos(th), np.sin(th), color=BLUE_FILL, lw=0); ax.plot(np.cos(th), np.sin(th), color=BLUE, lw=1.4)
ax.fill(s(1)*np.cos(th), s(2)*np.sin(th), color=GREEN_FILL, lw=0); ax.plot(s(1)*np.cos(th), s(2)*np.sin(th), color=GREEN, lw=1.4)
ax.annotate('', xy=(1.3, 0), xytext=(-1.3, 0), arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=.85, shrinkA=0, shrinkB=0))
ax.annotate('', xy=(0, 1.3), xytext=(0, -1.3), arrowprops=dict(arrowstyle='-|>', color=MUTED, lw=.85, shrinkA=0, shrinkB=0))
ax.text(1.22, -.3, '$a_1$', ha='right'); ax.text(.08, 1.18, '$a_2$', ha='left')
ax.set_aspect('equal'); ax.set_xlim(-1.35, 1.35); ax.set_ylim(-1.35, 1.35); ax.axis('off')
ax = axes[1]; n = np.arange(0, 17); v = s(n)
ax.bar(n[:4], v[:4], width=.62, color=BLUE, lw=0); ax.bar(n[4:], v[4:], width=.62, color=RED, lw=0)
ax.axhline(.1, color=MUTED, lw=.85, ls=(0, (3, 2))); ax.text(16.4, .13, r'$\varepsilon=0.1$', ha='right')
ax.set_xlim(-.7, 16.7); ax.set_ylim(0, 1.08); ax.set_xticks([0, 4, 8, 12, 16]); ax.set_yticks([0, .5, 1]); ax.set_xlabel('$n$', labelpad=0); ax.set_ylabel('$s_n$', labelpad=1)
q0, q1 = axes[0].get_position(), axes[1].get_position()
fig.text((q0.x0+q0.x1)/2, .02, '(a)', ha='center', va='bottom'); fig.text((q1.x0+q1.x1)/2, .02, '(b)', ha='center', va='bottom')
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 's_n=(1+pi^2 n^2)^(-1/2)'})
