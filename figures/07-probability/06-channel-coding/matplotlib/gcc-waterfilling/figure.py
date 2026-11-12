from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# (a) Water filling for parallel Gaussian channels with noise levels sigma_j^2 = (1, 2, 5) and total power 5.
#     Yellow: the floor sigma_j^2; blue: power P_j = (nu - sigma_j^2)^+ on top; red line: water level nu = 4;
#     powers (3, 2, 0).
# (b) Reverse water filling (rate distortion of independent Gaussian components) with variances (1, 2, 5) and
#     total distortion 5: distortion D_j = min(theta, sigma_j^2) (red fill), theta = 2 (red line); the part of the
#     variance above theta (blue outline) is what must be described; rates (0, 0, 0.661) bit.
s = np.array([1., 2., 5.]); x = np.arange(3)
fig, axs = figure(width_mm=106, height_mm=46, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.27, wspace=.25)
ax = axs[0]
nu, p = waterfill(s, 5.0)
ax.bar(x, s, width=.9, color=YELLOW_FILL, edgecolor=YELLOW, lw=.7)
ax.bar(x, p, bottom=s, width=.9, color=BLUE_FILL, edgecolor=BLUE, lw=.7)
ax.plot([-.55, 2.55], [nu, nu], color=RED, lw=1.2)
for j in range(3):
    if p[j] > 0:
        lab(ax, j, s[j]+p[j]/2, '%g' % p[j], BLUE, ha='center', va='center')
    lab(ax, j, s[j]/2, '%g' % s[j], YELLOW, ha='center', va='center')
lab(ax, 2.58, nu, r'$\nu=%g$' % nu, RED, va='center')
ax = axs[1]
th = 2.0; D = np.minimum(th, s); rate = .5*np.log2(np.maximum(s/th, 1))
ax.bar(x, s, width=.9, color='white', edgecolor=BLUE, lw=.7)
ax.bar(x, D, width=.9, color=RED_FILL, edgecolor=RED, lw=.7)
ax.plot([-.55, 2.55], [th, th], color=RED, lw=1.2)
for j in range(3):
    lab(ax, j, D[j]/2, '%g' % D[j], RED, ha='center', va='center')
    if s[j] > th:
        lab(ax, j, (s[j]+th)/2, '%.3f bit' % rate[j], BLUE, ha='center', va='center')
lab(ax, 2.58, th, r'$\theta=%g$' % th, RED, va='center')
for ax in axs:
    ax.set_xlim(-.6, 3.3); ax.set_ylim(0, 6)
    ax.set_xticks(x); ax.set_xticklabels([r'$j=1$', r'$j=2$', r'$j=3$']); ax.set_yticks([0, 2, 4, 6])
tags(fig, axs)
save(fig, HERE, 'figure', {'water level': float(nu), 'powers': [float(v) for v in p],
                            'theta': th, 'distortions': [float(v) for v in D], 'rates': [float(v) for v in rate]})
