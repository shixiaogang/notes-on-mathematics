from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：A=[[-1,2],[-2,-1]] 特征值 -1±2i，相平面螺线与分量的包络。
A = np.array([[-1., 2], [-2, -1]])
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, .07, .985, .97, .24, .28)
a, b = axes
lim = (-1.3, 1.3)
a.set_xlim(*lim); a.set_ylim(*lim); a.set_aspect('equal')
phase_field(a, A, lim, lim, nx=13, ny=13)
t = np.linspace(0, 6, 1500)
x = np.exp(-t)*np.cos(2*t); y = -np.exp(-t)*np.sin(2*t)
a.plot(x, y, color=BLUE, lw=MAIN, zorder=3); a.plot([1], [0], 'o', ms=3.8, color=RED, mew=0, zorder=5)
for i in (70, 240, 420):
    arrow_on(a, x, y, i)
a.set_xticks([-1, 0, 1]); a.set_yticks([-1, 0, 1]); label(a, '$x_1$', '$x_2$')
b.plot(t, x, color=BLUE, lw=MAIN); b.plot(t, np.exp(-t), color=PURPLE, lw=1.0, ls=(0, (4, 2))); b.plot(t, -np.exp(-t), color=PURPLE, lw=1.0, ls=(0, (4, 2)))
b.plot([0], [1], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
b.axhline(0, color=GRID, lw=.6, zorder=0)
b.text(1.1, .46, '$\\mathrm{e}^{-t}$', color=PURPLE); b.text(2.05, -.33, '$x_1$', color=BLUE)
b.set_xlim(0, 6); b.set_ylim(-1.1, 1.1); b.set_xticks([0, 2, 4, 6]); b.set_yticks([-1, 0, 1]); label(b, '$t$', '')
tags(fig, axes)
save(fig, HERE, 'figure', {'A': A.tolist(), 'formula': 'x1=e^-t cos 2t, x2=-e^-t sin 2t', 'x0': [1, 0]})
