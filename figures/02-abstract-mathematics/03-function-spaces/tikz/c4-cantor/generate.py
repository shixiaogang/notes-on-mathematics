"""第4章 4.2.2 图数据：Cantor 函数 c 与一枚测试函数。
c 由三进制构造给出：在第 m 层保留的 2^m 个闭区间端点处取精确值（二进有理数），在被挖去的开区间上为常数；
这里取 m=8 层端点连成折线（端点值精确，折线与 c 的一致误差 <= 2^{-8}）。
测试 phi：在 (1/9,2/9) 内由 0 光滑升到 1，在 [2/9,7/9] 上为 1，在 (7/9,8/9) 内光滑降到 0；
用 s(t)=e^{-1/t}/(e^{-1/t}+e^{-1/(1-t)}) 作光滑台阶，过渡区取 (0.13,0.20) 与 (0.80,0.87)。
运行：python3 generate.py，输出 cantor.dat、test.dat。
"""
import math, pathlib
from fractions import Fraction as F
HERE=pathlib.Path(__file__).resolve().parent
pts={F(0):F(0),F(1):F(1)}
def build(a,b,ca,cb,m):
    if m==0: return
    l=a+(b-a)/3; r=a+2*(b-a)/3; mid=(ca+cb)/2
    pts[l]=mid; pts[r]=mid
    build(a,l,ca,mid,m-1); build(r,b,mid,cb,m-1)
build(F(0),F(1),F(0),F(1),8)
with open(HERE/"cantor.dat","w") as f:
    f.write("x y\n")
    for x in sorted(pts): f.write(f"{float(x):.6f} {float(pts[x]):.6f}\n")
def s(t):
    if t<=0: return 0.0
    if t>=1: return 1.0
    a=math.exp(-1/t); b=math.exp(-1/(1-t)); return a/(a+b)
def phi(x):
    return s((x-0.13)/0.07)*s((0.87-x)/0.07)
with open(HERE/"test.dat","w") as f:
    f.write("x y\n")
    for i in range(501):
        x=i/500; f.write(f"{x:.4f} {phi(x):.6f}\n")
