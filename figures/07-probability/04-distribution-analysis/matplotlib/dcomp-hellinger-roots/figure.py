from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# (a) sqrt densities of P=N(0,1), Q=N(1.5,1); shaded area int sqrt(pq) = B = exp(-1.5^2/8) = 0.7548.
# (b) running example: sqrt(p), sqrt(q) are unit vectors in R^3; angle theta with cos(theta)=B=0.9243,
#     chord length ||sqrt p - sqrt q||_2 = sqrt(2) d_H = sqrt(2(1-B)).  Drawn in the plane they span.
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.07, right=.98, top=.95, bottom=.26, wspace=.2)
ax = axs[0]
x = np.linspace(-3.5, 5, 1200)
sp, sq = np.sqrt(npdf(x)), np.sqrt(npdf(x, 1.5))
ax.fill_between(x, 0, np.sqrt(npdf(x)*npdf(x, 1.5)), color=BLUE_FILL, lw=0)
ax.plot(x, sp, color=BLUE, lw=1.4)
ax.plot(x, sq, color=YELLOW, lw=1.6)
lab(ax, -2.1, .52, r'$\sqrt{p}$', BLUE, ha='center', fontsize=8)
lab(ax, 3.6, .52, r'$\sqrt{q}$', YELLOW, ha='center', fontsize=8)
lab(ax, .75, .2, r'$\sqrt{pq}$', BLUE, ha='center')
ax.set_xlim(-3.5, 5); ax.set_ylim(0, .72); ax.set_yticks([0, .3, .6])
axlab(ax, '$x$', None)
B = float(np.sqrt(P_EX*Q_EX).sum()); th = math.acos(B)
ax = axs[1]
t = np.linspace(-.15, th+.45, 200)
ax.plot(np.cos(t), np.sin(t), color=STROKE, lw=.85, ls=DOT)
a = .55
ax.annotate('', xy=(1, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=BLUE, lw=1.3, mutation_scale=8))
ax.annotate('', xy=(math.cos(th), math.sin(th)), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=YELLOW, lw=1.5, mutation_scale=8))
ax.plot([1, math.cos(th)], [0, math.sin(th)], color=RED, lw=1.4)
tt = np.linspace(0, th, 50)
ax.plot(a*np.cos(tt), a*np.sin(tt), color=STROKE, lw=.85)
lab(ax, a*math.cos(th/2)+.04, a*math.sin(th/2)-.02, r'$\theta$', INK, va='center')
lab(ax, 1.02, -.07, r'$\sqrt{\mathbf{p}}$', BLUE, ha='left', va='top', fontsize=8)
lab(ax, math.cos(th)-.06, math.sin(th)+.08, r'$\sqrt{\mathbf{q}}$', YELLOW, ha='right', fontsize=8)
lab(ax, 1.06, .17, r'$\sqrt{2}\,d_{\mathrm{H}}$', RED, ha='left')
lab(ax, .06, .5, r'$\cos\theta=B$', INK, ha='left')
ax.set_aspect('equal'); ax.set_xlim(-.1, 1.45); ax.set_ylim(-.22, .82)
ax.axis('off')
tags(fig, axs)
save(fig, HERE, 'figure', {'B_gauss': float(math.exp(-1.5**2/8)), 'B_table': B, 'theta_deg': math.degrees(th),
                            'chord': math.sqrt(2*(1-B))})
