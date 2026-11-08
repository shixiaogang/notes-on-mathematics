from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures"))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np

def panel_labels(fig, axes, y=.02):
    for ax, s in zip(axes, "(a) (b) (c)".split()):
        q = ax.get_position(); fig.text((q.x0+q.x1)/2, y, s, ha="center", va="bottom")

# (a) hat functions on the grid i/4. (b) f*=|x-1/2| and its interpolant on the grid i/3, where 1/2 is not a node. (c) uniform errors for N odd.
fig, axes = figure(width_mm=112, height_mm=50, ncols=3)
fig.set_layout_engine(None)
fig.subplots_adjust(left=.05, right=.985, top=.97, bottom=.27, wspace=.3)
x = np.linspace(0, 1, 4001)
ax = axes[0]
t4 = np.arange(5)/4
cols = [BLUE, GREEN, YELLOW, RED, PURPLE]
for i in range(5):
    y = np.interp(x, t4, np.eye(5)[i]); ax.plot(x, y, color=cols[i], lw=1.3)
for i, xp in enumerate(t4): ax.text(xp, 1.07, rf'$\varphi_{i}$', ha='center')
ax.set_xlim(-.09, 1.09); ax.set_ylim(0, 1.3); ax.set_xticks(t4); ax.set_xticklabels(['0', '', '1/2', '', '1']); ax.set_yticks([0, 1]); ax.set_xlabel('$x$', labelpad=0)
ax = axes[1]
t3 = np.arange(4)/3; fs = np.abs(x-.5)
ax.plot(x, fs, color=BLUE, lw=1.4); ax.plot(x, np.interp(x, t3, np.abs(t3-.5)), color=GREEN, lw=1.2)
ax.plot(t3, np.abs(t3-.5), 'o', ms=3.2, color=GREEN, mew=0)
ax.plot([.5, .5], [0, 1/6], color=RED, lw=1.4)
ax.text(.54, .07, r'$h/2$', ha='left'); ax.text(.5, .21, r'$S_hf_*$', ha='center'); ax.text(.87, .27, r'$f_*$', ha='left')
ax.set_xlim(0, 1); ax.set_ylim(-.02, .56); ax.set_xticks([0, 1/3, 2/3, 1]); ax.set_xticklabels(['0', '1/3', '2/3', '1']); ax.set_yticks([0, .25, .5]); ax.set_yticklabels(['0', '1/4', '1/2']); ax.set_xlabel('$x$', labelpad=0)
ax = axes[2]
Ns = np.array([3, 5, 9, 17, 33, 65]); xs = np.linspace(0, 1, 200001); es = []
for N in Ns:
    t = np.linspace(0, 1, N+1); es.append(np.abs(np.sin(np.pi*xs)-np.interp(xs, t, np.sin(np.pi*t))).max())
h = 1/Ns
ax.loglog(h, np.pi**2*h**2/8, color=MUTED, lw=.85, ls=(0, (3, 2)))
ax.loglog(h, es, color=BLUE, lw=0, marker='o', ms=3, mew=0)
ax.loglog(h, h/2, color=RED, lw=1.2, marker='s', ms=2.8, mew=0)
ax.text(.06, 1.2e-3, r'$\sin\pi x$', ha='left'); ax.text(.021, .028, r'$f_*$', ha='left')
ax.set_xlim(.012, .45); ax.set_ylim(1.5e-4, .4); ax.set_xlabel('$h$', labelpad=0); ax.set_xticks([.02, .1]); ax.set_xticklabels(['0.02', '0.1']); ax.minorticks_off()
panel_labels(fig, axes)
save(fig, Path(__file__).resolve().parent, 'figure', {'formula': 'hat functions; piecewise linear interpolation errors; sin(pi x) vs pi^2 h^2/8; f* error = h/2 for odd N'})
