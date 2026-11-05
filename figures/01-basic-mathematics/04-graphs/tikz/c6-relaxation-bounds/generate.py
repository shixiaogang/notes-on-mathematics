"""枚举七点图全部63个非空二分的RatioCut，生成“松弛下界—扫描候选—全部二分”的TikZ图源。"""
from fractions import Fraction as F
from pathlib import Path
from collections import defaultdict

W = {(1, 2): F(1), (2, 3): F(1), (1, 3): F(1), (4, 5): F(1), (5, 6): F(1),
     (4, 6): F(1), (3, 4): F(1), (2, 7): F(3, 5)}
N = 7
LAMBDA2 = 0.31738  # L 的第二特征值（数值求得，见 c6-seven-vertex-sweep）
SWEEP = [{7}, {2, 7}, {1, 2, 7}, {1, 2, 3, 7}, {1, 2, 3, 4, 7}]
UNIT = 24.0  # mm / 单位 RatioCut


def canon(s):
    s = frozenset(s)
    return s if 1 in s else frozenset(range(1, N + 1)) - s


sweep = {canon(s) for s in SWEEP}
cols = defaultdict(list)
for mask in range(1, 2 ** N - 1):
    S = frozenset(i + 1 for i in range(N) if mask >> i & 1)
    if 1 not in S:
        continue
    cut = sum(w for (i, j), w in W.items() if (i in S) != (j in S))
    a = len(S)
    cols[cut * (F(1, a) + F(1, N - a))].append(S in sweep)
assert sum(len(v) for v in cols.values()) == 63
best = min(cols)
out = ["% 第6章 6.7.2：七点图上RatioCut的松弛下界、扫描候选与全部63个非空二分（由 generate.py 生成）。",
       f"% 最小值 J*={best}≈{float(best):.4f}，最大值 {max(cols)}；谱下界 lambda_2≈{LAMBDA2}。",
       "% 每个圆点是一个二分，相同取值竖直堆叠，取值相差不足 1.5mm 的两列略微错开；蓝色实心为阈值扫描的五个候选，空心为其余二分。",
       "% 各取值及个数：" + "，".join(f"{float(k):.4f}×{len(v)}" for k, v in sorted(cols.items())),
       r"""\begin{tikzpicture}[x=1mm,y=1mm,font=\figurefont\footnotesize,text=FigureInk,
  other/.style={circle,draw=FigureMuted,fill=white,line width=.5pt,minimum size=1.25mm,inner sep=0pt},
  cand/.style={circle,draw=FigureBlue,fill=FigureBlue,line width=.5pt,minimum size=1.25mm,inner sep=0pt},
  lab/.style={font=\figurefont\fontsize{7.5}{9}\selectfont},
  note/.style={font=\FigureNoteFont\fontsize{7.5}{9}\selectfont,text=FigureMuted}]"""]
xmax = 4.2 * UNIT
out.append(rf"\draw[draw=FigureStroke,line width=.6pt,-{{Stealth[length=1.4mm]}}] (0,0)--({xmax:.2f},0);")
for t in range(0, 5):
    out.append(rf"\draw[draw=FigureStroke,line width=.6pt] ({t*UNIT:.2f},0)--({t*UNIT:.2f},-1) node[lab,below] {{${t}$}};")
out.append(rf"\node[lab,anchor=north east] at ({xmax:.2f},-4.2) {{RatioCut}};")
xs = {v: float(v) * UNIT for v in cols}
vals = sorted(cols)
for a, b in zip(vals, vals[1:]):  # 取值过近的两列略微错开，避免圆点重叠
    gap = xs[b] - xs[a]
    if gap < 1.5:
        xs[a] -= (1.5 - gap) / 2
        xs[b] += (1.5 - gap) / 2
for v, flags in sorted(cols.items()):
    x = xs[v]
    for k, is_c in enumerate(sorted(flags, reverse=True)):
        out.append(rf"\node[{'cand' if is_c else 'other'}] at ({x:.2f},{1.5 + 1.55*k:.2f}) {{}};")
lx = LAMBDA2 * UNIT
out.append(rf"\draw[draw=FigureRed,dashed,line width=.8pt] ({lx:.2f},-1)--({lx:.2f},24);")
out.append(rf"\node[lab,text=FigureRed,anchor=south west] at ({lx-2:.2f},24) {{谱下界$\lambda_2\approx0.317$}};")
bx = float(best) * UNIT
out.append(rf"\draw[draw=FigureBlue,line width=.6pt,-{{Stealth[length=1.2mm]}}] ({bx+6:.2f},12)--({bx+0.6:.2f},2.6);")
out.append(rf"\node[lab,anchor=south west,text=FigureBlue] at ({bx+4.5:.2f},12) {{$J^\star=U=\tfrac7{{12}}$}};")
# 图例
out.append(rf"""\node[cand] at (60,24) {{}}; \node[note,anchor=west] at (61.5,24) {{阈值扫描的五个候选}};
\node[other] at (60,19.5) {{}}; \node[note,anchor=west] at (61.5,19.5) {{其余二分}};""")
out.append(r"\end{tikzpicture}")
Path(__file__).with_name("figure.tex").write_text("\n".join(out) + "\n")
