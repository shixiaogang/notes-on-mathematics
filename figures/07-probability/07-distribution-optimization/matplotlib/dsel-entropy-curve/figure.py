"""Die faces {1..6}, constraint E[X]=m, 1<m<6. Max-entropy q propto e^{theta x}.
(a) maximal entropy H*(m) (blue), upper bound ln 6 (purple dashed), red point m=4.5 (H*=1.6136).
(b) multiplier theta(m) (blue), red point (4.5, 0.3710); theta -> +-inf as m -> 6 or 1."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

f = np.arange(1, 7, dtype=float)
def stats(t):
    w = np.exp(t*f); q = w/w.sum(); return q@f, -np.sum(q*np.log(q))
ts = np.linspace(-6, 6, 1200)
M = np.array([stats(t)[0] for t in ts]); H = np.array([stats(t)[1] for t in ts])
lo, hi = -20, 20
for _ in range(200):
    mid = (lo+hi)/2
    if stats(mid)[0] < 4.5: lo = mid
    else: hi = mid
t45 = (lo+hi)/2; m45, H45 = stats(t45)
fig, (a, b) = figure(width_mm=112, height_mm=46, ncols=2)
a.plot(M, H, color=BLUE, lw=1.4)
a.axhline(math.log(6), color=PURPLE, lw=1.0, ls='--')
a.scatter([4.5], [H45], s=16, color=RED, zorder=5)
a.text(1.1, math.log(6)+0.04, r'$\ln 6$', color=PURPLE, fontsize=7.5, va='bottom')
a.set_xlim(1, 6); a.set_ylim(0, 2.0)
a.set_xlabel(r'$m$', labelpad=1); a.set_ylabel(r'$H^{*}(m)$', labelpad=1)
b.plot(M, ts, color=BLUE, lw=1.4)
b.scatter([4.5], [t45], s=16, color=RED, zorder=5)
b.axhline(0, color=STROKE, lw=0.6)
b.set_xlim(1, 6); b.set_ylim(-4, 4)
b.set_xlabel(r'$m$', labelpad=1); b.set_ylabel(r'$\theta(m)$', labelpad=1)
tag(a, '(a)', y=-0.29); tag(b, '(b)', y=-0.29)
save(fig, HERE, 'figure', {'theta_4.5': t45, 'H_4.5': float(H45), 'ln6': math.log(6)})
