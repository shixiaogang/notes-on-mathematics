from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/06-differential-equations/01-ordinary-differential-equations/matplotlib/lde-common'))
from lde_common import *
HERE = Path(__file__).resolve().parent
# 目标：A(t)=[[0,t],[0,1]]，x0=(0,1)。真解 x1=(t-1)e^t+1（RK4 核对），直接取指数的结果 (e^t-1)t/2 不同。
A = lambda t: np.array([[0., t], [0, 1]])
fig, ax = figure(width_mm=92, height_mm=50)
panel(fig, .095, .975, .96, .16)
t = np.linspace(0, 3, 300)
ax.plot(t, (t-1)*np.exp(t)+1, color=BLUE, lw=MAIN)
ax.plot(t, (np.exp(t)-1)*t/2, color=RED, lw=1.4, ls=(0, (4, 2)))
ts, xs = rk4(lambda s, x: A(s)@x, 0, [0, 1], 3, 60)
ax.plot(ts[::6], xs[::6, 0], 'o', ms=3.2, color=GREEN, mew=0, zorder=4)
naive2 = np.array([expm(np.array([[0, s*s/2], [0, s]]))[0, 1] for s in ts[::12]])
ax.plot(ts[::12], naive2, 's', ms=2.8, color=RED, mew=0, zorder=4)
ax.plot([0], [0], 'o', ms=3.8, color=RED, mew=0, clip_on=False, zorder=5)
ax.text(1.72, 14, '真解', color=BLUE); ax.text(2.5, 8, '$\\mathrm{e}^{\\int \\mathbf{A}}$', color=RED)
ax.set_xlim(0, 3); ax.set_ylim(0, 42); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, 20, 40]); label(ax, '$t$', '$x_1$')
print(float(xs[-1, 0]), (3-1)*np.exp(3)+1)
save(fig, HERE, 'figure', {'A(t)': '[[0,t],[0,1]]', 'x0': [0, 1], 'true': '(t-1)e^t+1 checked with RK4 h=0.05', 'naive': '(e^t-1)t/2'})
