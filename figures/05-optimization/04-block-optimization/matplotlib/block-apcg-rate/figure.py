from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from block_common import *
HERE = Path(__file__).resolve().parent
# (a) chain quadratic f=1/2 x^T Q x-x_1, n=200, Q tridiag(-1,2,-1), L_i=2; uniform coordinate: BCGD vs APCG (mu=0, alpha_{-1}=1/n), mean of 4 runs.
# (b) f=x1^2+1.5 x1 x2+x2^2 (mu=1/4 in L-norm), x0=(3,4), alternating coordinates 1,2,1,...: APCG with alpha=beta=1/4 is not monotone.
n = 200; Lc = 2.; T = 200000; bv = np.zeros(n); bv[0] = 1.
xs = (n-np.arange(n))/(n+1.); fs = -.5*xs[0]
def Fv(x): return .5*x@(2*x-np.r_[x[1:], 0]-np.r_[0, x[:-1]])-x[0]
def gi(v, i): return 2*v[i]-(v[i-1] if i > 0 else 0)-(v[i+1] if i < n-1 else 0)-(1. if i == 0 else 0)
grid = np.unique(np.geomspace(1, T, 300).astype(int))
def rbcgd(s):
    I = np.random.default_rng(s).integers(0, n, T); x = np.zeros(n); G = []; c = 0
    for t, i in enumerate(I):
        x[i] -= gi(x, i)/Lc
        if t+1 == grid[c]: G.append(Fv(x)-fs); c += 1
    return np.array(G)
def apcg(s):
    I = np.random.default_rng(s).integers(0, n, T); x = np.zeros(n); z = x.copy(); al = 1/n; G = []; c = 0
    for t, i in enumerate(I):
        al = .5*(np.sqrt(al**4+4*al**2)-al**2); y = (1-al)*x+al*z; g = gi(y, i)
        dz = -g/(n*al*Lc); z[i] += dz; x = y; x[i] += n*al*dz
        if t+1 == grid[c]: G.append(Fv(x)-fs); c += 1
    return np.array(G)
gb = np.mean([rbcgd(s) for s in range(4)], 0); ga = np.mean([apcg(s) for s in range(4)], 0)
fig, (a, b) = figure(width_mm=112, height_mm=58, ncols=2)
panel(fig, .1, .985, .97, .25, wspace=.3)
a.loglog(grid, gb, color=YELLOW, lw=1.6); a.loglog(grid, ga, color=GREEN, lw=1.4)
k = np.searchsorted(grid, 40000); ref = ga[k]*(grid[k]/grid)**2; m = grid >= 8000; a.loglog(grid[m], ref[m], color=MUTED, lw=.85, ls=(0, (3, 2)))
a.text(3000, gb[np.searchsorted(grid, 3000)]*1.5, 'BCGD', fontsize=7.5, color=INK); a.text(300, .015, 'APCG', fontsize=7.5, color=INK)
a.text(50000, 1.5e-3, '$t^{-2}$', fontsize=7.5, color=INK); a.set_xlim(100, T)
a.set_xlabel('$t$', labelpad=1); a.set_ylabel('目标差', labelpad=1)
c = 1.5; f = lambda x: x[0]**2+c*x[0]*x[1]+x[1]**2
x = np.array([3., 4.]); z = x.copy(); Fa = [f(x)]; Pts = [x.copy()]
for k in range(14):
    i = k % 2; y = (x+.25*z)/1.25; g = 2*y[i]+c*y[1-i]; ctr = .75*z+.25*y; zn = ctr.copy(); zn[i] = ctr[i]-g
    x = y.copy(); x[i] = y[i]-.5*g; z = zn; Fa.append(f(x)); Pts.append(x.copy())
x = np.array([3., 4.]); Fb = [f(x)]
for k in range(14):
    i = k % 2; x[i] -= .5*(2*x[i]+c*x[1-i]); Fb.append(f(x))
b.semilogy(Fb, '-o', color=YELLOW, lw=1.6, ms=3, mew=0); b.semilogy(Fa, '-o', color=GREEN, lw=1.4, ms=3, mew=0)
b.text(8.8, Fb[9]*6, 'BCGD', fontsize=7.5, color=INK, ha='left'); b.text(4.4, Fa[5]*1.6, 'APCG', fontsize=7.5, color=INK)
b.set_xlabel('$t$', labelpad=1); b.set_ylabel('$f(x^{(t)})$', labelpad=1); b.set_xlim(0, 14)
tag(fig, a, '(a)'); tag(fig, b, '(b)')
save(fig, HERE, 'figure', {'n': n, 'T': T, 'gb_end': float(gb[-1]), 'ga_end': float(ga[-1]), 'apcg_values': Fa[:6], 'points': [p.tolist() for p in Pts[:4]]})
print(Fa, Fb)
