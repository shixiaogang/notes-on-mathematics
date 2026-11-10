from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：卷积积分的被积函数 sin(t-s)cos(ws)，t=4.5 pi：共振时同号累积，非共振时互相抵消。
T = 4.5*np.pi
fig, axes = figure(width_mm=112, height_mm=46, ncols=2)
panel(fig, .075, .985, .95, .27, .25)
s = np.linspace(0, T, 1600)
out = []
for ax, w in zip(axes, (1., 2.)):
    y = np.sin(T-s)*np.cos(w*s)
    ax.fill_between(s, 0, y, where=y >= 0, color=BLUE_FILL, lw=0, interpolate=True)
    ax.fill_between(s, 0, y, where=y <= 0, color=RED_FILL, lw=0, interpolate=True)
    ax.plot(s, y, color=BLUE, lw=1.2)
    ax.axhline(0, color=MUTED, lw=.6)
    out.append(float(np.trapezoid(y, s)))
    ax.set_xlim(0, T); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, 5, 10, 14]); ax.set_yticks([-1, 0, 1]); label(ax, '$s$', '')
print(out)
tags(fig, axes)
save(fig, HERE, 'figure', {'t': T, 'integrals': out, 'expected': [T*np.sin(T)/2, 1/3]})
