"""Triangle model, A=[3/4,1]: (a) colour of (x,y) in the triangle is h_A(y)=P(X in A|Y=y);
(b) the function h_A(y)=1/(4(1-y)) for y<=3/4 and 1 afterwards."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE])
def h(y): return np.minimum(1.0, 0.25/(1-np.minimum(y, 0.999999)))
fig, (a, b) = figure(width_mm=104, height_mm=50, ncols=2)
n = 400
xs = np.linspace(0, 1, n); ys = np.linspace(0, 1, n)
Xg, Yg = np.meshgrid(xs, ys)
Z = np.where(Yg <= Xg, h(Yg), np.nan)
im = a.imshow(Z, origin='lower', extent=(0, 1, 0, 1), cmap=cmap, vmin=0, vmax=1, interpolation='nearest')
a.plot([0, 1, 1, 0], [0, 0, 1, 0], color=BLUE, lw=1.0)
a.plot([0.75, 0.75], [0, 0.75], color=STROKE, lw=0.85, ls=DASH)
a.text(0.78, 0.06, '$x=3/4$', fontsize=7.5, ha='left')
cb = fig.colorbar(im, ax=a, fraction=0.05, pad=0.03, ticks=[0, 0.5, 1])
cb.outline.set_linewidth(0.6); cb.ax.tick_params(labelsize=7, width=0.6)
a.set_aspect('equal'); a.set_xlim(-0.02, 1.03); a.set_ylim(-0.02, 1.03)
a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 0.5, 1]); a.set_xlabel('$x$', labelpad=1); a.set_ylabel('$y$', rotation=0)
yy = np.linspace(0, 0.98, 300)
b.plot(yy, h(yy), color=BLUE, lw=1.4)
b.scatter([0.75], [1.0], s=18, color=RED, zorder=4)
b.set_xlim(0, 1); b.set_ylim(0, 1.08); b.set_xticks([0, 0.25, 0.5, 0.75, 1]); b.set_yticks([0, 0.25, 0.5, 1])
b.set_xlabel('$y$', labelpad=1); b.set_ylabel('$h_A(y)$')

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'A': '[3/4,1]', 'h_A': '1/(4(1-y)) for y<=3/4, 1 otherwise'})
