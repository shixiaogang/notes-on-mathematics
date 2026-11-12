from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Ideal proposals q* = |f| p / E_P|f|.
# (a) p = Exp(1), f = 1{x>4}: |f|p = e^{-x} on x>4 (area e^{-4}), q*(x) = e^{-(x-4)} on x>4.
# (b) p = N(0,1), f(x) = x: |f|p = |x| phi(x), q*(x) = |x| phi(x)/sqrt(2/pi); I = 0, minimal variance 2/pi.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.22)
a, b = axs
x = np.linspace(0, 9, 900); p = np.exp(-x); qs = np.where(x > 4, np.exp(-(x-4)), 0)
m = x > 4
a.fill_between(x[m], 0, p[m], color=BLUE_FILL, lw=0)
a.plot(x, p, color=BLUE, lw=1.4)
a.plot(x[m], qs[m], color=YELLOW, lw=1.6); a.plot([4, 4], [0, 1], color=YELLOW, lw=1.6)
a.axvline(4, color=RED, lw=1.0, ymax=.08)
a.set_xlim(0, 9); a.set_ylim(0, 1.1); a.set_xticks([0, 2, 4, 6, 8]); a.set_yticks([0, .5, 1])
lab(a, 1.0, .45, r'$p$', BLUE); lab(a, 5.0, .55, r'$q^{*}$', YELLOW)
axlab(a, '$x$')
x = np.linspace(-4, 4, 801); p = phi(x); c = np.abs(x)*p; qs = c/math.sqrt(2/math.pi)
b.fill_between(x, 0, c, color=BLUE_FILL, lw=0)
b.plot(x, p, color=BLUE, lw=1.4); b.plot(x, qs, color=YELLOW, lw=1.6)
b.set_xlim(-4, 4); b.set_ylim(0, .55); b.set_xticks([-4, -2, 0, 2, 4]); b.set_yticks([0, .25, .5])
lab(b, -.5, .43, r'$p$', BLUE); lab(b, 1.75, .36, r'$q^{*}$', YELLOW); lab(b, 2.6, .09, r'$|f|p$', BLUE)
axlab(b, '$x$')
tags(fig, axs)
save(fig, HERE, 'figure', {'E_abs_f_b': math.sqrt(2/math.pi), 'min_var_b': 2/math.pi, 'I_a': math.exp(-4)})
