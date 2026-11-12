from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/08-sampling-and-integration/matplotlib/sgen-common"))
from sgen_common import *
from statistics import NormalDist
# Target: leapfrog for U(x) = x^2/2 (standard normal target), H = x^2/2 + p^2/2, start (x, p) = (1, Phi^{-1}(0.8)).
# (a) exact orbit (blue circle) and 12 leapfrog steps with eps = 0.5 (green) and eps = 1.8 (yellow).
# (b) max |H - H_0| along a trajectory of length about 3 (L = round(3/eps)) against eps; purple reference slope eps^2.
x0, p0 = 1.0, NormalDist().inv_cdf(.8)
def lf(x, p, eps, L):
    P = [(x, p)]
    for _ in range(L):
        p = p-eps/2*x; x = x+eps*p; p = p-eps/2*x; P.append((x, p))
    return np.array(P)
H = lambda P: .5*P[:, 0]**2+.5*P[:, 1]**2
fig, (A, B) = figure(width_mm=112, height_mm=54, ncols=2)
style(A); style(B)
r = math.sqrt(x0**2+p0**2); th = np.linspace(0, 2*np.pi, 300)
A.plot(r*np.cos(th), r*np.sin(th), color=BLUE, lw=1.2)
for eps, col in ((.5, GREEN), (1.8, YELLOW)):
    P = lf(x0, p0, eps, 12)
    A.plot(P[:, 0], P[:, 1], '-o', ms=2.2, lw=.7, color=col)
A.plot([x0], [p0], 'o', ms=3.8, color=RED, zorder=6)
A.set_aspect('equal'); A.set_xlim(-2.6, 2.6); A.set_ylim(-2.6, 2.6); A.set_xticks([-2, 0, 2]); A.set_yticks([-2, 0, 2])
A.set_ylabel('$p$'); sub(A, 'a', '$x$')
E = np.geomspace(.05, 1.95, 40); err = []
for eps in E:
    P = lf(x0, p0, eps, max(1, round(3/eps))); err.append(np.max(np.abs(H(P)-H(P[:1]))))
B.loglog(E, err, color=GREEN, lw=1.3)
B.loglog(E, .25*E**2, color=PURPLE, lw=1.0, ls='--')
B.text(.12, .25*.12**2*0.35, r'$\propto\varepsilon^2$', fontsize=7.5, color=INK)
B.set_xlim(.05, 2); B.set_ylabel(r'$\max|H-H_0|$'); sub(B, 'b', r'$\varepsilon$')
P2 = lf(x0, p0, .5, 2)
save(fig, HERE(__file__), 'figure', {'two_steps_eps_0.5': P2.tolist(), 'dH': float(H(P2)[-1]-H(P2)[0])})
print(P2, H(P2)[-1]-H(P2)[0])
