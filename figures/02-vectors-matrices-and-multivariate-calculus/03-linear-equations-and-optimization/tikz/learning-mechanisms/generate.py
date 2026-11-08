"""Editable exact teaching schematics, 2026-11-08; no external artwork.
Run this file, then render the sibling .tex files with academic-drawing/render_tikz.py.
All geometry uses the repository palette and embedded 8 pt figure fonts.
"""
from pathlib import Path
HERE=Path(__file__).resolve().parent
HEAD=r'''\begin{tikzpicture}[x=1cm,y=1cm,font=\figurefont\fontsize{8}{10}\selectfont,
 >={Stealth[length=1.5mm]},line width=.7pt,text=FigureInk]
'''
END='\\end{tikzpicture}\n'
def save(name,s): (HERE/(name+'.tex')).write_text(HEAD+s+END)
def matrix(x,y,n=4,size=.5,fill=None,labels=None,cols=None):
 # Matrix brackets carry the contour; white gutters separate meaningful cells.
 # There is no decorative grid in empty or zero regions.
 cols=cols or n;s='';gap=.025
 for i in range(n):
  for j in range(cols):
   c=fill(i,j) if fill else 'white'
   if c!='white':s+=fr'\fill[{c}] ({x+j*size+gap},{y-i*size-gap}) rectangle ++({size-2*gap},-{size-2*gap});'+'\n'
   if labels and (i,j) in labels:s+=fr'\node at ({x+(j+.5)*size},{y-(i+.5)*size}) {{$'+labels[i,j]+'$};\n'
 left=x-.06;right=x+cols*size+.06;top=y+.04;bottom=y-n*size-.04
 s+=fr'\draw[FigureStroke,line width=.75pt] ({left+.16},{top})--({left},{top})--({left},{bottom})--({left+.16},{bottom});'+'\n'
 s+=fr'\draw[FigureStroke,line width=.75pt] ({right-.16},{top})--({right},{top})--({right},{bottom})--({right-.16},{bottom});'+'\n'
 return s
save('minimum-norm-representative',r'''
\draw[->,FigureMuted] (0,0)--(5.8,0) node[right] {$x_1$};
\draw[->,FigureMuted] (0,0)--(0,3.3) node[above] {$x_2$};
\draw[FigureBlue,line width=1.1pt] (.5,3.2)--(5.3,.8) node[right] {$\bm x_\star+\ker\bm A$};
\draw[FigureGreen,dashed] (0,0)--(2.9,3.3) node[right] {$\operatorname{range}(\bm A^\top)$};
\draw[->,FigureBlue,line width=1.1pt] (0,0)--(2.56,2.17) node[above left] {$\bm x_\star$};
\draw[->,FigureMuted] (0,0)--(4.8,1.05) node[below right] {$\bm x$};
\draw[->,FigureYellow,line width=1.1pt] (2.56,2.17)--(4.8,1.05) node[midway,above] {$\bm z$};
\fill[FigureBlue] (2.56,2.17) circle (1.5pt);
'''.replace('(2.56,2.17)','(1.48,2.71)').replace('(2.9,3.3)','(1.8,3.3)').replace('(4.8,1.05)','(4.8,1.05)'))
# Replace with exact perpendicular projection onto x+2y=7: x*=(1.4,2.8).
p=HERE/'minimum-norm-representative.tex';s=p.read_text().replace('(.5,3.2)--(5.3,.8)','(.5,3.25)--(5.3,.85)').replace('(1.48,2.71)','(1.4,2.8)').replace('(1.8,3.3)','(1.65,3.3)').replace('(4.8,1.05)','(4.8,1.1)');p.write_text(s)
s=''
for k,x in enumerate([0,3.25,6.5]):
 s+=matrix(x,2.7,n=4,fill=lambda i,j,k=k:'white' if i<j else ('FigureGreenFill' if j<k else 'FigureYellowFill' if j==k and i==j else 'FigureBlueFill' if j==k else 'white'))
 s+=fr'\node at ({x+1},3.15) {{$j={k+1}$}};'
 if k<2:s+=fr'\draw[->,FigureMuted] ({x+2.3},1.7)--({x+2.95},1.7);'
