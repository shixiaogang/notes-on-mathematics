"""Triangle model: (X,Y) uniform on 0<=y<=x<=1 (density 2). For events {X<=a} compare
E[Y; X<=a] = a^3/3 (blue) with E[Z; X<=a] for candidates Z = X/2 (green dashed, equal: a^3/3),
Z = 1/3 (yellow: a^2/3) and Z = X/3 (purple: 2a^3/9). Values computed by numerical integration."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

a = np.linspace(0, 1, 201)
x = np.linspace(0, 1, 20001); dx = x[1]-x[0]
def cum(h):  # E[h(X); X<=a] with f_X(x)=2x
    g = h(x)*2*x
    c = np.r_[0, np.cumsum((g[1:]+g[:-1])/2*dx)]
    return np.interp(a, x, c)
target = cum(lambda t: t/2)          # E[Y|X=x]=x/2 inner integral: int_0^x y*2 dy = x^2 = (x/2)*2x
fig, ax = figure(width_mm=80, height_mm=50)
ax.plot(a, target, color=BLUE, lw=2.4)
ax.plot(a, cum(lambda t: t/2), color=GREEN, lw=1.2, ls='--')
ax.plot(a, cum(lambda t: np.full_like(t, 1/3)), color=YELLOW, lw=1.5)
ax.plot(a, cum(lambda t: t/3), color=PURPLE, lw=1.3)
ax.text(0.48, 0.20, r'$Z=1/3$', color=YELLOW, fontsize=7.5)
ax.annotate(r'$Z=X/3$', xy=(0.86, 2*0.86**3/9), xytext=(0.98, 0.05), color=PURPLE, fontsize=7.5, ha='right',
            arrowprops=dict(arrowstyle='-', color=PURPLE, lw=0.7))
ax.annotate(r'$Y,\ Z=X/2$', xy=(0.62, 0.62**3/3), xytext=(0.42, 0.16), color=BLUE, fontsize=7.5, ha='right',
            arrowprops=dict(arrowstyle='-', color=BLUE, lw=0.7))
ax.set_xlim(0, 1); ax.set_ylim(0, 0.36); ax.set_xlabel('$a$', labelpad=1)
ax.set_ylabel(r'$\mathrm{E}[\,\cdot\,;\,X\leq a]$')
save(fig, Path(__file__).resolve().parent, 'figure', {'target': 'a^3/3', 'const': 'a^2/3', 'X/3': '2a^3/9', 'at_a=1': [1/3, 1/3, 2/9]})
