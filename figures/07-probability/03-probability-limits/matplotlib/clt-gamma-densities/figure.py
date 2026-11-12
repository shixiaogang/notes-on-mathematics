from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'clt-common'))
from clt_fig import *
# X_i ~ Exp(1) i.i.d.; S_n ~ Gamma(n,1) exactly. Density of Z_n=(S_n-n)/sqrt(n)
# is sqrt(n) * gamma_pdf(n, n+z sqrt(n)); n = 1, 4, 16 against phi.
NS = (1, 4, 16); COLS = (YELLOW, PURPLE, GREEN)
z = np.linspace(-3.5, 4, 1501)
fig, ax = figure(width_mm=96, height_mm=54)
facts = {}
for i, n in enumerate(NS):
    f = math.sqrt(n)*gamma_pdf(n, n+z*math.sqrt(n))
    ax.plot(z, f, color=COLS[i], lw=1.3)
    facts[str(n)] = {'mode_z': float(z[np.argmax(f)]), 'skewness': 2/math.sqrt(n)}
ax.plot(z, phi(z), color=BLUE, lw=1.5)
lab(ax, -.8, .9, '$n=1$', YELLOW, ha='left')
lab(ax, -.75, .46, '$n=4$', PURPLE, ha='right')
lab(ax, .62, .375, '$n=16$', GREEN, ha='left')
lab(ax, -1.62, .19, r'$\varphi$', BLUE, ha='right')
ax.set_xlim(-3.5, 4); ax.set_ylim(0, 1.02); ax.set_xticks([-3, -2, -1, 0, 1, 2, 3, 4])
axlab(ax, '$z$', '密度')
save(fig, HERE, 'figure', facts)
