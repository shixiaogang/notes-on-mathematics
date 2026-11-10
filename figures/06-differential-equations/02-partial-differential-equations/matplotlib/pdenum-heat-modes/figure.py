from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# Spectrum of -Laplacian: continuous m^2 pi^2 vs discrete for h=1/8, 1/16; and modes for h=1/8.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.095, wspace=.24, bottom=.27)
ax = axes[0]
for n, c, mk_ in ((8, GREEN, 'o'), (16, YELLOW, 's')):
    m = np.arange(1, n); ax.plot(m, 4*n**2*np.sin(m*PI/(2*n))**2, color=c, lw=1.2, marker=mk_, ms=3, mew=0)
m = np.arange(1, 16); ax.plot(m, m**2*PI**2, color=BLUE, lw=1.4)
ax.set_xlim(0, 16); ax.set_ylim(0, 1100); ax.set_xticks([1, 7, 15]); ax.set_yticks([0, 500, 1000]); ax.set_xlabel('$m$', labelpad=1); ax.set_ylabel(r'$\lambda_m$', labelpad=1)
lab(ax, 7.2, 720, r'$m^2\pi^2$', BLUE, ha='right'); lab(ax, 11.2, 560, '$h=1/16$', YELLOW, ha='left', va='top'); lab(ax, 8.2, 210, '$h=1/8$', GREEN, ha='left')
ax = axes[1]; X = np.linspace(0, 1, 401); n = 8; xn = np.linspace(0, 1, n+1)
for m, c, off in ((1, BLUE, 2.4), (7, RED, 0)):
    ax.plot(X, off+np.sin(m*PI*X), color=c, lw=.9, ls=DOT)
    ax.plot(xn, off+np.sin(m*PI*xn), color=GREEN if m == 1 else RED, lw=1.3, marker='o', ms=3.2, mew=0)
lab(ax, 1.02, 3.2, '$m=1$', GREEN, ha='right', va='bottom'); lab(ax, 1.02, 1.08, '$m=7$', RED, ha='right', va='bottom')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-1.2, 3.75); ax.set_xticks([0, 1]); ax.set_yticks([]); ax.set_xlabel('$x$', labelpad=1); ax.spines['left'].set_visible(False)
tags(fig, axes)
save(fig, HERE, 'figure', {'lam_max_h8': float(4*64*np.sin(7*PI/16)**2), 'continuous_m7': 49*PI**2})
print(4*64*np.sin(7*PI/16)**2, 4*64*np.sin(PI/16)**2)
