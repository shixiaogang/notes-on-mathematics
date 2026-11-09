from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/05-optimization/05-stochastic-optimization/matplotlib/bo-common'))
from bo_common import *
# 五次读数后的 EI；八个等距起点上的数值爬升（中心差分、回溯）。
xo=np.array(RUN_X[:5]);yo=f(xo);b0=yo.min()
def A(x):
    m,v=posterior(xo,yo,np.atleast_1d(x));return ei(b0,m,np.sqrt(v))
fig,ax=figure(width_mm=100,height_mm=46)
Ag=A(XG);ax.plot(XG,Ag,color=BLUE,lw=1.4)
st=np.linspace(.5,7.5,8);end=[]
for x0 in st:
    x=float(x0)
    for _ in range(300):
        g=float(A(x+1e-4)[0]-A(x-1e-4)[0])/2e-4
        if abs(g)<1e-6: break
        step=.5
        while step>1e-6:
            nx=float(np.clip(x+step*g,0,8))
            if A(nx)[0]>A(x)[0]+1e-4*step*g*g: break
            step*=.5
        else: break
        x=nx
    end.append(x)
end=np.array(end);ax.scatter(st,A(st),s=11,facecolors='white',edgecolors=YELLOW,lw=.9,zorder=4)
ax.scatter(end,A(end),s=13,color=GREEN,lw=0,zorder=5)
best=end[A(end).argmax()];ax.scatter([best],A(best),s=20,color=RED,lw=0,zorder=6)
for a,b in zip(st,end):
    if abs(a-b)>.02:
        ax.annotate('',xy=(b,float(A(b)[0])),xytext=(a,float(A(a)[0])),arrowprops=dict(arrowstyle='->',color=MUTED,lw=.7,shrinkA=2,shrinkB=2))
ax.set_xlim(0,8);ax.set_xticks(range(9));ax.set_ylim(0,Ag.max()*1.2);axes_style(ax,'$x$','EI')
print('starts',st,'ends',np.round(end,3),'vals',np.round(A(end),4),'grid max',XG[Ag.argmax()],Ag.max())
FACTS={'starts':st.tolist(),'ends':end.tolist()}
save(fig, Path(__file__).resolve().parent, 'figure', FACTS)
