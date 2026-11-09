from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
X = pgd(T=30); XY = bary(X); gaps = np.maximum(f(X)-FS, 1e-18)
fig, axs = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [1.05, 1]})
ax = axs[0]; triangle(ax); contours(ax); active(ax, V[0], V[1]); path(ax, XY[:8]); dot(ax, bary(XS)); off(ax, (-.1, 1.1), (-.1, .95))
ax.text(XY[0, 0]-.03, XY[0, 1]+.02, '$x^{(0)}$', fontsize=8, ha='right'); ax.text(XY[1, 0]-.04, XY[1, 1], '$x^{(1)}$', fontsize=8, ha='right'); ax.text(XY[2, 0]+.03, XY[2, 1]+.015, '$x^{(2)}$', fontsize=8); ax.text(XY[3, 0], XY[3, 1]-.035, '$x^{(3)}$', fontsize=8, ha='center', va='top')
ax = axs[1]; T = np.arange(0, 15); ax.semilogy(T, gaps[:15], '-o', color=GREEN, lw=1.4, ms=3, mew=0)
R2 = np.sum((X0-XS)**2); B = np.arange(1, 15); ax.semilogy(B, L*R2/(2*B), color=PURPLE, lw=1.2, ls=(0, (4, 2)))
ax.text(9.2, 2.6*L*R2/(2*9.2)/1.8, '$LR^2/(2T)$', color=PURPLE, fontsize=8)
setup(ax, (0, 14), (1e-7, 10), [0, 5, 10], [1e-6, 1e-3, 1], xl='$t$', yl='$f(x^{(t)})-f^*$')
panels(fig, .01, .985, .985, .17, .2); tags(fig, axs)
save(fig, HERE, 'figure', {'alpha': .25, 'iterates': X[:6].tolist(), 'gaps': gaps[:6].tolist(), 'R2': float(R2)})
