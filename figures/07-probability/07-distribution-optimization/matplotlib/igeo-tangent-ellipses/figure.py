"""Same tangent vector in two coordinates at N(1,4). (a) (mu,v): G=diag(1/4,1/32); (b) (mu,tau=ln v): G=diag(1/4,1/2).
Ellipse (1/2) d^T G d = 0.125; vector (0.6, 2.263) in (a) equals (0.6, 0.566) in (b) (dv = v dtau), both on the ellipse."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"igeo-common"))
from common import *

fig, (a, b) = figure(width_mm=104, height_mm=50, ncols=2)
eps = 0.125; ang = np.linspace(0, 2*np.pi, 300)
dtau = np.sqrt((2*eps-0.25*0.36)/0.5); dvec_b = np.array([0.6, dtau]); dvec_a = np.array([0.6, 4*dtau])
for ax, c, G, dv, lab in ((a, (1, 4), (0.25, 1/32), dvec_a, r'$v$'), (b, (1, np.log(4)), (0.25, 0.5), dvec_b, r'$\tau$')):
    ra, rb = np.sqrt(2*eps/G[0]), np.sqrt(2*eps/G[1])
    ax.fill(c[0]+ra*np.cos(ang), c[1]+rb*np.sin(ang), color=BLUE_FILL, lw=0)
    ax.plot(c[0]+ra*np.cos(ang), c[1]+rb*np.sin(ang), color=BLUE, lw=1.2)
    ax.annotate('', xy=(c[0]+dv[0], c[1]+dv[1]), xytext=c, arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.4, mutation_scale=8))
    ax.scatter([c[0]], [c[1]], s=14, color=RED, zorder=5)
    ax.set_xlabel(r'$\mu$', labelpad=1); ax.set_ylabel(lab, labelpad=1)
a.set_xlim(-0.5, 2.5); a.set_ylim(0.8, 7.2)
b.set_xlim(-0.5, 2.5); b.set_ylim(0.2, 2.6)
tag(a, '(a)', y=-0.24); tag(b, '(b)', y=-0.24)
q_a = 0.5*(0.25*dvec_a[0]**2+dvec_a[1]**2/32); q_b = 0.5*(0.25*dvec_b[0]**2+0.5*dvec_b[1]**2)
save(fig, HERE, 'figure', {'vec_a': dvec_a.tolist(), 'vec_b': dvec_b.tolist(), 'quad_a': q_a, 'quad_b': q_b})
