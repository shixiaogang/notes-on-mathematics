from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'quant-common'))
from quant_fig import *
# Infinite mid-tread quantizer, step 1. (a) Conditional mean squared error given X = x:
# no dither (x - round x)^2 (blue), subtractive uniform dither 1/12 (green), non-subtractive uniform dither s(1-s),
# s = x - floor x (yellow). (b) Errors of the subtractive scheme at x = 0.3 for 20000 dither values
# U ~ Unif[-1/2,1/2) (seed 4): histogram (green) and the uniform density (blue); red line: undithered error -0.3.
x = np.linspace(-1, 1, 2001)
q = np.floor(x + .5); s = x - np.floor(x)
fig, (a, b) = figure(width_mm=108, height_mm=50, ncols=2)
panel(fig, left=.08, right=.98, bottom=.27, top=.95, wspace=.3)
a.plot(x, (x-q)**2, color=BLUE, lw=1.4); a.plot(x, s*(1-s), color=YELLOW, lw=1.6)
a.axhline(1/12, color=GREEN, lw=1.4)
lab(a, -.98, .27, '不抖动', BLUE); lab(a, .25, .265, '非减性', YELLOW); lab(a, .55, .1, '减性', GREEN)
a.set_xlim(-1, 1); a.set_ylim(0, .3); a.set_xlabel('$x$', labelpad=1)
rng = np.random.default_rng(4); U = rng.random(20000) - .5; X0 = .3
E = np.floor(X0 + U + .5) - U - X0
b.hist(E, bins=20, range=(-.5, .5), density=True, color=GREEN_FILL, edgecolor=GREEN, lw=.6)
b.plot([-.5, .5], [1, 1], color=BLUE, lw=1.4)
b.axvline(-.3, color=RED, lw=1.2)
lab(b, -.28, 1.35, '$-0.3$', RED)
b.set_xlim(-.6, .6); b.set_ylim(0, 1.5); b.set_xlabel('误差', labelpad=1)
tags(fig, (a, b))
save(fig, HERE, 'figure', {'mean_E': float(E.mean()), 'mse_E': float((E**2).mean()), 'n': 20000, 'seed': 4})
