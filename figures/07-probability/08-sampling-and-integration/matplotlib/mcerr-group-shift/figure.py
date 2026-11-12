from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Shifted grid groups for I = int_0^1 e^u du: group r uses U_i = (i/4 + Delta_r) mod 1, i = 0..3.
# (a) the four groups with Delta = 0.37, 0.81, 0.19, 0.64 (green dots, red ring marks the point i = 0, i.e. Delta itself).
# (b) 5000 repetitions of the whole experiment (R = 4 groups, seed 3133): histogram of the correct estimate
#     s_Q^2 / R (green) and of the naive estimate S^2/(nR) from the 16 pooled values (yellow);
#     true Var(Q-bar) = Var(Q)/4 (blue line), Var(Q) by fine quadrature over Delta.
Ds = [0.37, 0.81, 0.19, 0.64]
fig, (a, b) = figure(width_mm=112, height_mm=50, ncols=2, gridspec_kw={'width_ratios': [1, 1.25]})
panel(fig, left=.07, right=.98, bottom=.28, top=.95, wspace=.25)
for r, d in enumerate(Ds):
    y = 4 - r; a.plot([0, 1], [y, y], color=STROKE, lw=.6)
    p = (np.arange(4)/4 + d) % 1
    a.plot(p, [y]*4, 'o', ms=3.6, color=GREEN, mew=0)
    a.plot([d], [y], 'o', ms=6, mfc='none', mec=RED, mew=.9)
    lab(a, 1.04, y, r'$\Delta=%.2f$' % d, INK, va='center')
a.set_xlim(0, 1.35); a.set_ylim(.4, 4.6); a.set_xticks([0, .5, 1]); a.set_yticks([1, 2, 3, 4]); a.set_yticklabels(['4', '3', '2', '1'])
a.spines['bottom'].set_bounds(0, 1); axlab(a, '$u$')
x = (np.arange(400000)+.5)/400000; q = np.mean([np.exp((x+i/4) % 1) for i in range(4)], axis=0); vq = q.var()
rng = np.random.default_rng(3133); E = 5000
Dl = rng.random((E, 4)); pts = (Dl[:, :, None] + np.arange(4)/4) % 1; v = np.exp(pts)
Q = v.mean(2); good = Q.var(1, ddof=1)/4; naive = v.reshape(E, 16).var(1, ddof=1)/16
bins = np.logspace(-4.5, -1.5, 46)
for arr, fc, ec in [(good, GREEN_FILL, GREEN), (naive, YELLOW_FILL, YELLOW)]:
    h, e = np.histogram(arr, bins=bins); b.bar(e[:-1], h/E, width=np.diff(e), align='edge', color=fc, edgecolor=ec, lw=.5)
b.axvline(vq/4, color=BLUE, lw=1.3)
b.set_xscale('log'); b.set_xlim(10**-4.5, 10**-1.5); logticks(b, [-4, -3, -2], 'x'); b.set_yticks([0, .2, .4, .6]); axlab(b, '方差估计')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'var_Q': vq, 'var_Qbar': vq/4, 'mean_good': float(good.mean()), 'median_good': float(np.median(good)),
     'mean_naive': float(naive.mean()), 'frac_good_below_true': float(np.mean(good < vq/4))})
