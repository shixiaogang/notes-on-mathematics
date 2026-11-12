from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: three ways two random variables on Omega=[0,1] can be "equal".
# (a) U(omega)=omega and 1-U agree only at omega=1/2 yet have the same uniform distribution.
# (b) U' equals U except at the points k/8 (a countable, length-zero set), where it is set to 0: equal almost surely.
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2)
for ax in (a, b): style(ax)
w = np.linspace(0, 1, 200)
a.plot(w, w, color=BLUE, lw=1.4)
a.plot(w, 1-w, color=YELLOW, lw=1.6)
a.plot([0.5], [0.5], 'o', ms=3.6, color=RED, zorder=5)
a.text(0.86, 0.95, '$U$', color=BLUE, fontsize=8); a.text(0.86, 0.22, '$1-U$', color=YELLOW, fontsize=8)
a.set_xlim(0, 1); a.set_ylim(0, 1.05); a.set_xticks([0, 0.5, 1]); a.set_yticks([0, 0.5, 1])
sub(a, 'a', r'$\omega$')
b.plot(w, w, color=BLUE, lw=1.4)
ks = np.arange(1, 8)/8
b.plot(ks, ks, 'o', ms=3.2, mfc='white', mec=BLUE, mew=.9, zorder=5)
b.plot(ks, np.zeros_like(ks), 'o', ms=3.2, color=RED, zorder=5, clip_on=False)
b.text(0.62, 0.86, "$U'$", color=BLUE, fontsize=8)
b.set_xlim(0, 1); b.set_ylim(0, 1.05); b.set_xticks([0, 0.5, 1]); b.set_yticks([0, 0.5, 1])
sub(b, 'b', r'$\omega$')
save(fig, HERE(__file__), 'figure', {'P(U=1-U)': 0, 'changed points': [float(k) for k in ks]})
