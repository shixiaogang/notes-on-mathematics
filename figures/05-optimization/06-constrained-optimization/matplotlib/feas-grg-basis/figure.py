from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"feas-common"))
from feas_fig import *
HERE = Path(__file__).resolve().parent
# GRG on min y s.t. y^2+z^2=1, start (y,z)=(.8,.6), basis = variable with larger |partial c|.
Y = [.8]; Z = [.6]; basis = ['y']; a = .25
for t in range(60):
    y, z = Y[-1], Z[-1]; b = 'y' if abs(y) >= abs(z) else 'z'
    if b == 'y':
        Fp = -z/y; zn = z-a*Fp; yn = np.sign(y)*np.sqrt(max(1-zn*zn, 0)); 
        while zn*zn >= 1: a *= .5; zn = z-a*Fp; yn = np.sign(y)*np.sqrt(1-zn*zn)
    else:
        Fp = 1.; yn = y-a*Fp; zn = np.sign(z)*np.sqrt(1-yn*yn)
    basis.append(b); Y.append(yn); Z.append(zn)
    if abs(Fp) < 1e-3: break
Y = np.array(Y); Z = np.array(Z)
fig, axs = figure(width_mm=112, height_mm=54, ncols=2)
ax = axs[0]; t = np.linspace(0, 2*np.pi, 400); ax.plot(np.sin(t), np.cos(t), color=EDGE, lw=1.6, zorder=2)
col = {'y': GREEN, 'z': PURPLE}
for i in range(1, len(Y)): ax.plot([Z[i-1]], [Y[i-1]], 'o', color=col[basis[i]], ms=3.6, mew=0, zorder=5)
dot(ax, (0, -1), RED); ax.axhline(0, color=MUTED, lw=.6, zorder=0); ax.axvline(0, color=MUTED, lw=.6, zorder=0)
ax.text(1.07, .55, 'y 为基本', fontsize=7.5, color=GREEN, va='center'); ax.text(1.07, -.18, 'z 为基本', fontsize=7.5, color=PURPLE, va='center')
setup(ax, (-1.2, 1.75), (-1.2, 1.2), [-1, 0, 1], [-1, 0, 1], xl='$z$', yl='$y$', equal=True)
ax = axs[1]; n = 16; I = np.arange(0, n); ax.semilogy(I, 1/np.maximum(2*np.abs(Y[:n]), 1e-3), color=YELLOW, lw=1.2, ls=(0, (3, 2)))
ax.semilogy(I, 1/np.maximum(2*np.maximum(np.abs(Y[:n]), np.abs(Z[:n])), 1e-3), color=GREEN, lw=1.4)
ax.text(5.4, 2.0, '不换基 1/|2y|', color=YELLOW, fontsize=7.5); ax.text(10, .45, '换基', color=GREEN, fontsize=7.5)
setup(ax, (0, 15), (.3, 40), [0, 5, 10, 15], [1, 10], xl='$t$', yl='$\\Vert B^{-1}\\Vert$')
panels(fig, .08, .985, .98, .2, .3); tags(fig, axs)
save(fig, HERE, 'figure', {'step': a, 'iterates': [[float(y), float(z)] for y, z in zip(Y[:12], Z[:12])], 'bases': basis[:13], 'n': len(Y)})
print(np.c_[Y, Z][:16], basis[:16], len(Y))
