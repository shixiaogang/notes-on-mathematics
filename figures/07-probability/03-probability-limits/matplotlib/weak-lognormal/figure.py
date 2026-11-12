from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"weak-common"))
from weak_fig import *
# Lognormal Y=e^Z, density f(y)=varphi(ln y)/y; f_a = f(1+a sin(2 pi ln y)), a=1/2. Same moments e^{k^2/2}.
a = .5
f = lambda y: npdf(np.log(y))/y
z = np.linspace(-12, 16, 400001)
mom = {k: [float(np.trapezoid(np.exp(k*z)*npdf(z), z)), float(np.trapezoid(np.exp(k*z)*npdf(z)*(1+a*np.sin(2*np.pi*z)), z)), float(np.exp(k*k/2))] for k in range(5)}
for k, (m0, m1, ex) in mom.items(): assert abs(m0-ex) < 1e-6*ex and abs(m1-ex) < 1e-6*ex, (k, m0, m1, ex)
fig, ax = figure(width_mm=100, height_mm=46)
fig.set_layout_engine(None); fig.subplots_adjust(left=.1, right=.97, top=.96, bottom=.2)
y = np.linspace(1e-4, 4, 2000)
ax.plot(y, f(y), color=BLUE, lw=1.4); ax.plot(y, f(y)*(1+a*np.sin(2*np.pi*np.log(y))), color=YELLOW, lw=1.6)
lab(ax, 1.55, .38, r'$f$', BLUE); lab(ax, .62, .92, r'$f_{1/2}$', YELLOW)
ax.set_xlim(0, 4); ax.set_ylim(0, 1.0); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, .5, 1])
axlab(ax, r'$y$')
save(fig, HERE, 'figure', {'moments_k_f_fa_exact': mom})
