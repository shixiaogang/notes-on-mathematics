from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ccode-common"))
from ccode_fig import *
# Lossless source-channel transmission of a Bern(theta) source over BSC(0.1).
# Blue: the largest ratio r = k/n (source symbols per channel use) allowed by r H(S) < C, i.e. r < C / h2(theta).
# Yellow dashed: sending the raw bits through a channel code without compression, r < C.  Red: theta = 0.1.
C = float(1-h2(P))
th = np.linspace(.005, .5, 400)
r = C/h2(th)
fig, ax = figure(width_mm=86, height_mm=52)
panel(fig, left=.13, right=.96, top=.96, bottom=.18)
ax.plot(th, r, color=BLUE, lw=1.4)
ax.axhline(C, color=YELLOW, lw=1.4, ls=DASH)
dot(ax, .1, C/float(h2(.1)))
lab(ax, .115, C/float(h2(.1))+.08, r'$1.13$', RED)
lab(ax, .25, C+.1, '不压缩', YELLOW); lab(ax, .33, C+.1, r'$C=0.531$', YELLOW); lab(ax, .06, 2.3, r'$C/H(S)$', BLUE)
ax.set_xlim(0, .5); ax.set_ylim(0, 3); ax.set_yticks([0, 1, 2, 3])
ax.set_xlabel(r'$\theta$', labelpad=1); ax.set_ylabel(r'$r$', labelpad=1)
save(fig, HERE, 'figure', {'C': C, 'H_0.1': float(h2(.1)), 'r_max_0.1': C/float(h2(.1))})
