"""第4章 4.1.1 图数据：光滑凸起 psi 与光滑截断 chi。
psi(t)=exp(-1/(1-t^2)) (|t|<1)，否则为 0；归一化常数 c=∫psi≈0.443994。
chi = 1_{[-0.6,0.6]} * rho_{0.3}，rho_eps(t)=psi(t/eps)/(c*eps)，故 chi 在 [-0.3,0.3] 上等于 1，支撑为 [-0.9,0.9]。
运行：python3 generate.py（纯标准库，梯形/Simpson 数值积分），输出 bump.dat、cutoff.dat。
"""
import math, pathlib
HERE = pathlib.Path(__file__).resolve().parent
def psi(t):
    return math.exp(-1.0/(1.0-t*t)) if abs(t) < 1 else 0.0
def simpson(f, a, b, n=2000):
    h=(b-a)/n; s=f(a)+f(b)
    for i in range(1,n): s += (4 if i%2 else 2)*f(a+i*h)
    return s*h/3
C = simpson(psi,-1,1)
def chi(x, a=0.6, eps=0.3):
    # ∫_{-a}^{a} rho_eps(x-y) dy = ∫_{(x-a)/eps}^{(x+a)/eps} psi(s) ds / C
    lo=max(-1.0,(x-a)/eps); hi=min(1.0,(x+a)/eps)
    if hi<=lo: return 0.0
    return simpson(psi,lo,hi,400)/C
if __name__=="__main__":
    print("C=",C)
    xs=[-1.5+i*0.0125 for i in range(241)]
    (HERE/"bump.dat").write_text("x y\n"+"".join(f"{x:.4f} {psi(x):.6f}\n" for x in xs))
    xs=[-1.2+i*0.01 for i in range(241)]
    (HERE/"cutoff.dat").write_text("x y\n"+"".join(f"{x:.4f} {min(1.0,chi(x)):.6f}\n" for x in xs))
