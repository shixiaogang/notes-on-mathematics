"""Redundant statistic T(x)=(x, 2-x) on {0,1,2}, P uniform, m=(10/7, 4/7).
Dual function g(theta)=A(theta)-<theta,m> = a(theta1-theta2) - (10/7)(theta1-theta2), a(s)=ln((1+e^s+e^{2s})/3).
Level lines (thin blue) are parallel to (1,1); the minimizers form the line theta1-theta2=ln2 (red), every point
giving the same Q*=(1/7,2/7,4/7). Two such points (0,-ln2) and (ln2,0) in green."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

t1, t2 = np.meshgrid(np.linspace(-2, 2.5, 300), np.linspace(-2, 2.5, 300))
s = t1-t2
g = np.log((1+np.exp(s)+np.exp(2*s))/3)-10/7*s
fig, ax = figure(width_mm=70, height_mm=62)
lev = [-0.1, 0.0, 0.2, 0.5, 1.0, 1.6]
ax.contour(t1, t2, g, levels=lev, colors=[BLUE], linewidths=0.7, linestyles='solid')
L = math.log(2); xx = np.linspace(-2, 2.5, 10)
ax.plot(xx, xx-L, color=RED, lw=1.6)
ax.scatter([0, L], [-L, 0], s=14, color=GREEN, zorder=5)
ax.text(0.08, -L-0.08, r'$(0,-\ln 2)$', fontsize=7.5, color=MUTED, ha='left', va='top')
ax.text(L+0.08, -0.08, r'$(\ln 2,0)$', fontsize=7.5, color=MUTED, ha='left', va='top')
ax.set_xlim(-2, 2.5); ax.set_ylim(-2, 2.5); ax.set_aspect('equal')
ax.set_xlabel(r'$\theta_1$', labelpad=1); ax.set_ylabel(r'$\theta_2$', labelpad=1)
save(fig, HERE, 'figure', {'min_value': math.log(7/3)-10/7*L, 'valley': 'theta1-theta2=ln2', 'levels': lev})
