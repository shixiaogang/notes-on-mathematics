from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Predictor-corrector: products after a unit step, and convergence against fixed sigma.
pc = predictor_corrector(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, eta=.9, tol=1e-6)
pf = path_following(A_RUN, B_RUN, C_RUN, X0_RUN, Y0_RUN, S0_RUN, sigma=.3, eta=.9, tol=1e-6)
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
r = pc[0]
P = (r['x'] + r['dxa']) * (r['s'] + r['dsa']); C = (r['x'] + r['dx']) * (r['s'] + r['ds']); tg = r['sigma'] * r['mu']
w = .32; idx = np.arange(3)
a.bar(idx - w / 2, P, w, color=YELLOW_FILL, edgecolor=YELLOW, lw=.9, zorder=3)
a.bar(idx + w / 2, C, w, color=GREEN_FILL, edgecolor=GREEN, lw=.9, zorder=3)
a.axhline(tg, color=RED, lw=1.1, ls='--', zorder=4); a.axhline(0, color='#4C4D4F', lw=.95, zorder=5)
a.set_xticks(idx); a.set_xticklabels(['$i=1$', '$i=2$', '$i=3$'])
a.text(-.55, tg + .015, '$\\sigma\\mu$', fontsize=7.5, ha='left', color=INK)
a.text(-.5, .16, '黄：预测', fontsize=7.5); a.text(-.5, .1, '绿：校正后', fontsize=7.5)
a.set_ylim(-.42, .3); a.set_xlim(-.6, 2.5)
a.set_xlabel('(a) 单位步之后的互补积', labelpad=1)
b.semilogy([q['t'] for q in pf], [q['x'] @ q['s'] for q in pf], color=YELLOW, lw=1.6, marker='o', ms=2.4)
b.semilogy([q['t'] for q in pc], [q['x'] @ q['s'] for q in pc], color=GREEN, lw=1.6, marker='o', ms=2.4)
b.text(6.8, 2.2e-2, '$\\sigma=0.3$', fontsize=7.5); b.text(.3, 1.2e-4, '预测—校正', fontsize=7.5)
xlab(b, '$t$', '(b) 互补量')
save(fig, OUT, 'figure', {'rounds_pc': len(pc) - 1, 'rounds_fixed': len(pf) - 1, 'predictor_products': P.tolist(), 'corrected_products': C.tolist(), 'target': tg})
