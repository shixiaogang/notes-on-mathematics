from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'ot-common'))
from common import *
# mu = N(0, I) (blue unit circle = 1-sigma contour), nu = N(m, diag(4, 1/4)), m = (3, 1) (yellow ellipse).
# (a) optimal affine map T(x) = m + diag(2, 1/2) x; cost E|X-T(X)|^2 = |m|^2 + (1-2)^2 + (1-1/2)^2 = 11.25.
# (b) T'(x) = m + diag(2, 1/2) R x with R = rotation by +90 deg: same image law, cost |m|^2 + 2 + 4.25 - 2 tr(D R) = 16.25.
m = np.array([3., 1.]); Dg = np.diag([2., .5]); R = np.array([[0., -1.], [1., 0.]])
th = np.linspace(0, 2*np.pi, 300); circ = np.vstack([np.cos(th), np.sin(th)])
ell = m[:, None]+Dg@circ
ang = np.arange(8)*np.pi/4; pts = np.vstack([np.cos(ang), np.sin(ang)])
def cost(M):
    return float(m@m+np.trace(np.eye(2))+np.trace(M@M.T)-2*np.trace(M))
fig, axs = figure(width_mm=112, height_mm=38, ncols=2)
panel(fig, left=.05, right=.99, top=.99, bottom=.2, wspace=.12)
for ax, M in zip(axs, (Dg, Dg@R)):
    ax.plot(circ[0], circ[1], color=BLUE, lw=1.4)
    ax.plot(ell[0], ell[1], color=YELLOW, lw=1.6)
    img = m[:, None]+M@pts
    for k in range(8):
        ax.annotate('', xy=img[:, k], xytext=pts[:, k], arrowprops=dict(arrowstyle='->', color=STROKE, lw=.7, shrinkA=1.5, shrinkB=1.5))
        dot(ax, pts[0, k], pts[1, k], color=BLUE, ms=3)
        dot(ax, img[0, k], img[1, k], color=YELLOW, ms=3)
    dot(ax, pts[0, 0], pts[1, 0], color=RED, ms=4.2, z=7); dot(ax, img[0, 0], img[1, 0], color=RED, ms=4.2, z=7)
    ax.set_aspect('equal'); ax.set_xlim(-1.4, 5.4); ax.set_ylim(-1.3, 1.9)
    ax.set_xticks([0, 3]); ax.set_yticks([0, 1])
tags(fig, axs)
save(fig, HERE, 'figure', {'cost_optimal': cost(Dg), 'cost_rotated': cost(Dg@R)})
