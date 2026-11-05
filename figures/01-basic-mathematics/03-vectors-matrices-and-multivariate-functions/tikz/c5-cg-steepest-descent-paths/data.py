"""c5-cg-steepest-descent-paths 的数据：贯穿例 A=[[4,1],[1,3]], b=(1,2), x0=0。

用有理数精确计算 CG 两步与最速下降（精确线搜索）前若干步，以及经过各迭代点的
二次函数等值线（以 x_star 为心的椭圆）的半轴与转角，写入 path-data.tex。
只用标准库；从任意目录运行：python3 data.py
"""
from fractions import Fraction as Fr
from pathlib import Path
import math

HERE = Path(__file__).resolve().parent
SCALE = 60.0  # 总览：1 个坐标单位 = 60 mm；figure.tex 使用 x=1mm
ZOOM = 600.0  # 放大：1 个坐标单位 = 600 mm
A = [[Fr(4), Fr(1)], [Fr(1), Fr(3)]]
b = [Fr(1), Fr(2)]

def mv(M, v): return [M[0][0]*v[0]+M[0][1]*v[1], M[1][0]*v[0]+M[1][1]*v[1]]
def dot(u, v): return u[0]*v[0]+u[1]*v[1]
def add(u, v, a=Fr(1)): return [u[0]+a*v[0], u[1]+a*v[1]]

xstar = [Fr(1, 11), Fr(7, 11)]
assert mv(A, xstar) == b

# CG
x = [Fr(0), Fr(0)]; r = add(b, mv(A, x), Fr(-1)); p = r[:]
cg = [x[:]]; cg_coef = []
for _ in range(2):
    q = mv(A, p); a = dot(r, r)/dot(p, q)
    x = add(x, p, a); rn = add(r, q, -a)
    beta = dot(rn, rn)/dot(r, r) if any(rn) else Fr(0)
    cg_coef.append((a, beta)); cg.append(x[:])
    p = add(rn, p, beta); r = rn
assert cg[-1] == xstar

# 最速下降（方向取残差，精确线搜索）
x = [Fr(0), Fr(0)]; sd = [x[:]]
for _ in range(6):
    r = add(b, mv(A, x), Fr(-1)); a = dot(r, r)/dot(r, mv(A, r))
    x = add(x, r, a); sd.append(x[:])

# 等值线：(x-x*)^T A (x-x*) = c 的椭圆，特征值 (7±√5)/2
l1, l2 = (7+math.sqrt(5))/2, (7-math.sqrt(5))/2
angle = math.degrees(math.atan2(l1-4, 1))  # 对应 l1 的特征向量 (1, l1-4)
def level(pt):
    e = add(pt, xstar, Fr(-1)); return float(dot(e, mv(A, e)))
levels = [level(pt) for pt in sd[:6]]

def block(tag, scale, origin):
    """以 origin 为原点、scale mm/单位 输出一组宏。"""
    g = lambda v, o: f"{(float(v)-o)*scale:.3f}"
    ox, oy = float(origin[0]), float(origin[1])
    pts = lambda seq: " -- ".join(f"({g(p[0], ox)},{g(p[1], oy)})" for p in seq)
    return [r"\def\%sxs{%s}\def\%sys{%s}" % (tag, g(xstar[0], ox), tag, g(xstar[1], oy)),
            r"\def\%slevels{" % tag + ",".join(
                "%.3f/%.3f" % (math.sqrt(c/l1)*scale, math.sqrt(c/l2)*scale) for c in levels) + "}",
            r"\def\%scg{" % tag + pts(cg) + "}",
            r"\def\%ssd{" % tag + pts(sd) + "}",
            r"\def\%ssdpts{" % tag + ",".join(f"{g(p[0], ox)}/{g(p[1], oy)}" for p in sd[2:5]) + "}"]
lines = ["%% 由 data.py 生成，勿手改。单位 mm；O=总览（%g mm/单位，原点 x0），Z=放大（%g mm/单位，原点 x_star）。" % (SCALE, ZOOM),
         r"\def\CGangle{%.4f}" % angle]
lines += block("O", SCALE, [0, 0]) + block("Z", ZOOM, xstar)
(HERE/"path-data.tex").write_text("\n".join(lines)+"\n")
print("CG iterates:", [[str(c) for c in p] for p in cg], "alpha,beta:", [(str(a), str(bb)) for a, bb in cg_coef])
print("SD iterates:", [[str(c) for c in p] for p in sd])
print("SD errors ||x-x*||_A:", [round(math.sqrt(level(p)), 5) for p in sd])
print("angle", angle, "levels", levels)
