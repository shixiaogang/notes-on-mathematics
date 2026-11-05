"""Uniform-grid linear interpolation errors on [0,1], N cells, h=1/N (N odd so 1/2 is not a node).
g(x)=sin(pi x): sup error vs bound pi^2 h^2/8; f*(x)=|x-1/2|: sup error (=h/2)."""
from math import sin, pi
def interp_err(f, N, K=400):
    err = 0.0
    for i in range(N):
        a, b = i / N, (i + 1) / N
        for k in range(K + 1):
            s = k / K; x = a + s * (b - a)
            err = max(err, abs(f(x) - ((1 - s) * f(a) + s * f(b))))
    return err
for N in (3, 5, 9, 17, 33, 65):
    h = 1 / N
    print(f"{h:.5f} {interp_err(lambda x: sin(pi*x), N):.3e} {pi*pi*h*h/8:.3e} {interp_err(lambda x: abs(x-0.5), N):.3e}")
