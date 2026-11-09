from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
# 贯穿全章的目标 f(x)=0.5(x1-1)^2+(x2-x1^2)^2，最优解 (1,1)。
def f(x):
    u = x[1]-x[0]**2
    return .5*(x[0]-1)**2+u**2
def grad(x):
    u = x[1]-x[0]**2
    return np.array([x[0]-1-4*x[0]*u, 2*u])
def hess(x):
    u = x[1]-x[0]**2
    return np.array([[1-4*u+8*x[0]**2, -4*x[0]], [-4*x[0], 2.]])
XS = np.array([1., 1.])
def panel(fig, left, right, top, bottom, wspace=.3):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace)
def tags(fig, axes, y=.015):
    for ax, s in zip(axes, ('(a)', '(b)', '(c)', '(d)')):
        p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
def grid2(a, b, c, d, n=600):
    X, Y = np.meshgrid(np.linspace(a, b, n), np.linspace(c, d, n))
    return X, Y
def region(ax, a, b, c, d):
    t = np.linspace(a, b, 300); y = t**2+.25
    ax.fill_between(t, y, d, color=RED_FILL, lw=0, zorder=0)
    ax.plot(t, y, color=STROKE, lw=.85, ls=(0, (3, 2)), zorder=1)
    ax.set_xlim(a, b); ax.set_ylim(c, d)
def arrow(ax, p, q, color=GREEN, lw=1.3, z=4):
    ax.annotate('', xy=q, xytext=p, zorder=z, arrowprops=dict(arrowstyle='-|>,head_width=.17,head_length=.34', color=color, lw=lw, shrinkA=0, shrinkB=0))

n = 1000
def F(x):
    u = x[1:]-x[:-1]**2
    return .5*np.sum((x[:-1]-1)**2)+np.sum(u**2)
def G(x):
    u = x[1:]-x[:-1]**2; g = np.zeros(n)
    g[:-1] += x[:-1]-1-4*x[:-1]*u; g[1:] += 2*u
    return g
def HV(x, v):
    u = x[1:]-x[:-1]**2; d = np.zeros(n); d[:-1] = 1-4*u+8*x[:-1]**2; d[1:] += 2
    return d*v+np.r_[-4*x[:-1]*v[1:], 0.]+np.r_[0., -4*x[:-1]*v[:-1]]
def ncg(g, x, eta):
    z = np.zeros(n); r = -g; p = r.copy(); rho = r@r; ng = np.linalg.norm(g); k = 0
    for j in range(5*n):
        q = HV(x, p); k += 1; c = p@q
        if c <= 1e-12*(p@p): return (r.copy() if j == 0 else z), k
        a = rho/c; z = z+a*p; r = r-a*q; rn = r@r
        if np.sqrt(rn) <= eta*ng: return z, k
        p = r+(rn/rho)*p; rho = rn
    return z, k
def run(eta_fun):
    x = np.where(np.arange(n) % 2 == 0, -1.2, 1.0); Gs = [np.linalg.norm(G(x))]; W = [0]; fev = 0
    for t in range(200):
        g = G(x)
        if np.linalg.norm(g) <= 1e-9: break
        d, k = ncg(g, x, eta_fun(np.linalg.norm(g))); s = g@d; al = 1.; fx = F(x); fev += 1
        while F(x+al*d) > fx+1e-4*al*s: al /= 2; fev += 1
        x = x+al*d; Gs.append(np.linalg.norm(G(x))); W.append(W[-1]+k)
    return np.array(Gs), np.array(W)
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, .105, .985, .96, .215, .3)
a, b = axes
cases = {'0.5': (lambda g: .5, YELLOW), '0.1': (lambda g: .1, PURPLE), 'adaptive': (lambda g: min(.5, np.sqrt(g)), GREEN), '1e-10': (lambda g: 1e-10, BLUE)}
Res = {}
for k_, (fn, c) in cases.items():
    Gs, W = run(fn); a.semilogy(range(len(Gs)), Gs, color=c, lw=1.4); b.semilogy(W, Gs, color=c, lw=1.4); Res[k_] = {'outer': len(Gs)-1, 'hv': int(W[-1])}
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('$\\Vert g^{(t)}\\Vert_2$', labelpad=1); a.set_yticks([1e-8, 1e-4, 1]); b.set_xlabel('累计$Hv$次数' if 0 else '$Hv$', labelpad=1); b.set_yticks([1e-8, 1e-4, 1])
b.set_xlim(left=0)
print(Res)
tags(fig, axes); save(fig, HERE, 'figure', {'objective': 'sum_i 0.5(x_i-1)^2+(x_{i+1}-x_i^2)^2', 'n': n, 'start': 'alternating -1.2,1', 'c': 1e-4, 'results': Res})
