from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# (a) term-wise contributions p_i ln(p_i/q_i) (blue) and q_i ln(q_i/p_i) (yellow)
#     for the running example; sums 0.4 ln2 = 0.2773 and 0.5 ln2 = 0.3466.
# (b) Gaussian scale family: D(N(0,1)||N(0,s^2)) = ln s + 1/(2 s^2) - 1/2 (blue),
#     D(N(0,s^2)||N(0,1)) = -ln s + s^2/2 - 1/2 (yellow), s in [0.3, 3].
p, q, x = P_EX, Q_EX, X_EX
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.11, right=.98, top=.95, bottom=.26, wspace=.3)
ax = axs[0]
tp = p*np.log(p/q); tq = q*np.log(q/p)
bars(ax, x, tp, BLUE, BLUE_FILL, width=.34, offset=-.18)
bars(ax, x, tq, YELLOW, YELLOW_FILL, width=.34, offset=.18)
ax.axhline(0, color=STROKE, lw=.85)
for xi, a, b in zip(x, tp, tq):
    for off, v, c in ((-.18, a, BLUE), (.18, b, YELLOW)):
        if abs(v) > 1e-12:
            lab(ax, xi+off, v+(.025 if v > 0 else -.065), f'{v:.3f}', c, ha='center', fontsize=6.5)
ax.set_xticks(x); ax.set_xlim(-.6, 2.6); ax.set_ylim(-.28, .65); ax.set_yticks([-.2, 0, .2, .4, .6])
axlab(ax, '$x$', '各项贡献')
ax = axs[1]
s = np.linspace(.3, 3, 600)
f1 = np.log(s)+1/(2*s*s)-.5
f2 = -np.log(s)+s*s/2-.5
ax.plot(s, f1, color=BLUE, lw=1.4)
ax.plot(s, f2, color=YELLOW, lw=1.6)
dot(ax, 1, 0, RED, ms=4)
lab(ax, .62, 2.35, r'$D_{\mathrm{KL}}(P\Vert Q_s)$', BLUE, ha='left')
lab(ax, 2.05, 2.35, r'$D_{\mathrm{KL}}(Q_s\Vert P)$', YELLOW, ha='center')
ax.set_xlim(.3, 3); ax.set_ylim(0, 3.2); ax.set_xticks([.5, 1, 2, 3])
axlab(ax, '$s$', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'KLpq': float(tp.sum()), 'KLqp': float(tq.sum()),
                            'gauss_s=0.5': [float(np.log(.5)+2-.5), float(-np.log(.5)+.125-.5)]})
