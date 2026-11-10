from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"heat-common"))
from heat_fig import *
# Whole-line convolution ignores walls; odd reflections restore the zero boundary values.
fig, axes = figure(width_mm=112, height_mm=50, ncols=2)
panel(fig, left=.105, wspace=.26, bottom=.27)
yy = np.linspace(-3, 4, 28001); dy = yy[1]-yy[0]; t = .05
xx = np.linspace(-.6, 1.6, 221)
def odd(y):
    z = np.mod(y, 2.); return np.where(z <= 1, tent(z), -tent(z-1))
ax = axes[0]; u0 = np.where((yy >= 0) & (yy <= 1), tent(np.clip(yy, 0, 1)), 0.)
W = np.array([(gauss(x-yy, t)*u0).sum()*dy for x in xx]); ins = (xx >= 0) & (xx <= 1)
ax.plot(xx, W, color=YELLOW, lw=1.4); ax.plot(xx[ins], uD(xx[ins], t), color=BLUE, lw=1.4)
dot(ax, 0, 0, RED); dot(ax, 1, 0, RED); dot(ax, 0, W[np.argmin(np.abs(xx))], YELLOW, ms=4)
ax.axvline(0, color=STROKE, lw=.9); ax.axvline(1, color=STROKE, lw=.9); ax.set_xlim(-.6, 1.6); ax.set_ylim(-.01, .32); ax.set_xticks([0, 1]); ax.set_yticks([0, .1, .2, .3]); axlab(ax, yl='$u(x,0.05)$')
lab(ax, .5, .262, '区间解', BLUE, ha='center'); lab(ax, 1.08, .085, '实轴卷积', YELLOW, ha='left')
ax = axes[1]; zz = np.linspace(-2, 3, 1500)
ax.plot(zz, odd(zz), color=RED, lw=1.3)
Z = np.array([(gauss(x-yy, t)*odd(yy)).sum()*dy for x in zz[::5]])
ax.plot(zz[::5], Z, color=BLUE, lw=1.4); ax.axhline(0, color=STROKE, lw=.6)
for b in (-2, -1, 0, 1, 2, 3): ax.axvline(b, color=STROKE, lw=.6, ls=DOT)
dot(ax, 0, 0, RED); dot(ax, 1, 0, RED)
ax.set_xlim(-2, 3); ax.set_ylim(-.56, .56); ax.set_xticks([-2, -1, 0, 1, 2, 3]); ax.set_yticks([-.5, 0, .5]); axlab(ax)
tags(fig, axes)
save(fig, HERE, 'figure', {'wholeline u(0,.05)': float(W[np.argmin(np.abs(xx))]), 'image u(.5,.05)': float((gauss(.5-yy, t)*odd(yy)).sum()*dy), 'series': float(uD(.5, t)[0])})
print(W[np.argmin(np.abs(xx))], (gauss(.5-yy, t)*odd(yy)).sum()*dy, uD(.5, t)[0])
