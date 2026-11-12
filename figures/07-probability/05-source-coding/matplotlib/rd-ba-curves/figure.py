"""(a) Blahut-Arimoto points (green) for Bern(0.3), Hamming, s from 1.4 to 8 (24 values, 4000 iterations
or certified gap <= 1e-10, uniform start) on the closed form R(D) (blue).
(b) Supporting lines R = F_s - s D (purple dashed) for s=2, log2 9, 5 touching the curve at D_s=1/(1+2^s)."""
from pathlib import Path
import sys
import math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

px = np.array([.7, .3]); d = np.array([[0, 1], [1, 0.]])
S = np.linspace(1.4, 8, 24)
pts = []
for s in S:
    h = blahut_arimoto(px, d, s, iters=4000, tol=1e-10)[-1]
    pts.append((h['D'], h['I']))
pts = np.array(pts)
fig, axs = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.09, right=.985, top=.95, bottom=.27, wspace=.3)
D = np.linspace(0, .34, 400)
for ax in axs:
    ax.plot(D, rd_binary(D), color=BLUE, lw=1.4, zorder=2)
    ax.set_xlim(0, .34); ax.set_ylim(0, .95)
    axlab(ax, '$D$', '码率（bit）')
axs[0].plot(pts[:, 0], pts[:, 1], 'o', ms=3, color=GREEN, mew=0, zorder=3)
ax = axs[1]
out = {}
for s in (2., math.log2(9), 5.):
    Ds = 1/(1+2**s); F = float(rd_binary(Ds))+s*Ds
    ax.plot(D, F-s*D, color=PURPLE, lw=.9, ls=DASH, zorder=1)
    dot(ax, Ds, float(rd_binary(Ds)), RED)
    out[f'{s:.4f}'] = [Ds, F]
lab(ax, .105, .45, '$s=\\log_2 9$', INK, ha='left')
lab(ax, .212, .17, '$s=2$', INK, ha='left')
lab(ax, .04, .67, '$s=5$', INK, ha='left')
tags(fig, axs)
save(fig, HERE, 'figure', {'ba_points': pts.round(6).tolist(), 'tangent': out})
