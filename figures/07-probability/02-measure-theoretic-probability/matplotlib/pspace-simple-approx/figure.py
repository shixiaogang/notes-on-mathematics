from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: expectation as a limit of simple approximations.
# Omega=[0,1) with length, X(omega) = -ln(1-omega) ~ Exp(1).
# phi_n = min(n, floor(2^n X)/2^n);  E[phi_n] = sum_k (k/2^n) P(k/2^n <= X < (k+1)/2^n) + n e^{-n}, increasing to E[X] = 1.
e = np.exp
def Ephi(n):
    k = np.arange(n*2**n)
    return float(np.sum(k/2**n*(e(-k/2**n)-e(-(k+1)/2**n))) + n*e(-n))
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
for ax in (a, b): style(ax)
w = np.linspace(0, 0.995, 3000)
X = -np.log(1-w)
phi2 = np.minimum(2, np.floor(4*X)/4)
a.plot(w, X, color=BLUE, lw=1.4)
a.plot(w, phi2, color=GREEN, lw=1.2, drawstyle='steps-post')
a.fill_between(w, 0, phi2, step='post', color=GREEN_FILL, lw=0)
a.set_xlim(0, 1); a.set_ylim(0, 3.2); a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 1, 2, 3])
a.text(0.9, 2.95, '$X$', color=BLUE); a.text(0.6, 2.15, r'$\varphi_2$', color=GREEN)
sub(a, 'a', r'$\omega$')
ns = np.arange(1, 9); vals = [Ephi(n) for n in ns]
b.plot(ns, vals, 'o-', ms=3.2, color=GREEN, lw=1.0)
b.axhline(1, color=PURPLE, lw=.85, ls='--')
b.set_xlim(0.5, 8.5); b.set_ylim(0, 1.1); b.set_xticks(ns); b.set_yticks([0, 0.5, 1])
b.set_ylabel(r'$\mathrm{E}[\varphi_n]$'.replace(r'\mathrm{E}', 'E')); sub(b, 'b', '$n$')
assert abs(vals[0]-0.4872) < 1e-4 and abs(vals[1]-0.7611) < 1e-4
save(fig, HERE(__file__), 'figure', {'E[phi_n], n=1..8': [round(v, 4) for v in vals]})
