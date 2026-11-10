from pathlib import Path
import sys
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent/"pdenum-common"))
from pdenum_fig import *
# (a) CN heat T=0.1: tau tied to h vs fixed tau=0.05. (b) Poisson: Thomas roundoff for sin data; CG stopped at relative residual 1e-2 for u=(x-x^2)e^x.
fig, axes = figure(width_mm=112, height_mm=54, ncols=2)
panel(fig, left=.105, wspace=.25, bottom=.25)
def heat(n, tau, T=.1):
    h = 1/n; x = np.linspace(h, 1-h, n-1); A = lap1d(n); I = np.eye(n-1); N = round(T/tau); tau = T/N
    U = np.sin(PI*x); B = np.linalg.solve(I+tau/2*A, I-tau/2*A)
    for _ in range(N): U = B@U
    return np.max(abs(U-np.exp(-PI**2*T)*np.sin(PI*x)))
ns = np.array([10, 20, 40, 80, 160]); hs = 1/ns
E1 = np.array([heat(n, 1/n) for n in ns]); E2 = np.array([heat(n, .05) for n in ns])
ax = axes[0]; ax.loglog(hs, E1, color=GREEN, lw=1.4, marker='o', ms=3, mew=0); ax.loglog(hs, E2, color=RED, lw=1.4, marker='s', ms=3, mew=0)
ax.loglog(hs, 1.5*E1[-1]*(hs/hs[-1])**2, color=PURPLE, lw=.9, ls=DASH); ax.set_xlabel('$h$', labelpad=1); ax.set_ylabel('最大模误差', labelpad=1)
lab(ax, .0145, 4.3e-3, r'$\tau=0.05$', RED, ha='center'); lab(ax, .019, 2e-4, r'$\tau=h$', GREEN, ha='center')
def thomas(n):
    h = 1/n; x = h*np.arange(1, n); f = PI**2*np.sin(PI*x)*h*h
    d = np.zeros(n-1); y = np.zeros(n-1); d[0] = 2.; y[0] = f[0]
    for j in range(1, n-1):
        m = -1/d[j-1]; d[j] = 2+m; y[j] = f[j]-m*y[j-1]
    u = np.zeros(n-1); u[-1] = y[-1]/d[-1]
    for j in range(n-3, -1, -1): u[j] = (y[j]+u[j+1])/d[j]
    return np.max(abs(u-np.sin(PI*x)))
def cg(n, tol):
    h = 1/n; x = h*np.arange(1, n); b = (3*x+x*x)*np.exp(x)*h*h
    ue = (x-x*x)*np.exp(x); Ax = lambda v: 2*v-np.r_[v[1:], 0]-np.r_[0, v[:-1]]
    u = 0*b; r_ = b.copy(); p = r_.copy(); rr = r_@r_; b0 = np.sqrt(rr)
    while np.sqrt(rr) > tol*b0:
        q = Ax(p); al = rr/(p@q); u += al*p; r_ -= al*q; new = r_@r_; p = r_+new/rr*p; rr = new
    return np.max(abs(u-ue))
nt = 2**np.arange(3, 21); Et = np.array([thomas(int(n)) for n in nt]); hsT = 1/nt
nc = 2**np.arange(3, 11); Ec = np.array([cg(int(n), 1e-2) for n in nc])
ax = axes[1]; ax.loglog(hsT, Et, color=GREEN, lw=1.4, marker='o', ms=2.6, mew=0); ax.loglog(1/nc, Ec, color=RED, lw=1.4, marker='s', ms=2.8, mew=0)
ax.set_xlabel('$h$', labelpad=1); ax.set_xticks([1e-6, 1e-4, 1e-2])
lab(ax, 3e-6, 3e-5, '舍入误差', GREEN, ha='center'); lab(ax, 2.5e-2, 1.4e-1, '提前停止', RED, ha='center')
tags(fig, axes)
save(fig, HERE, 'figure', {'heat_tied': E1.tolist(), 'heat_fixed': E2.tolist(), 'thomas': Et.tolist(), 'cg': Ec.tolist()})
print(E1, E2); print(Et); print(Ec)
