"""生成七点图上RatioCut阈值扫描逐步执行图的 TikZ 源，并用分数复算割权与RatioCut。"""
from fractions import Fraction as F
from pathlib import Path

W = {(1, 2): F(1), (2, 3): F(1), (1, 3): F(1), (4, 5): F(1), (5, 6): F(1),
     (4, 6): F(1), (3, 4): F(1), (2, 7): F(3, 5)}
POS = {1: (4, 0), 2: (4, 9), 3: (10.5, 4.5), 4: (18.5, 4.5), 5: (25, 9), 6: (25, 0), 7: (-2.5, 14)}
ORDER = [7, 2, 1, 3, 4]
N = 7


def frac(x):
    return str(x.numerator) if x.denominator == 1 else rf"\tfrac{{{x.numerator}}}{{{x.denominator}}}"


def dec(x):
    s = f"{float(x):.1f}"
    return s


panels = []
S = []
for step, v in enumerate(ORDER, 1):
    S.append(v)
    cut = sum(w for (i, j), w in W.items() if (i in S) != (j in S))
    a = len(S)
    rc = cut * (F(1, a) + F(1, N - a))
    panels.append((step, v, list(S), cut, rc))

best = min(p[4] for p in panels)
out = [
    "% 第6章 6.7.2：七点图上RatioCut阈值扫描的逐步执行（由 generate.py 生成并用分数复算）。",
    "% 两个单位权三角形 {1,2,3}、{4,5,6} 由单位权桥 3-4 相连，顶点 7 以权 0.6 挂在顶点 2 上。",
    "% 按第二特征向量的坐标依次移入 7,2,1,3,4（5 与 6 坐标相同，留在最后一组）。",
]
for step, v, s, cut, rc in panels:
    out.append(f"%   ({step}) 移入 {v}：S={sorted(s)}，割权 {float(cut):g}，RatioCut={rc}≈{float(rc):.4f}")
out.append("% 蓝色：S；绿色：S 的补；红色粗边：跨组边；蓝色粗描边：本步移入的顶点；红字：到该步为止的最优值。")
out.append(r"""\begin{tikzpicture}[x=1mm,y=1mm,font=\figurefont\footnotesize,text=FigureInk,
  vS/.style={circle,draw=FigureBlue,fill=FigureBlueFill,line width=.9pt,minimum size=5mm,inner sep=0pt,font=\figurefont\fontsize{7.5}{9}\selectfont},
  vC/.style={circle,draw=FigureGreen,fill=FigureGreenFill,line width=.9pt,minimum size=5mm,inner sep=0pt,font=\figurefont\fontsize{7.5}{9}\selectfont},
  vN/.style={vS,draw=FigureBlue,line width=1.9pt},
  edge/.style={draw=FigureStroke,line width=.7pt},
  cutedge/.style={draw=FigureRed,line width=1.5pt},
  lab/.style={font=\figurefont\fontsize{7.5}{9}\selectfont,align=center},
  note/.style={font=\FigureNoteFont\fontsize{7.5}{9}\selectfont,text=FigureMuted,align=left}]""")
PITCH_X, PITCH_Y = 36, 33
for idx, (step, v, s, cut, rc) in enumerate(panels):
    col, row = idx % 3, idx // 3
    ox, oy = col * PITCH_X, -row * PITCH_Y
    out.append(rf"\begin{{scope}}[shift={{({ox},{oy})}}]")
    for u in range(1, 8):
        style = "vN" if u == v else ("vS" if u in s else "vC")
        x, y = POS[u]
        out.append(rf"  \node[{style}] (v{u}) at ({x},{y}) {{${u}$}};")
    for (i, j), w in W.items():
        st = "cutedge" if (i in s) != (j in s) else "edge"
        out.append(rf"  \draw[{st}] (v{i})--(v{j});")
    rc_s = frac(rc) if rc.denominator != 1 else str(rc)
    rc_txt = dec(rc) if rc.denominator in (1, 2, 5, 10) else rf"{rc_s}\approx{float(rc):.2f}"
    colour = r"\color{FigureRed}" if rc == best else ""
    out.append(rf"  \node[lab,anchor=north] at (11.25,-4) {{({step}) 移入${v}$，割权${float(cut):g}$\\{colour}RatioCut${{}}={rc_txt}$}};")
    out.append(r"\end{scope}")
# 图例放在第二行第三格
lx, ly = 2 * PITCH_X - 3, -PITCH_Y + 14
out.append(rf"""\begin{{scope}}[shift={{({lx},{ly})}}]
  \node[vS,minimum size=3.6mm] at (0,0) {{}}; \node[note,anchor=west] at (2.8,0) {{属于$S$}};
  \node[vC,minimum size=3.6mm] at (0,-5) {{}}; \node[note,anchor=west] at (2.8,-5) {{属于$\bar S$}};
  \node[vN,minimum size=3.6mm] at (0,-10) {{}}; \node[note,anchor=west] at (2.8,-10) {{本步移入}};
  \draw[cutedge] (-1.8,-15)--(1.8,-15); \node[note,anchor=west] at (2.8,-15) {{跨组边}};
\end{{scope}}""")
out.append(r"\end{tikzpicture}")
Path(__file__).with_name("figure.tex").write_text("\n".join(out) + "\n")
