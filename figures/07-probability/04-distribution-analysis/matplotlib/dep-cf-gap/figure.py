"""Three-point parabola: X uniform on {-1,0,1}, Y = X^2.  Delta(t,s) = phi_XY - phi_X phi_Y = 2(1-cos t)(1-e^{is})/9, so
(a) |Delta|^2 = 8 (1-cos t)^2 (1-cos s)/81 (white-to-blue); (b) weighted integrand |Delta|^2/(pi^2 t^2 s^2).
Numerical double integral of (b) over R^2 is checked against dCov^2 = 8/81."""
from pathlib import Path
import sys, math
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dep-common"))
from common import *

cmap = LinearSegmentedColormap.from_list('wb', ['#FFFFFF', BLUE_FILL, BLUE])
t = np.linspace(-8, 8, 481); s = np.linspace(-8, 8, 481)
T, S = np.meshgrid(t, s)
D2 = 8*(1-np.cos(T))**2*(1-np.cos(S))/81
with np.errstate(divide='ignore', invalid='ignore'):
    Wt = np.where(np.abs(T) < 1e-9, 0.0, (1-np.cos(T))**2/T**2)
    Ws = np.where(np.abs(S) < 1e-9, 0.5, (1-np.cos(S))/S**2)
G = 8*Wt*Ws/(81*math.pi**2)
fig, axs = figure(width_mm=108, height_mm=50, ncols=2)
for ax, Z, lab, vmax in [(axs[0], D2, '(a)', D2.max()), (axs[1], G, '(b)', G.max())]:
    ax.pcolormesh(t, s, Z, cmap=cmap, shading='auto', vmin=0, vmax=vmax, rasterized=True)
    ax.axhline(0, color=STROKE, lw=.6); ax.axvline(0, color=STROKE, lw=.6)
    ax.set_xticks([-2*np.pi, 0, 2*np.pi]); ax.set_xticklabels(['$-2\\pi$', '0', '$2\\pi$'])
    ax.set_yticks([-2*np.pi, 0, 2*np.pi]); ax.set_yticklabels(['$-2\\pi$', '0', '$2\\pi$'])
    ax.set_xlabel('$t$', labelpad=0); ax.set_ylabel('$s$', labelpad=0)
    ax.set_box_aspect(1)
    tag(ax, lab, y=-.26)
# numerical check: 1-D factors
u = np.linspace(-3000, 3000, 6_000_001); u[u == 0] = 1e-12
I1 = float(np.trapezoid((1-np.cos(u))**2/u**2, u)); I2 = float(np.trapezoid((1-np.cos(u))/u**2, u))
save(fig, HERE, 'figure', {'int_(1-cos)^2/t^2': I1, 'int_(1-cos)/s^2': I2, 'dCov2_numeric': 8*I1*I2/(81*math.pi**2), 'dCov2_exact': 8/81})
