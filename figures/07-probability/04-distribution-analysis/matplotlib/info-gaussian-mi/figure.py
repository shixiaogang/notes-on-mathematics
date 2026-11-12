from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/'info-common'))
from info_fig import *
# Standard bivariate normal with correlation rho.
# (a) rho = 0.9: density level lines (blue); red line x = 1 and the conditional density
#     N(0.9, 0.19) of Y given X = 1 drawn sideways (green), marginal N(0,1) of Y (yellow).
# (b) h(Y) = 1.419 (purple dashed), h(Y|X) = 0.5 ln(2 pi e (1-rho^2)) (blue),
#     I(X;Y) = -0.5 ln(1-rho^2) (green) versus rho.
fig, (a, b) = figure(width_mm=112, height_mm=52, ncols=2)
panel(fig, left=.07, right=.98, bottom=.27, top=.95, wspace=.28)
r = .9
g = np.linspace(-3, 3, 300); X, Y = np.meshgrid(g, g)
Z = np.exp(-(X*X-2*r*X*Y+Y*Y)/(2*(1-r*r)))/(2*math.pi*math.sqrt(1-r*r))
a.contour(X, Y, Z, levels=[.02, .1, .3], colors=[BLUE], linewidths=.8)
a.axvline(1, color=RED, lw=1.0, zorder=5)
y = np.linspace(-3, 3, 400); s2 = 1-r*r
cd = np.exp(-(y-r)**2/(2*s2))/math.sqrt(2*math.pi*s2)
md = np.exp(-y*y/2)/math.sqrt(2*math.pi)
a.plot(1+cd*.8, y, color=GREEN, lw=1.3); a.plot(1+md*.8, y, color=YELLOW, lw=1.2)
a.set_xlim(-3, 3); a.set_ylim(-3, 3); a.set_aspect('equal'); axlab(a, '$x$', '$y$')
a.annotate(r'$f_{Y\mid X}(\cdot\mid 1)$', xy=(1.62, .6), xytext=(1.75, -.9), color=GREEN, fontsize=7.5, arrowprops=dict(arrowstyle='-', color=GREEN, lw=.6)); lab(a, 1.3, -2.3, '$f_Y$', YELLOW)
rho = np.linspace(0, .995, 400)
hY = .5*math.log(2*math.pi*math.e)
b.axhline(hY, color=PURPLE, lw=.85, ls=DASH)
b.plot(rho, .5*np.log(2*math.pi*math.e*(1-rho**2)), color=BLUE, lw=1.4)
b.plot(rho, -.5*np.log(1-rho**2), color=GREEN, lw=1.4)
b.axhline(0, color=STROKE, lw=.6)
dot(b, .9, .5*math.log(2*math.pi*math.e*.19)); dot(b, .9, -.5*math.log(.19))
lab(b, .05, hY+.12, '$h(Y)$', PURPLE); lab(b, .05, 1.1, r'$h(Y\mid X)$', BLUE); lab(b, .05, .15, '$I(X;Y)$', GREEN)
b.set_xlim(0, 1); b.set_ylim(-1.5, 2.6); axlab(b, r'$\rho$', 'nat')
tags(fig, (a, b))
save(fig, HERE, 'figure', {'rho': r, 'h(Y|X)': .5*math.log(2*math.pi*math.e*.19), 'I': -.5*math.log(.19), 'h(Y)': hY})
