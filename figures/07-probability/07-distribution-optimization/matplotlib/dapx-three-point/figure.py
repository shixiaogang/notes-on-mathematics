from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Target PI3=(0.6,0.3,0.1), candidates Q_t=(t,1-2t,t).
# (a) D(Q_t||Pi) (yellow), minimiser t=(4-sqrt6)/5=0.3101, value 0.2359;
#     D(Pi||Q_t) (purple), minimiser t=0.35, value 0.1981.
# (b) probabilities of Pi (blue), Q_0.3101 (yellow), Q_0.35 (purple) on states 1,2,3.
t = np.linspace(.06, .47, 600)
f = np.array([kl(Q3(s), PI3) for s in t]); g = np.array([kl(PI3, Q3(s)) for s in t])
tr = (4-math.sqrt(6))/5; tf = .35
fig, axs = figure(width_mm=112, height_mm=48, ncols=2)
panel(fig, left=.08, right=.98, top=.95, bottom=.27, wspace=.28)
ax = axs[0]
ax.plot(t, f, color=YELLOW, lw=1.6); ax.plot(t, g, color=PURPLE, lw=1.4)
dot(ax, tr, kl(Q3(tr), PI3), RED, ms=4); dot(ax, tf, kl(PI3, Q3(tf)), RED, ms=4)
for v in (tr, tf):
    ax.plot([v, v], [0, .2], color=STROKE, lw=.85, ls=DOT)
lab(ax, tr-.012, .03, '0.310', INK, ha='right', fontsize=7); lab(ax, tf+.012, .03, '0.35', INK, ha='left', fontsize=7)
lab(ax, .3, .6, r'$D_{\mathrm{KL}}(Q_t\Vert\Pi)$', YELLOW); lab(ax, .13, 1.05, r'$D_{\mathrm{KL}}(\Pi\Vert Q_t)$', PURPLE)
ax.set_xlim(.06, .47); ax.set_ylim(0, 1.25); axlab(ax, '$t$', None)
ax = axs[1]
xs = np.array([1, 2, 3])
bars(ax, xs, PI3, BLUE, BLUE_FILL, width=.24, offset=-.26)
bars(ax, xs, Q3(tr), YELLOW, YELLOW_FILL, width=.24, offset=0)
bars(ax, xs, Q3(tf), PURPLE, PURPLE_FILL, width=.24, offset=.26)
ax.set_xticks(xs); ax.set_xlim(.5, 3.5); ax.set_ylim(0, .68)
lab(ax, .62, .62, r'$\Pi$', BLUE); lab(ax, 1.5, .55, r'$t=0.310$', YELLOW, fontsize=7); lab(ax, 2.35, .47, r'$t=0.35$', PURPLE, fontsize=7)
axlab(ax, '状态', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'t_rev': tr, 'Q_rev': Q3(tr).tolist(), 'D(Qrev||Pi)': kl(Q3(tr), PI3), 'D(Pi||Qrev)': kl(PI3, Q3(tr)),
                           't_fwd': tf, 'D(Pi||Qfwd)': kl(PI3, Q3(tf)), 'D(Qfwd||Pi)': kl(Q3(tf), PI3)})
