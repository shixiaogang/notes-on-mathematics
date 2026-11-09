from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Infeasible starts on the running example: a reasonably large start and a tiny one.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
facts = {}
for ax, x0, lab in [(a, 1., '(a) $\\mathbf{x}^{(0)}=\\mathbf{s}^{(0)}=\\mathbf{1}$'), (b, 1e-3, '(b) $\\mathbf{x}^{(0)}=\\mathbf{s}^{(0)}=10^{-3}\\mathbf{1}$')]:
    h = path_following(A_RUN, B_RUN, C_RUN, x0 * np.ones(3), np.zeros(1), x0 * np.ones(3), sigma=.3, eta=.9, tol=1e-3, maxit=40)
    T = np.array([r['t'] for r in h]); rp = np.array([np.linalg.norm(r['rp']) for r in h]); rd = np.array([np.linalg.norm(r['rd']) for r in h]); g = np.array([r['x'] @ r['s'] for r in h])
    keep = rp > 1e-9
    ax.semilogy(T[keep], rp[keep], color=RED, lw=1.5, marker='o', ms=2.2)
    keep = rd > 1e-9
    ax.semilogy(T[keep], rd[keep], color=RED, lw=1.5, ls='--', marker='o', ms=2.2)
    ax.semilogy(T, g, color=GREEN, lw=1.5, marker='o', ms=2.2)
    ax.set_xlabel('$t$\n' + lab, labelpad=1); ax.set_ylim(1e-12, 30)
    facts[str(x0)] = {'rounds': len(h) - 1, 'alphas': [r.get('alpha') for r in h]}
a.text(1.0, 3.2, '$\\|\\mathbf{r}_{\\mathrm{d}}\\|_2$', fontsize=7.5); a.text(.2, .14, '$\\|\\mathbf{r}_{\\mathrm{p}}\\|_2$', fontsize=7.5); a.text(5.2, .05, '$\\mathbf{x}^{\\top}\\mathbf{s}$', fontsize=7.5)
b.text(1.6, 5.5, '$\\|\\mathbf{r}_{\\mathrm{d}}\\|_2$', fontsize=7.5); b.text(5, .2, '$\\|\\mathbf{r}_{\\mathrm{p}}\\|_2$', fontsize=7.5); b.text(1.1, 2e-5, '$\\mathbf{x}^{\\top}\\mathbf{s}$', fontsize=7.5)
save(fig, OUT, 'figure', facts)
