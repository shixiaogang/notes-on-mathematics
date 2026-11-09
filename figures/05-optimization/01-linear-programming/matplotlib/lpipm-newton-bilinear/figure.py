from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Newton on mu/x-s=0 against Newton on xs-mu=0, with s=mu=1 fixed for the picture.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
x = np.linspace(.16, 3, 500); x0 = 2.4
a.plot(x, 1 / x - 1, color=BLUE, lw=1.4)
g0 = 1 / x0 - 1; dg = -1 / x0 ** 2; xn = x0 - g0 / dg
tt = np.array([xn - .2, x0 + .2]); a.plot(tt, g0 + dg * (tt - x0), color=GREEN, lw=1.2)
a.plot([x0], [g0], 'o', color=GREEN, ms=4); a.plot([xn], [0], 'o', color=RED, ms=4, zorder=6)
a.plot([1], [0], 'o', color=RED, ms=4, mfc='white', zorder=6)
a.axhline(0, color='#6B7280', lw=.85); a.axvline(0, color='#4C4D4F', lw=1.8)
a.text(x0 + .02, g0 + .34, '$x^{(t)}$', fontsize=7.5, ha='center')
a.text(xn - .05, .22, '$x^{(t+1)}$', fontsize=7.5, ha='center')
a.text(1.0, .22, '根', fontsize=7.5, ha='center')
a.set_xlim(-1.4, 3); a.set_ylim(-1, 2)
a.set_xlabel('$x$\n(a) $\\mu/x-s=0$', labelpad=1)
b.plot(x, x - 1, color=BLUE, lw=1.4); b.plot(np.array([-1.4, 3]), np.array([-1.4, 3]) - 1, color=BLUE, lw=1.4)
b.plot([x0], [x0 - 1], 'o', color=GREEN, ms=4); b.plot([1], [0], 'o', color=RED, ms=4, zorder=6)
b.axhline(0, color='#6B7280', lw=.85); b.axvline(0, color='#4C4D4F', lw=1.8)
b.text(x0, x0 - 1 + .3, '$x^{(t)}$', fontsize=7.5, ha='center'); b.text(1.05, -.4, '根', fontsize=7.5)
b.set_xlim(-1.4, 3); b.set_ylim(-1, 2)
b.set_xlabel('$x$\n(b) $xs-\\mu=0$', labelpad=1)
save(fig, OUT, 'figure', {'s': 1, 'mu': 1, 'x0': x0, 'newton_on_inverse': xn})
