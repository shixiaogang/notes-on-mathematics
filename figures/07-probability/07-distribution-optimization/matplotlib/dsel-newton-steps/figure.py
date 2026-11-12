"""Newton's method for the moment equation A'(theta)=m, P uniform on {0,1,2}, T(x)=x, m=10/7, solution ln 2.
Update theta <- theta - (A'(theta)-m)/A''(theta).
(a) Mean map A'(theta) (blue), level m (red), tangent lines (green dashed) from theta^(0)=-1:
    iterates -1 -> 1.365 -> 0.446 -> ... (overshoot, then convergence).
(b) |A'(theta^(t)) - m| on log scale for the starts theta^(0)=0 (green solid) and theta^(0)=-1 (green dashed)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

def mv(t):
    q = tilt(U3, X3, t); mu = q@X3; return mu, q@(X3**2)-mu**2
m = 10/7
def newton(t0, n):
    its = [t0]
    for _ in range(n):
        mu, v = mv(its[-1]); its.append(its[-1]-(mu-m)/v)
    return its
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
th = np.linspace(-2, 2.5, 400)
a.plot(th, [mv(t)[0] for t in th], color=BLUE, lw=1.4)
a.axhline(m, color=RED, lw=1.1)
its = newton(-1.0, 6)
for k in range(2):
    t = its[k]; mu, v = mv(t); t1 = its[k+1]
    lo, hi = min(t, t1)-0.15, max(t, t1)+0.15
    tt = np.linspace(lo, hi, 20)
    a.plot(tt, mu+v*(tt-t), color=GREEN, lw=1.0, ls='--')
    a.plot([t1, t1], [m, mv(t1)[0]], color=STROKE, lw=0.6, ls=':')
for k in range(3):
    a.scatter([its[k]], [mv(its[k])[0]], s=14, color=GREEN, zorder=5)
    dx, dy, ha, va = [(0.1, -0.04, 'left', 'top'), (0.0, 0.07, 'center', 'bottom'), (0.08, -0.03, 'left', 'top')][k]
    a.text(its[k]+dx, mv(its[k])[0]+dy, rf'$\theta^{{({k})}}$', fontsize=7.5, color=MUTED, ha=ha, va=va)
a.scatter([math.log(2)], [m], s=16, color=RED, zorder=6)
a.set_xlim(-2, 2.5); a.set_ylim(0, 2)
a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel(r"$A'(\theta)$", labelpad=1)
for t0, ls in ((0.0, '-'), (-1.0, '--')):
    it = newton(t0, 7)
    r = np.array([abs(mv(t)[0]-m) for t in it])
    k = np.arange(len(it)); keep = r > 1e-15
    b.semilogy(k[keep], r[keep], color=GREEN, lw=1.3, ls=ls, marker='o', ms=2.6)
b.set_xlabel(r'$t$', labelpad=1); b.set_ylabel(r'$|A^{\prime}(\theta^{(t)})-m|$', labelpad=1)
b.set_xlim(-0.3, 6.3); b.set_ylim(1e-16, 3)
b.text(0.9, 1e-9, r'$\theta^{(0)}=0$', color=GREEN, fontsize=7.5, ha='left')
b.text(5.2, 1e-4, r'$\theta^{(0)}=-1$', color=GREEN, fontsize=7.5, ha='left')
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
save(fig, HERE, 'figure', {'iterates_from_0': newton(0.0, 5), 'iterates_from_-1': newton(-1.0, 7),
     'residuals_from_0': [abs(mv(t)[0]-m) for t in newton(0.0, 5)],
     'residuals_from_-1': [abs(mv(t)[0]-m) for t in newton(-1.0, 7)]})
