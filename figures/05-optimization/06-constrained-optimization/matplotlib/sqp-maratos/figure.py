from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]/"sqp-common"))
from sqp_fig import *
HERE = Path(__file__).resolve().parent
x=np.array([.8,.6]); nu=np.array([-1.5]); p,nun=kkt_step(pg(x),pHL(x,nu),pA(x),ph(x)); y=x+p; a=pA(x)
ph_=-a.T@np.linalg.solve(a@a.T,ph(y)); z=y+ph_
fig,axes=figure(width_mm=112,height_mm=62,ncols=2); panels(fig,.08,.99,.985,.22,.26); A,b=axes
X,Y=np.meshgrid(np.linspace(.4,1.4,400),np.linspace(-.3,.9,400)); F=2*(X**2+Y**2-1)-X
A.contour(X,Y,F,levels=[-.95,-.8,-.44,0],colors=BLUE,linewidths=.7,linestyles='solid',zorder=1)
circle(A,r=1.); linline(A,x,a[0],0,span=.72)
arrow(A,x,y); arrow(A,y,z,color=PURPLE); dot(A,x,GREEN); dot(A,y,GREEN); dot(A,z,GREEN,ms=4); dot(A,(1,0))
A.text(.83,.61,'$\\mathbf{x}$',fontsize=8,ha='left'); A.text(1.17,.16,'$\\mathbf{x}+\\mathbf{d}$',fontsize=8); A.text(1.03,-.11,'$\\mathbf{x}^*$',fontsize=8)
A.text(1.12,.015,'$\\hat{\\mathbf{d}}$',color=PURPLE,fontsize=8)
setup(A,(.62,1.32),(-.18,.72),xt=(.75,1,1.25),yt=(0,.25,.5))
for soc,col,mk_,ms_,lab in ((False,YELLOW,'s',3,'无修正'),(True,GREEN,'o',3.2,'二阶修正')):
    L=ls_merit_sqp(x,nu,rho=2.,T=12,f=pf,g=pg,h=ph,A=pA,HL=pHL,soc=soc)
    e=[np.linalg.norm(l['x']-np.array([1,0])) for l in L]; idx=[i for i,v in enumerate(e) if v>1e-15]
    b.semilogy(idx,[e[i] for i in idx],color=col,lw=1.5,marker=mk_,ms=ms_,mew=0,label=lab)
    if soc: es=e;ks=[l['kind'] for l in L[:-1]]
    else: en=e;kn=[(l['kind'],l['alpha']) for l in L[:-1]]
b.legend(loc='lower left',handlelength=1.6,borderaxespad=.2)
setup(b,(-.4,12),(1e-16,3),xt=(0,3,6,9,12),yt=[1e-15,1e-10,1e-5,1],xl='$t$',yl='到解的距离',equal=False); b.minorticks_off()
tags(fig,[A,b])
save(fig,HERE,'figure',{'p':p.tolist(),'x_plus_p':y.tolist(),'soc':ph_.tolist(),'z':z.tolist(),'no_soc':en,'with_soc':es,'kinds_no':kn,'kinds_soc':ks})
