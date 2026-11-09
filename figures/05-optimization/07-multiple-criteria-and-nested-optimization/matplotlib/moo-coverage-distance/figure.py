from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"moo-common"))
from moo_fig import *
HERE = Path(__file__).resolve().parent
# Two 3-point sets on the isotropic front with equal hypervolume at r=(1.2,1.2) but different coverage.
r = np.array([1.2, 1.2]); f = lambda s: np.array([s**2, (1-s)**2])
def hv(S):
    S = sorted(S); P = np.array([f(s) for s in S]); xs = np.r_[P[:, 0], r[0]]
    return float(sum((xs[i+1]-xs[i])*(r[1]-P[i, 1]) for i in range(len(S))))
S1 = (.1, .5, .9); H1 = hv(S1)
s_ref = np.linspace(0, 1, 4001); RF = np.c_[s_ref**2, (1-s_ref)**2]
def igd(S): P = np.array([f(s) for s in S]); return float(np.mean([np.min(np.linalg.norm(P-p, axis=1)) for p in RF[::4]]))
def maxgap(S):
    P = np.array([f(s) for s in sorted([0, *S, 1])]); return float(np.max(np.linalg.norm(np.diff(P, axis=0), axis=1)))
G = np.arange(.02, .985, .005); A, B, C = np.meshgrid(G, G, G, indexing='ij')
m = (B > A+.02)&(C > B+.02); A, B, C = A[m], B[m], C[m]
def hv_v(a, b, c):
    x = [a**2, b**2, c**2]; y = [(1-a)**2, (1-b)**2, (1-c)**2]
    return (x[1]-x[0])*(r[1]-y[0])+(x[2]-x[1])*(r[1]-y[1])+(r[0]-x[2])*(r[1]-y[2])
def gap_v(a, b, c):
    Z = [np.zeros_like(a), a, b, c, np.ones_like(a)]
    return np.max([np.hypot(Z[i+1]**2-Z[i]**2, (1-Z[i+1])**2-(1-Z[i])**2) for i in range(4)], axis=0)
ok = abs(hv_v(A, B, C)-H1) < 2e-4; i = int(np.argmax(np.where(ok, gap_v(A, B, C), -1)))
a, b, c = float(A[i]), float(B[i]), float(C[i]); lo, hi = c-.02, c+.02
for _ in range(60):
    m_ = (lo+hi)/2
    if (hv((a, b, lo))-H1)*(hv((a, b, m_))-H1) <= 0: hi = m_
    else: lo = m_
best = (0, (a, b, (lo+hi)/2))
S2 = best[1]
fig, axes = figure(width_mm=112, height_mm=56, ncols=2)
panels(fig, .08, .985, .985, .2, .24)
for ax, S in zip(axes, (S1, S2)):
    setup(ax, (0, 1.25), (0, 1.25), [0, .5, 1], [0, .5, 1], equal=True); ax.plot(RF[:, 0], RF[:, 1], color=BLUE, lw=1.1, zorder=2)
    P = np.array([f(s) for s in sorted(S)]); xs = np.r_[P[:, 0], r[0]]
    for i in range(len(P)): ax.fill([xs[i], xs[i+1], xs[i+1], xs[i]], [P[i, 1], P[i, 1], r[1], r[1]], facecolor=GREEN_FILL, edgecolor=GREEN, lw=.6, zorder=1)
    ax.plot(P[:, 0], P[:, 1], 'o', color=GREEN, ms=5, mew=0, zorder=4); dot(ax, r, PURPLE); ax.text(1.17, 1.21, '$r$', color=PURPLE, ha='right')
tags(fig, axes)
facts = {'S1': S1, 'S2': [float(x) for x in S2], 'hv': [hv(S1), hv(S2)], 'igd': [igd(S1), igd(S2)], 'maxgap': [maxgap(S1), maxgap(S2)]}
save(fig, HERE, 'figure', facts); print(facts)
