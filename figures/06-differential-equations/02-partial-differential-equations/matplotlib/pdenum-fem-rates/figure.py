from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# P1 errors. In 1D with a(u,v)=int u'v' the Galerkin solution equals the nodal interpolant.
# (a) running example: H1 seminorm and L2. (b) u=x^0.75-x, uniform vs graded x_i=(i/n)^4, closed-form element integrals.
from numpy.polynomial.legendre import leggauss
gx, gw = leggauss(24)
def smooth(n):
    nodes = np.linspace(0, 1, n+1); U = uex(nodes); e1 = e0 = 0
    for a, b, ua, ub in zip(nodes[:-1], nodes[1:], U[:-1], U[1:]):
        h = b-a; q = (a+b)/2+h/2*gx; w = h/2*gw; s = (ub-ua)/h
        e0 += np.sum(w*(uex(q)-ua-s*(q-a))**2); e1 += np.sum(w*(PI*np.cos(PI*q)+1-s)**2)
    return np.sqrt(e1), np.sqrt(e0)
al = .75
u = lambda x: x**al-x
G = lambda x: al**2/(2*al-1)*x**(2*al-1)-2*x**al+x  # antiderivative of (u')^2
def rough(nodes):
    a, b = nodes[:-1], nodes[1:]; h = b-a; s = (u(b)-u(a))/h
    return np.sqrt(np.sum(G(b)-G(a)-2*s*(u(b)-u(a))+s*s*h))
ns = 2**np.arange(3, 12)
S = np.array([smooth(n) for n in ns if n <= 1024]); ns_s = ns[ns <= 1024]
Ru = np.array([rough(np.linspace(0, 1, n+1)) for n in ns]); Rg = np.array([rough((np.arange(n+1)/n)**4) for n in ns])
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, left=.105, wspace=.25, bottom=.25)
ax = axes[0]; h = 1/ns_s
ax.loglog(h, S[:, 0], color=GREEN, lw=1.4, marker='o', ms=3, mew=0); ax.loglog(h, S[:, 1], color=YELLOW, lw=1.5, marker='s', ms=3, mew=0)
ax.loglog(h, 1.7*S[-1, 0]*(h/h[-1]), color=PURPLE, lw=.9, ls=DASH); ax.loglog(h, 1.7*S[-1, 1]*(h/h[-1])**2, color=PURPLE, lw=.9, ls=DASH)
lab(ax, .012, .13, r'$H^1$', GREEN, ha='center'); lab(ax, .012, 2.2e-5, r'$L^2$', YELLOW, ha='center'); ax.set_xlabel('$h$', labelpad=1); ax.set_ylabel('误差', labelpad=1)
ax = axes[1]; h = 1/ns
ax.loglog(h, Ru, color=RED, lw=1.4, marker='o', ms=3, mew=0); ax.loglog(h, Rg, color=GREEN, lw=1.4, marker='s', ms=3, mew=0)
ax.loglog(h, 1.3*Rg[-1]*(h/h[-1]), color=PURPLE, lw=.9, ls=DASH); ax.loglog(h, 1.25*Ru[-1]*(h/h[-1])**.25, color=PURPLE, lw=.9, ls=DOT)
lab(ax, .01, .34, '均匀网格', RED, ha='center'); lab(ax, .012, .0045, '加密网格', GREEN, ha='center'); ax.set_xlabel('$1/n$', labelpad=1)
tags(fig, axes)
save(fig, HERE, 'figure', {'H1_rate': np.log2(S[:-1, 0]/S[1:, 0]).tolist(), 'L2_rate': np.log2(S[:-1, 1]/S[1:, 1]).tolist(), 'uniform_rate': np.log2(Ru[:-1]/Ru[1:]).tolist(), 'graded_rate': np.log2(Rg[:-1]/Rg[1:]).tolist()})
print(np.log2(S[:-1]/S[1:]).round(3)); print(np.log2(Ru[:-1]/Ru[1:]).round(3)); print(np.log2(Rg[:-1]/Rg[1:]).round(3))
