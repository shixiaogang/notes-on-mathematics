# coding: utf-8
"""Exact analytic teaching figures; no random samples or external measurements."""
from pathlib import Path
import importlib.util
import json
import numpy as np

ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').is_file() and (p/'tex/book.tex').is_file())
spec=importlib.util.spec_from_file_location('support',ROOT/'figures/00-shared/mathematical-preliminaries-upper/00-shared/comprehension-figures/support.py')
s=importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
OUT=Path(__file__).resolve().parent
records=[]

def finish(fig,name,facts):
    records.append(s.save(fig,OUT,name,facts))

def clean(ax,xlabel,ylabel):
    ax.set_xlabel(xlabel); ax.set_ylabel(ylabel)
    ax.grid(axis='y'); ax.set_axisbelow(True)

# Big O compares bounded ratios; little o requires the ratio to vanish.
n=np.arange(1,201)
fig,ax=s.figure(height_mm=48)
ax.plot(n,(3*n+7)/n,color=s.BLUE,label='(3n+7)/n')
ax.plot(n,n/10/n,color=s.GREEN,linestyle='--',label='(n/10)/n')
ax.plot(n,10*np.sqrt(n)/n,color=s.PURPLE,linestyle=':',label='10√n/n')
ax.axhline(3,color=s.BLUE,linestyle='--',linewidth=.6)
clean(ax,'n','比值'); ax.set_xscale('log'); ax.set_ylim(0,10.4)
ax.legend(loc='upper right',ncol=1)
finish(fig,'asymptotic-ratios',{'domain':'integer n=1,...,200','ratios':['3+7/n','0.1','10/sqrt(n)'],'limits':[3,.1,0],'question':'bounded ratio versus vanishing ratio; finite plot does not prove limits'})

n=np.arange(1,65)
fig,ax=s.figure(height_mm=45)
ax.plot(n,n,color=s.BLUE,label='一元：N',marker='o',markersize=2,markevery=4)
ax.step(n,np.floor(np.log2(n))+1,where='post',color=s.GREEN,label=r'$\lfloor\log_2 N\rfloor+1$')
ax.scatter([1,2,4,8,16,32,64],[1,2,3,4,5,6,7],s=8,color=s.GREEN)
clean(ax,'正整数 N','编码长度'); ax.set_ylim(0,68); ax.legend(loc='upper left')
finish(fig,'encoding-lengths',{'domain':'positive integers N=1,...,64','unary_length':'N symbols','binary_length':'floor(log2(N))+1 bits','sampling':'all 64 integer values; stair segment is a visual guide, not a continuous encoding definition'})

# Use error coordinates because decimal approximants become visually inseparable.
ns=np.arange(0,7); q=np.floor(np.sqrt(2)*10.**ns)/10.**ns
fig,axs=s.figure(height_mm=48,ncols=2,gridspec_kw={'width_ratios':[1,1.15]})
axs[0].plot(ns,q,color=s.BLUE,marker='o',markersize=3)
axs[0].axhline(np.sqrt(2),color=s.GREEN,linestyle='--',linewidth=.8)
axs[0].set_xticks([0,2,4,6]); axs[0].set_xlabel('截断小数位数 n'); axs[0].set_ylabel(r'$q_n\inℚ$')
axs[0].text(.3,1.43,r'$\sqrt{2}∉ℚ$',fontsize=7.5,color=s.GREEN)
axs[1].semilogy(ns,np.sqrt(2)-q,color=s.BLUE,marker='o',markersize=3,label=r'$\sqrt{2}-q_n$')
axs[1].semilogy(ns,10.**(-ns),color=s.GREEN,linestyle='--',label='$10^{-n}$')
axs[1].set_xlabel('n'); axs[1].set_ylabel('实数距离'); axs[1].legend(loc='upper right')
finish(fig,'cauchy-completeness',{'q_n':'floor(10^n sqrt(2))/10^n, n=0,...,6','bound':'0<sqrt(2)-q_n<10^-n','ambient_spaces':'all q_n rational; real limit sqrt(2) is not rational','numerical_precision':'IEEE double; n at most 6, errors well above machine precision'})

fig,ax=s.figure(height_mm=48)
x=np.linspace(0,2.2,400)
ax.plot(x,x/2+1,color=s.BLUE,label='T(x)=x/2+1')
ax.plot(x,x,color=s.GREEN,linestyle='--',label='y=x')
x0=0.
for _ in range(7):
    x1=x0/2+1
    ax.plot([x0,x0,x1],[x0,x1,x1],color=s.PURPLE,linewidth=.8)
    x0=x1
