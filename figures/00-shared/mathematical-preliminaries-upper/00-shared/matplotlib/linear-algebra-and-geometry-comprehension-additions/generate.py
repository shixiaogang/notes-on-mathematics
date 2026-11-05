# coding: utf-8
"""Nine analytic teaching charts. No sampled empirical or random data."""
from pathlib import Path
import sys
import math
import numpy as np
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT/'figures/01-mathematical-preliminaries-upper/00-shared/comprehension-figures'))
from support import figure, save, BLUE, GREEN, PURPLE, RED, INK, MUTED, GRID, BLUE_FILL, GREEN_FILL
D=Path(__file__).resolve().parent


def conjugate_directions():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-.6,4.7,360); y=np.linspace(-1.35,1.35,240)
    xx,yy=np.meshgrid(x,y)
    ax.contour(xx,yy,.5*(xx**2+4*yy**2),levels=[.5,2,4,8],colors=GRID,linewidths=.6)
    points=np.array([[4.,0.],[3.2,-.8],[0.,0.]])
    ax.plot(points[:,0],points[:,1],color=BLUE,marker='o',ms=3)
    for a,b,c in zip(points[:-1],points[1:],[BLUE,GREEN]):
        ax.annotate('',xy=b,xytext=a,arrowprops={'arrowstyle':'->','color':c,'lw':1.1})
    ax.text(4.07,.12,r'$𝐱^{(0)}$');ax.text(3.25,-1.12,r'$𝐱^{(1)}$');ax.text(-.2,.15,r'$𝐱_* = 0$')
    ax.text(3.85,-.55,r'$𝐩$',color=BLUE);ax.text(1.6,-.67,r'$𝐪$',color=GREEN)
    ax.set(xlim=(-.6,4.7),ylim=(-1.35,1.35),xlabel=r'$x_1$',ylabel=r'$x_2$')
    ax.set_xticks([0,2,4]); ax.set_yticks([-1,0,1])
    save(fig,D,'linear-conjugate-directions',{'objective':'phi(x)=0.5*(x1^2+4*x2^2)','A':[[1,0],[0,4]],'p':[1,1],'q':[-4,1],'pTAq':0,'start':[4,0],'line_search_steps':[-.8,.8],'points':points.tolist(),'scope':'Conjugate line-search example, not the CG recurrence from this initial residual.'})


def jordan_accumulation():
    fig,ax=figure(height_mm=46)
    k=np.arange(21);a=.8**k;b=np.zeros_like(a);b[1:]=k[1:]*.8**(k[1:]-1)
    ax.plot(k,b,'o-',color=BLUE,ms=2.5,label=r'$x_1^{(k)}=k\,0.8^{k-1}$')
    ax.plot(k,a,'s--',color=GREEN,ms=2.2,label=r'$x_2^{(k)}=0.8^k$')
    ax.set(xlabel=r'$k$',ylabel='坐标值',xlim=(0,20),ylim=(0,2.25));ax.set_xticks([0,5,10,15,20]);ax.legend(loc='upper right')
    save(fig,D,'linear-jordan-accumulation',{'matrix':[[.8,1],[0,.8]],'initial':[0,1],'k_range':[0,20],'first_coordinate_at_k0':0,'first_coordinate_k_ge_1':'k*0.8**(k-1)','second_coordinate':'0.8**k','data':np.column_stack([k,b,a]).tolist()})


def incomplete_continuous():
    fig,ax=figure(height_mm=46)
    x=np.linspace(0,1,2401)
    for n,c,ls in [(4,BLUE,'-'),(12,GREEN,'--'),(48,PURPLE,':')]:
        fn=np.clip(n*(x-.5),0,1)
        ax.plot(x,fn,color=c,ls=ls,label=rf'$n={n}$')
    ax.plot([0,.5],[0,0],color=INK,lw=.7);ax.plot([.5,1],[1,1],color=INK,lw=.7,label=r'$q$')
    ax.scatter([.5],[0],s=12,c=INK,zorder=6);ax.scatter([.5],[1],s=12,edgecolors=INK,facecolors='white',zorder=6)
    ax.set(xlim=(0,1),ylim=(-.05,1.15),xlabel=r'$x$',ylabel='函数值');ax.set_xticks([0,.5,1]);ax.set_yticks([0,1]);ax.legend(loc='upper left',ncol=2)
    save(fig,D,'functional-incomplete-continuous',{'domain':[0,1],'measure':'Lebesgue dx','q':'I{x>1/2}','fn':'clip(n*(x-1/2),0,1)','n':[4,12,48],'grid_points':2401,'L2_error_squared':'1/(3*n)','conclusion':'C([0,1]) is not complete in the L2 norm; no continuous representative equals q almost everywhere.'})


def orthogonal_functions():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-1,1,401)
    ax.fill_between(x,x,0,where=x>=0,facecolor=BLUE_FILL)
    ax.fill_between(x,x,0,where=x<=0,facecolor=GREEN_FILL)
    ax.plot(x,x,color=BLUE,label=r'$1\cdot x$');ax.axhline(0,color=MUTED,lw=.6)
    ax.text(.54,.37,r'$+1/2$',ha='center');ax.text(-.57,-.45,r'$-1/2$',ha='center')
    ax.set(xlim=(-1,1),ylim=(-1.05,1.1),xlabel=r'$x$',ylabel=r'$f(x)g(x)$');ax.set_xticks([-1,0,1]);ax.set_yticks([-1,0,1])
    ax.text(-.9,.72,r'$f=1,\quad g=x$')
    save(fig,D,'functional-integral-orthogonality',{'domain':[-1,1],'measure':'Lebesgue dx','f':'1','g':'x','inner_product':0,'positive_integral':.5,'negative_integral':-.5,'grid_points':401,'scope':'Orthogonality is a relation between whole functions under the integral inner product.'})


