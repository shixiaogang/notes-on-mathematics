from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：A=[[0,1],[-2,-3]]，原坐标中的结点轨线与特征坐标中的解耦轨线使用同一组初值。
A = np.array([[0., 1], [-2, -3]])
V = np.array([[1., 1], [-1, -2]]); Vi = np.linalg.inv(V)
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .07, .985, .975, .21, .3)
a, b = axes
lim = (-2.2, 2.2)
for ax in axes:
    ax.set_xlim(*lim); ax.set_ylim(*lim); ax.set_aspect('equal')
phase_field(a, A, lim, lim)
phase_field(b, np.diag([-1., -2]), lim, lim)
for v, name, pos in ((V[:, 0], '$\\mathbf{v}_1$', (1.42, -1.72)), (V[:, 1], '$\\mathbf{v}_2$', (.58, -2.0))):
    s = np.array([-5, 5])
    a.plot(s*v[0], s*v[1], color=STROKE, lw=.85, ls=(0, (4, 2)), zorder=2)
    a.text(*pos, name, color=STROKE)
b.axhline(0, color=STROKE, lw=.85, ls=(0, (4, 2)), zorder=2); b.axvline(0, color=STROKE, lw=.85, ls=(0, (4, 2)), zorder=2)
b.text(1.6, .12, '$y_1$', color=STROKE); b.text(.1, 1.75, '$y_2$', color=STROKE)
ts = np.linspace(0, 7, 400)
inits = [(2, 0), (-2, 0), (0, 2), (0, -2), (2, -1.0), (-2, 1.0), (1.5, 1.5), (-1.5, -1.5)]
for x0 in inits:
    x0 = np.array(x0, float)
    y0 = Vi@x0
    y = np.vstack([y0[0]*np.exp(-ts), y0[1]*np.exp(-2*ts)])
    x = V@y
    a.plot(x[0], x[1], color=BLUE, lw=1.2, zorder=3)
    b.plot(y[0], y[1], color=BLUE, lw=1.2, zorder=3)
    a.plot(*x0, 'o', ms=3.4, color=RED, mew=0, zorder=5)
    if np.abs(y0).max() <= 2.2:
        b.plot(*y0, 'o', ms=3.4, color=RED, mew=0, zorder=5)
    arrow_on(a, x[0], x[1], 30); arrow_on(b, y[0], y[1], 30)
a.set_xticks([-2, 0, 2]); a.set_yticks([-2, 0, 2]); b.set_xticks([-2, 0, 2]); b.set_yticks([-2, 0, 2])
label(a, '$x_1$', '$x_2$'); label(b, '$y_1$', '$y_2$')
tags(fig, axes)
save(fig, HERE, 'figure', {'A': A.tolist(), 'V': V.tolist(), 'formula': 'x=V y, y1=y1(0)e^-t, y2=y2(0)e^-2t'})
