"""Undefined objective E_Q[V] + tau D(Q||P) on {1,2,...}.
P(k)=2^{-k}, V(k)=-k, Q(k)=6/(pi^2 k^2), tau=1/ln 2.
Cost partial sums C_N = sum_{k<=N} q_k V(k) -> -infinity (yellow);
KL partial sums K_N = tau sum_{k<=N} q_k ln(q_k/p_k) -> +infinity (blue);
paired sums C_N + K_N (green, solid) and C_N + K_{2N} (green, dashed) converge to different finite limits."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

tau = 1/math.log(2)
Kmax = 200000
k = np.arange(1, 2*Kmax+1, dtype=float)
q = 6/(math.pi**2*k**2)
lnp = -k*math.log(2)
C = np.cumsum(q*(-k))
Kl = tau*np.cumsum(q*(np.log(q)-lnp))
N = np.unique(np.round(np.logspace(0, math.log10(Kmax), 300)).astype(int))
c = C[N-1]; kk = Kl[N-1]; s1 = c+kk; s2 = c+Kl[2*N-1]
lim1 = tau*np.sum(q*(math.log(6/math.pi**2)-2*np.log(k)))
fig, ax = figure(width_mm=96, height_mm=50)
ax.plot(N, c, color=YELLOW, lw=1.5)
ax.plot(N, kk, color=BLUE, lw=1.4)
ax.plot(N, s1, color=GREEN, lw=1.4)
ax.plot(N, s2, color=GREEN, lw=1.3, ls='--')
ax.axhline(0, color=STROKE, lw=0.6)
ax.set_xscale('log'); ax.set_xlim(1, Kmax); ax.set_ylim(-8.5, 8.5)
ax.set_xlabel(r'$N$', labelpad=1)
ax.text(3e4, 6.2, r'$K_N$', color=BLUE); ax.text(2e4, -5.6, r'$C_N$', color=YELLOW)
ax.text(3e4, s1[-1]-0.5, r'$C_N+K_N$', color=GREEN, va='top')
ax.text(3e4, s2[-1]+0.5, r'$C_N+K_{2N}$', color=GREEN, va='bottom')
save(fig, HERE, 'figure', {'tau': tau, 'C_last': float(c[-1]), 'K_last': float(kk[-1]),
     'paired_last': float(s1[-1]), 'paired2_last': float(s2[-1]), 'limit_paired_series': float(lim1),
     'difference_expected': 6/math.pi**2*math.log(2)})
