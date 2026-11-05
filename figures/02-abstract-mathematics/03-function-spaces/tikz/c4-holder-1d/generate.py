"""第4章 4.2.3 图数据：u(x)=x^{3/4} 的 Hölder 包络多边形。
||u'||_2=sqrt(9/8)=1.06066，u(0.3)=0.3^{0.75}=0.40536；包络 u(0.3)±1.06066|x-0.3|^{1/2}，x∈[0,1]。
运行：python3 generate.py，输出 band.dat（上包络正向、下包络反向，构成闭合多边形）。
"""
import math, pathlib
HERE=pathlib.Path(__file__).resolve().parent
M=math.sqrt(9/8); c=0.3**0.75
xs=[i/400 for i in range(401)]
up=[(x,c+M*math.sqrt(abs(x-0.3))) for x in xs]
lo=[(x,c-M*math.sqrt(abs(x-0.3))) for x in reversed(xs)]
(HERE/"band.dat").write_text("x y\n"+"".join(f"{x:.4f} {y:.6f}\n" for x,y in up+lo))
print(M,c)