def kernel_pointwise_bound():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-3,3,401)
    ax.plot(x,x,color=BLUE,label=r'$f_1(x)=x$');ax.plot(x,-x,color=GREEN,ls='--',label=r'$f_{-1}(x)=-x$')
    ax.plot(x,np.abs(x),color=PURPLE,ls=':',lw=1.5,label=r'$C_x=|x|$')
    ax.set(xlim=(-3,3),ylim=(-3.1,3.5),xlabel=r'$x$',ylabel='函数值或读取常数');ax.set_xticks([-3,0,3]);ax.set_yticks([-3,0,3]);ax.legend(loc='lower center',ncol=3,bbox_to_anchor=(.5,1),borderaxespad=.1)
    save(fig,D,'functional-pointwise-bound-growth',{'kernel':'K(x,z)=x*z','space':'f_a(x)=a*x, norm=abs(a)','unit_norm_functions':['x','-x'],'optimal_readout_constant':'C_x=abs(x)','display_window':[-3,3],'actual_domain':'R','grid_points':401,'scope':'The finite display window is not the domain; C_x is unbounded on R.'})


def kernel_action():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-1,1,401)
    ax.plot(x,1+x,color=BLUE,label=r'$f(x)=1+x$');ax.plot(x,1+x/3,color=GREEN,ls='--',label=r'$(T_K f)(x)=1+x/3$')
    ax.set(xlim=(-1,1),ylim=(-.05,2.15),xlabel=r'$x$',ylabel='函数值');ax.set_xticks([-1,0,1]);ax.set_yticks([0,1,2]);ax.legend(loc='upper left')
    save(fig,D,'functional-integral-operator-action',{'kernel':'K(x,z)=1+x*z','domain':[-1,1],'measure':'dz/2','f':'1+x','TKf':'1+x/3','calculation':'integral_-1^1 (1+x*z)*(1+z) dz/2 = 1+x/3','grid_points':401})


def invisible_directions():
    fig,ax=figure(height_mm=46)
    x=np.linspace(-1,1,601)
    ax.plot(x,0*x,color=BLUE,label=r'$f=0$');ax.plot(x,x*(x*x-1),color=GREEN,ls='--',label=r'$g=x(x^2-1)$')
    ax.scatter([-1,0,1],[0,0,0],color=INK,s=17,zorder=6)
    ax.set(xlim=(-1.08,1.08),ylim=(-.48,.6),xlabel=r'$x$',ylabel='函数值');ax.set_xticks([-1,0,1]);ax.set_yticks([-.4,0,.4]);ax.legend(loc='upper center',ncol=2)
    save(fig,D,'functional-unseen-observation-direction',{'domain':[-1,1],'f':'0','g':'x*(x*x-1)','observations':[-1,0,1],'values_f':[0,0,0],'values_g':[0,0,0],'grid_points':601,'scope':'Finite observations are noninjective on the polynomial class when degree is unrestricted.'})


def effective_dimension():
    fig,ax=figure(height_mm=46)
    ax.bar([0,1],[.5,.25],color=[BLUE,GREEN],width=.55)
    ax.axhline(1,color=GRID,lw=.75,ls='--')
    ax.text(0,.55,r'$1/2$',ha='center');ax.text(1,.3,r'$1/4$',ha='center')
    ax.set_xticks([0,1],[r'$\mu_1=1$',r'$\mu_2=1/3$']);ax.set_yticks([0,.5,1]);ax.set_ylim(0,1.12)
    ax.set_ylabel(r'$\mu_j/(\mu_j+\lambda)$')
    ax.text(1.6,.8,r'$\lambda=1$');ax.text(1.6,.56,r'$d_{\mathrm{eff}}=3/4$');ax.text(1.6,.28,'代数维数为2');ax.set_xlim(-.6,3.0)
    save(fig,D,'functional-effective-dimension-soft-count',{'mu':[1,1/3],'lambda':1,'contributions':[.5,.25],'effective_dimension':.75,'algebraic_dimension':2,'scope':'Finite affine-kernel example; soft count depends on lambda.'})


def separated_remainder():
    fig,ax=figure(height_mm=46)
    p=np.linspace(-1,1,601)
    for r,c,ls in [(1,BLUE,'-'),(2,GREEN,'--'),(4,PURPLE,':')]:
        approx=sum(p**k/math.factorial(k) for k in range(r))
        err=np.abs(np.exp(p)-approx)
        ax.plot(p,err,color=c,ls=ls,label=rf'$r={r}$')
        assert err.max() <= math.e/math.factorial(r)+1e-12
    ax.set(xlim=(-1,1),ylim=(-.02,1.8),xlabel=r'$p$  $(q=1)$',ylabel=r'$|E-E_r|$');ax.set_xticks([-1,0,1]);ax.set_yticks([0,.5,1,1.5]);ax.legend(loc='upper left',ncol=3)
    save(fig,D,'functional-separated-taylor-remainder',{'E':'exp(p*q)','Er':'sum_(k=0)^(r-1) (p*q)^k/k!','domain_pq':[-1,1],'shown_slice_q':1,'r':[1,2,4],'bound':'e/r! uniformly on [-1,1]^2','grid_points':601,'scope':'Displayed error is a q=1 section; the uniform bound is analytical, not inferred from this plot.'})


if __name__=='__main__':
    for draw in [conjugate_directions,jordan_accumulation,incomplete_continuous,orthogonal_functions,kernel_pointwise_bound,kernel_action,invisible_directions,effective_dimension,separated_remainder]:
        draw()
    print('Generated nine analytic charts.')