save('cholesky-column-dependencies',s)
s='% Preserve the previous canvas while relocating panel labels.\n\\path[use as bounding box] (-0.077798,0.842169) rectangle (5.277896,3.256401);\n\\begin{scope}[yshift=6mm]\n'+matrix(0,2.5,n=2,size=.8,fill=lambda i,j:'FigureRedFill' if i==j else 'white',labels={(0,0):'0',(0,1):'1',(1,0):'1',(1,1):'0'})
s+=r'\node[anchor=north,inner sep=0pt,font=\fontsize{8}{10}\selectfont] at (.8,.54) {(a)};\draw[->,FigureMuted] (2.2,1.7)--(3.0,1.7);'
s+=matrix(3.6,2.5,n=2,size=.8,fill=lambda i,j:'FigureBlueFill',labels={(0,0):'0',(0,1):'1',(1,0):'1',(1,1):'0'})
s+=r'\node[anchor=north,inner sep=0pt,font=\fontsize{8}{10}\selectfont] at (4.4,.54) {(b)};'
save('ldlt-two-by-two-pivot',s+r'\end{scope}'+'\n')
s=r'\node at (1.0,3.0) {$\bm Q^\top\bm A$};\node at (4.2,3.0) {$\bm x$};\node at (7.1,3.0) {$\bm Q^\top\bm b$};'
# Tall 5x3 matrix: only the upper-triangular block is colored.
s+=matrix(.4,2.6,n=5,cols=3,fill=lambda i,j:'FigureBlueFill' if i<=j else 'white')
s+=r'\draw[FigureStroke,line width=.65pt] (.4,1.1)--(1.9,1.1);\node at (2.7,1.3) {$\cdot$};\node at (5.5,1.3) {$\approx$};\node at (1.15,1.85) {$\bm R$};\node at (1.15,.6) {$\bm0$};'
s+=matrix(3.95,2.1,n=3,cols=1,fill=lambda i,j:'FigureGreenFill')
s+=r'\filldraw[fill=FigureBlueFill,draw=FigureStroke,line width=.75pt] (6.7,2.6) rectangle (7.5,1.1);\filldraw[fill=FigureYellowFill,draw=FigureStroke,line width=.75pt] (6.7,1.1) rectangle (7.5,.1);\node at (7.1,1.85) {$\bm c_1$};\node at (7.1,.6) {$\bm c_2$};'
save('qr-residual-split',s)
s=''
for k,x in enumerate([0,4]):
 s+=matrix(x,3.0,n=4,size=.6,fill=lambda i,j,k=k:'FigureYellowFill' if i==j else ('FigureGreenFill' if k and j<i else 'FigureBlueFill'))
 s+=fr'\node at ({x+1.2},3.5) {{'+['Jacobi','Gauss--Seidel'][k]+'};'
 s+=fr'\draw[->,FigureMuted] ({x+2.75},2.7)--({x+2.75},.8);'
s+=r'\node[anchor=west] at (0,0) {$x_j^{(k)}$};\fill[FigureBlueFill] (-.4,-.1) rectangle (-.15,.15);\node[anchor=west] at (4,0) {$x_j^{(k+1)}$};\fill[FigureGreenFill] (3.6,-.1) rectangle (3.85,.15);'
save('iteration-value-availability',s)
s=r'\node at (1.5,3.0) {$\bm A\bm v_j$};'
for x,t in [(0,r'\bm v_{j-1}'),(1.5,r'\bm v_j'),(3,r'\bm v_{j+1}')]:
 s+=fr'\draw[FigureBlue,fill=FigureBlueFill] ({x-.2},.6) rectangle ({x+.2},2.0);\node at ({x},.2) {{$'+t+'$};'
