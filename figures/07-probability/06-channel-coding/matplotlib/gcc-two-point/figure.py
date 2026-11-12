from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Two-point input X in {-A, +A} over Y = X + Z, Z ~ N(0,1). Output densities given X = -A (yellow) and X = +A (blue);
# the minimum-distance decision threshold 0 (dark grey); red fill: error probability Q(A) when +A is sent.
# (a) A = 1: error 0.159;  (b) A = 3: error 0.00135.  Larger amplitude separates the two output laws.
fig, axs = figure(width_mm=108, height_mm=44, ncols=2)
panel(fig, left=.04, right=.98, top=.95, bottom=.3, wspace=.1)
y = np.linspace(-6.5, 6.5, 1500)
facts = {}
for ax, A in zip(axs, (1.0, 3.0)):
    f1, f0 = phi(y-A), phi(y+A)
    m = y < 0
    ax.fill_between(y[m], 0, f1[m], color=RED_FILL, lw=0)
    ax.plot(y, f0, color=YELLOW, lw=1.5)
    ax.plot(y, f1, color=BLUE, lw=1.4)
    ax.axvline(0, color=STROKE, lw=.85, ls=DASH)
    dot(ax, A, 0); dot(ax, -A, 0, color=YELLOW)
    ax.set_xlim(-6.5, 6.5); ax.set_ylim(0, .45); ax.set_yticks([])
    ax.spines['left'].set_visible(False)
    ax.set_xticks([-A, 0, A]); ax.set_xticklabels([r'$-%g$' % A, '0', r'$%g$' % A])
    ax.set_xlabel(r'$y$', labelpad=1)
    pe = float(Qf(A)); facts['A=%g' % A] = pe
    lab(ax, -6.2, .36, '%.3f' % pe if A < 2 else '%.5f' % pe, RED)
tags(fig, axs)
save(fig, HERE, 'figure', facts)
