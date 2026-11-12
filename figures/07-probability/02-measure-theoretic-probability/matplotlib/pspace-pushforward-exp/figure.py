from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: Omega=[0,1) with length as probability, X(omega) = -ln(1-omega).
# Preimage of B=(1,2] is (1-e^{-1}, 1-e^{-2}], of length e^{-1}-e^{-2}; this equals the Exp(1) mass of (1,2].
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
for ax in (a, b): style(ax)
w = np.linspace(0, 0.97, 400)
lo, hi = 1-np.exp(-1), 1-np.exp(-2)
xs = np.linspace(1, 2, 100)
a.fill_betweenx(xs, 0, 1-np.exp(-xs), color=BLUE_FILL, lw=0, zorder=0)
ws = np.linspace(lo, hi, 100)
a.fill_between(ws, 0, -np.log(1-ws), color=BLUE_FILL, lw=0, zorder=0)
a.plot(w, -np.log(1-w), color=BLUE, lw=1.4)
for v in (lo, hi):
    a.plot([v, v], [0, -np.log(1-v)], color=LINE, lw=.85, ls='--')
    a.plot([0, v], [-np.log(1-v)]*2, color=LINE, lw=.85, ls='--')
a.plot([lo, hi], [0, 0], color=RED, lw=2.4, solid_capstyle='butt', zorder=5)
a.plot([0, 0], [1, 2], color=RED, lw=2.4, solid_capstyle='butt', zorder=5, clip_on=False)
a.set_xlim(0, 1); a.set_ylim(0, 3.5)
a.set_xticks([0, lo, hi, 1]); a.set_xticklabels(['0', '0.632', '0.865', '1'])
a.set_yticks([0, 1, 2, 3])
a.set_ylabel(r'$x=X(\omega)$'); sub(a, 'a', r'$\omega$')
x = np.linspace(0, 3.5, 400)
b.fill_between(x, 0, np.exp(-x), where=(x >= 1) & (x <= 2), color=BLUE_FILL, lw=0)
b.plot(x, np.exp(-x), color=BLUE, lw=1.4)
b.plot([1, 2], [0, 0], color=RED, lw=2.4, solid_capstyle='butt', zorder=5)
b.text(1.5, 0.08, '0.2325', ha='center', fontsize=7.5, color=INK)
b.set_xlim(0, 3.5); b.set_ylim(0, 1.05); b.set_xticks([0, 1, 2, 3]); b.set_yticks([0, 0.5, 1])
b.set_ylabel(r'$f_X(x)=\mathrm{e}^{-x}$'); sub(b, 'b', '$x$')
p = np.exp(-1)-np.exp(-2); assert abs(p-0.23254) < 1e-4
save(fig, HERE(__file__), 'figure', {'preimage': [lo, hi], 'P(1<X<=2)': p})
