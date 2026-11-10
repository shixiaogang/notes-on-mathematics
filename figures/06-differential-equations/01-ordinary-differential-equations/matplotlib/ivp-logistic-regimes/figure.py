from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：x'=x(1-x) 的三种初值区域与各自的存在区间，右侧为相线。
fig, axes = figure(width_mm=104, height_mm=56, ncols=2, gridspec_kw={'width_ratios': [6, 1]})
panel(fig, .075, .96, .97, .15, .16)
a, b = axes
T0 = -np.log(2); T1 = np.log(3)
sol = lambda t, x0: x0*np.exp(t)/(1 - x0 + x0*np.exp(t))
t = np.linspace(-2, 5, 700); a.plot(t, sol(t, .1), color=BLUE, lw=1.4, zorder=4)
t = np.linspace(T0 + 2e-3, 5, 700); a.plot(t, sol(t, 2), color=YELLOW, lw=1.6, zorder=4)
t = np.linspace(-2, T1 - 2e-3, 700); a.plot(t, sol(t, -.5), color=PURPLE, lw=1.4, zorder=4)
a.axhline(0, color=BLUE, lw=1, zorder=2); a.axhline(1, color=BLUE, lw=1, zorder=2)
a.axvline(T0, color=RED, lw=.95, ls=(0, (4, 2)), zorder=1); a.axvline(T1, color=RED, lw=.95, ls=(0, (4, 2)), zorder=1)
dot(a, 0, .1); dot(a, 0, 2); dot(a, 0, -.5)
a.set_xlim(-2, 5); a.set_ylim(-4, 5); a.set_yticks([-4, -2, 0, 1, 2, 4]); a.set_xticks([-2, T0, 0, T1, 3, 5]); a.set_xticklabels(['$-2$', '$-\\ln 2$', '0', '$\\ln 3$', '3', '5'])
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$x$', labelpad=1)
b.set_ylim(-4, 5); b.set_xlim(-1, 1); b.set_xticks([]); b.spines['bottom'].set_visible(False); b.spines['left'].set_visible(False); b.set_yticks([])
b.plot([0, 0], [-4, 5], color=STROKE, lw=.95, zorder=1)
ar = dict(arrowstyle='-|>', color=BLUE, lw=1.1, mutation_scale=8, shrinkA=0, shrinkB=0)
for y0, y1 in [(.2, .8), (4.4, 2.4), (-1.3, -3.2)]:
    b.annotate('', xy=(0, y1), xytext=(0, y0), arrowprops=ar)
b.plot([0, 0], [0, 1], 'o', ms=4.6, color=BLUE, mew=0, zorder=4)
b.text(.3, 0, '0', va='center', fontsize=7.5); b.text(.3, 1, '1', va='center', fontsize=7.5)
b.set_xlabel('$x$', labelpad=1)
save(fig, HERE, 'figure', {'formula': "x'=x(1-x)", 'x0': [.1, 2, -.5], 'blowup_times': [T0, T1]})
