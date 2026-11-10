from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"odenum-common"))
from odenum_common import *

LAM = 50.0
def exact_stiff(t):
    t = np.asarray(t, float)
    return np.exp(-t), LAM/(LAM-1)*(np.exp(-t)-np.exp(-LAM*t))
def g2(t, x):
    return np.array([-x[0], LAM*(x[0]-x[1])])

# Target: backward Euler and trapezoid on the stiff system with h=0.2.
h = .2; T = 3.0; n = int(round(T/h))
a = LAM*h
def run(kind):
    x1, x2 = 1.0, 0.0; xs = [(x1, x2)]
    for k in range(n):
        if kind == 'be':
            y1 = x1/(1+h); y2 = (x2+a*y1)/(1+a)
        else:
            y1 = x1*(1-h/2)/(1+h/2); y2 = ((1-a/2)*x2+a/2*(x1+y1))/(1+a/2)
        x1, x2 = y1, y2; xs.append((x1, x2))
    return np.array(xs)
tt = np.linspace(0, T, 500); tg = h*np.arange(n+1)
fig, ax = figure(width_mm=112, height_mm=52, ncols=2, sharey=True)
for a_, kind, c, cap in zip(ax, ('be', 'tr'), (GREEN, PURPLE), ('(a) 后向 Euler', '(b) 梯形方法')):
    a_.plot(tt, exact_stiff(tt)[1], color=BLUE, lw=1.4)
    a_.plot(tg, run(kind)[:, 1], 'o-', color=c, lw=.95, ms=2.8)
    a_.plot([0], [0], 'o', color=RED, ms=4.5, zorder=5, clip_on=False)
    a_.set_xlabel(r'$t$'); a_.set_xlim(0, T)
    panel(a_, cap, -.3)
ax[0].set_ylabel(r'$x_2$')
save(fig, Path(__file__).resolve().parent, 'figure', {'be': run('be')[:4].tolist(), 'tr': run('tr')[:4].tolist()})
