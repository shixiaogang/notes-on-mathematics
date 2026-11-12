from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Binary example (X ~ Bern(1/2), Y = X xor Bern(1/4)), N = 2 candidates, restricted score s(x,y) = c 1{x=y}.
# Exact value of ln 2 - L(c) (green); maximum at c = ln 3 (red) equals 0.0654 = optimal-score value;
# I(X;Y) = 0.1308 (purple dashed). Negative values: the score is a poor posterior model.
def L(c, N=2, e=.25):
    t = 0.0
    for mJ, pJ in ((1, 1-e), (0, e)):
        for k in range(N):
            pk = math.comb(N-1, k)*.5**(N-1); m = k+mJ; Z = m*math.exp(c)+(N-m)
            t += pJ*pk*(math.log(Z) - c*mJ)
    return t
fig, ax = figure(width_mm=86, height_mm=48)
panel(fig, left=.14, right=.96, bottom=.21, top=.95)
c = np.linspace(-1, 3.5, 500); v = np.array([LN2 - L(x) for x in c])
ax.plot(c, v, color=GREEN, lw=1.4); ax.axhline(LN2-float(hb(.25)), color=PURPLE, lw=.85, ls=DASH); ax.axhline(0, color=STROKE, lw=.6)
dot(ax, math.log(3), LN2-L(math.log(3)))
ax.plot([math.log(3)]*2, [-.1, LN2-L(math.log(3))], color=STROKE, lw=.6, ls=DOT)
lab(ax, -.9, .137, r'$I(X;Y)$', PURPLE); lab(ax, math.log(3)+.08, .072, r'$c=\ln 3$', RED)
ax.set_xlim(-1, 3.5); ax.set_ylim(-.1, .15); axlab(ax, '$c$', r'$\ln 2-L$ / nat')
save(fig, HERE, 'figure', {'max': LN2-L(math.log(3)), 'c0': LN2-L(0), 'c3': LN2-L(3)})
