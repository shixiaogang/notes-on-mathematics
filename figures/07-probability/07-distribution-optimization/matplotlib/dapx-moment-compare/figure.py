from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Quartic target pi=exp(-x^4/4)/Z: E X^2 = 2 Gamma(3/4)/Gamma(1/4)=0.6760, E X^4 = 1.
# Gaussian fits: D(Q||Pi) -> N(0, 3^{-1/2}) (var 0.5774, E X^4 = 3 var^2 = 1) (yellow);
#                D(Pi||Q) -> N(0, 0.6760) (E X^4 = 1.3709) (purple).
# (a) densities; (b) second and fourth moments of the three distributions.
Z = math.exp(LNZ4)
m2 = 2*math.gamma(.75)/math.gamma(.25)
vr = 3**-0.5
x = np.linspace(-3, 3, 1201)
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.28)
ax = axs[0]
ax.plot(x, np.exp(-x**4/4)/Z, color=BLUE, lw=1.4)
ax.plot(x, npdf(x, 0, math.sqrt(vr)), color=YELLOW, lw=1.6)
ax.plot(x, npdf(x, 0, math.sqrt(m2)), color=PURPLE, lw=1.3, ls=DASH)
lab(ax, -2.9, .45, r'$\pi$', BLUE); ax.annotate('', xy=(-1.0, .38), xytext=(-2.6, .46), arrowprops=dict(arrowstyle='->', color=BLUE, lw=.85))
ax.set_xlim(-3, 3); ax.set_ylim(0, .6); axlab(ax, '$x$', None)
ax = axs[1]
vals = {'target': (m2, 1.0), 'rev': (vr, 3*vr*vr), 'fwd': (m2, 3*m2*m2)}
xs = np.array([0, 1])
bars(ax, xs, vals['target'], BLUE, BLUE_FILL, width=.24, offset=-.26)
bars(ax, xs, vals['rev'], YELLOW, YELLOW_FILL, width=.24, offset=0)
bars(ax, xs, vals['fwd'], PURPLE, PURPLE_FILL, width=.24, offset=.26)
for i in range(2):
    for off, k, c in ((-.26, 'target', BLUE), (0, 'rev', YELLOW), (.26, 'fwd', PURPLE)):
        v = vals[k][i]; lab(ax, i+off, v+.03, f'{v:.2f}', INK, ha='center', fontsize=6.5)
ax.set_xticks(xs); ax.set_xticklabels(['二阶矩', '四阶矩'])
ax.set_xlim(-.55, 1.55); ax.set_ylim(0, 1.55)
tags(fig, axs)
save(fig, HERE, 'figure', {k: list(v) for k, v in vals.items()})
