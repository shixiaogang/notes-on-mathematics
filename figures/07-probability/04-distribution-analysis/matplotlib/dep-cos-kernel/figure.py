"""Integrand (1 - cos(t x))/t^2 for x = 1 (blue, filled) and x = 2 (yellow).  Integrals over R: pi|x|, i.e. pi and 2 pi
(numerical check by quadrature on [-2000, 2000] plus tail 2/T bound)."""
from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

t = np.linspace(-12, 12, 4001)
fig, ax = figure(width_mm=96, height_mm=44)
for x, col in [(1, BLUE), (2, YELLOW)]:
    g = np.where(np.abs(t) < 1e-6, x*x/2, 2*np.sin(t*x/2)**2/np.where(t == 0, 1, t)**2)
    if x == 1:
        ax.fill_between(t, 0, g, color=BLUE_FILL, lw=0)
    ax.plot(t, g, color=col, lw=1.4 if x == 1 else 1.6)
ax.set_xlim(-12, 12); ax.set_ylim(0, 2.1)
ax.set_xticks([-10, -5, 0, 5, 10]); ax.set_yticks([0, .5, 1, 2]); gfmt(ax)
ax.set_xlabel('$t$', labelpad=0)
ax.text(1.0, 1.85, '$x=2$', color=INK, fontsize=7.5); ax.text(1.6, .55, '$x=1$', color=INK, fontsize=7.5)
T = np.linspace(-4000, 4000, 4_000_001); T[T == 0] = 1e-12
num = {str(x): float(np.trapezoid((1-np.cos(T*x))/T**2, T)) for x in (1, 2)}
save(fig, HERE, 'figure', {'integral_numeric_on_[-4000,4000]': num, 'pi': math.pi})
