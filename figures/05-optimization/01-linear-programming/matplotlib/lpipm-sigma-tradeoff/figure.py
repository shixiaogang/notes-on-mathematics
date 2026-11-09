from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Effect of the centering parameter on the running example.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
spec = [(.9, BLUE, ':'), (.5, PURPLE, '--'), (.3, GREEN, '-'), (.1, YELLOW, '-')]
rounds = {}
for sg, c, ls in spec:
    h = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=sg, eta=.9, tol=1e-6, maxit=24)
    T = [r['t'] for r in h]; g = [r['x'] @ r['s'] for r in h]; ce = [np.min(r['x'] * r['s']) / r['mu'] for r in h]
    a.semilogy(T, g, color=c, ls=ls, lw=1.5, marker='o', ms=2.2)
    b.plot(T[:13], ce[:13], color=c, ls=ls, lw=1.5, marker='o', ms=2.2)
    rounds[str(sg)] = len(h) - 1
a.axhline(1e-6, color=MUTED, lw=.85); a.set_ylim(3e-7, 4); a.set_xlim(0, 24)
a.text(15.5, 1.1, '$\\sigma=0.9$', fontsize=7.5); a.text(16, 3.1e-4, '$\\sigma=0.5$', fontsize=7.5, ha='left'); a.text(1.8, 3e-6, '$\\sigma=0.1$', fontsize=7.5); a.text(13.6, 3e-6, '$\\sigma=0.3$', fontsize=7.5)
xlab(a, '$t$', '(a) 互补量')
b.set_ylim(0, 1.05); b.set_xlim(0, 12); xlab(b, '$t$', '(b) 中心性')
save(fig, OUT, 'figure', {'rounds_to_1e-6_or_24': rounds})
