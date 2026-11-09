from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Isotropic pair along x(s)=(1-s,s)+delta*(1,1)/sqrt2: stationarity residual versus weighted (1/2,1/2) gradient residual.
s = np.linspace(0, 1, 401)
def res(s, dl):
    x = np.c_[1-s, s]+dl*np.array([1, 1])/np.sqrt(2); R = []; W = []
    for p in x:
        g1, g2 = p-A0, p-B0; _, g = minnorm2(g1, g2); R.append(np.linalg.norm(g)); W.append(np.linalg.norm(.5*(g1+g2)))
    return np.array(R), np.array(W)
fig, ax = figure(width_mm=96, height_mm=52)
setup(ax, (0, 1), (0, .8), [0, .25, .5, .75, 1], [0, .2, .4, .6, .8], '$s$', '残差')
for dl, ls in ((0, '-'), (.1, (0, (3, 2)))):
    R, W = res(s, dl); ax.plot(s, R, color=GREEN, lw=1.4, ls=ls, zorder=3); ax.plot(s, W, color=YELLOW, lw=1.7, ls=ls, zorder=2)
save(fig, HERE, 'figure', {'delta': [0, .1]})
