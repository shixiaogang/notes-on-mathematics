from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: frozen eigenvalues in the left half plane do not imply decay (Markus-Yamabe matrix).
def A(t):
    c, s = np.cos(t), np.sin(t)
    return np.array([[-1+1.5*c*c, 1-1.5*c*s], [-1-1.5*c*s, -1+1.5*s*s]])
g = lambda t, x: A(t)@x
h = 1e-3; n = int(6/h); x = np.array([1., 0.]); xs = [x.copy()]
for k in range(n):
    x = rk4_step(g, k*h, x, h); xs.append(x.copy())
xs = np.array(xs); t = h*np.arange(n+1)
ev = np.array([np.linalg.eigvals(A(s)).real.max() for s in np.linspace(0, 6, 61)])
fig, ax = figure(width_mm=86, height_mm=64)
ax.plot(xs[:, 0], xs[:, 1], color=BLUE, lw=1.4)
ax.plot([1], [0], 'o', color=RED, ms=4.8, zorder=5)
ax.set_aspect('equal'); ax.set_xlabel(r'$x_1$'); ax.set_ylabel(r'$x_2$')
ax.axhline(0, color=STROKE, lw=.7); ax.axvline(0, color=STROKE, lw=.7)
save(fig, Path(__file__).resolve().parent, 'figure', {'max_real_part_frozen': float(ev.max()), 'x_T_norm': float(np.linalg.norm(xs[-1])), 'expected': float(np.exp(3))})
print(ev.max(), np.linalg.norm(xs[-1]), np.exp(3))
