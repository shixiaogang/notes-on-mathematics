from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Four-letter alphabet, theta = ||P-Q||_1 <= 1/2.
# Purple: proven bound theta ln(4/theta).
# Green: explicit pairs P = (1,0,0,0), Q = (1-theta/2, theta/6, theta/6, theta/6):
#        |H(P)-H(Q)| = h_b(theta/2) + (theta/2) ln 3 (computed directly from the two tables).
# Green dots: largest |dH| over 200000 random pairs per theta-bin (P ~ Dir(1,1,1,1), Q mixes P with
#        another Dir(1,1,1,1) draw, weight Unif(0,0.3); seed 1).
# Red: P = (1/2,1/4,1/8,1/8), Q = (0.45,0.3,0.125,0.125), theta = 0.1, |dH| = 0.0274.
rng = np.random.default_rng(1)
n = 200000
P = rng.dirichlet(np.ones(4), n)
D = rng.dirichlet(np.ones(4), n); t = rng.uniform(0, .3, n)[:, None]
Q = (1-t)*P + t*D
def Hm(A):
    A = np.clip(A, 1e-300, 1); return -(A*np.log(A)).sum(1)
th = np.abs(P-Q).sum(1); dH = np.abs(Hm(P)-Hm(Q))
bins = np.linspace(0, .5, 26); mx = []
for lo, hi in zip(bins[:-1], bins[1:]):
    m = (th >= lo) & (th < hi); mx.append(dH[m].max() if m.any() else np.nan)
fig, ax = figure(width_mm=86, height_mm=48)
panel(fig, left=.13, right=.96, bottom=.21, top=.95)
x = np.linspace(1e-4, .5, 400)
ax.plot(x, x*np.log(4/x), color=PURPLE, lw=1.3)
fam = [H([1-v/2, v/6, v/6, v/6]) for v in x]
ax.plot(x, fam, color=GREEN, lw=1.3)
ax.plot((bins[:-1]+bins[1:])/2, mx, 'o', color=GREEN, ms=2.4, mew=0)
p0 = np.array([.5, .25, .125, .125]); q0 = np.array([.45, .3, .125, .125])
t0 = np.abs(p0-q0).sum(); d0 = abs(H(p0)-H(q0)); dot(ax, t0, d0)
lab(ax, .3, .85, r'$\theta\ln(4/\theta)$', PURPLE); ax.annotate('点质量对', xy=(.12, float(H([.94, .02, .02, .02]))), xytext=(.03, .62), color=GREEN, fontsize=7.5, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.6)); lab(ax, .3, .22, '随机对的最大差', GREEN)
ax.set_xlim(0, .5); ax.set_ylim(0, 1.05); axlab(ax, r'$\theta=\|P-Q\|_1$', 'nat')
save(fig, HERE, 'figure', {'example_theta': t0, 'example_dH': d0, 'example_bound': t0*math.log(4/t0),
     'family_at_0.5': H([.75, 1/12, 1/12, 1/12]), 'bound_at_0.5': .5*math.log(8)})
