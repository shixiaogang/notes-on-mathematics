"""Three densities with mean 0 and variance 1: Gaussian (blue, h=2.047 bit),
Laplace b=1/sqrt2 (yellow, h=log2(2eb)=1.943 bit), uniform on [-sqrt3,sqrt3] (purple, h=log2(2sqrt3)=1.792 bit).
Entropies also checked by numerical integration."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

x = np.linspace(-4, 4, 4001)
g = npdf(x)
b = 1/math.sqrt(2); lap = np.exp(-np.abs(x)/b)/(2*b)
a = math.sqrt(3); uni = np.where(np.abs(x) <= a, 1/(2*a), 0.)


def ent(f):
    m = f > 0
    return float(-np.trapezoid(np.where(m, f*np.log2(np.where(m, f, 1)), 0), x))


hs = {'gauss': ent(g), 'laplace': ent(lap), 'uniform': ent(uni)}
fig, ax = figure(width_mm=86, height_mm=48)
ax.plot(x, g, color=BLUE, lw=1.4, zorder=3)
ax.plot(x, lap, color=YELLOW, lw=1.5, zorder=2)
ax.plot(x, uni, color=PURPLE, lw=1.2, zorder=2)
lab(ax, 1.15, .33, '高斯', BLUE, ha='left')
lab(ax, .45, .64, 'Laplace', YELLOW, ha='left')
lab(ax, -1.95, .31, '均匀', PURPLE, ha='right')
ax.set_xlim(-4, 4); ax.set_ylim(0, .74)
axlab(ax, '$x$', '密度')
save(fig, HERE, 'figure', {'h_bits_numeric': hs, 'h_gauss_exact': .5*math.log2(2*math.pi*math.e),
                          'h_laplace_exact': math.log2(2*math.e*b), 'h_uniform_exact': math.log2(2*a)})
