from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：因果 Green 函数 e^{-(t-s)}1_{t>=s} 的支撑在下三角；对照边值 Green 函数 min(x,s)(1-max(x,s))。
from matplotlib.colors import LinearSegmentedColormap as C
cmap = C.from_list('v', ['#FFFFFF', BLUE_FILL, BLUE])
fig, axes = figure(width_mm=112, height_mm=60, ncols=2)
panel(fig, .075, .985, .975, .21, .28)
a, b = axes
n = 400
s = np.linspace(0, 4, n); t = np.linspace(0, 4, n); S, T = np.meshgrid(s, t)
G = np.where(T >= S, np.exp(-(T-S)), 0.)
a.imshow(G, origin='lower', extent=(0, 4, 0, 4), cmap=cmap, vmin=0, vmax=1, aspect='equal', interpolation='bilinear')
a.plot([0, 4], [0, 4], color=STROKE, lw=1.4)
a.text(.55, 2.95, '$t>s$', color=INK); a.text(2.75, 1.2, '$t<s$', color=INK); a.text(2.7, .78, '$G=0$', color=MUTED, fontsize=7.5)
a.set_xticks([0, 2, 4]); a.set_yticks([0, 2, 4]); label(a, '$s$', '$t$')
s = np.linspace(0, 1, n); S, X = np.meshgrid(s, s)
B = np.minimum(S, X)*(1-np.maximum(S, X))
b.imshow(B, origin='lower', extent=(0, 1, 0, 1), cmap=cmap, vmin=0, vmax=.25, aspect='equal', interpolation='bilinear')
b.set_xticks([0, .5, 1]); b.set_yticks([0, .5, 1]); b.set_xticklabels(['0', '0.5', '1']); b.set_yticklabels(['0', '0.5', '1']); label(b, '$s$', '$x$')
tags(fig, axes)
save(fig, HERE, 'figure', {'a': 'e^{-(t-s)}1_{t>=s}', 'b': 'min(x,s)(1-max(x,s))'})
