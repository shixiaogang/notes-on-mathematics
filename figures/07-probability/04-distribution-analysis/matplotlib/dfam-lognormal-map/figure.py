"""Invertible nonlinear pushforward: Z~N(0,1), x=exp(z).
(a) the map with the six equal-probability cut points z_k=Phi^{-1}(k/6) and their images exp(z_k);
(b) log-normal densities mu=0, sigma in {0.25,0.5,1}; skewness (e^{s^2}+2)sqrt(e^{s^2}-1)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dfam-common'))
from common import *

fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
z = np.linspace(-2.4, 1.45, 400)
a.plot(z, np.exp(z), color=BLUE, lw=1.4)
zk = Phi_inv(np.arange(1, 6)/6)
for v in zk:
    a.plot([v, v], [0, np.exp(v)], color=STROKE, lw=0.85)
    a.plot([-2.4, v], [np.exp(v), np.exp(v)], color=STROKE, lw=0.6, ls=':')
a.scatter(np.full(5, -2.4), np.exp(zk), s=14, color=RED, zorder=4, clip_on=False)
a.set_xlim(-2.4, 1.45); a.set_ylim(0, 4.2)
a.set_xlabel('$z$', labelpad=1); a.set_ylabel(r'$x=\mathrm{e}^{z}$')
x = np.linspace(0.001, 4, 1500)
sk = {}
for s, c, lab, pos in [(0.25, BLUE, r'$\sigma=0.25$', (1.25, 1.45)), (0.5, YELLOW, r'$\sigma=0.5$', (1.7, 0.62)), (1.0, PURPLE, r'$\sigma=1$', (2.4, 0.24))]:
    f = phi(np.log(x)/s)/(s*x)
    b.plot(x, f, color=c, lw=1.4)
    b.text(*pos, lab, color=c, fontsize=7.5)
    sk[s] = float((np.exp(s*s)+2)*np.sqrt(np.exp(s*s)-1))
b.set_xlim(0, 4); b.set_ylim(0, 1.75); b.set_xlabel('$x$', labelpad=1); b.set_ylabel('$f_X(x)$')
tag(a, '(a)', y=-0.26); tag(b, '(b)', y=-0.26)
save(fig, HERE, 'figure', {'cut_points_z': [float(v) for v in zk], 'images': [float(np.exp(v)) for v in zk], 'skewness': sk})
