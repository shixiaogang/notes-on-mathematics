from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# N = 8 mid-rise uniform quantizer for Laplace(0,1), range L = 4*delta, saturation outside.
# Exact granular MSE (yellow), exact overload MSE e^{-L}(delta^2/4+delta+2) (red), total (blue);
# purple dashed: granular approximation delta^2/12 * P(|X|<=L). Red dot: optimum (grid search).
ds = np.linspace(.3, 2.0, 400)
G = []; O = []
for d in ds:
    g, o = uniform_parts(8, d); G.append(g); O.append(o)
G = np.array(G); O = np.array(O); T = G+O
fig, ax = figure(width_mm=96, height_mm=52)
panel(fig, left=.11, right=.97, bottom=.17, top=.97)
ax.plot(ds, ds**2/12*(1-np.exp(-4*ds)), color=PURPLE, lw=1.1, ls=DASH)
ax.plot(ds, G, color=YELLOW, lw=1.6); ax.plot(ds, O, color=RED, lw=1.4); ax.plot(ds, T, color=BLUE, lw=1.4)
i = int(np.argmin(T)); dot(ax, ds[i], T[i])
lab(ax, .75, .3, '总误差', BLUE); lab(ax, .52, .22, '过载', RED); lab(ax, 1.62, .27, '舍入', YELLOW)
lab(ax, ds[i], T[i]+.025, '$\\Delta^*\\approx1.03$', RED, ha='center')
ax.set_xlim(.3, 2.0); ax.set_ylim(0, .5); ax.set_xlabel('$\\Delta$', labelpad=1); ax.set_ylabel('均方误差', labelpad=1)
save(fig, HERE, 'figure', {'opt_step': float(ds[i]), 'opt_total': float(T[i]),
     'at_1': [float(v) for v in uniform_parts(8, 1.0)], 'at_0.5': [float(v) for v in uniform_parts(8, .5)],
     'at_1.5': [float(v) for v in uniform_parts(8, 1.5)]})
