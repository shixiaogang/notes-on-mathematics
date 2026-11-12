from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Lloyd-Max for Laplace(0,1), N = 4, start c = (-1.5,-0.5,0.5,1.5).
# (a) positive threshold t (gray) and positive points (green) per round; dotted lines = fixed point.
# (b) distortion D per round, round 0 = starting quantizer; dotted line = fixed-point value 0.3524.
R = 20
hist = lloyd([-1.5, -.5, .5, 1.5], R)
star = lloyd([-1.5, -.5, .5, 1.5], 400)[-1]
r = np.arange(0, R+1)
tt = [1.0] + [h[0][2] for h in hist]
ci = [.5] + [h[1][2] for h in hist]; co = [1.5] + [h[1][3] for h in hist]
D = [mse([-1, 0, 1], [-1.5, -.5, .5, 1.5])] + [h[2] for h in hist]
fig, (a, b) = figure(width_mm=108, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.3)
a.plot(r, co, 'o-', color=GREEN, lw=1.1, ms=2.6); a.plot(r, ci, 'o-', color=GREEN, lw=1.1, ms=2.6)
a.plot(r, tt, 's-', color=STROKE, lw=.85, ms=2.4)
for v in (star[0][2], star[1][2], star[1][3]): a.axhline(v, color=MUTED, lw=.6, ls=DOT)
lab(a, 14.5, star[1][3]+.13, '$c_4$', GREEN); lab(a, 14.5, star[0][2]+.13, '$t_3$', STROKE); lab(a, 14.5, star[1][2]+.13, '$c_3$', GREEN)
a.set_xlim(-.5, R+.5); a.set_ylim(0, 2.9); a.set_xlabel('轮次', labelpad=1)
b.plot(r, D, 'o-', color=GREEN, lw=1.1, ms=2.6)
b.axhline(star[2], color=MUTED, lw=.6, ls=DOT)
lab(b, 10, star[2]+.012, '$0.3524$', MUTED)
b.set_xlim(-.5, R+.5); b.set_ylim(.33, .53); b.set_xlabel('轮次', labelpad=1); b.set_ylabel('$D$', labelpad=1)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'rounds': [[float(x) for x in (tt[i], ci[i], co[i], D[i])] for i in range(9)],
     'fixed': [float(star[0][2]), float(star[1][2]), float(star[1][3]), float(star[2])]})
