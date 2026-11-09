from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 连续六次评价（贯穿例的 EI 轨迹），目标是过九个整点读数的三次样条。
fig, ax = figure(width_mm=100, height_mm=46)
ax.plot(XG, f(XG), color=BLUE, lw=1.4)
xo = np.array(RUN_X); yo = f(xo)
obs(ax, xo, yo)
off = {1.:(0,5),4.:(0,5),7.:(7,-3),8.:(-5,3),6.:(0,-9),0.:(5,3)}
for i,(a,b) in enumerate(zip(xo,yo),1):
    ax.annotate(f'{i}', (a,b), textcoords='offset points', xytext=off[a], ha='center', color=INK, fontsize=7.5)
ax.scatter([6.],[f(6.)], s=22, color=RED, zorder=6, lw=0)
ax.annotate('推荐解', (6.,f(6.)), xytext=(4.75,-.95), color=INK, arrowprops=dict(arrowstyle='-',color=MUTED,lw=.7,shrinkB=3), va='center', ha='right')
ax.set_xlim(-.2,8.2); ax.set_ylim(-1.4,1.25)
ax.set_xticks(range(9))
axes_style(ax,'$x$','$f(x)$')
FACTS={'formula':'natural cubic spline through integer readings','queries':RUN_X}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
