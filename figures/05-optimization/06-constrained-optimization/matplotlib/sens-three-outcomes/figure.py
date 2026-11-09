from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'sens-common'))
from sens_core import *
# f(x,theta)=exp(x)-theta*x on R for theta=1, 0, -0.5: attained, finite but unattained, unbounded below.
fig, axs = figure(width_mm=112, height_mm=42, ncols=3)
X = np.linspace(-5, 1.6, 400)
for ax, th, sub in zip(axs, [1, 0, -.5], ['(a)', '(b)', '(c)']):
    ax.plot(X, np.exp(X)-th*X, color=BLUE, lw=1.4)
    clean(ax, (-5, 1.6), (-3.2, 5), xlabel='$x$', sub=sub)
    ax.set_xticks([-4, -2, 0]); ax.set_yticks([-2, 0, 2, 4])
    ax.text(-2.6, 4.25, rf'$\theta={th}$', fontsize=8)
opt_point(axs[0], (0, 1))
axs[1].axhline(0, color=PURPLE, lw=.95, ls='--')
axs[2].annotate('', xy=(-4.7, -3.0), xytext=(-2.9, -2.1), arrowprops=dict(arrowstyle='-|>', color=RED, lw=1.0, mutation_scale=7))
save(fig, Path(__file__).resolve().parent, 'figure', {'objective': 'exp(x)-theta*x', 'theta': [1, 0, -.5]})
