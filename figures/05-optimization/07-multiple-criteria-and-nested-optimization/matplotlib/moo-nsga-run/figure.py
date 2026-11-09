from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# NSGA-II on f1=x1, g=1+9*mean(x2..x5), f2=g(1-(f1/g)^2), x in [0,1]^5, population 40, 200 generations, seed 7.
rng = np.random.default_rng(7); n = 5; N = 40; T = 200
def evalf(X):
    f1 = X[:, 0]; g = 1+9*X[:, 1:].mean(axis=1); return np.c_[f1, g*(1-(f1/g)**2)]
def layers(F):
    N_ = len(F); S = [[] for _ in range(N_)]; c = np.zeros(N_, int); out = [[]]
    for p in range(N_):
        for q in range(N_):
            if np.all(F[p] <= F[q]) and np.any(F[p] < F[q]): S[p].append(q)
            elif np.all(F[q] <= F[p]) and np.any(F[q] < F[p]): c[p] += 1
        if c[p] == 0: out[0].append(p)
    while out[-1]:
        nxt = []
        for p in out[-1]:
            for q in S[p]:
                c[q] -= 1
                if c[q] == 0: nxt.append(q)
        out.append(nxt)
    return out[:-1]
def crowd(F, idx):
    d = dict.fromkeys(idx, 0.)
    for m in range(F.shape[1]):
        s = sorted(idx, key=lambda i: F[i, m]); span = F[s[-1], m]-F[s[0], m] or 1.
        d[s[0]] = d[s[-1]] = np.inf
        for a, b, c in zip(s, s[1:], s[2:]): d[b] += (F[c, m]-F[a, m])/span
    return d
def offspring(X, rank, dist):
    def pick():
        a, b = rng.integers(0, N, 2)
        return a if (rank[a], -dist[a]) < (rank[b], -dist[b]) else b
    C = []
    while len(C) < N:
        p1, p2 = X[pick()].copy(), X[pick()].copy(); ch = p1.copy()
        if rng.random() < .9:
            for j in range(n):
                if rng.random() < .5:
                    u = rng.random(); b = (2*u)**(1/16) if u <= .5 else (1/(2*(1-u)))**(1/16); ch[j] = .5*((1+b)*p1[j]+(1-b)*p2[j])
        for j in range(n):
            if rng.random() < 1/n:
                u = rng.random(); dl = (2*u)**(1/21)-1 if u < .5 else 1-(2*(1-u))**(1/21); ch[j] += dl
        C.append(np.clip(ch, 0, 1))
    return np.array(C)
def step(X):
    F = evalf(X); L = layers(F); rank = np.zeros(N, int); dist = np.zeros(N)
    for r, l in enumerate(L):
        d = crowd(F, l)
        for i in l: rank[i] = r; dist[i] = d[i]
    Y = offspring(X, rank, dist); R = np.vstack([X, Y]); FR = evalf(R); keep = []
    for l in layers(FR):
        if len(keep)+len(l) <= N: keep += l
        else:
            d = crowd(FR, l); keep += sorted(l, key=lambda i: -d[i])[:N-len(keep)]; break
    return R[keep]
def hv(F, r):
    Fn = np.array([p for p in F if np.all(p < r)])
    if len(Fn) == 0: return 0.
    L0 = layers(Fn)[0]; P = Fn[L0]; P = P[np.argsort(P[:, 0])]; xs = np.r_[P[:, 0], r[0]]
    return float(sum((xs[i+1]-xs[i])*(r[1]-P[i, 1]) for i in range(len(P))))
ref_x = np.linspace(0, 1, 2001); RF = np.c_[ref_x, 1-ref_x**2]
def igd(F): return float(np.mean([np.min(np.linalg.norm(F-p, axis=1)) for p in RF[::4]]))
X = rng.random((N, n)); hist = []; snaps = {}
for t in range(T+1):
    F = evalf(X); hist.append((hv(F, np.array([1.1, 1.1])), igd(F[layers(F)[0]]), len(layers(F)[0])))
    if t in (0, 10, 40, 200): snaps[t] = F.copy()
    if t < T: X = step(X)
hist = np.array(hist); import json; (HERE/'run.json').write_text(json.dumps({'hist': hist.tolist(), 'snaps': {str(k): v.tolist() for k, v in snaps.items()}}))
fig, axes = figure(width_mm=112, height_mm=44, ncols=3)
panels(fig, .08, .99, .985, .26, .28)
for ax, t, ym in zip(axes, (0, 10, 200), (7, 3.5, 1.2)):
    setup(ax, (0, 1.05), (0, ym), [0, .5, 1], None, yl='$f_2$' if t == 0 else '')
    ax.plot(ref_x, 1-ref_x**2, color=RED, lw=1.6, zorder=2)
    F = snaps[t]; nd = layers(F)[0]; ot = [i for i in range(N) if i not in nd]
    ax.plot(F[ot, 0], F[ot, 1], 'o', mfc='white', mec=MUTED, mew=.7, ms=3.2, zorder=3); ax.plot(F[nd, 0], F[nd, 1], 'o', color=GREEN, ms=3.4, mew=0, zorder=4)
tags(fig, axes)
save(fig, HERE, 'figure', {'hv_final': hist[-1, 0], 'igd_final': hist[-1, 1], 'nd_final': int(hist[-1, 2])}); print(hist[[0, 10, 40, 100, 200]])
