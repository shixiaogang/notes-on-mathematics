from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Normalised information density (1/n) i(x^n;y^n) = (1/n) log2 W^n(y|x)/p^n(y) for BSC(0.1) with uniform input.
# It depends only on the number k of disagreements: 1 + (k/n) log2 p + (1-k/n) log2(1-p).
# Blue: matched pair (k ~ Bin(n,0.1));  yellow: codeword independent of the output (k ~ Bin(n,1/2)). Exact pmfs.
# Red line: I = 1 - h2(0.1) = 0.531;  dotted line: mean -0.737 for the independent pair.
p = BSC_P; C = 1-float(h2(p)); Dm = .5*np.log2(2*(1-p)) + .5*np.log2(2*p)
fig, axs = figure(width_mm=110, height_mm=48, ncols=2)
panel(fig, left=.03, right=.98, top=.95, bottom=.28, wspace=.12)
for ax, n in zip(axs, (25, 200)):
    k = np.arange(n+1); v = 1 + k/n*np.log2(p) + (1-k/n)*np.log2(1-p)
    w = (np.log2(1-p)-np.log2(p))/n*.8
    for pm, col, fc in ((binpmf(n, p), BLUE, BLUE_FILL), (binpmf(n, .5), YELLOW, YELLOW_FILL)):
        m = pm > 1e-5
        ax.bar(v[m], pm[m], width=w, color=fc, edgecolor=col, lw=.6)
    ax.axvline(C, color=RED, lw=1.1); ax.axvline(Dm, color=STROKE, lw=.7, ls=DOT)
    ax.set_xlim(-2.4, 1.3); ax.set_xticks([-2, -1, 0, 1]); ax.set_xlabel(r'$i/n$', labelpad=1)
    ax.set_yticks([]); ax.spines['left'].set_visible(False)
    top = ax.get_ylim()[1]*1.15; ax.set_ylim(0, top)
    lab(ax, C-.06, top*.92, r'$I$', RED, ha='right')
    lab(ax, -2.35, top*.88, r'$n=%d$' % n, MUTED)
tags(fig, axs)
save(fig, HERE, 'figure', {'p': p, 'I': C, 'independent_mean': float(Dm)})
