from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/05-optimization/06-constrained-optimization/matplotlib/nlipm-common"))
from nlipm import *
OUT = Path(__file__).resolve().parent
# Conditioning along the central path of the running example.
data = central_path(np.logspace(1, -8, 120)); 
mu, cH, cA = [], [], []
for m, c in data:
    gg = -g(c); l = m/gg; JJ = J(c); H = W(c, l)+JJ.T@np.diag(l/gg)@JJ
    A3 = np.block([[W(c, l), JJ.T], [JJ, -np.diag(gg/l)]])
    mu.append(m); cH.append(np.linalg.cond(H)); cA.append(np.linalg.cond(A3))
mu = np.array(mu)
fig, ax = figure(width_mm=88, height_mm=50)
ax.loglog(mu, cH, color=RED, lw=1.5); ax.loglog(mu, cA, color=GREEN, lw=1.5); ax.loglog(mu, 1/mu, color=MUTED, lw=.85, ls='--')
ax.invert_xaxis(); ax.set_xlabel('$\\mu$', labelpad=1); ax.set_ylabel('条件数', labelpad=1)
save(fig, OUT, 'figure', {'mu': mu[[0, 40, 80, 119]].tolist(), 'cond_H': [cH[i] for i in (0, 40, 80, 119)], 'cond_A3': [cA[i] for i in (0, 40, 80, 119)]})
