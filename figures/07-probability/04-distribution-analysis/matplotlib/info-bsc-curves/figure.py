from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# X ~ Bern(1/2), Y = X xor N, N ~ Bern(e) independent. H(X|Y) = h_b(e) (blue),
# I(X;Y) = ln2 - h_b(e) (green); the two add up to H(X) = ln 2 (purple dashed). Red: e = 1/4.
fig, ax = figure(width_mm=86, height_mm=50)
panel(fig, left=.12, right=.96, bottom=.2, top=.95)
e = np.linspace(0, 1, 801)
ax.plot(e, hb(e), color=BLUE, lw=1.4); ax.plot(e, LN2-hb(e), color=GREEN, lw=1.4)
ax.axhline(LN2, color=PURPLE, lw=.85, ls=DASH)
for v in (float(hb(.25)), LN2-float(hb(.25))): dot(ax, .25, v)
ax.plot([.25, .25], [0, float(hb(.25))], color=STROKE, lw=.6, ls=DOT)
lab(ax, .5, .58, r'$H(X\mid Y)$', BLUE, ha='center'); lab(ax, .5, .05, r'$I(X;Y)$', GREEN, ha='center')
lab(ax, .82, LN2+.02, r'$H(X)=\ln 2$', PURPLE, ha='center')
ax.set_xlim(0, 1); ax.set_ylim(0, .8); axlab(ax, r'$\varepsilon$', 'nat')
save(fig, HERE, 'figure', {'H(X|Y) e=1/4': float(hb(.25)), 'I e=1/4': LN2-float(hb(.25))})
