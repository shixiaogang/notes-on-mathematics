from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"kkt-common"))
from kkt_fig import *
HERE = Path(__file__).resolve().parent
# Budget example: optimal point path and multipliers as tau varies.
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .07, .985, .985, .25, .25)
a, b = axes
ts = np.linspace(.0, 3.6, 400); P = np.array([budget_x(t) for t in ts])
xl, yl = (-.2, 2.9), (-.2, 2.4)
for t, c_ in ((.5, MUTED), (1, MUTED), (2, MUTED), (3, MUTED)):
    a.plot([0, t], [t, 0], color=c_, lw=.75, zorder=1)
    a.text(t+.03, .06-.26 if 0 else -.14, '', fontsize=7.5)
a.plot([0, 0], [0, 2.4], color=MUTED, lw=.75); a.plot([0, 2.9], [0, 0], color=MUTED, lw=.75)
a.plot(P[:, 0], P[:, 1], color=GREEN, lw=1.7, zorder=3)
hollow(a, C, BLUE)
setup(a, xl, yl, range(0, 3), range(0, 3))
for t in (.5, 1, 2, 3):
    p = budget_x(t); dot(a, p, RED, ms=4.2)
a.text(.5, .1, '$0.5$', fontsize=7.5, ha='center'); a.text(1.02, .14, '$1$', fontsize=7.5, ha='center')
a.text(1.5, .62, '$2$', fontsize=7.5, ha='right'); a.text(2.12, 1.06, '$\\tau\\geq3$', fontsize=7.5)
tl = np.linspace(0, 4, 400); L = np.array([budget_lam(t) for t in tl])
b.plot(tl, L[:, 0], color=PURPLE, lw=1.5, label='$\\lambda_1$'); b.plot(tl, L[:, 1], color=PURPLE, lw=1.5, ls=(0, (4, 2)), label='$\\lambda_3$')
setup(b, (0, 4), (-.08, 2.2), range(0, 5), [0, 1, 2], xl='$\\tau$', yl='乘子', equal=False)
for t in (1, 3): b.axvline(t, color=MUTED, lw=.8, ls=(0, (2, 2)))
b.text(1.95, 1.0, '$\\lambda_1$', color=PURPLE, fontsize=8); b.text(.08, .62, '$\\lambda_3$', color=PURPLE, fontsize=8)
tags(fig, axes, y=.01)
save(fig, HERE, 'figure', {'x*': 'piecewise (tau,0); ((1+tau)/2,(tau-1)/2); (2,1)', 'lam': 'lam1=2-tau,(3-tau)/2,0; lam3=1-tau,0,0'})
