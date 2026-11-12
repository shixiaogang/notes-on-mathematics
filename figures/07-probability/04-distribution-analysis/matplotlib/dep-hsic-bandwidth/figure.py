"""HSIC with Gaussian kernels of common bandwidth s on both coordinates, as a function of s (log scale):
standard bivariate Gaussian rho = 0.5 (blue, closed form), continuous parabola X ~ Unif(-1,1), Y = X^2 (yellow, quadrature 1000 nodes).
Red dots at s = 1: 0.0108 and 0.0026; the two curves cross between s = 0.5 and s = 1."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

S = np.logspace(math.log10(.04), math.log10(6), 50)
g = np.array([gauss_hsic(.5, s) for s in S])
p = np.array([parabola_hsic(0, s, s, 1000) for s in S])
fig, ax = figure(width_mm=92, height_mm=48)
ax.plot(S, g, color=BLUE, lw=1.4)
ax.plot(S, p, color=YELLOW, lw=1.6)
ax.plot([1, 1], [gauss_hsic(.5, 1), parabola_hsic(0, 1, 1, 1000)], 'o', color=RED, ms=3, ls='none')
ax.set_xscale('log'); ax.set_xlim(S[0], S[-1]); ax.set_ylim(0, .075)
ax.set_xticks([.05, .1, .5, 1, 5]); ax.set_xticklabels(['0.05', '0.1', '0.5', '1', '5'])
ax.set_xlabel('$s$', labelpad=0)
ax.text(.13, .066, '抛物线', fontsize=7.5); ax.text(1.6, .012, '高斯', fontsize=7.5)
d = g-p; i = int(np.flatnonzero(np.diff(np.sign(d)))[0])
save(fig, HERE, 'figure', {'s_cross_between': [float(S[i]), float(S[i+1])], 'gauss_s1': float(gauss_hsic(.5, 1)), 'parab_s1': parabola_hsic(0, 1, 1, 1000),
     'gauss_max': [float(S[g.argmax()]), float(g.max())], 'parab_max': [float(S[p.argmax()]), float(p.max())]})
