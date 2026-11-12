"""Natural parameter domains, T(x)=x on (0,inf). Blue: h=1 (A=-ln(-theta), mean -1/theta), Theta=(-inf,0).
Yellow: h=(1+x)^-2, Theta=(-inf,0], A(0)=0, mean -> inf as theta->0- (numerical quadrature on log grid up to 1e7)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

xs = np.concatenate([np.linspace(0, 1, 2001), np.logspace(0, 7, 60001)[1:]])
h = (1+xs)**-2
def Zm(t):
    w = h*np.exp(t*xs)
    Z = np.trapezoid(w, xs)
    return Z, np.trapezoid(xs*w, xs)/Z
th = -np.logspace(np.log10(3.2), -3, 160)
A2 = []; M2 = []
for t in th:
    Z, m = Zm(t); A2.append(np.log(Z)); M2.append(m)
fig, (a, b) = figure(width_mm=108, height_mm=46, ncols=2)
t1 = np.linspace(-3.2, -0.02, 400)
a.plot(t1, -np.log(-t1), color=BLUE, lw=1.4)
a.plot(th, A2, color=YELLOW, lw=1.5)
a.scatter([0], [0], s=16, color=RED, zorder=5, clip_on=False)
a.axvline(0, color=STROKE, lw=0.6, ls=':')
a.set_xlim(-3.2, 0.25); a.set_ylim(-1.5, 3.5); a.set_xlabel(r'$\theta$', labelpad=1); a.set_ylabel(r'$A(\theta)$')
b.plot(t1, -1/t1, color=BLUE, lw=1.4)
b.plot(th, M2, color=YELLOW, lw=1.5)
b.axvline(0, color=STROKE, lw=0.6, ls=':')
b.set_xlim(-3.2, 0.25); b.set_ylim(0, 8); b.set_xlabel(r'$\theta$', labelpad=1); b.set_ylabel(r'$\mathrm{E}_\theta[X]$')
a.text(-1.0, 1.3, '$h=1$', color=BLUE, fontsize=7.5)
a.text(-1.25, -1.38, '$h=(1+x)^{-2}$', color=YELLOW, fontsize=7.5)
tag(a, '(a)', y=-0.27); tag(b, '(b)', y=-0.27)
Z0, _ = Zm(0.0)
save(fig, HERE, 'figure', {'Z0_numeric': float(Z0), 'A_yellow_at_-1e-3': float(A2[-1]), 'mean_yellow_at_-1e-3': float(M2[-1]), 'mean_yellow_at_-1': float(Zm(-1.0)[1])})
