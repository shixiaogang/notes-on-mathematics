from pathlib import Path
import sys, math
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"gcc-common"))
from gcc_fig import *
# Output densities of Y = X + Z, Z ~ N(0,1), for three inputs with the same power E X^2 = 3:
#   binary X = +-sqrt(3) (yellow), uniform X on [-3,3] (purple), Gaussian X ~ N(0,3) (blue).
# Mutual information I = h(Y) - h(Z) by numerical integration on a fine grid: 0.845, 0.972, 1.000 bit.
P = 3.0
y = np.linspace(-11, 11, 44001); dy = y[1]-y[0]
fb = .5*(phi(y-math.sqrt(P))+phi(y+math.sqrt(P)))
a = math.sqrt(3*P)
Phi = np.vectorize(lambda u: .5*(1+math.erf(u/math.sqrt(2))))
fu = (Phi(y+a)-Phi(y-a))/(2*a)
fg = phi(y, P+1)
hz = .5*math.log2(2*math.pi*math.e)
I = [diff_entropy(f, dy)-hz for f in (fb, fu, fg)]
fig, ax = figure(width_mm=88, height_mm=48)
panel(fig, left=.05, right=.97, top=.95, bottom=.2)
ax.plot(y, fb, color=YELLOW, lw=1.5)
ax.plot(y, fu, color=PURPLE, lw=1.3)
ax.plot(y, fg, color=BLUE, lw=1.4)
ax.set_xlim(-6.5, 6.5); ax.set_ylim(0, .25); ax.set_yticks([]); ax.spines['left'].set_visible(False)
ax.set_xlabel(r'$y$', labelpad=1)
for k, (s, col) in enumerate((('二点输入', YELLOW), ('均匀输入', PURPLE), ('高斯输入', BLUE))):
    lab(ax, -6.3, .215-.025*k, s, col); lab(ax, -4.0, .215-.025*k, r'$I=%.3f$' % I[k], col)
save(fig, HERE, 'figure', {'I_binary': I[0], 'I_uniform': I[1], 'I_gauss': I[2], 'h_Z': hz})
