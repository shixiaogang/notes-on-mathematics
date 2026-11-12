from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Density of the normalised squared noise length |Z^n|^2 / n for Z_i iid N(0,1): this is chi^2_n / n,
# i.e. Gamma(shape n/2, rate n/2). Curves for n = 4 (yellow), 32 (purple), 256 (blue); red line at sigma^2 = 1.
# Exact density, no simulation. Probability of |Z|^2/n in [0.8, 1.2] is reported in the facts.
fig, ax = figure(width_mm=84, height_mm=48)
panel(fig, left=.12, right=.97, top=.95, bottom=.2)
t = np.linspace(1e-4, 3, 3000); dt = t[1]-t[0]
def dens(n):
    a = n/2
    return np.exp(a*np.log(a) + (a-1)*np.log(t) - a*t - math.lgamma(a))
facts = {}
for n, col in ((4, YELLOW), (32, PURPLE), (256, BLUE)):
    f = dens(n); ax.plot(t, f, color=col, lw=1.5 if n == 4 else 1.4)
    m = (t >= .8) & (t <= 1.2); facts['P(0.8<=|Z|^2/n<=1.2), n=%d' % n] = float(f[m].sum()*dt)
ax.axvline(1, color=RED, lw=1.1)
ax.set_xlim(0, 3); ax.set_ylim(0, 5.0)
ax.set_xlabel(r'$\Vert Z^n\Vert_2^2/n$', labelpad=1); ax.set_ylabel('密度', labelpad=2)
lab(ax, .2, 1.0, r'$n=4$', YELLOW); lab(ax, 1.42, 1.0, r'$n=32$', PURPLE); lab(ax, 1.22, 3.0, r'$n=256$', BLUE)
lab(ax, 1.06, 4.6, r'$\sigma^2=1$', RED)
save(fig, HERE, 'figure', facts)
