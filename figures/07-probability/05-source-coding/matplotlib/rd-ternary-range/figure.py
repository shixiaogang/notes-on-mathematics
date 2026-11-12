"""Ternary example: X in {0,1,2} with p=(0.3,0.4,0.3), reconstructions {0,2}, d=(x-xhat)^2.
D_min=0.4, D_max=1.6, R(D_min)=0.6 bit, H(X)=1.571 bit. Curve traced by Blahut-Arimoto
(400 values of s, 3000 iterations each, uniform start)."""
from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'rd-common'))
from common import *

px = np.array([.3, .4, .3]); d = np.array([[0, 4], [1, 1], [4, 0.]])
Ds, Rs = [], []
for s in np.concatenate([np.linspace(0.05, 3, 120), np.linspace(3, 40, 80)]):
    h = blahut_arimoto(px, d, s, iters=3000, tol=1e-10)[-1]
    Ds.append(h['D']); Rs.append(h['I'])
o = np.argsort(Ds); Ds = np.array(Ds)[o]; Rs = np.array(Rs)[o]
Ds = np.concatenate([Ds, [1.6, 2.0]]); Rs = np.concatenate([Rs, [0, 0]])
Hx = float(-np.sum(px*np.log2(px)))
fig, ax = figure(width_mm=92, height_mm=50)
ax.axvspan(0, .4, color=RED_FILL, lw=0, zorder=0)
ax.plot(Ds, Rs, color=BLUE, lw=1.4, zorder=3)
ax.axhline(Hx, color=PURPLE, lw=.9, ls=DASH)
ax.axvline(.4, color=STROKE, lw=.7, ls=DOT); ax.axvline(1.6, color=STROKE, lw=.7, ls=DOT)
dot(ax, .4, .6, RED); dot(ax, 1.6, 0, RED)
lab(ax, .2, .8, '不可行', RED, ha='center')
lab(ax, .45, .63, '$R(D_{\\min})=0.6$', INK, ha='left')
lab(ax, 1.62, .07, '$D_{\\max}=1.6$', INK, ha='left')
lab(ax, 1.05, Hx-.16, '$H(X)=1.571$', PURPLE, ha='left')
ax.set_xlim(0, 2.0); ax.set_ylim(0, 1.75)
ax.set_xticks([0, .4, .8, 1.2, 1.6, 2.0])
axlab(ax, '$D$', '$R(D)$ (bit)')
save(fig, HERE, 'figure', {'R_at_smallest_D': [float(Ds[0]), float(Rs[0])], 'H': Hx})
