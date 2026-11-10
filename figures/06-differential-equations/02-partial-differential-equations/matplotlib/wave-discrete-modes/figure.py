from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: eigenvectors of the fixed bead chain and its frequencies against the continuum n*pi.
fig, axs = figure(width_mm=112, height_mm=44, ncols=2)
ax = axs[0]; style(ax); N = 3; h = 1/(N+1); xj = np.arange(0, N+2)*h
for k, col, lw in zip([1, 2, 3], [BLUE, YELLOW, PURPLE], [1.5, 1.6, 1.2]):
    v = np.sin(k*np.pi*xj)
    ax.plot(xj, v, color=col, lw=lw, marker='o', ms=3.2)
    xf = np.linspace(0, 1, 201); ax.plot(xf, np.sin(k*np.pi*xf), color=col, lw=.85, ls=(0, (2, 2)))
ax.plot([0, 1], [0, 0], 'o', ms=4, color=RED, clip_on=False, zorder=5)
ax.set_xlim(0, 1); ax.set_ylim(-1.15, 1.15); ax.set_xticks([0, .25, .5, .75, 1]); ax.set_xticklabels(['0', '1/4', '1/2', '3/4', '1']); ax.set_yticks([-1, 0, 1]); sub(ax, 'a', '$x$')
ax = axs[1]; style(ax)
n = np.arange(1, 16); ax.plot(n, n*np.pi, color=BLUE, lw=1.5, label='连续弦')
om = lambda N, k: (2*(N+1))*np.sin(k*np.pi/(2*(N+1)))
k3 = np.arange(1, 4); k15 = np.arange(1, 16)
ax.plot(k15, om(15, k15), color=GREEN, lw=1.3, marker='o', ms=2.8)
ax.plot(k3, om(3, k3), color=YELLOW, lw=1.6, marker='s', ms=3)
ax.text(10.6, 39.5, r'$n\pi$', color=BLUE); ax.text(11.3, 22.6, '$N=15$', color=GREEN); ax.text(3.6, 2.5, '$N=3$', color=YELLOW)
ax.set_xlim(0, 16); ax.set_ylim(0, 50); ax.set_ylabel(r'$\omega$'); sub(ax, 'b', '模式序号'); 
save(fig, HERE(__file__), 'figure', {'formula': 'omega_k=(2/h) sin(k pi h/2), h=1/(N+1); continuum n pi'})
