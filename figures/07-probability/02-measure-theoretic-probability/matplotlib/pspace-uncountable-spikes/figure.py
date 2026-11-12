from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/07-probability/02-measure-theoretic-probability/matplotlib/pspace-common"))
from pspace_common import *
# Target: X_t(omega) = 1{U(omega) = t}, t in [0,1], with U uniform.
# For each fixed t, X_t = 0 almost surely, yet every path t -> X_t(omega) has one spike of height 1 at t = U(omega).
# Three outcomes with U(omega) = 0.23, 0.58, 0.81 are drawn; the dashed line is a fixed time t0 = 0.4.
fig, ax = figure(width_mm=96, height_mm=46)
style(ax)
us = [0.23, 0.58, 0.81]
for i, u in enumerate(us):
    base = 1.6*i
    ax.plot([0, 1], [base, base], color=BLUE, lw=1.4)
    ax.plot([u, u], [base, base+1], color=BLUE, lw=1.4)
    ax.plot([u], [base+1], 'o', ms=3.4, color=RED, zorder=5)
    ax.plot([u], [base], 'o', ms=3.0, mfc='white', mec=BLUE, mew=.9, zorder=5)
    ax.text(1.02, base, rf'$U(\omega_{i+1})={u}$', fontsize=7.5, color=INK, va='center')
ax.axvline(0.4, color=LINE, lw=.85, ls='--')
ax.text(0.4, 4.35, '$t_0$', ha='center', fontsize=8, color=INK)
ax.set_xlim(0, 1); ax.set_ylim(-0.2, 4.3)
ax.set_yticks([0, 1.6, 3.2]); ax.set_yticklabels([r'$\omega_1$', r'$\omega_2$', r'$\omega_3$'])
ax.spines['left'].set_visible(False); ax.tick_params(axis='y', length=0)
ax.set_xticks([0, 0.5, 1]); ax.set_xlabel('$t$')
save(fig, HERE(__file__), 'figure', {'U values': us, 't0': 0.4})
