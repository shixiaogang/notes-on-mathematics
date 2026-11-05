"""第4章 4.1.3 图数据：phi_n(x)=chi(x) sin(nx)，n=3,10。
chi 为 c4-bump-cutoff 中的光滑截断（[-0.3,0.3]上为1，支撑[-0.9,0.9]），故 sup|phi_n|<=1，phi_n'(0)=n。
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
    f.write("x n3 n10\n")
    for x in xs:
        c=chi(x); f.write(f"{x:.4f} {c*math.sin(3*x):.6f} {c*math.sin(10*x):.6f}\n")
