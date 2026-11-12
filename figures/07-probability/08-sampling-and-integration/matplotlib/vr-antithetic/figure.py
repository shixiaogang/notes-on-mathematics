from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Antithetic pairs (u, 1-u) for u = 0.37 and 0.81.
# (a) F(u) = e^u (increasing): the two values of a pair lie on opposite sides of I = e - 1; pair means marked.
# (b) F(u) = (u - 1/2)^2 (symmetric about 1/2): F(u) = F(1-u), so the pair repeats one value; I = 1/12.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.26)
u = np.linspace(0, 1, 300)
info = {}
for ax, F, I, name in ((axs[0], np.exp, E-1, 'exp'), (axs[1], lambda t: (t-.5)**2, 1/12, 'sq')):
    ax.plot(u, F(u), color=BLUE, lw=1.4)
    ax.axhline(I, color=PURPLE, lw=.85, ls=DASH)
    for k, v in enumerate((.37, .81)):
        col = GREEN if k == 0 else YELLOW
        y1, y2 = float(F(np.array(v))), float(F(np.array(1-v)))
        ax.plot([v, 1-v], [y1, y2], color=col, lw=.9, ls=DOT)
        dot(ax, v, y1, color=col, ms=3.8); dot(ax, 1-v, y2, color=col, ms=3.8)
        ax.plot([.5], [(y1+y2)/2], 'o', ms=4.4, mfc='white', mec=col, mew=1.1, zorder=7)
        info[f'{name}_pair_{v}'] = [y1, y2, (y1+y2)/2]
    ax.set_xlim(0, 1); ax.set_xticks([0, .5, 1]); axlab(ax, '$u$')
axs[0].set_ylim(.9, 2.8); axs[0].set_yticks([1, 1.5, 2, 2.5])
axs[1].set_ylim(0, .27); axs[1].set_yticks([0, .1, .2])
lab(axs[0], .05, 1.82, r'$I$', PURPLE); lab(axs[1], .03, 1/12+.012, r'$I$', PURPLE)
tags(fig, axs)
s2 = (E*E-1)/2-(E-1)**2; g = E-(E-1)**2
info.update({'var_exp': s2, 'cov_exp_anti': g, 'pair_var_exp': (s2+g)/2, 'var_sq': 1/80-1/144})
save(fig, HERE, 'figure', info)
