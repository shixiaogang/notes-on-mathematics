from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
L=newton_sqp([1.5,.5],[1.],T=7)
P=np.array([l[0] for l in L]); nus=[l[1][0] for l in L]
fig,axes=figure(width_mm=112,height_mm=58,ncols=2); panels(fig,.08,.99,.985,.23,.26); a,b=axes
X,Y=np.meshgrid(np.linspace(.7,1.7,300),np.linspace(.3,1.3,300))
a.contour(X,Y,-X-Y,levels=[-2.8,-2.4,-2,-1.6,-1.2],colors=BLUE,linewidths=.7,linestyles="solid",zorder=1)
circle(a); a.plot(P[:6,0],P[:6,1],color=GREEN,lw=1.4,marker='o',ms=3.6,mew=0,zorder=5); dot(a,(1,1),ms=5)
a.text(1.53,.44,'$\\mathbf{x}^{(0)}$',fontsize=8); a.text(1.28,.76,'$\\mathbf{x}^{(1)}$',fontsize=8); a.text(1.07,1.05,'$\\mathbf{x}^{(2)}$',fontsize=8)
setup(a,(.75,1.7),(.3,1.25),xt=(1,1.5),yt=(.5,1))
t=np.arange(7); d=[np.linalg.norm(P[i]-1) for i in t]; v=[abs(ch(P[i])[0]) for i in t]; r=[np.linalg.norm(cg(P[i])+cA(P[i]).T@np.array([nus[i]])) for i in t]
def cut(y): return [m if m>1e-15 else np.nan for m in y]
b.semilogy(t,cut(d),color=GREEN,lw=1.4,marker='o',ms=3.2,mew=0,label='$\\Vert\\mathbf{x}-\\mathbf{x}^*\\Vert_2$'); b.semilogy(t,cut(v),color=RED,lw=1.4,marker='s',ms=3,mew=0,label='$|h|$'); b.semilogy(t,cut(r),color=PURPLE,lw=1.4,marker='^',ms=3.2,mew=0,label='$\\Vert\\nabla_x\\mathcal{L}\\Vert_2$')
b.legend(loc='lower left',handlelength=1.6,labelspacing=.25,borderaxespad=.2)
setup(b,(-.2,6.2),(1e-16,10),xt=range(0,7),yt=[1e-15,1e-10,1e-5,1],xl='$t$',yl='残差',equal=False); b.minorticks_off()
tags(fig,axes)
save(fig,HERE,'figure',{'iters':P.tolist(),'nu':nus,'dist':d,'h':v,'res':r})
