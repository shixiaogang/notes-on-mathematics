from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) f=1/2(u+v)^2 from (1,1): serial, parallel step 1 (oscillates), parallel step 1/2. (b) n=3, Q=(1-a)I+a11^T, a=.75, L_j=1: parallel with step 1 diverges.
fig, (a, b) = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .085, .985, .97, .25, wspace=.28)
U, V = np.meshgrid(np.linspace(-1.6, 1.6, 400), np.linspace(-1.6, 1.6, 400))
a.contour(U, V, .5*(U+V)**2, levels=[.02, .25, 1, 2, 3.5], colors=[BLUE], linewidths=.65)
a.annotate('', xy=(-.95, -.95), xytext=(.95, .95), arrowprops=dict(arrowstyle='<|-|>', color=YELLOW, lw=1.6, shrinkA=0, shrinkB=0))
a.annotate('', xy=(-.97, 1), xytext=(.97, 1), arrowprops=dict(arrowstyle='-|>', color=GREEN, lw=1.4, shrinkA=0, shrinkB=0))
a.plot([1, -1], [1, -1], 'o', color=YELLOW, ms=4.5, mew=0, zorder=5); a.plot([1, -1], [1, 1], 'o', color=GREEN, ms=4.5, mew=0, zorder=6); a.plot([0], [0], 'o', color=PURPLE, ms=4.5, mew=0, zorder=6)
a.text(1.08, 1.12, '$(1,1)$', fontsize=7.5, color=INK, ha='center'); a.text(-1.02, 1.17, '$(-1,1)$', fontsize=7.5, color=INK, ha='center'); a.text(-1.48, -1.3, '$(-1,-1)$', fontsize=7.5, color=INK); a.text(.12, -.25, '$(0,0)$', fontsize=7.5, color=INK)
a.set_xlabel('$u$', labelpad=1); a.set_ylabel('$v$', labelpad=1); a.set_aspect('equal'); a.set_xlim(-1.6, 1.6); a.set_ylim(-1.6, 1.6)
n = 3; c = .75; Q = (1-c)*np.eye(n)+c*np.ones((n, n)); x0 = np.array([1., 2., -1.5]); f = lambda x: .5*x@Q@x; R = 14
def par(al):
    x = x0.copy(); G = [f(x)]
    for r in range(R): x = x-al*Q@x; G.append(f(x))
    return G
def ser():
    x = x0.copy(); G = [f(x)]
    for r in range(R):
        for i in range(n): x[i] -= Q[i]@x
        G.append(f(x))
    return G
b.semilogy(par(1.), '-o', color=YELLOW, lw=1.6, ms=2.8, mew=0); b.semilogy(par(1/3), '-o', color=PURPLE, lw=1.4, ms=2.8, mew=0); b.semilogy(ser(), '-o', color=GREEN, lw=1.4, ms=2.8, mew=0)
b.text(3.2, 3e2, r'$\alpha=1$', fontsize=7.5, color=INK, ha='left'); b.text(7.8, 6e-1, r'$\alpha=\frac{1}{3}$', fontsize=7.5, color=INK); b.text(4.2, 3e-4, '串行', fontsize=7.5, color=INK)
b.set_xlabel('轮数', labelpad=1); b.set_ylabel('$f$', labelpad=1); b.set_xlim(0, R)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'par1': par(1.)[:4], 'par13': par(1/3)[:4], 'ser': ser()[:4]})
print(par(1.)[:4], par(1/3)[:4], ser()[:4], f(x0))
