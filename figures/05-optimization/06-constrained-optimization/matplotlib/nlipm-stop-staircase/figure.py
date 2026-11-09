from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Monotone parameter updates: the barrier error E_mu against the true error E_0.
x, s, l = np.array([1., 2.]), np.array([1., 2.]), np.array([1., .5])
mu = 1.; kap = .1; tau = .2; eta = .9
def E(x, s, l, m):
    rd, rp, _ = residuals(x, s, l, 0); return max(np.abs(rd).max(), np.abs(rp).max(), np.abs(s*l-m).max())
E0 = []; Em = []; Mu = []
for k in range(60):
    E0.append(E(x, s, l, 0.)); Em.append(E(x, s, l, mu)); Mu.append(mu)
    while E(x, s, l, mu) <= kap*mu and mu > 1e-7:
        mu *= tau
    if E0[-1] < 1e-6: break
    d = direction(x, s, l, mu)
    am = np.inf
    for v, dv in ((s, d['ds']), (l, d['dl'])):
        n = dv < 0
        if n.any(): am = min(am, (v[n]/-dv[n]).min())
    a = min(1, eta*am); x = x+a*d['dx']; s = s+a*d['ds']; l = l+a*d['dl']
fig, ax = figure(width_mm=92, height_mm=52)
T = np.arange(len(E0))
ax.step(T, Mu, where='post', color=PURPLE, lw=1.3); ax.semilogy(T, E0, color=GREEN, lw=1.5, marker='o', ms=2.8); ax.semilogy(T, Em, color=YELLOW, lw=1.6, marker='o', ms=2.8)
ax.set_yscale('log'); ax.set_xlim(0, T[-1]); ax.set_xlabel('$t$', labelpad=1)
save(fig, OUT, 'figure', {'E0': E0, 'Emu': Em, 'mu': Mu, 'kappa': kap, 'tau': tau})
