from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
# inverse of second-difference matrix vs Green's function.
def K(n):
    h = 1/(n+1)
    return (2*np.eye(n)-np.eye(n, k=1)-np.eye(n, k=-1))/h**2, h
G = lambda x, y: np.where(x <= y, x*(1-y), y*(1-x))
fig, axes = figure(width_mm=112, height_mm=54, ncols=2, gridspec_kw={'width_ratios': [.8, 1]})
panel(fig, left=.075, wspace=.24, bottom=.25)
n = 63; M, h = K(n); inv = np.linalg.inv(M)/h
ax = axes[0]
im = ax.imshow(inv, origin='lower', extent=[0, 1, 0, 1], cmap=FIELD, vmin=0, vmax=.25)
ax.set_xticks([0, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('列：源的位置', labelpad=1); ax.set_ylabel('行：观测位置', labelpad=-2)
ax = axes[1]
n = 7; M, h = K(n); inv = np.linalg.inv(M)/h; pts = np.arange(1, n+1)*h
for j, c in ((1, BLUE), (3, BLUE), (5, BLUE)):
    ax.plot(X, G(X, pts[j]), color=c, lw=1.4)
    ax.plot(np.r_[0, pts, 1], np.r_[0, inv[:, j], 0], 'o', ms=3.4, color=GREEN, mew=0, zorder=5)
    lab(ax, pts[j], G(pts[j], pts[j])+.012, '$y=%g$' % pts[j], BLUE, ha='center')
err = max(abs(inv[i, j]-G(pts[i], pts[j])) for i in range(n) for j in range(n))
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.01, .3); ax.set_xticks([0, 1]); ax.set_yticks([0, .25]); hat01(ax, yl=None)
tags(fig, axes)
save(fig, HERE, 'figure', {'max_abs_difference_Kinv_over_h_vs_G': float(err)})
print('err', err)
