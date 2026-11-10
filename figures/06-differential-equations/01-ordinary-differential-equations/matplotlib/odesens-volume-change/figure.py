from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odesens-common"))
from common import *
HERE = Path(__file__).resolve().parent
# 目标：三种流下面积变化，点为多边形（shoelace）数值，线为 Liouville 公式 exp(t div)。
fig, axes = figure(width_mm=112, height_mm=52, ncols=3)
panel(fig, .085, .985, .96, .24, .36)
def phi_a(a, b, t): return np.array([a*np.exp(-t), (b+a**2/3)*np.exp(t)-a**2/3*np.exp(-2*t)])
def square(c, r, n=160):
    s = np.linspace(-r, r, n); return np.r_[np.c_[c[0]+s, c[1]-r+0*s], np.c_[c[0]+r+0*s, c[1]+s], np.c_[c[0]-s, c[1]+r+0*s], np.c_[c[0]-r+0*s, c[1]-s]]
Q = square((1., 0.), .25)
ax = axes[0]; T = np.log(2); P = phi_a(Q[:, 0], Q[:, 1], T).T
ax.fill(P[:, 0], P[:, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1); ax.plot(np.r_[Q[:, 0], Q[0, 0]], np.r_[Q[:, 1], Q[0, 1]], color=RED, lw=1.1)
ax.set_aspect('equal'); ax.set_xlim(.2, 1.4); ax.set_ylim(-.5, 1.6); ax.set_xticks([.5, 1]); ax.set_yticks([0, 1]); ax.set_xlabel('$x_1$', labelpad=0); ax.set_ylabel('$x_2$', labelpad=1)
A = np.array([[0, 1.], [-1, -.5]]); ax = axes[1]
def expm(M, t):
    w, V = np.linalg.eig(M); return np.real(V@np.diag(np.exp(w*t))@np.linalg.inv(V))
Q2 = square((1., 0.), .25); P2 = (expm(A, 2.)@Q2.T).T
ax.fill(P2[:, 0], P2[:, 1], facecolor=BLUE_FILL, edgecolor=BLUE, lw=1.1); ax.plot(np.r_[Q2[:, 0], Q2[0, 0]], np.r_[Q2[:, 1], Q2[0, 1]], color=RED, lw=1.1)
ax.set_aspect('equal'); ax.set_xlim(-.6, 1.4); ax.set_ylim(-1.1, .5); ax.set_xticks([0, 1]); ax.set_yticks([-1, 0]); ax.set_xlabel('$q$', labelpad=0); ax.set_ylabel('$p$', labelpad=1)
ax = axes[2]; ts = np.linspace(0, 2, 200)
A0 = shoelace(Q); ax.plot(ts, 0*ts+1, color=BLUE, lw=1.4); ax.plot(ts, np.exp(-.5*ts), color=YELLOW, lw=1.4); ax.plot(ts, np.exp(.5*ts), color=PURPLE, lw=1.4)
tt = np.linspace(0, 2, 6)
ax.plot(tt, [shoelace(phi_a(Q[:, 0], Q[:, 1], t).T)/A0 for t in tt], 'o', ms=3, color=BLUE, mew=0, zorder=4)
ax.plot(tt, [shoelace((expm(A, t)@Q2.T).T)/A0 for t in tt], 'o', ms=3, color=YELLOW, mew=0, zorder=4)
ax.plot(tt, [shoelace(np.exp(.25*t)*Q)/A0 for t in tt], 'o', ms=3, color=PURPLE, mew=0, zorder=4)
ax.text(.9, 2.1, '$\\mathrm{e}^{0.5t}$', color=PURPLE, fontsize=7.5, ha='right'); ax.text(1.7, 1.1, '$1$', color=BLUE, fontsize=7.5); ax.text(.85, .42, '$\\mathrm{e}^{-0.5t}$', color=YELLOW, fontsize=7.5, ha='right')
ax.set_xlim(0, 2); ax.set_ylim(0, 3); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2, 3]); ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('面积比', labelpad=1)
tags(fig, axes)
print('areas', A0, shoelace(P), shoelace(P2), A0*np.exp(-1))
save(fig, HERE, 'figure', {'square': 'center (1,0), half width .25', 'a': 'phi at ln 2', 'b': 'damped, t=2', 'c': 'area ratios'})
