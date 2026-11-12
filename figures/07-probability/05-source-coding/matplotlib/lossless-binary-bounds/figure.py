from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"lossless-common"))
from lossless_fig import *
# Bernoulli(theta) source: entropy H(theta) (blue), the bound H+1 (purple dashed), the average length of the
# Shannon code with lengths ceil(-log2 p) (yellow), and the optimal single-symbol code length 1 (green).
# Red dot: theta = 0.1 for which H = 0.469 and Shannon length = 1.3.
t = np.linspace(.00037, .99963, 2000)  # grid avoids theta = 1/2, where the Shannon code has the isolated value 1
Hb = -(t*np.log2(t)+(1-t)*np.log2(1-t))
Ls = t*np.ceil(-np.log2(t)) + (1-t)*np.ceil(-np.log2(1-t))
fig, ax = figure(width_mm=92, height_mm=52)
panel(fig, left=.11, right=.97, bottom=.2, top=.95)
ax.plot(t, Hb+1, color=PURPLE, lw=1.1, ls=DASH)
ax.plot(t, Ls, color=YELLOW, lw=1.5)
ax.plot(t, np.ones_like(t), color=GREEN, lw=1.4)
ax.plot(t, Hb, color=BLUE, lw=1.4)
th = .1; h1 = -(th*np.log2(th)+(1-th)*np.log2(1-th)); l1 = th*4+(1-th)*1
dot(ax, th, h1); dot(ax, th, l1)
ax.set_xlim(0, 1); ax.set_ylim(0, 2.6); ax.set_yticks([0, 1, 2])
lab(ax, .5, 2.08, r'$H(\theta)+1$', PURPLE, ha='center')
lab(ax, .5, .78, r'$H(\theta)$', BLUE, ha='center')
lab(ax, .2, 1.62, 'Shannon码', YELLOW, ha='center')
lab(ax, .78, 1.06, '最优码', GREEN, ha='center')
lab(ax, th+.02, h1-.17, '%.3f' % h1, RED); lab(ax, th+.03, l1+.08, '%.1f' % l1, RED)
ax.set_xlabel(r'$\theta$', labelpad=1); ax.set_ylabel('bit', labelpad=1)
save(fig, HERE, 'figure', {'theta': th, 'H': h1, 'L_shannon': l1})
