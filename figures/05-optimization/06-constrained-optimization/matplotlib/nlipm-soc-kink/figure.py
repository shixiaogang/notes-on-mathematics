from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Scalar expansion of a cone constraint has a kink at u=0; the cone barrier does not.
fig, (a, b) = figure(width_mm=112, height_mm=48, ncols=2)
u = np.linspace(-.995, .995, 1001)
a.plot(u, np.abs(u)-1, color=YELLOW, lw=1.7); a.plot([0], [-1], 'o', color=RED, ms=4.5, zorder=6)
a.axhline(0, color=EDGE, lw=1.7); a.set_xlim(-1.05, 1.05); a.set_ylim(-1.1, .15); tag(a, '$u$', '(a)'); a.set_ylabel('$g=|u|-1$', labelpad=1)
b.plot(u, -np.log(1-np.abs(u)), color=YELLOW, lw=1.7); b.plot(u, -np.log(1-u**2), color=BLUE, lw=1.5)
b.plot([0], [0], 'o', color=RED, ms=4.5, zorder=6)
for v in (-1, 1): b.axvline(v, color=EDGE, lw=1.7)
b.set_xlim(-1.05, 1.05); b.set_ylim(-.15, 3); tag(b, '$u$', '(b)')
save(fig, OUT, 'figure', {'t': 1})
