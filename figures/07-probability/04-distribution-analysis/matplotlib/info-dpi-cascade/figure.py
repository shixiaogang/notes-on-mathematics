from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# X ~ Bern(1/2); Y = X xor N1, N1 ~ Bern(1/4); Z = Y xor N2, N2 ~ Bern(e2), all independent.
# I(X;Y) = ln2 - h_b(1/4) (purple dashed); I(X;Z) = ln2 - h_b(1/4*(1-e2)+3/4*e2) (green).
# Red: e2 = 1/4 gives overall flip 3/8 and I(X;Z) = 0.0316 nat.
fig, ax = figure(width_mm=86, height_mm=48)
panel(fig, left=.16, right=.96, bottom=.21, top=.95)
e2 = np.linspace(0, .5, 400); tot = .25*(1-e2) + .75*e2
IY = LN2 - float(hb(.25)); IZ = LN2 - hb(tot)
ax.axhline(IY, color=PURPLE, lw=.85, ls=DASH); ax.plot(e2, IZ, color=GREEN, lw=1.4)
dot(ax, .25, LN2-float(hb(.375)))
lab(ax, .3, IY+.004, r'$I(X;Y)=0.1308$', PURPLE); lab(ax, .04, .06, r'$I(X;Z)$', GREEN)
lab(ax, .26, LN2-float(hb(.375))+.006, r'$0.0316$', RED)
ax.set_xlim(0, .5); ax.set_ylim(0, .15); axlab(ax, r'$\varepsilon_2$', 'nat')
save(fig, HERE, 'figure', {'I(X;Y)': IY, 'I(X;Z) e2=1/4': LN2-float(hb(.375))})
