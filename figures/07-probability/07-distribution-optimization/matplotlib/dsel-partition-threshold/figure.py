"""Geometric reference P(k)=2^{-k} on {1,2,...}, cost V(k)=-k.
Z(tau)=E_P[e^{-V/tau}]=r/(1-r), r=e^{1/tau}/2, finite iff tau>1/ln2.
(a) optimal value -tau ln Z(tau) for tau in (1/ln2, 6] (blue); threshold tau=1/ln2 (grey dashed).
(b) objective J(Q_N)=E_{Q_N}[V]+tau D(Q_N||P) for Q_N uniform on {1..N}:
    J = -(N+1)/2 + tau((N+1)ln2/2 - ln N). tau=1/ln2 gives -log2 N -> -inf (green);
    tau=2 (yellow) stays above -2 ln Z(2) = -3.092 (purple dashed)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

t0 = 1/math.log(2)
def Zf(t):
    r = np.exp(1/t)/2
    return r/(1-r)
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
ts = np.linspace(t0+0.004, 6, 600)
a.plot(ts, -ts*np.log(Zf(ts)), color=BLUE, lw=1.4)
a.axvline(t0, color=STROKE, lw=0.8, ls='--')
a.text(t0+0.12, -7.3, r'$\tau=1/\ln 2$', color=MUTED, fontsize=7.5, ha='left')
a.set_xlim(1, 6); a.set_ylim(-8, 0)
a.set_xlabel(r'$\tau$', labelpad=1); a.set_ylabel(r'$-\tau\ln Z(\tau)$', labelpad=1)
N = np.arange(1, 61)
def J(t):
    return -(N+1)/2 + t*((N+1)*math.log(2)/2 - np.log(N))
b.plot(N, J(t0), color=GREEN, lw=1.4)
b.plot(N, J(2.0), color=YELLOW, lw=1.5)
lb = -2*math.log(Zf(2.0))
b.axhline(lb, color=PURPLE, lw=1.0, ls='--')
b.text(58, J(t0)[-1]+0.25, r'$\tau=1/\ln 2$', color=GREEN, ha='right', va='bottom', fontsize=7.5)
b.text(58, 0.6, r'$\tau=2$', color=YELLOW, ha='right', va='center', fontsize=7.5)
b.set_xlim(0, 60); b.set_ylim(-6.5, 3)
b.set_xlabel(r'$N$', labelpad=1); b.set_ylabel(r'$J_\tau(Q_N)$', labelpad=1)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'threshold': t0, 'lower_bound_tau2': lb, 'J_min_tau2': float(J(2.0).min()),
     'N_at_min_tau2': int(N[J(2.0).argmin()]), 'J_60_tau0': float(J(t0)[-1])})
