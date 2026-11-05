"""第4章 4.5.2 图数据：两种失紧。
(a) d=3，p=2：u_lam(x)=lam^{(d-p)/p} psi(lam|x|)=lam^{1/2} psi(lam r)，lam=1,2,4；画径向剖面 r∈[0,1.1]。
    ||grad u_lam||_2 与 ||u_lam||_6 不随 lam 变化，||u_lam||_2=lam^{-1}||psi||_2。峰值 lam^{1/2}e^{-1}=0.368,0.520,0.736。
(b) 实轴上 psi(x-3k)，k=0,1,2,3：范数不变，支撑互不相交。
运行：python3 generate.py，输出 conc.dat、shift.dat。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
def psi(t): return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.0
with open(HERE/"conc.dat","w") as f:
    f.write("r l1 l2 l4\n")
    for i in range(441):
        r=i*0.0025; f.write(f"{r:.4f} {psi(r):.6f} {math.sqrt(2)*psi(2*r):.6f} {2*psi(4*r):.6f}\n")
with open(HERE/"shift.dat","w") as f:
    f.write("x k0 k1 k2 k3\n")
    for i in range(1301):
        x=-1.5+i*0.01; f.write(f"{x:.3f} "+" ".join(f"{psi(x-3*k):.6f}" for k in range(4))+"\n")
