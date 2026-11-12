from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"rvt-common"))
from rvt_fig import *
# X1~Gamma(2,1), X2~Gamma(3,1) independent: P=X1/S ~ Beta(2,3), S ~ Gamma(5,1), P independent of S. Seed 5, 20000 samples.
rng = np.random.default_rng(5); X1 = rng.gamma(2, 1, 20000); X2 = rng.gamma(3, 1, 20000)
S = X1+X2; P = X1/S
fig, axes = figure(width_mm=112, height_mm=42, ncols=3)
panel(fig, left=.06, right=.98, bottom=.3, top=.95, wspace=.38)
ax = axes[0]; hist(ax, P, 30, (0, 1)); p = np.linspace(0, 1, 300); ax.plot(p, beta_pdf(p, 2, 3), color=BLUE, lw=1.4)
ax.set_xlim(0, 1); ax.set_xticks([0, .4, 1]); ax.set_yticks([0, 1, 2]); axlab(ax, '$p$')
ax = axes[1]; hist(ax, S, 30, (0, 15)); s = np.linspace(0, 15, 300); ax.plot(s, gamma_pdf(s, 5, 1), color=BLUE, lw=1.4)
ax.set_xlim(0, 15); ax.set_xticks([0, 5, 10, 15]); ax.set_yticks([0, .1, .2]); axlab(ax, '$s$')
ax = axes[2]; q = np.quantile(S, [1/3, 2/3]); g = np.digitize(S, q)
shade = ['#B5C9B9', GREEN, '#55705E']; ks = []
for k in range(3):
    v = np.sort(P[g == k]); ax.plot(v, np.arange(1, len(v)+1)/len(v), color=shade[k], lw=1.1); ks.append(float(v.mean()))
ax.set_xlim(0, 1); ax.set_ylim(0, 1.02); ax.set_xticks([0, .4, 1]); ax.set_yticks([0, .5, 1]); axlab(ax, '$p$')
tags(fig, axes)
save(fig, HERE, 'figure', {'seed': 5, 'n': 20000, 'mean P': float(P.mean()), 'mean S': float(S.mean()), 'group means of P': ks, 'corr(P,S)': float(np.corrcoef(P, S)[0, 1])})
