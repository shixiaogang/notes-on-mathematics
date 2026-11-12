"""Diagonal sections C(u,u): W=max(2u-1,0), Pi=u^2, Gaussian rho=0.7 (numeric), M=u; red points at u=1-1/e."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

u = np.linspace(0.001, 0.999, 300)
zz = Phi_inv(u)
cg = np.array([binorm_cdf(t, t, 0.7) for t in zz])
fig, ax = figure(width_mm=64, height_mm=60)
ax.plot(u, u, color=PURPLE, lw=1.3, ls='--')
ax.plot(u, np.maximum(2*u-1, 0), color=PURPLE, lw=1.3, ls='--')
ax.plot(u, u*u, color=BLUE, lw=1.4)
ax.plot(u, cg, color=YELLOW, lw=1.5)
u0 = 1-np.exp(-1)
z0 = float(Phi_inv(u0)[0])
vals = [max(2*u0-1, 0), u0*u0, binorm_cdf(z0, z0, 0.7), u0]
ax.axvline(u0, color=STROKE, lw=0.6, ls=':')
ax.scatter([u0]*4, vals, s=14, color=RED, zorder=5)
ax.text(0.36, 0.43, '$M$', color=PURPLE, fontsize=8, ha='right')
ax.text(0.80, 0.53, '$W$', color=PURPLE, fontsize=8)
ax.text(0.86, 0.66, r'$\Pi$', color=BLUE, fontsize=8)
ax.annotate(r'$C_{0.7}$', xy=(0.3, binorm_cdf(float(Phi_inv(0.3)[0]), float(Phi_inv(0.3)[0]), 0.7)), xytext=(0.06, 0.62), color=YELLOW, fontsize=8, arrowprops=dict(arrowstyle='-', color=YELLOW, lw=0.8))
ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xlabel('$u$', labelpad=1); ax.set_ylabel('$C(u,u)$')
ax.set_box_aspect(1)
save(fig, HERE, 'figure', {'u0': u0, 'values_W_Pi_Gauss_M': vals})
