"""Analytic teaching diagrams for Chapter 3. No random or empirical data.

Run with Python from any directory. Each output has its own formula/sampling
record and is drawn at its final book width. Geometry is analytic, not artwork.
"""
from pathlib import Path
import importlib.util
import json
import warnings
import os
ROOT = next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
os.environ.setdefault('MPLCONFIGDIR',str(ROOT/'build/ch3-figures/mpl-cache'))
import numpy as np
from matplotlib import colors
from matplotlib.patches import Polygon, Rectangle, FancyArrowPatch
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

ROOT = next(p for p in Path(__file__).resolve().parents
            if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
spec = importlib.util.spec_from_file_location('chapter_figure_support',
    ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py')
s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
OUT = Path(__file__).resolve().parent
RECORDS = []
s.configure()

def axes2(ax, xlabel='$x$', ylabel='$y$'):
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.tick_params(length=2.5, width=.6)
    ax.grid(False)

def panel(ax, letter):
    ax.set_title('('+letter+')', loc='left', pad=4)

def axes3(ax, zlim=None):
    ax.set_xlabel('$x$', labelpad=-1)
    ax.set_ylabel('$y$', labelpad=-1)
    ax.set_zlabel('$z$', labelpad=-1)
    ax.set_xticks([-1,0,1]); ax.set_yticks([-1,0,1])
    ax.tick_params(labelsize=7, pad=0)
    ax.grid(False)
    for axis in (ax.xaxis, ax.yaxis, ax.zaxis):
        axis.pane.fill = False
        axis.pane.set_edgecolor(s.GRID)
    ax.view_init(elev=24, azim=-56)
    if zlim is not None: ax.set_zlim(*zlim)

def arrow(ax, p, q, color, **kwargs):
    ax.add_patch(FancyArrowPatch(p, q, arrowstyle='-|>', mutation_scale=9,
                                linewidth=.85, color=color, **kwargs))

def save(fig, name, facts):
    # Keep the canvas fixed: no tight bounding-box rescaling of final fonts.
    fig.canvas.draw()
    for ext in ('pdf','png'):
        fig.savefig(OUT/(name+'.'+ext), dpi=360, facecolor='white')
    record = dict(name=name, method='Matplotlib', width_mm=fig.get_figwidth()*25.4,
        height_mm=fig.get_figheight()*25.4, reference_width_mm=fig.get_figwidth()*25.4,
        scale=1, png_dpi=360, facts=facts,
        source='generate.py', data_source='exact analytic formulas; no empirical observations',
        random_sampling=False, filtering='none; singular points and plotting windows declared per figure',
        **s.provenance())
    (OUT/(name+'.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    RECORDS.append(record); s.plt.close(fig)

def sequence_tail():
    n=np.arange(1,41); v=(-1.)**n/n
    fig,ax=s.figure(112,53)
    ax.axhspan(-.12,.12,color=s.GREEN_FILL)
    ax.axhline(0,color=s.STROKE,lw=.6)
    ax.axhline(.12,color=s.GREEN,lw=.6,ls='--'); ax.axhline(-.12,color=s.GREEN,lw=.6,ls='--')
    ax.axvline(9,color=s.MUTED,lw=.6,ls=':')
    ax.scatter(n[:8],v[:8],s=11,color=s.RED)
    ax.scatter(n[8:],v[8:],s=11,color=s.BLUE)
    axes2(ax,'$n$','$x_n$'); ax.set(xlim=(0,41),ylim=(-1.07,.58))
    ax.set_xticks([1,9,20,40],['1','$N=9$','20','40'])
    ax.set_yticks([-1,-.12,0,.12,.5],['−1','$-\\varepsilon$','0','$\\varepsilon$','0.5'])
    save(fig,'sequence-tail',{'formula':'x_n=(-1)^n/n','n':'all integers 1..40',
        'epsilon':.12,'N':9,'analytic_check':'1/n <= 1/9 < 0.12 for every n>=9; finite drawing does not prove a limit'})

def series_sums():
    n=np.arange(1,81); h=np.cumsum(1/n); a=np.cumsum((-1.)**(n+1)/n)
    fig,axs=s.figure(169,54,ncols=2)
    axs[0].plot(n,1/n,color=s.BLUE)
    axs[0].plot(n,(-1.)**(n+1)/n,color=s.GREEN,lw=.8)
    axs[0].axhline(0,color=s.STROKE,lw=.6)
    axs[1].plot(n,h,color=s.BLUE,label=r'$\sum_{k=1}^N1/k$')
    axs[1].plot(n,a,color=s.GREEN,label=r'$\sum_{k=1}^N(-1)^{k+1}/k$')
    axs[1].axhline(np.log(2),color=s.MUTED,ls='--',lw=.6)
    axs[1].legend(loc='center right')
    for ax,letter in zip(axs,'ab'):
        panel(ax,letter); ax.set_xlim(1,80); ax.set_xticks([1,20,40,80])
    axes2(axs[0],'$n$','$a_n$'); axes2(axs[1],'$N$','$S_N$')
    save(fig,'series-terms-sums',{'n':'integers 1..80','terms':['1/n','(-1)^(n+1)/n'],
        'partial_sums':'exact finite cumulative sums','reference':'log(2)',
        'logical_role':'terms tending to zero are necessary but not sufficient for series convergence; proof remains in text'})

def epsilon_delta():
    fig,ax=s.figure(112,62); x=np.linspace(.3,1.5,601)
    ax.axhspan(.45,1.55,color=s.GREEN_FILL)
    ax.axvspan(.8,1.2,color=s.BLUE_FILL)
    for val in [.45,1.55]:ax.axhline(val,color=s.GREEN,ls='--',lw=.6)
    for val in [.8,1.2]:ax.axvline(val,color=s.BLUE,ls='--',lw=.6)
    lo=x<1; hi=x>1
    ax.plot(x[lo],x[lo]**2,color=s.BLUE); ax.plot(x[hi],x[hi]**2,color=s.BLUE)
    ax.plot(1,1,'o',mfc='white',mec=s.BLUE,ms=4)
    ax.plot(1,2,'o',color=s.RED,ms=4)
    ax.annotate('$L$',(1,1),xytext=(6,-12),textcoords='offset points')
    ax.annotate('$f(a)$',(1,2),xytext=(5,4),textcoords='offset points')
    ax.set(xlim=(.3,1.5),ylim=(0,2.45))
    ax.set_xticks([.8,1,1.2],['$a-\\delta$','$a$','$a+\\delta$'])
    ax.set_yticks([.45,1,1.55],['$L-\\varepsilon$','$L$','$L+\\varepsilon$'])
    axes2(ax)
    save(fig,'epsilon-delta-band',{'formula':'f(x)=x^2 for x!=1; f(1)=2',
        'a':1,'L':1,'epsilon':.55,'delta':.2,'sampling':'601 uniform abscissae, split at x=1',
        'analytic_check':'0<|x-1|<0.2 implies |x^2-1|<0.44<0.55',
        'point_value':'filled (1,2) is excluded from the punctured limit condition'})

def mean_value():
    fig,ax=s.figure(112,53); x=np.linspace(0,1,401)
    ax.plot(x,x*x,color=s.BLUE)
    ax.plot([0,1],[0,1],color=s.GREEN,ls='--')
    xx=np.array([.05,1.])
    ax.plot(xx,xx-.25,color=s.RED,ls='-.')
    ax.scatter([0,.5,1],[0,.25,1],s=14,color=[s.BLUE,s.RED,s.BLUE])
    ax.set(xlim=(-.03,1.03),ylim=(-.24,1.07))
    ax.set_xticks([0,.5,1],['$a=0$','$c$','$b=1$'])
    ax.set_yticks([0,.25,1],['0','$f(c)$','1'])
    axes2(ax)
    save(fig,'mean-value-parallel',{'formula':'f(x)=x^2 on [0,1]','secant':'y=x',
        'c':.5,'tangent':'y=x-1/4','check':'f_prime(c)=1=(f(1)-f(0))/(1-0)'})

def riemann_bounds():
    fig,axs=s.figure(169,56,ncols=2)
    xx=np.linspace(0,1,401)
    for ax,n,letter in zip(axs,[4,8],'ab'):
        edges=np.linspace(0,1,n+1)
        for a,b in zip(edges[:-1],edges[1:]):
            ax.add_patch(Rectangle((a,0),b-a,a*a,facecolor=s.BLUE_FILL,edgecolor=s.BLUE,lw=.6))
            ax.add_patch(Rectangle((a,a*a),b-a,b*b-a*a,facecolor=s.GREEN_FILL,edgecolor=s.GREEN,lw=.6))
        ax.plot(xx,xx**2,color=s.INK)
        panel(ax,letter);ax.text(.04,.92,'$n='+str(n)+'$',transform=ax.transAxes)
        axes2(ax);ax.set(xlim=(0,1),ylim=(0,1.07),xticks=[0,.5,1],yticks=[0,.5,1])
    save(fig,'riemann-upper-lower',{'formula':'f(x)=x^2 on [0,1]','partitions':[4,8],
        'lower':'left endpoint square','upper':'right endpoint square',
        'exact_gap':'U_n-L_n=1/n','sampling':'401 points for curve; exact analytic rectangle heights'})

def accumulation():
    fig,axs=s.figure(169,55,ncols=2); t=np.linspace(0,1,401); x=.4; h=.2
    axs[0].plot(t,2*t,color=s.BLUE)
    ts=np.linspace(x,x+h,81);axs[0].fill_between(ts,0,2*ts,color=s.GREEN_FILL)
    axs[0].vlines([x,x+h],0,[2*x,2*(x+h)],color=s.GREEN,lw=.75)
    axs[1].plot(t,t*t,color=s.BLUE)
    axs[1].plot([x,x+h],[x*x,(x+h)**2],color=s.GREEN,ls='--')
    axs[1].scatter([x,x+h],[x*x,(x+h)**2],color=s.GREEN,s=14)
    axs[1].annotate('',(.72,(x+h)**2),(.72,x*x),arrowprops={'arrowstyle':'|-|','color':s.GREEN,'lw':.75})
    axs[1].text(.76,.24,'$\\Delta F$',color=s.INK)
    for ax,letter in zip(axs,'ab'):
        panel(ax,letter);ax.set_xlim(0,1)
        ax.set_xticks([0,x,x+h,1],['0','$x$','$x+h$','1'])
    axes2(axs[0],'$t$','$f(t)$'); axes2(axs[1],'$x$','$F(x)$')
    save(fig,'accumulation-increment',{'f':'2t','F':'x^2','x':x,'h':h,
        'area':.2,'increment':.2,'sampling':'401 points; shaded interval [0.4,0.6]',
        'finite_difference':'Delta F/h=1 at h=0.2; derivative limit as h->0 is f(0.4)=0.8, not equality at finite h'})

def improper():
    fig,axs=s.figure(169,56,ncols=2)
    x=np.linspace(0,6,601); y=np.exp(-x)
    axs[0].plot(x,y,color=s.BLUE)
    axs[0].fill_between(x,0,y,where=x<=2,color=s.BLUE_FILL)
    axs[0].fill_between(x,0,y,where=x>=2,color=s.GREEN_FILL)
    axs[0].axvline(2,color=s.GREEN,lw=.6,ls='--')
    axs[0].set(xlim=(0,6),ylim=(0,1.05),xticks=[0,2,6],xticklabels=['0','$R$','6'])
    z=np.geomspace(.01,1,601); w=1/np.sqrt(z)
    axs[1].plot(z,w,color=s.BLUE)
    axs[1].fill_between(z,0,w,where=z>=.09,color=s.BLUE_FILL)
    axs[1].fill_between(z,0,w,where=z<=.09,color=s.GREEN_FILL)
    axs[1].axvline(.09,color=s.GREEN,lw=.6,ls='--')
    axs[1].set(xlim=(0,1),ylim=(0,10.3),xticks=[0,.09,.5,1],xticklabels=['0','$\\varepsilon$','0.5','1'])
    for ax,letter in zip(axs,'ab'):panel(ax,letter);axes2(ax,'$x$','$f(x)$')
    save(fig,'improper-two-truncations',{'left':'exp(-x), displayed [0,6], R=2, full discarded tail exp(-2)',
        'right':'x^(-1/2), displayed [0.01,1], epsilon=0.09; (0,0.01) omitted only from rendering',
        'right_full_discarded_integral':'2 sqrt(epsilon)=0.6',
        'sampling':'601 uniform / geometric abscissae respectively','interpretation':'finite plotting window, not finite integration domain'})

def first_index_below(x, eps):
    """Smallest n>=1 with x**n < eps, by exact integer search (0<x<1)."""
    n=1
    while x**n>=eps: n+=1
    return n

def convergence_modes():
    eps=.12; fig,axs=s.figure(169,60,ncols=2)
    x=np.linspace(0,1,801); xo=np.linspace(0,.9995,801)
    for ax,title in zip(axs,['一致收敛','逐点收敛']):
        # Band drawn over the plotted domain only, leaving the right margin for labels.
        ax.fill_between([0,1.04],-eps,eps,color=s.GREEN_FILL,lw=0)
        ax.hlines([-eps,eps],0,1.04,color=s.GREEN,ls='--',lw=.6)
        ax.hlines(0,0,1.04,color=s.STROKE,lw=.6)
        ax.set(xlim=(0,1.04),ylim=(-.2,1.06))
        ax.set_yticks([-eps,0,eps,.5,1],['$-\\varepsilon$','0','$\\varepsilon$','0.5','1'])
        ax.set_title(title,loc='center',pad=4)
    panel(axs[0],'a'); panel(axs[1],'b')
    # (a) g_n(x)=x/n: sup error 1/n, so one N works for all x.
    N=next(n for n in range(1,100) if 1/n<eps)
    styles={2:(s.BLUE,'-',1.1),4:(s.PURPLE,'--',1.1),N:(s.RED,'-',1.4),16:(s.RED,'-.',1.1)}
    for n,(c,ls,lw) in styles.items():
        axs[0].plot(x,x/n,color=c,ls=ls,lw=lw)
        lab='$n=N='+str(n)+'$' if n==N else '$n='+str(n)+'$'
        dy={N:1.5,16:-1.5}.get(n,0)
        axs[0].annotate(lab,(1,1/n),xytext=(3,dy),textcoords='offset points',ha='left',va='center',color=s.INK,fontsize=7.5)
    axes2(axs[0],'$x$','$g_n(x)$'); axs[0].set_xticks([0,.5,1],['0','0.5','1'])
    axs[0].set(xlim=(0,1.2),ylim=(-.2,.58)); axs[0].spines['bottom'].set_bounds(0,1.04)
    axs[0].set_yticks([-eps,0,eps,.5],['$-\\varepsilon$','0','$\\varepsilon$','0.5'])
    # (b) f_n(x)=x^n on [0,1): N depends on x; every f_n leaves the band.
    ns=[2,8,32]; cols=[s.BLUE,s.PURPLE,s.RED]; lss=['-','--','-.']
    x1,x2=.5,.9; N1,N2=first_index_below(x1,eps),first_index_below(x2,eps)
    exits={n:eps**(1/n) for n in ns}
    for xi in (x1,x2): axs[1].axvline(xi,color=s.MUTED,ls=':',lw=.6)
    for n,c,ls in zip(ns,cols,lss):
        axs[1].plot(xo,xo**n,color=c,ls=ls,label='$n='+str(n)+'$')
        axs[1].plot(exits[n],eps,'o',mfc='white',mec=c,ms=3.2,mew=.8,zorder=4)
        axs[1].plot([x1,x2],[x1**n,x2**n],'o',color=c,ms=2.6,zorder=4)
    axs[1].plot(1,1,'o',mfc='white',mec=s.INK,ms=3.2,mew=.8,zorder=4)
    axs[1].legend(loc='upper left',bbox_to_anchor=(0,1),handlelength=2.2)
    axs[1].text(x1+.012,.97,'$N(x_1)='+str(N1)+'$',ha='left',va='top',fontsize=7.5)
    axs[1].text(x2-.012,.97,'$N(x_2)='+str(N2)+'$',ha='right',va='top',fontsize=7.5)
    axes2(axs[1],'$x$','$f_n(x)$')
    axs[1].set_xticks([0,x1,x2,1],['0','$x_1$','$x_2$','1'])
    save(fig,'convergence-modes',{
        'epsilon':eps,
        'band':'|value-0|<epsilon, i.e. (-epsilon, epsilon) around the limit function 0',
        'left':{'formula':'g_n(x)=x/n on [0,1]','limit':'0','sup_error':'1/n',
            'n':list(styles),'N_epsilon':N,'N_check':'1/8=0.125>=0.12, 1/9=0.111<0.12; for n>=9 the whole graph lies in the band',
            'emphasis':'n=N=9 drawn thicker'},
        'right':{'formula':'f_n(x)=x^n on [0,1)','limit':'0 (continuous on [0,1))','n':ns,
            'x1':x1,'x2':x2,'N_x1':N1,'N_x2':N2,
            'N_rule':'smallest n with x^n<epsilon; then x^m<epsilon for all m>=n',
            'N_check':'0.5^3=0.125, 0.5^4=0.0625; 0.9^20=%.4f, 0.9^21=%.4f'%(.9**20,.9**21),
            'values_at_x1':{str(n):float('%.4g'%(x1**n)) for n in ns},'values_at_x2':{str(n):float('%.4g'%(x2**n)) for n in ns},
            'exit_points':{str(n):round(v,4) for n,v in exits.items()},
            'exit_rule':'x=epsilon^(1/n): f_n(x)>=epsilon for x>=epsilon^(1/n), so sup_{[0,1)} f_n=1 for every n',
            'domain_marker':'open circle at (1,1): x=1 excluded'},
        'sampling':'801 uniform points on [0,1] (left) and [0,0.9995] (right; 0.9995^32=0.984); N and exit points computed analytically'})

def joint_paths():
    fig,axs=s.figure(169,61,ncols=2)
    u=np.linspace(0,1,251); X,Y=np.meshgrid(u,u); den=X**4+Y**2
    Z=np.divide(X*X*Y,den,out=np.zeros_like(X),where=den>0)
    cmap=colors.LinearSegmentedColormap.from_list('bookblue',['#FFFFFF',s.BLUE_FILL,s.BLUE])
    im=axs[0].pcolormesh(X,Y,Z,vmin=0,vmax=.5,cmap=cmap,shading='nearest',rasterized=True)
    axs[0].plot(u,u,color=s.GREEN,ls='--');axs[0].plot(u,u*u,color=s.RED)
    axs[0].plot(u,np.zeros_like(u),color=s.INK,lw=.75)
    axs[0].scatter([0],[0],color=s.INK,s=10)
    axs[0].set(xlim=(0,1),ylim=(0,1),aspect='equal')
    fig.colorbar(im,ax=axs[0],ticks=[0,.25,.5],fraction=.05,pad=.025)
    t=np.geomspace(.001,1,401)
    axs[1].plot(t,t/(1+t*t),color=s.GREEN,ls='--',label='$y=x$')
    axs[1].plot(t,np.full_like(t,.5),color=s.RED,label='$y=x^2$')
    axs[1].plot(t,np.zeros_like(t),color=s.INK,lw=.75,label='$y=0$')
    axs[1].set(xscale='log',xlim=(.001,1),ylim=(-.03,.55),yticks=[0,.25,.5])
    axs[1].legend(loc='center left')
    axes2(axs[0]);axes2(axs[1],'$t$','$g(t,y(t))$')
    for ax,letter in zip(axs,'ab'):panel(ax,letter)
    save(fig,'joint-limit-paths',{'formula':'g=x^2*y/(x^4+y^2) off origin, g(0,0)=0',
        'map':'251x251 uniform coordinates on [0,1]^2; scalar range [0,1/2]',
        'paths':{'y=0':'0','y=x':'t/(1+t^2)','y=x^2':'1/2'},
        'path_sampling':'401 geometric t in [0.001,1]','meaning':'different path limits disprove a joint limit; finite straight paths cannot prove it'})

def gradient():
    fig,ax=s.figure(112,71); x=np.linspace(-.1,2.4,301);y=np.linspace(.5,3.2,301)
    X,Y=np.meshgrid(x,y); Z=X*X+X*Y+Y*Y
    cs=ax.contour(X,Y,Z,levels=[1,3,7,13,21],colors=s.BLUE,linewidths=.75)
    ax.clabel(cs,inline=True,fontsize=7,fmt='%g',manual=[(.3,.8),(.35,1.55),(.25,2.5),(1.8,2.3),(2.2,3.06)])
    a=np.array([1.,2.]);g=np.array([4.,5.])
    arrow(ax,a,a+.15*g,s.GREEN);arrow(ax,a,a+np.array([.65,0]),s.RED)
    tangent=np.array([5.,-4.])*.13
    ax.plot([*(a-tangent)[:1],*(a+tangent)[:1]],[a[1]-tangent[1],a[1]+tangent[1]],color=s.MUTED,ls='--',lw=.75)
    ax.scatter(*a,s=17,color=s.INK);ax.annotate('$a$',a,xytext=(-10,-12),textcoords='offset points')
    ax.text(1.62,2.84,r'$\nabla f(a)$',color=s.GREEN)
    ax.text(1.69,1.92,'$u$',color=s.RED)
    ax.set(xlim=(-.1,2.4),ylim=(.5,3.2),aspect='equal',xticks=[0,1,2],yticks=[1,2,3])
    axes2(ax)
    save(fig,'gradient-level-curves',{'formula':'f=x^2+xy+y^2','a':[1,2],'gradient':[4,5],
        'arrow_scale':.15,'unit_test_direction':[1,0],'tangent_direction':[5,-4],
        'check':'dot((4,5),(5,-4))=0; contour at a is f=7',
        'sampling':'301x301 for contours; exact vectors','interpretation':'gradient is normal to a regular level curve and maximizes directional derivative among unit directions'})

def linearization():
    fig=s.plt.figure(figsize=(169/25.4,69/25.4),layout='constrained')
    ax=fig.add_subplot(121,projection='3d');ax2=fig.add_subplot(122)
    h=np.linspace(-.45,.45,21);H,K=np.meshgrid(h,h);P=7+4*H+5*K;F=P+H*H+H*K+K*K
    ax.plot_surface(H,K,F,color=s.BLUE_FILL,shade=False,edgecolor=s.BLUE,linewidth=.25)
    ax.plot_wireframe(H,K,P,color=s.MUTED,linewidth=.6,rstride=5,cstride=5)
    ax.scatter([0],[0],[7],color=s.INK,s=9)
    axes3(ax);ax.set_xlabel('$h$',labelpad=-1);ax.set_ylabel('$k$',labelpad=-1)
    ax.set(xlim=(-.5,.5),ylim=(-.5,.5),zlim=(2.8,12));ax.set_zlabel('$f$',labelpad=-1);ax.set_xticks([-.4,0,.4]);ax.set_yticks([-.4,0,.4])
    r=np.linspace(0,.5,301)
    ax2.fill_between(r,.5*r,1.5*r,color=s.BLUE_FILL)
    for c,col,ls in zip([.5,1,1.5],[s.MUTED,s.BLUE,s.GREEN],[':','-','--']):
        ax2.plot(r,c*r,color=col,ls=ls,lw=.85)
    ax2.set(xlim=(0,.5),ylim=(0,.8));axes2(ax2,'$r$',r'$|R|/r$')
    panel(ax,'a');panel(ax2,'b')
    save(fig,'total-differential-remainder',{'formula':'f=x^2+xy+y^2 at a=(1,2)',
        'plane':'P=7+4h+5k','remainder':'R=h^2+hk+k^2',
        'left_sampling':'21x21 grid in [-0.45,0.45]^2, exact plane wireframe',
        'right':'r=sqrt(h^2+k^2); every direction satisfies r/2<=R/r<=3r/2; shading is analytic range, not sampled confidence band',
        'uniformity':'3r/2 ->0 independent of direction'})

def hessian():
    fig,axs=s.figure(169,68,ncols=3,subplot_kw={'projection':'3d'})
    v=np.linspace(-1,1,25);X,Y=np.meshgrid(v,v)
    zs=[X*X+2*Y*Y,X*X-Y*Y,X**4+Y**4]
    for ax,Z,letter in zip(axs,zs,'abc'):
        ax.plot_surface(X,Y,Z,color=s.BLUE_FILL,edgecolor=s.BLUE,linewidth=.25,shade=False)
        axes3(ax,(-1.2,3.1));ax.set_zticks([-1,0,2]);ax.set_box_aspect((1,1,1))
        ax.scatter([0],[0],[0],color=s.RED,s=9);panel(ax,letter)
    save(fig,'hessian-local-shapes',{'formulas':['x^2+2y^2','x^2-y^2','x^4+y^4'],
        'Hessian_at_origin':['diag(2,4)','diag(2,-2)','zero matrix'],
        'properties':['strict minimum','saddle','strict minimum despite zero Hessian'],
        'sampling':'25x25 deterministic mesh on [-1,1]^2; common z range [-1.2,3.1]',
        'boundary':'zero/semidefinite Hessian alone is inconclusive, not a certificate of no extremum'})

def jacobian():
    fig,axs=s.figure(169,62,ncols=2)
    T=lambda u,v:np.array([u+.25*v*v,.6*v+.3*u*u])
    q=np.linspace(0,1,201)
    for c in np.linspace(0,1,6):
        axs[0].plot(q,np.full_like(q,c),color=s.GRID,lw=.6);axs[0].plot(np.full_like(q,c),q,color=s.GRID,lw=.6)
        uv=T(q,np.full_like(q,c));axs[1].plot(*uv,color=s.BLUE,lw=.6)
        uv=T(np.full_like(q,c),q);axs[1].plot(*uv,color=s.BLUE,lw=.6)
    a=np.array([.5,.5]);width=.22
    corners=np.array([a+[-width,-width],a+[width,-width],a+[width,width],a+[-width,width]])
    axs[0].add_patch(Polygon(corners,facecolor=s.GREEN_FILL,edgecolor=s.GREEN))
    points=[]
    for u,v in zip(corners,np.roll(corners,-1,axis=0)):
        points.extend(u+(v-u)*np.linspace(0,1,81)[:,None])
    points=np.array(points);mapped=T(points[:,0],points[:,1]).T
    axs[1].add_patch(Polygon(mapped,facecolor=s.GREEN_FILL,edgecolor=s.GREEN))
    J=np.array([[1,.25],[.3,.6]]);Ta=T(*a)
    linear=Ta+(corners-a)@J.T
    axs[1].add_patch(Polygon(linear,facecolor='none',edgecolor=s.INK,linestyle='--',linewidth=.85))
    axs[0].scatter(*a,s=12,color=s.INK);axs[1].scatter(*Ta,s=12,color=s.INK)
    axs[0].annotate('$a$',a,xytext=(3,-12),textcoords='offset points')
    axs[1].annotate('$T(a)$',Ta,xytext=(3,-12),textcoords='offset points')
    axes2(axs[0],'$u$','$v$');axes2(axs[1],'$T_1$','$T_2$')
    for ax,letter in zip(axs,'ab'):panel(ax,letter);ax.set_aspect('equal');ax.set_xlim(-.05,1.3);ax.set_ylim(-.05,1.05)
    save(fig,'jacobian-grid-cell',{'map':'T(u,v)=(u+v^2/4,0.6v+0.3u^2)','a':a.tolist(),
        'Jacobian':J.tolist(),'determinant':float(np.linalg.det(J)),
        'half_side':width,'grid':'6 lines per coordinate, 201 samples per line; 81 samples per cell edge',
        'comparison':'green curved cell is exact map, dashed parallelogram is T(a)+J_T(a)(u-a); not identical at finite size'})

def slicing():
    fig,axs=s.figure(169,58,ncols=2)
    triangle=np.array([[0,0],[1,0],[1,1]])
    for ax in axs:
        ax.add_patch(Polygon(triangle,facecolor=s.BLUE_FILL,edgecolor=s.BLUE))
        ax.set(xlim=(-.05,1.06),ylim=(-.05,1.06),xticks=[0,1],yticks=[0,1],aspect='equal')
        axes2(ax)
    axs[0].add_patch(Polygon([[.62,0],[.68,0],[.68,.68],[.62,.62]],facecolor=s.GREEN_FILL,edgecolor=s.GREEN))
    axs[0].plot([.65,.65],[0,.65],color=s.GREEN,lw=1.1)
    axs[0].text(.68,.28,'$x$',color=s.GREEN)
    axs[1].add_patch(Polygon([[.32,.32],[1,.32],[1,.38],[.38,.38]],facecolor=s.GREEN_FILL,edgecolor=s.GREEN))
    axs[1].plot([.35,1],[.35,.35],color=s.GREEN,lw=1.1)
    axs[1].text(.63,.39,'$y$',color=s.GREEN)
    for ax,letter in zip(axs,'ab'):panel(ax,letter)
    save(fig,'region-slicing-orders',{'region':'0<=y<=x<=1','vertical_slice':.65,'horizontal_slice':.35,
        'displayed_strips':'vertical x in [0.62,0.68], horizontal y in [0.32,0.38]',
        'orders':['integral_0^1 integral_0^x dy dx','integral_0^1 integral_y^1 dx dy'],
        'check':'both integrals of 1 equal 1/2; swapping differential symbols without limits changes region'})

def path_dependence():
    fig,ax=s.figure(112,70);gx,gy=np.meshgrid(np.linspace(-1.1,1.1,9),np.linspace(-.1,1.1,6))
    ax.quiver(gx,gy,-gy,gx,color=s.MUTED,angles='xy',scale_units='xy',scale=4,width=.003)
    t=np.linspace(0,np.pi,301);p=np.c_[np.cos(t),np.sin(t)]
    ax.plot(*p.T,color=s.BLUE,lw=1.3)
    arrow(ax,p[95],p[110],s.BLUE)
    ax.plot([1,-1],[0,0],color=s.GREEN,lw=1.3);arrow(ax,[.2,0],[-.12,0],s.GREEN)
    ax.scatter([1,-1],[0,0],color=s.INK,s=12)
    ax.text(1.01,-.13,'$A$');ax.text(-1.1,-.13,'$B$')
    ax.set(xlim=(-1.25,1.25),ylim=(-.2,1.2),aspect='equal',xticks=[-1,0,1],yticks=[0,1])
    axes2(ax)
    save(fig,'rotation-field-paths',{'field':'F=(-y,x)','paths':['upper unit semicircle (cos t,sin t),t in [0,pi]','diameter (1-2t,0),t in [0,1]'],
        'common_start':[1,0],'common_end':[-1,0],'integrals':[float(np.pi),0],
        'sampling':'301 curve points; 9x6 exact field samples; arrows scaled by fixed factor 1/4',
        'meaning':'same endpoints and smooth field do not imply path independence'})

def surface_area():
    fig=s.plt.figure(figsize=(169/25.4,67/25.4),layout='constrained')
    a=fig.add_subplot(121);b=fig.add_subplot(122,projection='3d')
    a.add_patch(Rectangle((0,0),1,1,facecolor=s.BLUE_FILL,edgecolor=s.BLUE))
    a.add_patch(Rectangle((.4,.3),.25,.25,facecolor=s.GREEN_FILL,edgecolor=s.GREEN))
    for q in [.25,.5,.75]:
        a.axvline(q,color=s.GRID,lw=.6);a.axhline(q,color=s.GRID,lw=.6)
    a.set(xlim=(-.04,1.04),ylim=(-.04,1.04),aspect='equal',xticks=[0,1],yticks=[0,1])
    axes2(a,'$u$','$v$')
    v=np.linspace(0,1,9);U,V=np.meshgrid(v,v)
    b.plot_wireframe(U,V,U+V,color=s.BLUE,linewidth=.6)
    verts=[(.4,.3,.7),(.65,.3,.95),(.65,.55,1.2),(.4,.55,.95)]
    b.add_collection3d(Poly3DCollection([verts],facecolors=s.GREEN_FILL,edgecolors=s.GREEN,linewidths=.8))
    p=np.array([.15,.15,.3])
    b.quiver(*p,.4,0,.4,color=s.INK,arrow_length_ratio=.18,linewidth=.8)
    b.quiver(*p,0,.4,.4,color=s.INK,arrow_length_ratio=.18,linewidth=.8)
    b.text(.58,.1,.7,'$r_u$');b.text(.05,.59,.7,'$r_v$')
    axes3(b,(0,2));b.set(xlim=(0,1),ylim=(0,1));b.set_xticks([0,1]);b.set_yticks([0,1]);b.set_zticks([0,1,2])
    panel(a,'a');panel(b,'b')
    save(fig,'surface-area-stretch',{'parameterization':'r(u,v)=(u,v,u+v), (u,v) in [0,1]^2',
        'partials':[[1,0,1],[0,1,1]],'cross_product':[-1,-1,1],'area_weight':'sqrt(3)',
        'highlighted_cell':'[0.4,0.65]x[0.3,0.55]','sampling':'9x9 exact planar grid',
        'arrows':'both tangent vectors scaled by 0.4; no normal vector is needed for scalar area'})

def field_types():
    fig,axs=s.figure(169,62,ncols=2);gx,gy=np.meshgrid(np.linspace(-1,1,9),np.linspace(-1,1,9))
    t=np.linspace(0,2*np.pi,361)
    for ax,letter in zip(axs,'ab'):
        ax.plot(np.cos(t),np.sin(t),color=s.BLUE,lw=.75)
        ax.set(xlim=(-1.2,1.2),ylim=(-1.2,1.2),aspect='equal',xticks=[-1,0,1],yticks=[-1,0,1])
        axes2(ax);panel(ax,letter)
    axs[0].quiver(gx,gy,gx,gy,color=s.BLUE,angles='xy',scale_units='xy',scale=4,width=.005)
    axs[1].quiver(gx,gy,-gy,gx,color=s.BLUE,angles='xy',scale_units='xy',scale=4,width=.005)
    arrow(axs[0],(1,0),(1.18,0),s.GREEN);arrow(axs[1],(1,0),(1.18,0),s.GREEN)
    save(fig,'divergence-circulation-fields',{'fields':['F=(x,y)','G=(-y,x)'],
        'divergences':[2,0],'planar_curls':[0,2],'unit_circle_fluxes':['2*pi','0'],
        'unit_circle_circulations':['0','2*pi'],'sampling':'9x9 exact field samples, fixed arrow scale 1/4; 361 circle vertices',
        'green_arrows':'outward boundary normals, not field samples'})

def stokes_surfaces():
    fig,axs=s.figure(169,70,ncols=2,subplot_kw={'projection':'3d'})
    t=np.linspace(0,2*np.pi,81); rr=np.linspace(0,1,9);R,T=np.meshgrid(rr,t)
    axs[0].plot_wireframe(R*np.cos(T),R*np.sin(T),np.zeros_like(R),color=s.BLUE,lw=.6,rstride=8,cstride=2)
    ph=np.linspace(0,np.pi/2,11);Th,Ph=np.meshgrid(t,ph)
    axs[1].plot_wireframe(np.sin(Ph)*np.cos(Th),np.sin(Ph)*np.sin(Th),np.cos(Ph),color=s.GREEN,lw=.6,rstride=2,cstride=8)
    for ax,letter in zip(axs,'ab'):
        ax.plot(np.cos(t),np.sin(t),np.zeros_like(t),color=s.BLUE,lw=1.2)
        angle=np.pi/4;p=np.array([np.cos(angle),np.sin(angle),0])
        ax.quiver(*p,-.25*np.sin(angle),.25*np.cos(angle),0,color=s.BLUE,arrow_length_ratio=.32,linewidth=1)
        axes3(ax,(0,1.22));ax.set(xlim=(-1.1,1.1),ylim=(-1.1,1.1));ax.set_zticks([0,1]);panel(ax,letter)
    axs[0].quiver(0,0,0,0,0,.6,color=s.INK,arrow_length_ratio=.2)
    axs[0].text(0,0,.67,'$n$')
    p=np.array([.5,0,np.sqrt(.75)])
    axs[1].quiver(*p,*(p*.3),color=s.INK,arrow_length_ratio=.2)
    axs[1].text(.66,0,1.14,'$n$')
    save(fig,'stokes-spanning-surfaces',{'surfaces':['upward unit disk z=0','outward upper unit hemisphere'],
        'shared_boundary':'unit circle, counterclockwise viewed from +z',
        'field':'F=(-y/2,x/2,0)','curl':[0,0,1],'both_fluxes':'pi',
        'sampling':'disk: 81 angles x 9 radii; hemisphere: 81 angles x 11 polar angles',
        'normals':'upward on disk, radial outward on hemisphere; arrows not field values',
        'conditions':'field C1 near both surfaces, same oriented boundary'})

if __name__=='__main__':
    for fn in [sequence_tail,series_sums,epsilon_delta,mean_value,riemann_bounds,
               accumulation,improper,convergence_modes,joint_paths,gradient,linearization,
               hessian,jacobian,slicing,path_dependence,surface_area,field_types,stokes_surfaces]:
        with warnings.catch_warnings(record=True) as ws:
            warnings.simplefilter('always');fn()
            bad=[str(w.message) for w in ws if 'Glyph' in str(w.message) or 'constrained_layout' in str(w.message)]
            if bad:raise RuntimeError(fn.__name__+': '+str(bad))
    (OUT/'generation-manifest.json').write_text(json.dumps(RECORDS,ensure_ascii=False,indent=2)+'\n')
    print('Generated',len(RECORDS),'analytic figures.')
