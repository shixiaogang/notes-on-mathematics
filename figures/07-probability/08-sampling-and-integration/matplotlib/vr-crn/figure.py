from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"vr-common"))
from vr_fig import *
# Two schemes: A = min(X_A, 1), X_A ~ Exp(1); B = min(X_B, 1), X_B ~ Exp(1.25); both by inversion x = -ln(1-u)/rate.
# (a) independent inputs U, U' (seed 9, 300 pairs); (b) common input U (seed 9): B = a(U) with A, B both increasing in U.
# Variances of A - B: independent Var A + Var B; common 0.003817 (quadrature over u, 2e6 midpoints).
rng = np.random.default_rng(9); U = rng.random(300); U2 = rng.random(300)
A = np.minimum(-np.log(1-U), 1); Bi = np.minimum(-np.log(1-U2)/1.25, 1); Bc = np.minimum(-np.log(1-U)/1.25, 1)
x = (np.arange(2000000)+.5)/2000000
a_ = np.minimum(-np.log(1-x), 1); b_ = np.minimum(-np.log(1-x)/1.25, 1); br = np.minimum(-np.log(x)/1.25, 1)
fig, axs = figure(width_mm=100, height_mm=56, ncols=2)
panel(fig, left=.11, right=.97, bottom=.22, top=.97, wspace=.34)
for ax, Bv in zip(axs, (Bi, Bc)):
    ax.plot([0, 1], [0, 1], color=STROKE, lw=.6, ls=DASH)
    ax.plot(A, Bv, 'o', ms=1.8, color=GREEN, mew=0, clip_on=False)
    ax.set_xlim(0, 1.02); ax.set_ylim(0, 1.02); ax.set_aspect('equal'); ax.set_xticks([0, .5, 1]); ax.set_yticks([0, .5, 1])
    axlab(ax, '$A$', '$B$')
tags(fig, axs)
save(fig, HERE, 'figure', {'EA': float(a_.mean()), 'EB': float(b_.mean()), 'VarA': float(a_.var()), 'VarB': float(b_.var()),
     'Cov_common': float(np.mean(a_*b_)-a_.mean()*b_.mean()), 'Var_diff_common': float(np.var(a_-b_)),
     'Var_diff_indep': float(a_.var()+b_.var()), 'Var_diff_reversed': float(np.var(a_-br))})
