"""Probability integral transform. (a) F(X), X~Exp(1); (b) F(X), X~Bern(1/2): values 1/2,1; (c) distributional transform U=F(X-)+V dF(X) for the coin. 4000 draws, seed 716."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dfam-common"))
from common import *

rng = np.random.default_rng(SEED)
n = 4000
X = rng.exponential(1.0, n)
Ue = 1-np.exp(-X)
B = (rng.random(n) < 0.5).astype(int)
FB = np.where(B == 0, 0.5, 1.0)
Fm = np.where(B == 0, 0.0, 0.5)
Vv = rng.random(n)
Ud = Fm+Vv*0.5
fig, (a, b, c) = figure(width_mm=112, height_mm=42, ncols=3)
bins = np.linspace(0, 1, 21)
a.hist(Ue, bins=bins, density=True, color=GREEN_FILL, edgecolor=GREEN, lw=0.5)
a.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
p0 = float(np.mean(B == 0))
b.plot([0.5, 0.5], [0, p0], color=RED, lw=2.0); b.plot([1, 1], [0, 1-p0], color=RED, lw=2.0)
b.scatter([0.5, 1], [p0, 1-p0], s=14, color=RED, zorder=4, clip_on=False)
c.hist([Ud[B == 0], Ud[B == 1]], bins=bins, density=True, stacked=True, color=[GREEN_FILL, YELLOW_FILL], edgecolor=STROKE, lw=0.4)
c.plot([0, 1], [1, 1], color=BLUE, lw=1.4)
for ax_ in (a, b, c):
    ax_.set_xlim(0, 1.04); ax_.set_xticks([0, 0.5, 1]); ax_.set_xlabel('$u$', labelpad=1)
a.set_ylim(0, 1.4); c.set_ylim(0, 1.4); b.set_ylim(0, 0.7)
b.set_ylabel('概率', labelpad=1); a.set_ylabel('密度', labelpad=1)
c.text(0.25, 1.1, '$X=0$', ha='center', fontsize=7.5); c.text(0.75, 1.1, '$X=1$', ha='center', fontsize=7.5)
tag(a, '(a)', y=-0.32); tag(b, '(b)', y=-0.32); tag(c, '(c)', y=-0.32)
save(fig, HERE, 'figure', {'seed': SEED, 'n': n, 'coin_p0_emp': p0, 'mean_Ue': float(Ue.mean()), 'mean_Ud': float(Ud.mean())})
