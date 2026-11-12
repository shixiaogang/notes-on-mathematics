from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X ~ Unif(0, theta), f(x) = x, J(theta) = theta/2.  theta = 1, h = 0.25.
# f p_theta = x/theta on (0, theta) (blue), f p_{theta+h} = x/(theta+h) on (0, theta+h) (yellow).
# Red fill: interior loss int_0^theta x (1/theta - 1/(theta+h)) dx = 0.1 (what the score sees, -> -1/2 per unit h);
# blue fill: boundary gain int_theta^{theta+h} x/(theta+h) dx = 0.225 (missed by the score, -> theta*p(theta)=1 per unit h).
th, h = 1.0, .25
fig, ax = figure(width_mm=80, height_mm=50)
panel(fig, left=.12, right=.97, bottom=.18, top=.96)
x0 = np.linspace(0, th, 200); x1 = np.linspace(th, th+h, 100)
ax.fill_between(x0, x0/th, x0/(th+h), color=RED_FILL, lw=0)
ax.fill_between(x1, x1/(th+h), 0, color=BLUE_FILL, lw=0)
ax.plot(np.r_[x0, th, th], np.r_[x0/th, 1/th, 0], color=BLUE, lw=1.4)
ax.plot(np.r_[x0, x1, th+h], np.r_[x0/(th+h), x1/(th+h), 0], color=YELLOW, lw=1.5)
loss = float(np.trapezoid(x0/th - x0/(th+h), x0)); gain = float(np.trapezoid(x1/(th+h), x1))
ax.annotate('减少 0.1', xy=(.78, .70), xytext=(.18, .78), color=RED, fontsize=7.5, va='center', arrowprops=dict(arrowstyle='-', color=RED, lw=.7, shrinkA=1, shrinkB=1)); lab(ax, 1.03, .3, '新增\n0.225', BLUE)
ax.set_xlim(0, 1.4); ax.set_ylim(0, 1.1); ax.set_xticks([0, .5, 1, 1.25]); ax.set_xticklabels(['0', '0.5', r'$\theta$', r'$\theta+h$'])
ax.set_yticks([0, .5, 1])
axlab(ax, r'$x$')
save(fig, HERE, 'figure', {'interior_loss': loss, 'boundary_gain': gain, 'net': gain-loss, 'J_diff': h/2})
