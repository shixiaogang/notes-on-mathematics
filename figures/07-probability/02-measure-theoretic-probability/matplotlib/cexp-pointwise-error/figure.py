"""Squared prediction error per cell of the sensor table, predicting Y with
E[Y|H] (H=sigma(1{X=2}), yellow) and E[Y|X] (green). Seven cells of positive probability.
Red marks: cells (0,1) and (1,0) where the finer information gives a larger error.
Averages weighted by P: 43/105 = 0.410 (yellow dashed) and 1/3 (green dashed)."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/'cexp-common'))
from common import *

Yv = np.array([[y for y in range(3)] for x in range(3)], float)
mH = cond_mean(Yv, lambda x, y: x == 2); mX = cond_mean(Yv, lambda x, y: x)
cells = [(x, y) for x in range(3) for y in range(3) if P[x, y] > 0]
eH = np.array([(Yv[c] - mH[c])**2 for c in cells]); eX = np.array([(Yv[c] - mX[c])**2 for c in cells])
w = np.array([P[c] for c in cells])
fig, ax = figure(width_mm=100, height_mm=48)
k = np.arange(len(cells))
ax.bar(k - 0.18, eH, width=0.34, color=YELLOW_FILL, edgecolor=YELLOW, lw=0.9)
ax.bar(k + 0.18, eX, width=0.34, color=GREEN_FILL, edgecolor=GREEN, lw=0.9)
for i in range(len(cells)):
    if eX[i] > eH[i] + 1e-12:
        ax.scatter([k[i] + 0.18], [eX[i] + 0.09], marker='v', s=16, color=RED, zorder=4)
avgH = float((w*eH).sum()); avgX = float((w*eX).sum())
ax.axhline(avgH, color=YELLOW, lw=1.2, ls='--'); ax.axhline(avgX, color=GREEN, lw=1.2, ls='--')
ax.text(6.55, avgH + 0.03, f'{avgH:.3f}', fontsize=7, color=YELLOW, ha='right', va='bottom')
ax.text(6.55, avgX - 0.03, f'{avgX:.3f}', fontsize=7, color=GREEN, ha='right', va='top')
ax.set_xticks(k); ax.set_xticklabels([f'({x},{y})' for x, y in cells], fontsize=7.5)
ax.set_xlim(-0.6, 6.6); ax.set_ylim(0, 1.85)
ax.set_xlabel('$(x,y)$', labelpad=1)
save(fig, Path(__file__).resolve().parent, 'figure', {'cells': cells, 'err_H': list(eH), 'err_X': list(eX), 'avg_H': avgH, 'avg_X': avgX})