ax.scatter([2],[2],color=s.INK,s=13,zorder=5); ax.text(2.05,1.91,'x*=2',fontsize=7.5)
ax.set(xlim=(-.04,2.24),ylim=(-.04,2.24),xlabel='x',ylabel='y');ax.set_aspect('equal');ax.legend(loc='upper left')
finish(fig,'contraction-cobweb',{'map':'T(x)=x/2+1 on [0,2]','initial':0,'factor':.5,'steps':7,'exact_iterate':'x^(n)=2-2^(1-n)','fixed_point':2,'cobweb':'vertical evaluation T followed by horizontal copy to diagonal'})

fig,ax=s.figure(height_mm=46)
x=np.linspace(0,2.4,600)
ax.plot(x,np.sqrt(x),color=s.BLUE,label='y=√x');ax.plot(x,-np.sqrt(x),color=s.GREEN,linestyle='--',label='y=−√x')
from matplotlib.patches import Rectangle
ax.add_patch(Rectangle((.65,.65),.7,.7,facecolor=s.BLUE_FILL,edgecolor=s.BLUE,linewidth=.7,zorder=0))
ax.scatter([0,1],[0,1],color=[s.RED,s.BLUE],s=15,zorder=4)
ax.annotate('∂F/∂y=0',(0,0),(.2,-.36),fontsize=7.5,arrowprops={'arrowstyle':'-','color':s.MUTED,'linewidth':.6})
ax.text(1.4,.8,'局部选正支',fontsize=7.5,color=s.BLUE)
clean(ax,'x','y');ax.set(xlim=(-.2,2.5),ylim=(-1.65,1.65));ax.legend(loc='lower right')
finish(fig,'implicit-branches',{'equation':'F(x,y)=y^2-x=0','branches':'+sqrt(x), -sqrt(x), x>=0','marked_basepoint':[1,1],'positive_branch_neighborhood':'U=(.65,1.35), V=(.65,1.35); sqrt(U) subset V; negative branch excluded','singular_point':[0,0],'derivative':'F_y=2y; zero at origin'})

fig,axs=s.figure(height_mm=48,ncols=2)
x=np.linspace(-2,2,500)
axs[0].plot(x,x*x,color=s.BLUE);axs[0].axhline(1,color=s.GREEN,linestyle='--',linewidth=.8)
axs[0].fill_between(x,0,x*x,where=np.abs(x)<=1,color=s.BLUE_FILL)
axs[0].plot([-1,1],[0,0],color=s.GREEN,linewidth=2)
axs[0].set(xlim=(-2,2),ylim=(-.15,4.3),xlabel='x',ylabel='F(x)=x²');axs[0].text(-1,3.4,'$K_1=[-1,1]$',fontsize=7.5)
x=np.linspace(-1,4,500);axs[1].plot(x,np.exp(-x),color=s.BLUE)
vals=np.arange(0,5);axs[1].scatter(vals,np.exp(-vals),s=12,color=s.GREEN,zorder=3)
axs[1].annotate('',(3.9,.35),(.6,.35),arrowprops={'arrowstyle':'->','color':s.GREEN,'linewidth':.8})
axs[1].set(xlabel='x',ylabel='$G(x)=e^{-x}$',ylim=(-.1,2.9));axs[1].text(.3,2.2,r'$x_n=n\to\infty$',fontsize=7.5)
finish(fig,'coercive-sublevels',{'coercive_example':'F(x)=x^2; {F<=1}=[-1,1]','noncoercive_example':'G(x)=exp(-x); inf_R G=0 not attained; minimizing sequence x_n=n escapes to infinity','domain':'R for both objectives','scope':'contrasting examples, coercivity is sufficient in the stated existence theorem, not a necessary condition for every minimizer'})

fig,ax=s.figure(height_mm=48)
t=np.arange(0,13)
for eta,col,ls in [(.5,s.BLUE,'-'),(1.5,s.GREEN,'--'),(2.,s.PURPLE,':'),(2.1,s.RED,'-.')]:
    ax.plot(t,(1-eta)**t,color=col,linestyle=ls,marker='o',markersize=2.4,label='η='+str(eta))
clean(ax,'迭代步 t','$w^{(t)}$');ax.set(xticks=[0,3,6,9,12],ylim=(-3.4,3.4));ax.legend(ncol=4,loc='lower center',bbox_to_anchor=(.5,1.0),columnspacing=1.0)
finish(fig,'gradient-step-stability',{'objective':'f(w)=w^2/2; L=1','initial':1,'update':'w^(t)=(1-eta)^t','steps':12,'eta':[.5,1.5,2,2.1],'regimes':'eta<2 contracts; eta=2 equal amplitude; eta>2 diverges'})

