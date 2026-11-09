from pathlib import Path
import sys
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, YELLOW, RED, PURPLE, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
import numpy as np
HERE = Path(__file__).resolve().parent
STROKE = '#4C4D4F'
def panel(fig, left, right, top, bottom, wspace=.25, hspace=.2):
    fig.set_layout_engine(None)
    fig.subplots_adjust(left=left, right=right, top=top, bottom=bottom, wspace=wspace, hspace=hspace)
def tag(fig, ax, s, y=.03):
    p = ax.get_position(); fig.text((p.x0+p.x1)/2, y, s, ha='center', va='bottom')
# 贯穿例的精确二阶矩递推与加性噪声稳态方差公式。
a_=np.array([1.,2.,3.]); c_=a_*(1-np.array([-3.,0.,3.]))
def second_moment(al,be,T=400):
    # d'=d - al*(a d + c) + be*(d-dp)
    S=np.array([1.,1.,1.,1.,1.]) # E d^2,E d dp,E dp^2,E d,E dp ; 起点 x=2,d=1
    S=np.array([1.,1.,1.,1.,1.]); out=[]
    for t in range(T):
        out.append(S[0])
        Edd,Eddp,Edpdp,Ed,Edp=S
        m=np.zeros(5)
        for a,c in zip(a_,c_):
            A=1-al*a+be; B=-be; C=-al*c
            m0=A*A*Edd+B*B*Edpdp+C*C+2*A*B*Eddp+2*A*C*Ed+2*B*C*Edp
            m1=A*Edd+B*Eddp+C*Ed
            m2=Edd
            m3=A*Ed+B*Edp+C
            m4=Ed
            m+=np.array([m0,m1,m2,m3,m4])/3
        S=m
    return np.array(out)
fig,(a,b)=figure(width_mm=112,height_mm=56,ncols=2)
panel(fig,.125,.965,.97,.25,wspace=.3)
y=second_moment(.1,.5); a.semilogy(y,color=GREEN,lw=1.4)
y2=second_moment(.2,0.); a.semilogy(y2,color=YELLOW,lw=1.4)
y3=second_moment(.1,0.); a.semilogy(y3,color=PURPLE,lw=1.2,ls='--')
print('floors HB',y[-1],'SGD .2',y2[-1],28*.2/(6-7*.2),'SGD .1',y3[-1],28*.1/(6-.7))
a.set_xlim(0,60); a.yaxis.set_major_locator(__import__('matplotlib').ticker.LogLocator(subs=[1.],numticks=5)); a.yaxis.set_minor_locator(__import__('matplotlib').ticker.NullLocator()); a.set_xlabel('$t$',labelpad=1); a.set_ylabel('期望目标差',labelpad=1)
al=np.linspace(.002,.3,300); lam=2.; s2=1.
def V(al,be): return al*s2*(1+be)/(lam*(1-be)*(2*(1+be)-al*lam))
b.plot(al/(1-.0),[V(a0,0.)*lam/2 for a0 in al],color=YELLOW,lw=1.4)
b.plot(al/.5,[V(a0,.5)*lam/2 for a0 in al],color=GREEN,lw=1.4)
b.plot(al/.1,[V(a0,.9)*lam/2 for a0 in al],color=PURPLE,lw=1.2)
b.set_xlim(0,.8); b.set_ylim(0,.42); b.set_xlabel(r'$\alpha/(1-\beta)$',labelpad=1); b.set_ylabel('稳态目标差',labelpad=1)
b.text(.16,.14,r'$\beta=0$',fontsize=7.5); b.text(.47,.18,r'$\beta=0.5$',fontsize=7.5); b.text(.62,.095,r'$\beta=0.9$',fontsize=7.5)
tag(fig,a,'(a)'); tag(fig,b,'(b)')
save(fig,HERE,'figure',{'example':'chapter','additive_sigma2':s2,'lambda':lam})
