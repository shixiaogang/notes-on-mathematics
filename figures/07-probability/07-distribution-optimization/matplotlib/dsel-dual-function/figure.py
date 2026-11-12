"""Dual function g_m(theta)=A(theta)-theta m, A(theta)=ln((1+e^theta+e^{2theta})/3), P uniform on {0,1,2}, T(x)=x.
m=1 (yellow): minimum 0 at theta=0; m=10/7 (blue): minimum -D* = ln(7/3)-(10/7)ln2 = -0.1429 at theta=ln2;
m=2 (purple): strictly decreasing, infimum ln(1/3) = -ln 3 approached as theta->inf (grey dashed), not attained."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

th = np.linspace(-3, 6, 600)
A = np.log((1+np.exp(th)+np.exp(2*th))/3)
fig, ax = figure(width_mm=90, height_mm=52)
for m, col in ((1, YELLOW), (10/7, BLUE), (2, PURPLE)):
    ax.plot(th, A-th*m, color=col, lw=1.5 if col == YELLOW else 1.4)
ax.axhline(-math.log(3), color=STROKE, lw=0.8, ls='--')
t1 = math.log(2); v1 = math.log(7/3)-10/7*t1
ax.scatter([0, t1], [0, v1], s=16, color=RED, zorder=5)
ax.text(3.2, 3.2, r'$m=1$', color=YELLOW, ha='right'); ax.text(4.4, 1.05, r'$m=10/7$', color=BLUE, va='top')
ax.text(4.0, -0.75, r'$m=2$', color=PURPLE)
ax.text(5.9, -math.log(3)-0.08, r'$-\ln 3$', color=MUTED, ha='right', va='top', fontsize=7.5)
ax.set_xlim(-3, 6); ax.set_ylim(-1.6, 3.6)
ax.set_xlabel(r'$\theta$', labelpad=1); ax.set_ylabel(r'$A(\theta)-\theta m$', labelpad=1)
save(fig, HERE, 'figure', {'min_m10_7': v1, 'theta_m10_7': t1, 'inf_m2': -math.log(3)})
