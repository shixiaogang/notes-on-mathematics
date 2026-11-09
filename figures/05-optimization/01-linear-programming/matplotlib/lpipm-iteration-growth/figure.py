from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/01-linear-programming/matplotlib/lpipm-common"))
from ipm_plot import *
OUT = Path(__file__).resolve().parent

# Iterations against size on random dense LPs with a well-centered strictly feasible start.
ns = [10, 30, 100, 300, 1000]
rng = np.random.default_rng(20261109)
S, LO, PC, THEORY = [], [], [], []
for n in ns:
    m = n // 2; A = rng.standard_normal((m, n)); x = np.ones(n); s = np.ones(n); y = rng.standard_normal(m)
    b = A @ x; c = A.T @ y + s; eps = 1e-6 * n
    S.append(len(short_step(A, b, c, x, y, s, eps=eps)) - 1)
    LO.append(len(long_step(A, b, c, x, y, s, sigma=.1, gamma=1e-3, eps=eps)) - 1)
    PC.append(len(predictor_corrector(A, b, c, x, y, s, eta=.99, tol=eps)) - 1)
    THEORY.append(int(np.ceil(2.5 * np.sqrt(n) * np.log(n / eps))))
fig, ax = figure(width_mm=96, height_mm=54)
ax.loglog(ns, S, color=BLUE, lw=1.5, marker='o', ms=3)
ax.loglog(ns, LO, color=YELLOW, lw=1.6, marker='o', ms=3)
ax.loglog(ns, PC, color=GREEN, lw=1.6, marker='o', ms=3)
ax.text(ns[3] * .9, S[3] * 1.45, '短步', fontsize=7.5, ha='right'); ax.text(ns[3], LO[3] * 1.3, '长步', fontsize=7.5, ha='center'); ax.text(ns[3], PC[3] * .55, '预测—校正', fontsize=7.5, ha='center')
ax.set_xlabel('$n$', labelpad=1); ax.set_ylabel('迭代轮数', labelpad=1)
ax.set_xticks(ns); ax.set_xticklabels([str(k) for k in ns]); ax.minorticks_off()
ax.set_ylim(3, 2500)
save(fig, OUT, 'figure', {'n': ns, 'short': S, 'long': LO, 'predictor_corrector': PC, 'short_bound': THEORY, 'seed': 20261109})
print(ns, S, LO, PC, THEORY)
