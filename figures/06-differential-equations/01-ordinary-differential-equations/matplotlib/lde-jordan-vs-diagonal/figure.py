from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：-I 与 Jordan 块 [[-1,1],[0,-1]] 特征值相同，相图不同。
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .07, .985, .975, .21, .3)
a, b = axes
lim = (-2.2, 2.2)
J = np.array([[-1., 1], [0, -1]])
phase_field(a, -np.eye(2), lim, lim); phase_field(b, J, lim, lim)
for ax in axes:
    ax.set_xlim(*lim); ax.set_ylim(*lim); ax.set_aspect('equal'); ax.set_xticks([-2, 0, 2]); ax.set_yticks([-2, 0, 2])
ts = np.linspace(0, 9, 900)
for th in np.arange(8)*np.pi/4+np.pi/8:
    x0 = 2*np.array([np.cos(th), np.sin(th)])
    x = np.exp(-ts)*x0[0]; y = np.exp(-ts)*x0[1]
    a.plot(x, y, color=BLUE, lw=1.2, zorder=3); a.plot(*x0, 'o', ms=3.4, color=RED, mew=0, zorder=5); arrow_on(a, x, y, 40)
    x = np.exp(-ts)*(x0[0]+ts*x0[1]); y = np.exp(-ts)*x0[1]
    b.plot(x, y, color=BLUE, lw=1.2, zorder=3); b.plot(*x0, 'o', ms=3.4, color=RED, mew=0, zorder=5)
    arrow_on(b, x, y, 40)
b.plot([-2.2, 2.2], [0, 0], color=YELLOW, lw=1.8, zorder=4)
b.text(1.05, .14, '$\\mathbf{e}_1$', color=YELLOW)
label(a, '$x_1$', '$x_2$'); label(b, '$x_1$', '$x_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'A=-I', 'b': 'A=[[-1,1],[0,-1]]', 'formula': 'x1=e^-t(x1(0)+t x2(0)), x2=e^-t x2(0)'})
