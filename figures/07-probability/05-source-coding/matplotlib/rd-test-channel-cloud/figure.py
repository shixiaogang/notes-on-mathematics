"""Cloud of (E d, I) for all binary test channels q(1|0)=a, q(0|1)=b on a 61x61 grid,
source Bern(0.3), Hamming distortion. Lower envelope: R(D)=h2(0.3)-h2(D) (blue).
Red: forward flip a=b=0.1 (I=0.4558), optimal at D=0.1 (I=0.4123), constant 0 (D=0.3,I=0)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

p = P_SRC; px = np.array([1-p, p]); d = np.array([[0, 1], [1, 0.]])
g = np.linspace(0, 1, 61)
Ds, Is = [], []
for a in g:
    for b in g:
        q = np.array([[1-a, a], [b, 1-b]])
        Ds.append(exp_dist(px, q, d)); Is.append(mutual_info(px, q))
fig, ax = figure(width_mm=96, height_mm=54)
ax.plot(Ds, Is, 'o', ms=1.1, color=GREEN, mew=0, zorder=1)
D = np.linspace(0, .7, 400)
ax.plot(D, rd_binary(D), color=BLUE, lw=1.4, zorder=3)
ax.axvline(.1, color=RED, lw=.85, ls=DASH, zorder=2)
fwd = mutual_info(px, np.array([[.9, .1], [.1, .9]]))
r = .25; qopt = np.array([[1-r*.1/.7, r*.1/.7], [(1-r)*.1/.3, 1-(1-r)*.1/.3]])
opt = mutual_info(px, qopt)
dot(ax, .1, fwd, RED); dot(ax, .1, opt, RED); dot(ax, .3, 0, RED)
lab(ax, .115, fwd+.015, '逐位翻转', INK, ha='left')
lab(ax, .085, opt-.02, '最优', INK, ha='right')
lab(ax, .3, .07, '恒输出0', INK, ha='center')
ax.set_xlim(0, .72); ax.set_ylim(0, .92)
axlab(ax, '平均失真', '$I(X;\\hat X)$ (bit)')
save(fig, HERE, 'figure', {'forward_I': fwd, 'opt_I': opt, 'grid': 61})
