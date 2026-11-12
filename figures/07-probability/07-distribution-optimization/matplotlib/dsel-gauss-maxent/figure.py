"""Three densities on R with mean 0 and variance 1 (Lebesgue reference):
N(0,1) (blue, h=0.5 ln(2 pi e)=1.4189), Laplace(0, 1/sqrt2) (yellow, h=1+ln sqrt2=1.3466),
Unif(-sqrt3, sqrt3) (purple, h=ln(2 sqrt3)=1.2425).  Differential entropies in nats."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dsel-common"))
from common import *

x = np.linspace(-4, 4, 1601)
g = np.exp(-x**2/2)/math.sqrt(2*math.pi)
b = 1/math.sqrt(2); lap = np.exp(-np.abs(x)/b)/(2*b)
r3 = math.sqrt(3)
fig, ax = figure(width_mm=84, height_mm=46)
ax.plot(x, g, color=BLUE, lw=1.4)
ax.plot(x, lap, color=YELLOW, lw=1.5)
ax.plot([-4, -r3, -r3, r3, r3, 4], [0, 0, 1/(2*r3), 1/(2*r3), 0, 0], color=PURPLE, lw=1.3)
ax.text(0.55, 0.62, 'Laplace', color=YELLOW, fontsize=7.5, ha='left')
ax.text(1.05, 0.33, r'$\mathcal{N}(0,1)$', color=BLUE, fontsize=7.5, ha='left')
ax.text(-1.7, 0.30, '均匀', color=PURPLE, fontsize=7.5, ha='left', va='bottom')
ax.set_xlim(-4, 4); ax.set_ylim(0, 0.75)
ax.set_xlabel(r'$x$', labelpad=1)
# numerical check of entropies
def h(d):
    m = d > 0; return float(-np.trapezoid(np.where(m, d*np.log(np.where(m, d, 1)), 0), x))
xx = np.linspace(-40, 40, 400001)
gg = np.exp(-xx**2/2)/math.sqrt(2*math.pi); ll = np.exp(-np.abs(xx)/b)/(2*b)
hn = float(-np.trapezoid(gg*np.log(gg+1e-300), xx)); hl = float(-np.trapezoid(ll*np.log(ll+1e-300), xx))
save(fig, HERE, 'figure', {'h_gauss': 0.5*math.log(2*math.pi*math.e), 'h_gauss_numeric': hn,
     'h_laplace': 1+math.log(2*b), 'h_laplace_numeric': hl, 'h_uniform': math.log(2*r3)})
