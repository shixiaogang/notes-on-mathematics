"""第4章 4.4.1 图数据：一维磨光核与磨光后的 |x|、sgn x。
rho(t)=psi(t)/C，psi(t)=exp(-1/(1-t^2))，C=∫psi≈0.443994；rho_eps(t)=rho(t/eps)/eps，rho_eps(0)=0.82855/eps。
(|x|*rho_eps)(x)=∫|x-z|rho_eps(z)dz，(sgn*rho_eps)(x)=∫sgn(x-z)rho_eps(z)dz（Simpson 积分，eps=0.5）。
运行：python3 generate.py，输出 kernels.dat、smoothed.dat。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
def psi(t): return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.0
def simpson(f,a,b,n):
    h=(b-a)/n; s=f(a)+f(b)
    for i in range(1,n): s+=(4 if i%2 else 2)*f(a+i*h)
    return s*h/3
C=simpson(psi,-1,1,4000)
def rho(t,e): return psi(t/e)/(C*e)
with open(HERE/"kernels.dat","w") as f:
    f.write("x e1 e2 e4\n")
    for i in range(481):
        x=-1.2+i*0.005; f.write(f"{x:.4f} {rho(x,1):.6f} {rho(x,0.5):.6f} {rho(x,0.25):.6f}\n")
e=0.5
with open(HERE/"smoothed.dat","w") as f:
    f.write("x abs sabs sgn ssgn\n")
    for i in range(301):
        x=-1.5+i*0.01
        sa=simpson(lambda z: abs(x-z)*rho(z,e),-e,e,2000)
        ss=simpson(lambda z: (1 if x-z>0 else (-1 if x-z<0 else 0))*rho(z,e),-e,e,2000)
        f.write(f"{x:.4f} {abs(x):.6f} {sa:.6f} {(1 if x>0 else -1 if x<0 else 0)} {ss:.6f}\n")
print("rho(0)=",rho(0,1))
