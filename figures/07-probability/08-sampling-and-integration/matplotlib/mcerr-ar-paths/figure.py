from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"mcerr-common"))
from mcerr_fig import *
# Stationary Gaussian AR(1) chains X(t+1) = rho X(t) + sqrt(1-rho^2) xi with invariant N(0,1), started from N(0,1),
# 80 steps, the same noise sequence (seed 3129) for (a) rho = 0.9, (b) rho = 0, (c) rho = -0.5.
# Green: path; blue: I = E[X] = 0; red: running mean after 80 steps.
T = 80; rng = np.random.default_rng(3129); x0 = rng.standard_normal(); xi = rng.standard_normal(T)
fig, axes = figure(width_mm=112, height_mm=40, ncols=3, sharey=True)
panel(fig, left=.07, right=.98, bottom=.33, top=.95, wspace=.2)
means = {}
for ax, rho in zip(axes, (0.9, 0.0, -0.5)):
    x = x0; X = []
    for t in range(T):
        x = rho*x + math.sqrt(1-rho**2)*xi[t]; X.append(x)
    X = np.array(X); means[rho] = float(X.mean())
    ax.plot(np.arange(1, T+1), X, color=GREEN, lw=.8); ax.axhline(0, color=BLUE, lw=1.0)
    ax.plot([1, T], [X.mean()]*2, color=RED, lw=1.1, ls=DASH)
    ax.set_xlim(0, T); ax.set_ylim(-3.2, 3.2); ax.set_xticks([0, 40, 80]); ax.set_yticks([-2, 0, 2]); axlab(ax, '$t$')
tags(fig, axes)
save(fig, HERE, 'figure', {'means': means})
