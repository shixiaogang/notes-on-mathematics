from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"dcc-common"))
from dcc_fig import *
# Per-codeword average cost (1/n) sum c(X_i) for i.i.d. Z-channel inputs with q' = P(X=1) = 0.22 and cost c(1)=1:
# this is K/n with K ~ Bin(n, 0.22). Budget Gamma = 0.25 (red line), q' dashed blue; red bars exceed the budget.
qq, G = .22, .25
fig, axs = figure(width_mm=110, height_mm=48, ncols=2)
panel(fig, left=.03, right=.98, top=.95, bottom=.28, wspace=.12)
facts = {}
for ax, n in zip(axs, (50, 400)):
    k = np.arange(n+1); pm = binpmf(n, qq); v = k/n; over = v > G + 1e-12; m = pm > 1e-6
    ax.bar(v[m & ~over], pm[m & ~over], width=.8/n, color=GREEN_FILL, edgecolor=GREEN, lw=.5)
    ax.bar(v[m & over], pm[m & over], width=.8/n, color=RED_FILL, edgecolor=RED, lw=.5)
    ax.axvline(G, color=RED, lw=1.1); ax.axvline(qq, color=BLUE, lw=1.0, ls=DASH)
    ax.set_xlim(.04, .44); ax.set_yticks([]); ax.spines['left'].set_visible(False)
    ax.set_xlabel('码字的平均成本', labelpad=1)
    top = pm.max()*1.22; ax.set_ylim(0, top)
    lab(ax, .05, top*.9, r'$n=%d$' % n, MUTED)
    lab(ax, G+.008, top*.9, r'$\Gamma$', RED); lab(ax, qq-.008, top*.9, r'$q^{\prime}$', BLUE, ha='right')
    facts['P_over_n%d' % n] = float(pm[over].sum())
tags(fig, axs)
save(fig, HERE, 'figure', {'q_prime': qq, 'Gamma': G, **facts})
