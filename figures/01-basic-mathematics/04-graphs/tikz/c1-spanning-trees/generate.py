import itertools
from pathlib import Path
E=[(1,2),(1,3),(2,3),(2,4),(3,4)]
def conn(es):
    p={v:v for v in range(1,5)}
    def f(x):
        while p[x]!=x:x=p[x]
        return x
    for i,j in es:p[f(i)]=f(j)
    return len({f(v) for v in p})==1
T=[c for c in itertools.combinations(E,3) if conn(c)]
out=[r"""% 贯穿图的全部8棵生成树（由脚本枚举5条边中3条边的连通组合得到）。
% 粗蓝线为树边，浅色虚线为舍弃的原边。
\begin{tikzpicture}[>=Stealth,
  v/.style={circle,draw=FigureStroke,fill=FigureBlueFill,line width=.7pt,minimum size=5mm,inner sep=0pt,font=\figurefont\fontsize{7.5}{9}\selectfont},
  t/.style={draw=FigureBlue,line width=1.5pt},
  o/.style={draw=FigureMuted,dashed,line width=.5pt}]"""]
pos={1:(-.8,0),2:(0,.6),3:(0,-.6),4:(.8,0)}
for k,tree in enumerate(T):
    x=(k%4)*2.5; y=-(k//4)*2.3
    out.append(r"\begin{scope}[xshift=%.2fcm,yshift=%.2fcm]"%(x,y))
    for v,(a,b) in pos.items(): out.append(r"  \node[v] (%d) at (%.2f,%.2f) {$%d$};"%(v,a,b,v))
    for e in E:
        out.append(r"  \draw[%s] (%d)--(%d);"%("t" if e in tree else "o",e[0],e[1]))
    out.append(r"  \node at (0,-1.15) {$T_{%d}$};"%(k+1))
    out.append(r"\end{scope}")
out.append(r"\end{tikzpicture}")
open(Path(__file__).with_name("figure.tex"),"w").write("\n".join(out)+"\n")
for k,t in enumerate(T): print(k+1,t)
