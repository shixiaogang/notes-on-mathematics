"""Triangle-model kernel K(y,.)=Unif(y,1): (a) CDFs t->K(y,[0,t]) for y=0,0.3,0.6;
(b) y->K(y,A) for A=[0,1/2] and A=[3/4,1]."""
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"cdis-common"))
from common import *
from matplotlib.colors import LinearSegmentedColormap
HERE = Path(__file__).resolve().parent
fig, (a, b) = figure(width_mm=104, height_mm=46, ncols=2)
t = np.linspace(0, 1, 401)
for (yv, c), (tx, ty) in zip(((0.0, BLUE), (0.3, YELLOW), (0.6, PURPLE)), ((0.04, 0.30), (0.40, 0.14), (0.70, 0.06))):
    F = np.clip((t - yv)/(1 - yv), 0, 1)
    a.plot(t, F, color=c, lw=1.4)
    a.text(tx, ty, f'$y={yv:g}$', fontsize=7.5, color=INK)
a.set_xlim(0, 1); a.set_ylim(0, 1.05); a.set_xticks([0, 0.3, 0.6, 1]); a.set_yticks([0, 0.5, 1])
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$K(y,[0,t])$')
y = np.linspace(0, 0.98, 400)
b.plot(y, tri_kernel(y, 0, 0.5), color=BLUE, lw=1.4)
b.plot(y, tri_kernel(y, 0.75, 1), color=YELLOW, lw=1.6)
b.text(0.20, 0.06, '$A=[0,1/2]$', fontsize=7.5)
b.text(0.76, 0.86, '$A=[3/4,1]$', fontsize=7.5)
b.set_xlim(0, 1); b.set_ylim(0, 1.05); b.set_xticks([0, 0.5, 0.75, 1]); b.set_yticks([0, 0.5, 1])
b.set_xlabel('$y$', labelpad=1); b.set_ylabel('$K(y,A)$')

tags(fig, (a, b,), ('(a)', '(b)',))
save(fig, HERE, 'figure', {'kernel': 'Unif(y,1)', 'ys': [0, 0.3, 0.6]})
