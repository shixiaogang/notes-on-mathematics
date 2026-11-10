from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/"build.sh").is_file() and (p/"tex/book.tex").is_file())
sys.path.insert(0, str(ROOT/"figures/06-differential-equations/02-partial-differential-equations/matplotlib/wave-common"))
from wave_common import *
# Target: energy accounting. (a) plucked string, (b) heat L2 energy for same data, (c) tent on the line.
fig, axs = figure(width_mm=112, height_mm=48, ncols=3)
ax = axs[0]; style(ax); t = np.linspace(0, 2, 801); n = np.arange(1, 6001, 2)
a = 4*np.sin(n*np.pi/2)/(n*np.pi)**2; w = n*np.pi; wt = np.outer(t, w)
V = .25*(np.cos(wt)**2*(w*a)**2).sum(1); K = .25*(np.sin(wt)**2*(w*a)**2).sum(1)
ax.plot(t, K, color=YELLOW, lw=1.6); ax.plot(t, V, color=PURPLE, lw=1.2); ax.plot(t, K+V, color=BLUE, lw=1.5)
ax.set_xlim(0, 2); ax.set_ylim(0, .6); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .25, .5]); sub(ax, 'a', '$t$')
ax = axs[1]; style(ax); t2 = np.linspace(0, .3, 601)
H = .25*(a[None, :]**2*np.exp(-2*np.outer(t2, w**2))).sum(1)
ax.plot(t2, H, color=PURPLE, lw=1.4)
ax.set_xlim(0, .3); ax.set_ylim(0, .025); ax.set_xticks([0, .1, .2, .3]); ax.set_yticks([0, .01, .02]); sub(ax, 'b', '$t$')
ax = axs[2]; style(ax); t3 = np.linspace(0, 2, 401); x = np.linspace(-4, 4, 32001)
Ks = []; Vs = []; Mx = []
for tt in t3:
    ut = .5*(-tent_d(x-tt)+tent_d(x+tt)); ux = .5*(tent_d(x-tt)+tent_d(x+tt))
    Ks.append(.5*np.sum(ut**2)*(x[1]-x[0])); Vs.append(.5*np.sum(ux**2)*(x[1]-x[0])); Mx.append(wave_tent(x, tt).max())
Ks, Vs = np.array(Ks), np.array(Vs)
ax.plot(t3, Ks, color=YELLOW, lw=1.6); ax.plot(t3, Vs, color=PURPLE, lw=1.2); ax.plot(t3, Ks+Vs, color=BLUE, lw=1.5)
ax.plot(t3, Mx, color=RED, lw=1.3, ls=(0, (3, 2)))
ax.set_xlim(0, 2); ax.set_ylim(0, 1.15); ax.set_xticks([0, 1, 2]); ax.set_yticks([0, .5, 1]); sub(ax, 'c', '$t$')
save(fig, HERE(__file__), 'figure', {'formula': 'modal K,V for pluck; heat (1/4) sum a_n^2 exp(-2 n^2 pi^2 t); tent K,V,max|u| by quadrature'})
