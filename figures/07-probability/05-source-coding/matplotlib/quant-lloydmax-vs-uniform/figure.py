from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# N = 8 quantizers for Laplace(0,1): Lloyd-Max fixed point (green points, gray thresholds, upper row)
# and the best mid-rise uniform quantizer (step chosen by grid search, yellow, lower row).
lm = lloyd(np.linspace(-3.5, 3.5, 8), 3000)[-1]
ds = np.linspace(.3, 2.5, 22001); tot = [sum(uniform_parts(8, d)) for d in ds]; du = ds[int(np.argmin(tot))]
cu = (np.arange(8)-3.5)*du; tu = (np.arange(1, 8)-4)*du
x = np.linspace(-6, 6, 1201)
fig, ax = figure(width_mm=104, height_mm=50)
panel(fig, left=.1, right=.97, bottom=.15, top=.97)
ax.plot(x, pdf(x), color=BLUE, lw=1.4)
y1, y2 = -.07, -.16
for t in lm[0]: ax.plot([t, t], [y1-.03, y1+.03], color=STROKE, lw=.85)
for t in tu: ax.plot([t, t], [y2-.03, y2+.03], color=STROKE, lw=.85)
ax.plot([-6, 6], [y1, y1], color=STROKE, lw=.6); ax.plot([-6, 6], [y2, y2], color=STROKE, lw=.6)
for c in lm[1]: dot(ax, c, y1, color=GREEN)
for c in cu: dot(ax, c, y2, color=YELLOW)
ax.axhline(0, color=STROKE, lw=.6)
lab(ax, -5.9, y1+.015, 'Lloyd–Max', GREEN); lab(ax, -5.9, y2+.015, '均匀', YELLOW)
lab(ax, 1.3, .36, '$f(x)$', BLUE)
ax.set_xlim(-6, 6); ax.set_ylim(-.21, .55); ax.set_yticks([0, .25, .5]); ax.set_xlabel('$x$', labelpad=1)
save(fig, HERE, 'figure', {'lm_t': [float(v) for v in lm[0]], 'lm_c': [float(v) for v in lm[1]], 'lm_D': float(lm[2]),
     'uniform_step': float(du), 'uniform_D': float(min(tot))})
