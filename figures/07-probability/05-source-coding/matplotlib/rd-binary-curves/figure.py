"""Binary rate-distortion functions R(D)=h2(p)-h2(D), 0<=D<=min(p,1-p), Hamming distortion,
p=0.1 (yellow), 0.3 (blue, running example), 0.5 (purple). Red: D_max=min(p,1-p); green: (0.1,0.4123)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

fig, ax = figure(width_mm=86, height_mm=52)
D = np.linspace(0, .58, 600)
for p, c, y in ((.1, YELLOW, .5), (.3, BLUE, .9), (.5, PURPLE, 1.0)):
    ax.plot(D, rd_binary(D, p), color=c, lw=1.5 if c == YELLOW else 1.4)
    dot(ax, p, 0, RED)
    lab(ax, p+.008, .035, f'$p={p}$', c, ha='left', va='bottom', zorder=7,
        bbox=dict(facecolor='white', edgecolor='none', pad=.6))
dot(ax, .1, float(rd_binary(.1)), GREEN, ms=4.6)
ax.set_xlim(0, .58); ax.set_ylim(0, 1.12)
ax.set_xticks([0, .1, .2, .3, .4, .5])
axlab(ax, '$D$', '$R(D)$ (bit)')
save(fig, HERE, 'figure', {'h2': {p: h2(p) for p in (.1, .3, .5)}, 'R(0.1;0.3)': float(rd_binary(.1))})
