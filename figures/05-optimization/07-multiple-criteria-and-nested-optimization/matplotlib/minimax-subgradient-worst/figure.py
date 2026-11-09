from pathlib import Path
import sys
for _p in Path(__file__).resolve().parents:
    if (_p/"minimax-common").is_dir(): sys.path.insert(0, str(_p/"minimax-common")); break
from mm_fig import *
HERE = Path(__file__).resolve().parent
# Exact-response subgradient method on phi(x)=(|x|+1)^2, x0=0.8.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panels(fig, .09, .985, .96, .25, .32)
def g(x):
    y = -1 if x >= 1e-15 else (1 if x <= -1e-15 else 1); return 2*(x-y)
def run(st, T):
    x = .8; out = [x]
    for t in range(T): x = x-st(t)*g(x); out.append(x)
    return np.array(out)
T = 40; c = run(lambda t: .2, T); d = run(lambda t: .4/(t+1), T)
ax = axes[0]; setup(ax, (0, T), (-.5, 1), range(0, T+1, 10), (-.5, 0, .5, 1), xl='$t$', yl='$x^{(t)}$')
ax.axhline(0, color=MUTED, lw=.85, ls=':'); ax.plot(c, color=YELLOW, lw=1.2); ax.plot(d, color=GREEN, lw=1.4)
ax = axes[1]; phi = lambda v: (np.abs(v)+1)**2-1; setup(ax, (0, T), (0, 2.4), range(0, T+1, 10), (0, 1, 2), xl='$t$', yl=r'$\phi(x^{(t)})-1$')
ax.plot(phi(c), color=YELLOW, lw=1.2); ax.plot(phi(d), color=GREEN, lw=1.4)
tags(fig, axes)
save(fig, HERE, 'figure', {'phi': '(|x|+1)^2', 'x0': .8, 'alpha_const': .2, 'alpha_dim': '0.4/(t+1)', 'subgradient at 0': 'y=1'})
print(c[:5], d[:6])
