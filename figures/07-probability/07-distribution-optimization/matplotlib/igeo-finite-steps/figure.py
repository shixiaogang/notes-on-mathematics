"""One finite natural-gradient step, alpha=1/8, from N(1,4) toward Pi=N(0,1), L=D_KL(Q||Pi), drawn in the (mu,v) plane.
Blue: natural-gradient flow theta(t)=theta_Pi+e^{-t}(theta_0-theta_Pi) (same curve in every coordinate). Steps in coordinates
(mu,v) -> (0.5,2.5); natural (theta1,theta2) -> (0.636,2.909); (mu,ln v) -> (0.5,2.749). Gray arrow: common tangent direction -(4,12)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, ax = figure(width_mm=84, height_mm=58)
M, V = np.meshgrid(np.linspace(-0.3, 1.3, 200), np.linspace(0.6, 4.6, 200))
ax.contour(M, V, L_mv(M, V), levels=[0.05, 0.2, 0.5, 1.0, 1.5], colors=[GRID], linewidths=0.6)
t0 = nat_from_mv(1.0, 4.0); ts = np.linspace(0, 6, 300)
flow = np.array([mv_from_nat(THETA_PI+np.exp(-s)*(t0-THETA_PI)) for s in ts])
ax.plot(flow[:, 0], flow[:, 1], color=BLUE, lw=1.4)
a = 1/8
p_mv = (1-a*4, 4-a*12)
p_nat = mv_from_nat(t0-a*(t0-THETA_PI))
p_log = (1-a*4, 4*np.exp(-a*3))
ax.annotate('', xy=(1-0.06*4, 4-0.06*12), xytext=(1, 4), arrowprops=dict(arrowstyle='-|>', color=STROKE, lw=1.0, mutation_scale=7))
for (m_, v_), col, lab, off in ((p_mv, YELLOW, r'$(\mu,v)$', (-0.04, 0.0)), (p_nat, GREEN, r'$\theta$', (0.04, 0.0)), (p_log, PURPLE, r'$(\mu,\tau)$', (-0.04, 0.0))):
    ax.scatter([m_], [v_], s=16, color=col, zorder=6)
    ax.text(m_+off[0], v_+off[1], lab, color=col, ha='right' if off[0] < 0 else 'left', va='center', fontsize=7.5)
ax.scatter([1], [4], s=16, color=RED, zorder=6); ax.scatter([0], [1], s=16, color=RED, marker='x', zorder=6)
ax.set_xlim(-0.3, 1.3); ax.set_ylim(0.6, 4.6); ax.set_xlabel(r'$\mu$', labelpad=1); ax.set_ylabel(r'$v=\sigma^{2}$', labelpad=1)
save(fig, HERE, 'figure', {'mv': list(map(float, p_mv)), 'nat': list(map(float, p_nat)), 'log': list(map(float, p_log)),
                            'L': [float(L_mv(*p)) for p in (p_mv, p_nat, p_log)]})
