from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) soft threshold S_tau(v), tau=1/2. (b) cyclic coordinate prox on 1/2||Ax-b||^2+|x1|+|x2|, A=[[1,1],[1,0],[0,1]], b=(4,2,-1), x0=(3,4).
fig, (a, b2) = figure(width_mm=112, height_mm=62, ncols=2)
panel(fig, .115, .985, .97, .22, wspace=.27)
v = np.linspace(-2, 2, 401); S = np.sign(v)*np.maximum(abs(v)-.5, 0)
a.plot(v, v, color=MUTED, lw=.85, ls=(0, (3, 2))); a.plot(v, S, color=GREEN, lw=1.4)
a.axhline(0, color=STROKE, lw=.5); a.axvline(0, color=STROKE, lw=.5)
a.set_xlabel('$v$', labelpad=1); a.set_ylabel(r'$S_\tau(v)$', labelpad=1); a.set_xlim(-2, 2); a.set_ylim(-1.6, 1.6)
A = np.array([[1., 1], [1, 0], [0, 1]]); bb = np.array([4., 2, -1]); gam = 1.
F = lambda X, Y: .5*((X+Y-4)**2+(X-2)**2+(Y+1)**2)+gam*(abs(X)+abs(Y))
x = np.array([3., 4]); P = [x.copy()]; L = (A**2).sum(0); Vals = [float(F(*x))]
for k in range(8):
    i = k % 2; r = A@x-bb; t = x[i]-A[:, i]@r/L[i]; x[i] = np.sign(t)*max(abs(t)-gam/L[i], 0); P.append(x.copy()); Vals.append(float(F(*x)))
X, Y = np.meshgrid(np.linspace(-.8, 4, 700), np.linspace(-1.2, 4.6, 700))
b2.contour(X, Y, F(X, Y), levels=[3.4, 4, 5, 7, 10, 14, 19, 25], colors=[BLUE], linewidths=.65)
path(b2, P, GREEN); opt(b2, 2.5, 0)
b2.axhline(0, color=STROKE, lw=.5); b2.axvline(0, color=STROKE, lw=.5)
b2.text(3.08, 4.15, '$x^{(0)}$', fontsize=8, color=INK); b2.text(2.62, -.55, '$(2.5,0)$', fontsize=7.5, color=INK)
b2.set_xlabel('$x_1$', labelpad=1); b2.set_ylabel('$x_2$', labelpad=1); b2.set_aspect('equal'); b2.set_xlim(-.8, 4); b2.set_ylim(-1.2, 4.6)
tag(fig, a, '(a)'); tag(fig, b2, '(b)')
save(fig, HERE, 'figure', {'path': [p.tolist() for p in P], 'F': Vals})
print([p.tolist() for p in P], Vals)
