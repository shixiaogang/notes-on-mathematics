"""Construction of a conditional CDF from rational thresholds (triangle model).
(a) y=0.4: G_q(y)=clip((q-0.4)/0.6,0,1) at rationals q=a/b, b<=12, q in [-0.2,1.2]; inf-regularised CDF.
(b) an exceptional observation whose chosen values are not monotone (seed 11) -> replaced by delta_0."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
from fractions import Fraction
qs = sorted({Fraction(a, b) for b in range(1, 13) for a in range(-3*b, 3*b+1) if -0.2 <= a/b <= 1.2})
q = np.array([float(v) for v in qs])
fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
y0 = 0.4
G = np.clip((q - y0)/(1 - y0), 0, 1)
t = np.linspace(-0.2, 1.2, 600)
a.plot(t, np.clip((t - y0)/(1 - y0), 0, 1), color=BLUE, lw=1.4, zorder=2)
a.scatter(q, G, s=4, color=GREEN, zorder=3)
a.set_xlim(-0.2, 1.2); a.set_ylim(-0.05, 1.1); a.set_xticks([0, 0.4, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$F(t\\mid y)$')
rng = np.random.default_rng(11)
bad = np.clip(np.clip((q - 0.5)/0.5, 0, 1) + rng.normal(0, 0.18, q.size), 0, 1)
b.scatter(q, bad, s=4, color=RED, zorder=3)
b.plot([-0.2, 0], [0, 0], color=BLUE, lw=1.4); b.plot([0, 1.2], [1, 1], color=BLUE, lw=1.4)
b.scatter([0], [1], s=14, color=BLUE, zorder=4); b.scatter([0], [0], s=14, facecolor='white', edgecolor=BLUE, zorder=4, lw=0.9)
b.set_xlim(-0.2, 1.2); b.set_ylim(-0.05, 1.1); b.set_xticks([0, 0.5, 1]); b.set_yticks([0, 0.5, 1])
b.set_xlabel('$t$', labelpad=1)

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'y': y0, 'rationals': 'a/b, b<=12', 'n_rationals': int(q.size), 'bad_seed': 11})
