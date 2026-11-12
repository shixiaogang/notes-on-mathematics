from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Densities of sums of n iid Unif(0,1), n=1..4, by numerical convolution (grid step 1e-3); N(2,1/3) for comparison.
h = 1e-3; g = np.ones(int(1/h))
fig, ax = figure(width_mm=104, height_mm=48)
panel(fig, left=.08, right=.98, bottom=.22, top=.95)
sh = ['#BCC9D8', '#9AAEC4', '#7188A3', '#4E6784']; f = g.copy(); res = {}
for n in range(1, 5):
    x = (np.arange(len(f))+.5)*h
    xx = np.concatenate([[0], x, [x[-1]+h]]); ff = np.concatenate([[0], f, [0]])
    ax.plot(xx, ff, color=sh[n-1], lw=1.4); res[n] = float(f.sum()*h)
    lab(ax, n/2, f.max()+.04, f'$n={n}$', sh[n-1] if n > 1 else MUTED, ha='center')
    f = np.convolve(f, g)*h
t = np.linspace(0, 4, 400); ax.plot(t, phi(t, 2, np.sqrt(1/3)), color=YELLOW, lw=1.5, ls=DASH)
ax.set_xlim(-.1, 4.1); ax.set_ylim(0, 1.2); ax.set_xticks([0, 1, 2, 3, 4]); ax.set_yticks([0, .5, 1]); axlab(ax, '$z$')
save(fig, HERE, 'figure', {'total mass n=1..4': res})
