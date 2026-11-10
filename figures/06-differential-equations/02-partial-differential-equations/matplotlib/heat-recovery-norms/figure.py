from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Norm distance to the data as t->0: box (p=1,2,inf) and a continuous tent (sup norm).
fig, ax = figure(width_mm=84, height_mm=56)
panel(fig, left=.125, right=.98, bottom=.18, top=.97)
xx = np.linspace(-3, 3, 240001); dx = xx[1]-xx[0]; T = np.logspace(-4.5, -1, 22)
b = (np.abs(xx) < .5)*1.
def tentline_u(x, t):
    # tent on [-1,1]: u0=max(1-|x|,0), exact via integrated erfc
    F = lambda z: z*erf(z/(2*np.sqrt(t)))+2*np.sqrt(t/pi)*np.exp(-z**2/(4*t))
    return .5*(F(x+1)-2*F(x)+F(x-1))
l1, l2, li, lt = [], [], [], []
tu = np.maximum(1-np.abs(xx), 0)
for t in T:
    e = box(xx, t)-b
    l1.append(np.abs(e).sum()*dx); l2.append(np.sqrt((e**2).sum()*dx)); li.append(np.abs(e).max())
    lt.append(np.abs(tentline_u(xx[::8], t)-tu[::8]).max())
ax.loglog(T, l1, color=BLUE, lw=1.4); ax.loglog(T, l2, color=GREEN, lw=1.4); ax.loglog(T, li, color=RED, lw=1.4); ax.loglog(T, lt, color=YELLOW, lw=1.4)
lab(ax, 2e-3, .6, '方框，L∞', RED, ha='center', va='bottom'); lab(ax, 1e-4, .03, r'$L^1$', BLUE, ha='center', va='bottom'); lab(ax, 3e-4, .16, r'$L^2$', GREEN, ha='center', va='bottom')
lab(ax, 1.6e-3, 8e-3, '三角形，L∞', YELLOW, ha='left', va='top')
ax.set_xlim(2.5e-5, .12); ax.set_ylim(2e-3, 1.6); ax.minorticks_off(); ax.set_xticks([1e-4, 1e-3, 1e-2, 1e-1]); ax.set_xticklabels(['$10^{-4}$', '$10^{-3}$', '$10^{-2}$', '$10^{-1}$']); ax.set_yticks([1, 1e-1, 1e-2]); ax.set_yticklabels(['1', '$10^{-1}$', '$10^{-2}$'])
axlab(ax, '$t$', r'$\| u(\cdot,t)-u_0\|_p$')
save(fig, HERE, 'figure', {'l1(.01)': float(np.abs(box(xx, .01)-b).sum()*dx), '4sqrt(t/pi)': float(4*np.sqrt(.01/pi)), 'tent peak drop t=.01': float(1-tentline_u(np.array(0.), .01)), 'sqrt(t/pi)': float(np.sqrt(.01/pi))})
print(np.abs(box(xx, .01)-b).sum()*dx, 4*np.sqrt(.01/pi), 1-tentline_u(np.array(0.), .01), np.sqrt(.01/pi))
