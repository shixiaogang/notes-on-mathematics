"""Minimum KL with mean constraint not attained on {1,2,...}.
P(k)=c/k^3, c=1/zeta(3); E_P[X]=zeta(2)/zeta(3)=1.3684; constraint E_Q[X]=2.
Q_N=(1-eps)P+eps delta_N with eps=(2-E_P X)/(N-E_P X) satisfies the constraint.
(a) log-log masses P(k) (blue points); Q_100 differs by the factor (1-eps) and the extra mass eps at N=100 (red stem).
(b) D(Q_N||P) (green, exact sum truncated at 2e6) and the approximation eps ln(eps N^3/c) (purple dashed)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

K = np.arange(1, 2_000_001, dtype=float)
c = 1/np.sum(K**-3.0); P = c*K**-3.0; mu = float(np.sum(K*P))
def QN(N):
    eps = (2-mu)/(N-mu); q = (1-eps)*P.copy(); q[N-1] += eps; return eps, q
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
k = np.arange(1, 201)
eps, q = QN(100)
a.loglog(k, P[:200], 'o', ms=1.8, color=BLUE)
a.plot([100, 100], [P[99], q[99]], color=RED, lw=1.2)
a.scatter([100], [q[99]], s=16, color=RED, zorder=5)
a.text(100*0.85, q[99], r'$Q_N(N)$', fontsize=7.5, color=MUTED, va='center', ha='right')
a.text(8, 3e-2, r'$P(k)$', fontsize=7.5, color=BLUE, ha='left')
a.set_xlabel(r'$k$', labelpad=1); a.set_ylim(1e-7, 1.5)
Ns = np.unique(np.round(np.logspace(1, 6, 26)).astype(int))
Dv = []
for N in Ns:
    e_, q_ = QN(N); Dv.append(kl(q_, P))
Dv = np.array(Dv)
epsN = (2-mu)/(Ns-mu)
b.loglog(Ns, Dv, color=GREEN, lw=1.4, marker='o', ms=2.2)
b.loglog(Ns, epsN*np.log(epsN*Ns**3.0/c), color=PURPLE, lw=1.0, ls='--')
b.set_xlabel(r'$N$', labelpad=1); b.set_ylabel(r'$D_{\mathrm{KL}}(Q_N\Vert P)$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'c': float(c), 'mean_P': mu, 'N': Ns.tolist(), 'D': Dv.tolist(), 'eps_100': eps})
