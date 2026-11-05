"""Low-rank approximation of E(x,y)=exp(xy) on [-1,1]^2.
Taylor truncation E_r = sum_{k<r} (xy)^k/k!: sup error = e - sum_{k<r} 1/k!, bound e/r!, L2 error by quadrature.
Best rank-r L2 error = sqrt(sum_{j>r} sigma_j^2), sigma_j singular values of the coefficient matrix of E in the
orthonormal Legendre basis p_i=sqrt((2i+1)/2)P_i (n=14 terms; 48-point Gauss-Legendre quadrature)."""
from math import exp, e, factorial, sqrt, cos, pi
def legendre(n, x):
    p0, p1 = 1.0, x
    if n == 0: return 1.0, 0.0
    for k in range(2, n + 1): p0, p1 = p1, ((2*k-1)*x*p1 - (k-1)*p0)/k
    dp = n*(x*p1 - p0)/(x*x - 1)
    return p1, dp
def gauss(n):
    xs, ws = [], []
    for i in range(1, n + 1):
        x = cos(pi*(i-0.25)/(n+0.5))
        for _ in range(100):
            p, dp = legendre(n, x); dx = p/dp; x -= dx
            if abs(dx) < 1e-15: break
        p, dp = legendre(n, x); xs.append(x); ws.append(2/((1-x*x)*dp*dp))
    return xs, ws
X, W = gauss(48)
def P(i, x):
    return sqrt((2*i+1)/2)*(legendre(i, x)[0] if i > 0 else 1.0)
n = 14
Pv = [[P(i, x) for x in X] for i in range(n)]
C = [[sum(W[a]*W[b]*exp(X[a]*X[b])*Pv[i][a]*Pv[k][b] for a in range(48) for b in range(48)) for k in range(n)] for i in range(n)]
# symmetric matrix: singular values = |eigenvalues|; Jacobi eigenvalue iteration
A = [row[:] for row in C]
for sweep in range(60):
    off = sum(A[i][j]**2 for i in range(n) for j in range(n) if i != j)
    if off < 1e-30: break
    for p in range(n):
        for q in range(p+1, n):
            if abs(A[p][q]) < 1e-300: continue
            th = (A[q][q]-A[p][p])/(2*A[p][q]); t = (1 if th >= 0 else -1)/(abs(th)+sqrt(th*th+1))
            c = 1/sqrt(t*t+1); s = t*c
            for k in range(n):
                akp, akq = A[k][p], A[k][q]; A[k][p] = c*akp - s*akq; A[k][q] = s*akp + c*akq
            for k in range(n):
                apk, aqk = A[p][k], A[q][k]; A[p][k] = c*apk - s*aqk; A[q][k] = s*apk + c*aqk
sig = sorted((abs(A[i][i]) for i in range(n)), reverse=True)
total = sum(W[a]*W[b]*exp(2*X[a]*X[b]) for a in range(48) for b in range(48))
print("||E||_L2", sqrt(total), "sqrt(sum sig^2)", sqrt(sum(s*s for s in sig)))
print("r sup_taylor bound_e/r! L2_taylor L2_best sigma_r")
for r in range(1, 9):
    sup = e - sum(1/factorial(k) for k in range(r))
    L2t = sqrt(sum(W[a]*W[b]*(exp(X[a]*X[b]) - sum((X[a]*X[b])**k/factorial(k) for k in range(r)))**2 for a in range(48) for b in range(48)))
    L2b = sqrt(sum(s*s for s in sig[r:]))
    print(f"{r} {sup:.3e} {e/factorial(r):.3e} {L2t:.3e} {L2b:.3e} {sig[r-1]:.3e}")
