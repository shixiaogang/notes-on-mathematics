from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Mid-rise uniform quantizer, N = 8 levels, range [-L, L] = [-4, 4], step 1, saturation outside.
# Test inputs x = 1.3, -0.2, 5.7 (red) with their outputs 1.5, -0.5, 3.5.
N, d = 8, 1.0; L = N*d/2
x = np.linspace(-6.2, 6.2, 4001)
q = uniform_q(x, N, d)
fig, ax = figure(width_mm=92, height_mm=58)
panel(fig, left=.14, right=.97, bottom=.14, top=.97)
ax.plot(x, x, color=STROKE, lw=.85, ls=DOT)
# draw steps as separate horizontal segments
for i in range(N):
    a0 = -L + i*d if i > 0 else -6.2; b0 = -L + (i+1)*d if i < N-1 else 6.2
    ax.plot([a0, b0], [(i-N/2+.5)*d]*2, color=GREEN, lw=1.4, solid_capstyle='butt')
for t in (-L, L): ax.axvline(t, color=STROKE, lw=.85, ls=DASH)
ax.axhline(0, color=STROKE, lw=.6); ax.axvline(0, color=STROKE, lw=.6)
for xi in (1.3, -0.2, 5.7):
    qi = float(uniform_q(np.array([xi]), N, d)[0])
    ax.plot([xi, xi], [xi, qi], color=RED, lw=1.0)
    dot(ax, xi, qi)
lab(ax, 1.42, .85, '$x=1.3$', RED); lab(ax, -3.3, -0.9, '$x=-0.2$', RED)
lab(ax, 6.0, 2.5, '$x=5.7$', RED, ha='right')
lab(ax, -L+.1, -5.6, '$-L$', MUTED); lab(ax, L+.1, -5.6, '$L$', MUTED)
lab(ax, -3.0, -5.1, '$y=x$', MUTED)
ax.set_xlim(-6.2, 6.2); ax.set_ylim(-6, 6)
ax.set_xticks(range(-6, 7, 2)); ax.set_yticks([-3.5, -1.5, 0, 1.5, 3.5])
ax.set_xlabel('$x$', labelpad=1); ax.set_ylabel('$Q(x)$', labelpad=1)
save(fig, HERE, 'figure', {'N': N, 'step': d, 'outputs': [float(uniform_q(np.array([v]), N, d)[0]) for v in (1.3, -0.2, 5.7)]})
