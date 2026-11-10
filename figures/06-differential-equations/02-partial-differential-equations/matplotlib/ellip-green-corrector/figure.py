from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"ellip-common"))
from ellip_fig import *
y = .3
fig, ax = figure(width_mm=86, height_mm=52)
panel(fig, left=.12, right=.97, top=.96, bottom=.16)
Phi = -np.abs(X-y)/2
h = -y/2+X*(-(1-y)/2+y/2)
G = Phi-h
ax.axhline(0, color=STROKE, lw=.6)
ax.plot(X, Phi, color=YELLOW, lw=1.5); ax.plot(X, h, color=PURPLE, lw=1.3, ls=DASH); ax.plot(X, G, color=BLUE, lw=1.4)
dot(ax, 0, -y/2, RED); dot(ax, 1, -(1-y)/2, RED); dot(ax, 0, 0, BLUE, 3.8); dot(ax, 1, 0, BLUE, 3.8)
lab(ax, .31, .225, r'$G(x,y)$', BLUE); lab(ax, .63, -.12, r'$\Phi(x-y)$', YELLOW, va='bottom'); lab(ax, .42, -.26, r'$h(x)$', PURPLE, va='top')
ax.set_xlim(-.02, 1.02); ax.set_ylim(-.4, .27); ax.set_xticks([0, y, 1]); ax.set_xticklabels(['0', '$y$', '1']); ax.set_yticks([-.3, 0, .2]); hat01(ax)
save(fig, HERE, 'figure', {'y': y, 'G=Phi-h': 'x(1-y) for x<=y', 'h': 'affine with h(0)=Phi(-y), h(1)=Phi(1-y)'})