fig,ax=s.figure(height_mm=45)
t=np.linspace(0,1.5,300)
ax.plot(t,.75*t,color=s.BLUE,label='f(−tg)=3t/4')
ax.plot(t,-1.25*t,color=s.GREEN,linestyle='--',label='次梯度下界：−5t/4')
ax.scatter([0],[0],s=15,color=s.INK)
clean(ax,'沿负次梯度的步长 t ≥ 0','函数值 / 仿射下界');ax.legend(loc='lower left')
finish(fig,'subgradient-not-descent',{'objective':'f(x,y)=|x|+y/2','point':[0,0],'subgradient':[1,.5],'path':'(-t,-t/2), t>=0','true_value':'3t/4','support_lower_bound':'-||g||^2 t=-5t/4','scope':'valid global lower bound does not guarantee descent direction'})

fig,axs=s.figure(height_mm=49,ncols=2)
w=np.linspace(-1.5,3,700)
for ax,z in zip(axs,[.5,2.]):
    p=max(z-1,0)
    ax.plot(w,np.abs(w)+(w-z)**2/2,color=s.BLUE,label='完整子问题')
    ax.plot(w,np.abs(w),color=s.GREEN,linestyle='--',label='|w|')
    ax.plot(w,(w-z)**2/2,color=s.PURPLE,linestyle=':',label='(w−z)²/2')
    ax.scatter([p],[abs(p)+(p-z)**2/2],color=s.RED,s=14,zorder=5)
    ax.axvline(p,color=s.RED,linewidth=.6,linestyle='--')
    ax.set(xlabel='w',ylim=(0,5.5),xticks=[-1,0,1,2,3]);ax.set_title('z='+str(z)+'，p='+str(int(p)))
axs[0].set_ylabel('子问题目标 / 组成项');axs[1].legend(loc='upper right',fontsize=7.5)
finish(fig,'proximal-balance',{'regularizer':'r(w)=|w|','eta':1,'centres':[.5,2],'minimizers':[0,1],'objective':'|w|+(w-z)^2/2','domain':'w in R; display [-1.5,3]','scope':'exact minimizers verified by soft-threshold optimality; component minima are not minima of sum'})

fig,axs=s.figure(height_mm=48,ncols=2)
rho=np.linspace(0,50,600)
res=16/(16+17*rho);lmax=(17+2*rho+np.sqrt(225+4*rho*rho))/2
axs[0].plot(rho,res,color=s.BLUE);axs[0].set(xlabel='ρ',ylabel='等式残差绝对值',ylim=(0,1.03))
axs[1].plot(rho,lmax,color=s.GREEN);axs[1].set(xlabel='ρ',ylabel='Hessian 最大特征值')
for ax in axs: ax.grid(axis='y');ax.set_axisbelow(True)
finish(fig,'penalty-feasibility-curvature',{'objective':'(w1^2+16w2^2)/2 +rho(w1+w2-1)^2/2','domain':'rho>=0; display [0,50]','exact_solution':'(16rho,rho)/(16+17rho)','absolute_residual':'16/(16+17rho)','maximum_eigenvalue':'(17+2rho+sqrt(225+4rho^2))/2','scope':'larger penalty reduces residual but eventually adds arbitrarily large curvature; no claim that condition number increases monotonically'})

fig,axs=s.figure(height_mm=49,ncols=2)
eta=.5;steps=16
v=np.zeros((steps+1,2));u=np.zeros_like(v);v[0]=u[0]=[.5,0]
A=np.array([[1,-eta],[eta,1.]])
B=np.array([[1-eta*eta,-eta],[eta,1-eta*eta]])
for t in range(steps):v[t+1]=A@v[t];u[t+1]=B@u[t]
axs[0].plot(v[:,0],v[:,1],color=s.BLUE,marker='o',markersize=2,label='同时下降–上升')
axs[0].plot(u[:,0],u[:,1],color=s.GREEN,marker='s',markersize=2,label='外梯度')
axs[0].scatter([0],[0],color=s.INK,s=9);axs[0].set(xlabel='x',ylabel='z');axs[0].set_aspect('equal')
axs[1].semilogy(np.arange(steps+1),np.sum(v*v,axis=1),color=s.BLUE,label='同时下降–上升')
axs[1].semilogy(np.arange(steps+1),np.sum(u*u,axis=1),color=s.GREEN,linestyle='--',label='外梯度')
axs[1].set(xlabel='t',ylabel='x²+z²');axs[1].legend(loc='upper left')
finish(fig,'minimax-rotation',{'objective':'phi(x,z)=xz','eta':eta,'initial':[.5,0],'steps':steps,'simultaneous_matrix':A.tolist(),'extragradient_matrix':B.tolist(),'norm_square_multipliers':[1+eta**2,1-eta**2+eta**4],'simultaneous_scope':'unprojected iterates; after leaving [-1,1]^2 not feasible constrained candidates','extragradient_scope':'all trial and corrected iterates stay in box, so projections are inactive','saddle':[0,0]})

(OUT/'generated-records.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+r'\n')
print('Generated',len(records),'analytic figures')
