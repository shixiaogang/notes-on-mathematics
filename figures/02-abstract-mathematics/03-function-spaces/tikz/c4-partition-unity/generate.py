"""第4章 4.4.2 图数据：Omega=(0,1) 上的局部有限单位分解。
记 s=min(x,1-x) 为到边界的距离，tau=-log2(s)∈(1,∞)。取 b_j(tau)=psi(tau-j)（j=1,2,...），psi(t)=exp(-1/(1-t^2))，
其支撑为 tau∈[j-1,j+1]，即 s∈[2^{-j-1},2^{-j+1}]，紧含于 Omega。zeta_j=b_j/sum_i b_i，每点至多两个 b_j 非零，sum_j zeta_j=1。
运行：python3 generate.py，输出 pou.dat（列 zeta_1..zeta_6 与总和）。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
def psi(t): return math.exp(-1/(1-t*t)) if abs(t)<1 else 0.0
J=12
with open(HERE/"pou.dat","w") as f:
    f.write("x "+" ".join(f"z{j}" for j in range(1,7))+" sum\n")
    for i in range(1,4000):
        x=i/4000; s=min(x,1-x); tau=-math.log2(s)
        b=[psi(tau-j) for j in range(1,J+1)]; tot=sum(b)
        z=[v/tot for v in b]
        f.write(f"{x:.5f} "+" ".join(f"{z[j]:.5f}" for j in range(6))+f" {sum(z):.5f}\n")
