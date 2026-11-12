from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'dcomp-common'))
from common import *
# P=delta_0, Q=delta_h, g(x)=exp(-x^2/2) = k_1(x,0): osc(g)=1, Lip(g)=exp(-1/2), ||g||_H=1 (sigma=1).
# true |E_P g - E_Q g| = 1-exp(-h^2/2) (blue); bounds: TV: osc*d_TV = 1 (purple),
# W1: Lip*h (yellow), MMD: ||g||_H * sqrt(2-2exp(-h^2/2)) (red, dashed).
fig, ax = figure(width_mm=88, height_mm=54)
h = np.linspace(0, 3, 500)
ax.plot(h, 1-np.exp(-h**2/2), color=BLUE, lw=1.4)
ax.plot(h[1:], np.ones_like(h[1:]), color=PURPLE, lw=1.4)
ax.plot(h, math.exp(-.5)*h, color=YELLOW, lw=1.6)
ax.plot(h, np.sqrt(2-2*np.exp(-h**2/2)), color=RED, lw=1.3, ls=DASH)
lab(ax, 2.95, .86, '真实差', BLUE, ha='right', va='top')
lab(ax, 2.95, 1.04, 'TV', PURPLE, ha='right')
lab(ax, 2.3, 1.56, '$W_1$', YELLOW, ha='right')
lab(ax, 2.95, 1.45, 'MMD', RED, ha='right')
ax.set_xlim(0, 3); ax.set_ylim(0, 1.7); ax.set_xticks([0, 1, 2, 3]); ax.set_yticks([0, .5, 1, 1.5])
axlab(ax, '$h$', None)
save(fig, HERE, 'figure', {'lip': math.exp(-.5), 'h=0.5': [1-math.exp(-.125), math.exp(-.5)*.5, math.sqrt(2-2*math.exp(-.125))]})
