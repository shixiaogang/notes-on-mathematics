from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# Order statistics of n=5 iid Unif(0,1): U_(k) ~ Beta(k, 6-k); histogram of U_(2) from 20000 samples (seed 19).
fig, ax = figure(width_mm=104, height_mm=48)
panel(fig, left=.08, right=.98, bottom=.22, top=.95)
rng = np.random.default_rng(19); U = np.sort(rng.uniform(size=(20000, 5)), axis=1)
hist(ax, U[:, 1], 40, (0, 1))
sh = ['#BCC9D8', '#9AAEC4', '#7188A3', '#5F7894', '#4E6784']; t = np.linspace(1e-6, 1-1e-6, 400)
for k in range(1, 6):
    ax.plot(t, beta_pdf(t, k, 6-k), color=sh[k-1], lw=1.4); dot(ax, k/6, 0, RED, ms=4)
ax.set_xlim(0, 1); ax.set_ylim(0, 5.2); ax.set_xticks([0, 1/6, 2/6, .5, 4/6, 5/6, 1]); ax.set_xticklabels(['0', '1/6', '2/6', '3/6', '4/6', '5/6', '1']); ax.set_yticks([0, 2, 4]); axlab(ax, '$t$')
save(fig, HERE, 'figure', {'seed': 19, 'mean U_(2) sim': float(U[:, 1].mean()), 'exact': 2/6})
