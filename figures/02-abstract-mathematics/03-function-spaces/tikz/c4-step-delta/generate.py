"""第4章 4.2.2 图数据：支撑缩小的测试 phi_eps(x)=chi(x/eps)，eps=1,0.5,0.25。
chi 为 c4-bump-cutoff 中的光滑截断，phi_eps(0)=1，0<=phi_eps<=1，支撑[-0.9eps,0.9eps]。
运行：python3 generate.py，输出 tests.dat。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
def psi(t): return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.0
def simpson(f,a,b,n):
    h=(b-a)/n; s=f(a)+f(b)
    for i in range(1,n): s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3
C=simpson(psi,-1,1,2000)
def chi(x,a=0.6,eps=0.3):
    lo=max(-1.0,(x-a)/eps); hi=min(1.0,(x+a)/eps)
    return 0.0 if hi<=lo else min(1.0,simpson(psi,lo,hi,400)/C)
xs=[-1.1+i*0.004 for i in range(551)]
with open(HERE/"tests.dat","w") as f:
    f.write("x e1 e2 e4\n")
    for x in xs: f.write(f"{x:.4f} {chi(x):.6f} {chi(2*x):.6f} {chi(4*x):.6f}\n")
