from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

# Target: exact solutions through the Euler values (fan) and their telescoping contributions at T=1.
h, n = .25, 4
xs = integrate(euler_step, f, h, n); tg = h*np.arange(n+1)
fig, ax = figure(width_mm=112, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [1.25, 1]})
a = ax[0]
a.axhline(0, color=BLUE, lw=1.4)
for k in range(1, n):
    s = np.linspace(tg[k], 1, 80)
    a.plot(s, exact(s, tg[k], xs[k])-exact(s), color=YELLOW, lw=1.1)
a.plot(tg, xs-exact(tg), 'o-', color=GREEN, lw=1.2, ms=3.6, zorder=5)
a.set_xlabel(r'$t$'); a.set_ylabel(r'与真解之差')
a.set_xticks(tg); a.set_xticklabels([r'$t_0$', r'$t_1$', r'$t_2$', r'$t_3$', r'$t_4$'])
a.set_xlim(0, 1.04)
a.text(.02, .0009, '真解', color=BLUE)
b = ax[1]
parts = []
for k in range(n):
    p = float(exact(1.0, tg[k+1], xs[k+1])-exact(1.0, tg[k], xs[k]))
    parts.append(p)
    b.bar(k+.5, p, width=.7, color=RED_FILL, edgecolor=RED, lw=.85)
b.set_xticks(np.arange(n)+.5); b.set_xticklabels([rf'$k={k}$' for k in range(n)])
b.set_ylabel('对终点误差的贡献')
b.axhline(0, color=STROKE, lw=.75)
panel(a, '(a)', -.27); panel(b, '(b)', -.27)
total = float(xs[-1]-exact(1.0))
save(fig, Path(__file__).resolve().parent, 'figure', {'contributions': parts, 'sum': sum(parts), 'endpoint_error': total})
print(parts, sum(parts), total)
