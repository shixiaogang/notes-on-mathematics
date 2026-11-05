"""第4章 4.1.1 图数据：三种测试函数列。
psi(t)=exp(-1/(1-t^2))（|t|<1）。
(a) psi/n，n=1,2,4：支撑固定在[-1,1]，各阶导数一致趋零；
(b) phi_n=psi(x) sin(nx)/n，n=12：上确界<=e^{-1}/12，导数 phi_n'=psi' sin(nx)/n+psi cos(nx) 不趋零；
(c) psi(x-3k)/k，k=1,2,3：各阶导数一致趋零，支撑右移。
运行：python3 generate.py，输出 a.dat、b.dat、c.dat。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
def psi(t): return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.0
def dpsi(t): return psi(t)*(-2*t/(1-t*t)**2) if abs(t)<1 else 0.0
xs=[-1.3+i*0.005 for i in range(521)]
with open(HERE/"a.dat","w") as f:
    f.write("x n1 n2 n4\n")
    for x in xs: f.write(f"{x:.4f} {psi(x):.6f} {psi(x)/2:.6f} {psi(x)/4:.6f}\n")
n=12
with open(HERE/"b.dat","w") as f:
    f.write("x phi dphi\n")
    for x in xs: f.write(f"{x:.4f} {psi(x)*math.sin(n*x)/n:.6f} {dpsi(x)*math.sin(n*x)/n+psi(x)*math.cos(n*x):.6f}\n")
xs=[-0.5+i*0.01 for i in range(1101)]
with open(HERE/"c.dat","w") as f:
    f.write("x k1 k2 k3\n")
    for x in xs: f.write(f"{x:.3f} {psi(x-3):.6f} {psi(x-6)/2:.6f} {psi(x-9)/3:.6f}\n")
print(max(abs(dpsi(x)*math.sin(n*x)/n+psi(x)*math.cos(n*x)) for x in [i/10000 for i in range(-9999,10000)]))
