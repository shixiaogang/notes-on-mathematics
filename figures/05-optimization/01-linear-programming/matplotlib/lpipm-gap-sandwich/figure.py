from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Primal and dual objectives along feasible and infeasible runs of the running example.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
hf = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=.3, eta=.9, tol=1e-3)
hi = path_following(A_RUN, B_RUN, C_RUN, .1 * np.ones(3), np.zeros(1), np.ones(3), sigma=.3, eta=.9, tol=1e-3)
for ax, h, lab in [(a, hf, '(a) 严格可行起点'), (b, hi, '(b) 不可行起点')]:
    T = [r['t'] for r in h]; p = [C_RUN @ r['x'] for r in h]; d = [r['y'][0] for r in h]
    ax.plot(T, p, color=BLUE, lw=1.5, marker='o', ms=2.4); ax.plot(T, d, color=PURPLE, lw=1.5, marker='o', ms=2.4)
    ax.axhline(1, color=RED, lw=1.1, ls='--'); xlab(ax, '$t$', lab)
a.text(1.8, 1.5, '$\\mathbf{c}^{\\top}\\mathbf{x}$', fontsize=7.5); a.text(.15, .25, '$\\mathbf{b}^{\\top}\\mathbf{y}$', fontsize=7.5); a.text(4.8, 1.07, '$p^\\star=1$', fontsize=7.5)
b.text(2.6, .63, '$\\mathbf{c}^{\\top}\\mathbf{x}$', fontsize=7.5); b.text(.65, .28, '$\\mathbf{b}^{\\top}\\mathbf{y}$', fontsize=7.5); b.text(5.5, 1.06, '$p^\\star=1$', fontsize=7.5)
save(fig, OUT, 'figure', {'infeasible_primal': [float(C_RUN @ r['x']) for r in hi], 'infeasible_dual': [float(r['y'][0]) for r in hi], 'infeasible_rp': [float(r['rp'][0]) for r in hi]})
