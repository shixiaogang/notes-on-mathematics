from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"ivp-common"))
from ivp_common import *
HERE = Path(__file__).resolve().parent

# 目标：两类不能靠有限分段处理的可测输入及其累积：切换点聚集、胖 Cantor 集指示函数。
fig, axes = figure(width_mm=112, height_mm=78, ncols=2, nrows=2)
panel(fig, .085, .985, .975, .175, .27, .62)
(a, b), (c, d) = axes
N = 400000
t = (np.arange(N) + .5)/N
g = np.sign(np.sin(1/t))
x = np.cumsum(g)/N
a.fill_between(t, 0, g, color=BLUE_FILL, lw=0, step='mid')
tt = t[t > .03]
a.step(tt, g[t > .03], color=STROKE, lw=.8, where='mid')
a.set_xlim(0, 1); a.set_ylim(-1.2, 1.2); a.set_xticks([0, .5, 1]); a.set_xticklabels(['0', '0.5', '1']); a.set_yticks([-1, 0, 1]); a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$g$', labelpad=1)
b.plot(np.r_[0, t], np.r_[0, x], color=BLUE, lw=1.4); dot(b, 0, 0)
b.set_xlim(0, 1); b.set_xticks([0, .5, 1]); b.set_xticklabels(['0', '0.5', '1']); b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$x$', labelpad=1)
# Smith-Volterra-Cantor：第 n 步从每段中间挖去长度 4^-n 的开区间。
keep = [(0., 1.)]
for n in range(1, 12):
    new = []
    for l, r in keep:
        m = (l + r)/2; h = 4.0**-n/2
        new += [(l, m - h), (m + h, r)]
    keep = new
L = np.array(keep)
idx = np.zeros(N, bool)
for l, r in L:
    idx[int(np.ceil(l*N)):int(r*N)] = True
measure = L[:, 1].sum() - L[:, 0].sum()
print('measure', measure)
xc = np.cumsum(idx)/N
c.fill_between(t, 0, 1, where=idx, color=STROKE, lw=0, step='mid')
c.set_xlim(0, 1); c.set_ylim(0, 1.2); c.set_xticks([0, .5, 1]); c.set_xticklabels(['0', '0.5', '1']); c.set_yticks([0, 1]); c.set_xlabel('$t$', labelpad=1); c.set_ylabel('$g$', labelpad=1)
d.plot(np.r_[0, t], np.r_[0, xc], color=BLUE, lw=1.4); dot(d, 0, 0)
d.set_xlim(0, 1); d.set_ylim(0, .55); d.set_xticks([0, .5, 1]); d.set_xticklabels(['0', '0.5', '1']); d.set_yticks([0, .25, .5]); d.set_xlabel('$t$', labelpad=1); d.set_ylabel('$x$', labelpad=1)
for ax, s in zip([a, b, c, d], ('(a)', '(b)', '(c)', '(d)')):
    p = ax.get_position(); fig.text((p.x0 + p.x1)/2, p.y0 - .135, s, ha='center', va='bottom')
save(fig, HERE, 'figure', {'top': 'g=sign sin(1/t)', 'bottom': 'indicator of Smith-Volterra-Cantor set, measure 1/2, truncated at 11 levels', 'x_top_1': float(x[-1]), 'measure': float(measure)})
