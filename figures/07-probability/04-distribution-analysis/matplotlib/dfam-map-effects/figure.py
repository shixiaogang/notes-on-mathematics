"""Maps change support/type. (a) Z~Unif(0,1) -> r(cos 2piZ, sin 2piZ), r=1, 0.6, 400 pts each (seed 716).
(b) round(mu+Z), Z~N(0,1), mu=0.3: P(X=k)=Phi(k+1/2-mu)-Phi(k-1/2-mu). (c) max(mu+Z,0), mu=0.5: atom Phi(-mu) at 0."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dfam-common'))
from common import *

rng = np.random.default_rng(SEED)
fig, (a, b, c) = figure(width_mm=112, height_mm=46, ncols=3)
for r in (1.0, 0.6):
    zz = rng.random(400)
    a.scatter(r*np.cos(2*np.pi*zz), r*np.sin(2*np.pi*zz), s=1.2, color=GREEN, linewidths=0)
a.text(0, 0, r'$r=0.6$', ha='center', va='center', fontsize=7.5)
a.text(0.78, 0.92, r'$r=1$', fontsize=7.5)
a.set_box_aspect(1); b.set_box_aspect(1); c.set_box_aspect(1); a.set_xlim(-1.15, 1.15); a.set_ylim(-1.15, 1.15)
a.set_xticks([-1, 0, 1]); a.set_yticks([-1, 0, 1])
a.set_xlabel('$x_1$', labelpad=0); a.set_ylabel('$x_2$', labelpad=1)
mu = 0.3
k = np.arange(-3, 4)
pk = Phi(k+0.5-mu)-Phi(k-0.5-mu)
b.bar(k, pk, width=0.8, color=BLUE_FILL, edgecolor=BLUE, lw=0.8)
xx = np.linspace(-3.6, 3.6, 500)
b.plot(xx, phi(xx-mu), color=BLUE, lw=1.4)
for e in np.arange(-3.5, 4.0, 1.0):
    b.axvline(e, color=STROKE, lw=0.6, ls=':', zorder=0)
b.set_xlim(-3.6, 3.6); b.set_ylim(0, 0.42); b.set_xticks([-2, 0, 2]); b.set_xlabel('$k$', labelpad=1)
mu2 = 0.5
atom = float(Phi(-mu2))
x2 = np.linspace(0.0, 3.6, 400)
c.plot(x2, phi(x2-mu2), color=BLUE, lw=1.4)
c.plot([0, 0], [0, atom], color=RED, lw=2.0)
c.scatter([0], [atom], s=14, color=RED, zorder=4, clip_on=False)
c.text(0.14, 0.2, f'${atom:.3f}$', fontsize=7.5, color=RED, va='bottom')
c.set_xlim(-0.4, 3.6); c.set_ylim(0, 0.45); c.set_xlabel('$x$', labelpad=1)
tag(a, '(a)', y=-0.30); tag(b, '(b)', y=-0.30); tag(c, '(c)', y=-0.30)
save(fig, HERE, 'figure', {'seed': SEED, 'round_mu': mu, 'pk': {int(i): float(v) for i, v in zip(k, pk)}, 'clip_mu': mu2, 'atom': atom})