s+=r'\draw[->,FigureMuted] (1.5,2.65)--(0,2.05);\draw[->,FigureMuted] (1.5,2.65)--(1.5,2.05);\draw[->,FigureMuted] (1.5,2.65)--(3,2.05);\node at (6.4,3.0) {$\bm T_k$};'
s+=matrix(5,2.65,n=5,size=.55,fill=lambda i,j:'FigureBlueFill' if abs(i-j)<=1 else 'white')
save('lanczos-three-directions',s)
save('bicgstab-minimal-residual',r'''
\draw[FigureMuted,dashed] (-.8,2)--(5.6,2);
\draw[->,FigureBlue,line width=1.1pt] (0,0)--(4,2) node[right] {$\bm s_k$};
\draw[->,FigureYellow,line width=1.1pt] (4,2)--(0,2) node[midway,above] {$-\omega_k\bm t_k$};
\draw[->,FigureGreen,line width=1.1pt] (0,0)--(0,2) node[above left] {$\bm r_{k+1}$};
\draw[FigureMuted] (0,1.75)--(.25,1.75)--(.25,2);
\fill[FigureGreen] (0,2) circle (1.5pt);
\node[below] at (0,0) {$\bm0$};
''')
save('inconsistent-row-projections',r'''
\draw[->,FigureMuted] (0,0)--(7,0) node[right] {$x$};
\fill[FigureBlue] (1,0) circle (2pt) node[below=3pt] {$1$};
\fill[FigureYellow] (3.5,0) circle (2pt) node[below=3pt] {$2$};
\fill[FigureGreen] (6,0) circle (2pt) node[below=3pt] {$3$};
\draw[->,FigureGreen,line width=1.1pt] (1,.1) to[bend left=32] (6,.1);
\draw[->,FigureBlue,line width=1.1pt] (6,-.45) to[bend left=28] (1,-.45);
\node[above=7pt] at (3.5,0) {$\hat x$};
''')
s=''
for k,x in enumerate([0,4]):
 s+=matrix(x,3,n=4,size=.6,fill=lambda i,j,k=k:'white' if k and i>j else 'FigureBlueFill')
 for j in range(4):
  for i in range(4):
   if k and i>j:continue
   n=4*j+4-i if k==0 else j*(j+1)//2+i+1
   s+=fr'\node at ({x+(j+.5)*.6},{3-(i+.5)*.6}) {{{n}}};'
 s+=fr'\node at ({x+1.2},3.5) {{'+['Sylvester','Lyapunov'][k]+'};'
save('matrix-equation-solve-order',s)
s='% Preserve the previous canvas while relocating panel labels.\n\\path[use as bounding box] (-0.088670,-0.216599) rectangle (7.716713,3.556181);\n\\begin{scope}[yshift=6mm]\n'
# Two transformations of a deliberately asymmetric triangle; dashed original.
for dx,kind in [(0,'(a)'),(4.4,'(b)')]:
 s+=fr'\node[anchor=north,inner sep=0pt,font=\fontsize{{8}}{{10}}\selectfont] at ({dx+1.65},-.52) {{{kind}}};\draw[->,FigureMuted] ({dx},1.2)--({dx+3.3},1.2);\draw[->,FigureMuted] ({dx+1.6},-.2)--({dx+1.6},2.8);'
 orig=[(.3,.3),(1.4,.3),(.6,1.6)]
 s+='\\draw[FigureMuted,dashed] '+'--'.join(f'({dx+x},{y})' for x,y in orig)+'--cycle;'
 for (x,y),label in zip(orig,['1','2','3']):s+=fr'\node[below left,text=FigureMuted,font=\figurefont\fontsize{{7}}{{8}}\selectfont] at ({dx+x},{y}) {{{label}}};'
 # reflection through x=1.6 vs half-turn around (1.6,1.2)
 transformed=[(3.2-x,y) if kind=='(a)' else (3.2-x,2.4-y) for x,y in orig]
 s+='\\filldraw[fill=FigureBlueFill,draw=FigureBlue] '+'--'.join(f'({dx+x},{y})' for x,y in transformed)+'--cycle;'
 for (x,y),label in zip(transformed,['1','2','3']):s+=fr'\node[above right,font=\figurefont\fontsize{{7}}{{8}}\selectfont] at ({dx+x},{y}) {{{label}}};'
save('reflection-versus-rotation',s+r'\end{scope}'+'\n')
print('Generated 10 editable diagrams')
