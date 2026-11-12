from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dapx-common'))
from common import *
# Mean-field objective D(q1 x q2 || pi) on the table pi=[[0.45,0.05],[0.05,0.45]], a=q1(1), b=q2(1).
# Minima at (1/4,1/4) and (3/4,3/4) (value 0.4978), saddle at (1/2,1/2) (value 0.5108).
# (a) contour lines and coordinate-update paths from b0=0.9 (green solid) and b0=0.2 (green dashed), a0=0.5.
# (b) objective after each half step: b0=0.9 (solid), b0=0.2 (dashed), b0=0.5 (stays at the saddle, grey).
A = np.linspace(.02, .98, 241)
Zs = np.array([[mf_obj(a, b) for a in A] for b in A])
fig, axs = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.08, right=.98, top=.96, bottom=.24, wspace=.3)
ax = axs[0]
ax.contour(A, A, Zs, levels=[.5, .52, .56, .62, .7, .8], colors=[BLUE], linewidths=.7, linestyles='solid')
paths = {}
for b0, ls in ((.9, '-'), (.2, DASH)):
    P = cavi_table(b0, 12); paths[b0] = P
    xs = [p[0] for p in P]; ys = [p[1] for p in P]
    ax.plot(xs, ys, color=GREEN, lw=1.1, ls=ls, marker='o', ms=2.2)
for p in ((.25, .25), (.75, .75)):
    dot(ax, *p, RED, ms=4.5)
dot(ax, .5, .5, STROKE, ms=3.5)
ax.set_aspect('equal'); ax.set_xlim(0, 1); ax.set_ylim(0, 1)
ax.set_xticks([0, .25, .5, .75, 1]); ax.set_yticks([0, .25, .5, .75, 1])
ax.set_xticklabels(['0', '', '0.5', '', '1']); ax.set_yticklabels(['0', '', '0.5', '', '1'])
axlab(ax, '$a=q_1(1)$', '$b=q_2(1)$')
ax = axs[1]
for b0, ls in ((.9, '-'), (.2, DASH)):
    P = paths[b0]; v = [mf_obj(a, b) for a, b in P]
    ax.plot(np.arange(len(v))/2, v, color=GREEN, lw=1.2, ls=ls, marker='o', ms=2)
ax.axhline(mf_obj(.5, .5), color=STROKE, lw=.85, ls=DOT)
ax.axhline(mf_obj(.75, .75), color=RED, lw=.85)
lab(ax, 3.2, .5135, '0.5108', INK, fontsize=7); lab(ax, 3.2, .4935, '0.4978', RED, fontsize=7)
ax.set_xlim(0, 6); ax.set_ylim(.49, .56)
axlab(ax, '轮次', None)
tags(fig, axs)
save(fig, HERE, 'figure', {'path_b0=0.9': [[round(a, 4), round(b, 4), round(mf_obj(a, b), 4)] for a, b in paths[.9][:9]],
                           'path_b0=0.2': [[round(a, 4), round(b, 4)] for a, b in paths[.2][:9]],
                           'min': mf_obj(.75, .75), 'saddle': mf_obj(.5, .5)})
