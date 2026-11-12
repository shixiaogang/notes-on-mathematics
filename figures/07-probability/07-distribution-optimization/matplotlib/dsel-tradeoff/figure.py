"""Achievable pairs (D(Q||P), E_Q[V]) for Q on a grid of the simplex (step 1/60, light grey dots);
P uniform on {0,1,2}, V(x)=x. Lower frontier = Gibbs path Q_tau (blue).
Line E_Q[V] = J* - tau D through Q* (purple dashed) for tau=1/ln2, J*=log2(12/7)=0.7776."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

def gibbs(t):
    return tilt(U3, X3, -1/t)
tau = 1/math.log(2); Qs = gibbs(tau)
fig, b = figure(width_mm=84, height_mm=54)
G = simplex_grid(60)
D = np.array([kl(g, U3) for g in G]); E = G@X3
b.scatter(D, E, s=1.2, color=GRID, zorder=1, linewidths=0)
ts2 = np.exp(np.linspace(math.log(0.02), math.log(500), 600))
F = np.array([(kl(gibbs(t), U3), gibbs(t)@X3) for t in ts2])
b.plot(F[:, 0], F[:, 1], color=BLUE, lw=1.4, zorder=3)
Ds, Es = kl(Qs, U3), Qs@X3; Jst = Es+tau*Ds
dd = np.linspace(0, 0.62, 10)
b.plot(dd, Jst-tau*dd, color=PURPLE, lw=1.1, ls='--', zorder=2)
b.scatter([Ds], [Es], s=18, color=RED, zorder=5)
b.scatter([0], [1], s=16, color=YELLOW, zorder=5); b.text(0.03, 1.03, r'$P$', va='bottom')
b.scatter([math.log(3)], [0], s=16, color=STROKE, zorder=5); b.text(math.log(3)-0.02, 0.07, r'$\delta_0$', ha='right')
b.text(Ds+0.035, Es+0.03, r'$Q^{*}$', va='bottom')
b.set_xlim(-0.03, 1.15); b.set_ylim(-0.08, 2.08)
b.set_xlabel(r'$D_{\mathrm{KL}}(Q\Vert P)$', labelpad=1); b.set_ylabel(r'$\mathrm{E}_Q[V]$', labelpad=1)
save(fig, HERE, 'figure', {'tau': tau, 'Qstar': Qs.tolist(), 'D_star': Ds, 'E_star': float(Es), 'J_star': float(Jst),
     'log2_12_7': math.log2(12/7)})
