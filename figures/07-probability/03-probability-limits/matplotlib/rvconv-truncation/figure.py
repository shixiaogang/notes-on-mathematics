from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rvconv-common'))
from rvconv_fig import *
# Truncation phi_M(x) = max(-M, min(x, M)) with M = 2 (blue), identity (dashed grey), and the residual
# |x - phi_M(x)| = (|x| - M)^+ <= |x| 1{|x| > M}: the residual is nonzero only beyond the red thresholds +-M.
Mt = 2.0
fig, ax = figure(width_mm=66, height_mm=44)
fig.set_layout_engine(None); fig.subplots_adjust(left=.04, right=.96, top=.97, bottom=.04)
style(ax)
x = np.linspace(-4.2, 4.2, 801)
phi = np.clip(x, -Mt, Mt)
ax.plot(x, x, color=LINE, lw=.85, ls=DASH)
for s in (1, -1):
    xs = x[s*x >= Mt]
    ax.fill_between(xs, np.clip(xs, -Mt, Mt), xs, color=RED_FILL, lw=0)
ax.plot(x, phi, color=BLUE, lw=1.4)
for s in (1, -1):
    ax.axvline(s*Mt, color=RED, lw=.9, ls=DOT)
lab(ax, 3.3, 2.15, r'$\varphi_M(x)$', BLUE, ha='center', va='top')
lab(ax, 3.3, 4.1, r'$x$', LINE, ha='right', va='top')
lab(ax, 2.05, -.35, r'$M$', RED, ha='left', va='top')
lab(ax, -2.05, .35, r'$-M$', RED, ha='right', va='bottom')
ax.spines['left'].set_position('zero'); ax.spines['bottom'].set_position('zero')
ax.set_xlim(-4.2, 4.2); ax.set_ylim(-4.2, 4.2); ax.set_xticks([]); ax.set_yticks([])
save(fig, HERE, 'figure', {'M': Mt})
