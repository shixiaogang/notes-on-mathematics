from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pgrad-common"))
from pgrad_fig import *
# X ~ N(theta,1), f_theta(x) = x^2 - theta x, J(theta) = 1 for all theta.  Around theta0 = 1:
# A(t) = E_{theta0}[f_t(X)] = theta0^2 + 1 - t theta0 (only the function moves), slope -theta0;
# B(t) = E_t[f_{theta0}(X)] = t^2 + 1 - theta0 t (only the distribution moves), slope 2 theta0 - theta0 = theta0.
th0 = 1.0
t = np.linspace(0, 2, 300)
A = th0**2 + 1 - t*th0; B = t**2 + 1 - th0*t; J = np.ones_like(t)
fig, ax = figure(width_mm=78, height_mm=48)
panel(fig, left=.13, right=.97, bottom=.17, top=.96)
ax.plot(t, A, color=YELLOW, lw=1.5); ax.plot(t, B, color=PURPLE, lw=1.4); ax.plot(t, J, color=BLUE, lw=1.4)
dot(ax, th0, 1.0)
lab(ax, 1.12, .12, '只动函数', YELLOW); lab(ax, 1.55, 1.95, '只动分布', PURPLE); lab(ax, .05, 1.08, r'$J(\theta)=1$', BLUE)
ax.set_xlim(0, 2); ax.set_ylim(0, 2.4); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, 1, 2])
axlab(ax, r'$\theta$')
save(fig, HERE, 'figure', {'slope_function_only': -th0, 'slope_distribution_only': th0, 'slope_total': 0.0})
