"""Exact analytic examples migrated from quantitative TikZ plots; no experiments."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
import matplotlib.pyplot as plt
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,RED,MUTED,GREEN, YELLOW,STROKE
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL, note
configure();OUT=Path(__file__).parent
record={'type':'analytic teaching examples, not empirical measurements','style':style_record(),'figures':{}}
def save(fig,name,data):
 prepare_figure(fig)
 for fmt in ('pdf','svg','png'):fig.savefig(OUT/(name+'.'+fmt),dpi=300)
 plt.close(fig);record['figures'][name]=data
x=np.linspace(-2.05,2.05,101);fig,ax=plt.subplots(figsize=(112/25.4,67/25.4));fig.subplots_adjust(left=.14,right=.97,bottom=.17,top=.95)
for m in (-1,0,1):ax.plot(x,m*x-m*m/2,color=MUTED,ls='--',lw=.8)
ax.plot(x,x*x/2,color=BLUE,label='$f(x)=x^2/2$');ax.plot(x,np.maximum.reduce([-x-.5,np.zeros_like(x),x-.5]),color=GREEN,label='三个仿射下界的包络')
ax.scatter([-1,0,1],[.5,0,.5],c=STROKE,s=10,zorder=4);ax.set(xlim=(-2.05,2.05),ylim=(-.6,2.08),xlabel='$x$',ylabel='函数值',xticks=[-1,0,1]);ax.legend(loc='upper center',ncol=1,fontsize=8)
save(fig,'conjugate-affine-envelope',{'formula':'f=x²/2; minorant=m*x-m²/2, m=-1,0,1; envelope=max(minorants)','x':x.tolist()})
base=[[-3.5,0],[0,0],[1,2],[3,0],[4.5,0]]
ops=[('延迟 $x(t-1)$，$E=4$',[[-3.5,0],[1,0],[2,2],[4,0],[4.5,0]]),('反转 $x(-t)$，$E=4$',[[-3.5,0],[-3,0],[-1,2],[0,0],[4.5,0]]),('幅值放大 $2x(t)$，$E=16$',[[-3.5,0],[0,0],[1,4],[3,0],[4.5,0]]),('时间压缩 $x(2t)$，$E=2$',[[-3.5,0],[0,0],[.5,2],[1.5,0],[4.5,0]])]
fig,axs=plt.subplots(2,2,figsize=(169/25.4,112/25.4));fig.subplots_adjust(left=.075,right=.98,bottom=.115,top=.92,wspace=.23,hspace=.5)
for ax,(title,values) in zip(axs.flat,ops):
 b=np.array(base);v=np.array(values);ax.plot(b[:,0],b[:,1],color=BLUE,label='原信号 $x(t)$');ax.plot(v[:,0],v[:,1],color=GREEN,ls='--',label='操作后的信号');ax.set(title=title,xlim=(-3.5,4.5),ylim=(-.25,4.5),xticks=[-3,-1,1,3],yticks=[0,2,4],xlabel='$t$');ax.grid()
axs[0,0].legend(fontsize=8)
save(fig,'signal-basic-operations',{'original':base,'original_energy':4,'operations':ops})
arrivals=np.array([.6,1.8,3.2]);ends=np.r_[0,arrivals,4.35];fig,ax=plt.subplots(figsize=(112/25.4,70/25.4));fig.subplots_adjust(left=.13,right=.96,bottom=.16,top=.92)
ax.step(ends,[0,1,2,3,3],where='post',color=BLUE,label='$N_t$')
for i,(a,b) in enumerate(zip(ends[:-1],ends[1:])):
 ax.plot([a,b],[i-a,i-b],color=GREEN,ls='--',label='$N_t-t$' if i==0 else None)
 if i>0:ax.plot([a,a],[i-1-a,i-a],color=GREEN,ls='--')
ax.set(xlim=(0,4.35),ylim=(-1.55,3.7),xlabel='$t$',ylabel='过程取值');ax.legend();ax.grid(axis='y')
save(fig,'poisson-compensation',{'arrival_times':[.6,1.8,3.2],'rate':1,'construction':'chosen illustrative arrivals, not sampled observations','count':'N_t=count(arrival<=t)','compensated':'N_t-t'})
ks=np.arange(8);us=np.array([0,1,.5,.75,.625,.6875,.65625,.671875]);fig,axs=plt.subplots(1,2,figsize=(169/25.4,80/25.4));fig.subplots_adjust(left=.105,right=.98,bottom=.19,top=.88,wspace=.3)
a=axs[0];a.plot(ks,us,color=BLUE,marker='o',ms=3);a.axhline(2/3,color=MUTED,ls='--',lw=.8);a.set(title='相同初态下的加热输入更新',xlabel='$k$',ylabel='$u_1^{(k)}=u_2^{(k)}$',xticks=[0,2,4,6],yticks=[0,2/3,1]);a.set_yticklabels(['0','$2/3$','1']);a.grid()
a=axs[1];loop=[(1,1),(1,0),(0,0),(0,1),(1,1)]
for p,q in zip(loop[:-1],loop[1:]):a.annotate('',xy=q,xytext=p,arrowprops={'arrowstyle':'->','color':GREEN,'lw':1.1})
t=np.linspace(0,2*np.pi,181);a.plot(.5+.3*np.cos(t),.5+.3*np.sin(t),color=BLUE)
for ang in [0,np.pi]:a.annotate('',xy=(.5+.3*np.cos(ang-.25),.5+.3*np.sin(ang-.25)),xytext=(.5+.3*np.cos(ang),.5+.3*np.sin(ang)),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.1})
a.scatter([.5],[.5],c=BLUE,edgecolors=STROKE,s=25);a.annotate('均衡',(.5,.5),xytext=(0,7),textcoords='offset points',ha='center');a.set(title='匹配硬币的两种循环',xlabel='$p$',ylabel='$q$',xlim=(-.1,1.12),ylim=(-.1,1.12),xticks=[0,.5,1],yticks=[0,.5,1],aspect='equal');a.grid(ls=':');note(a.text(.5,-.24,'蓝色实线：连续梯度流；绿色箭头：同时响应',transform=a.transAxes,ha='center',fontsize=7.5))
save(fig,'game-update-trajectories',{'iterations':ks.tolist(),'both_players':us.tolist(),'limit':2/3,'discrete_cycle':loop,'continuous_orbit':{'center':[.5,.5],'radius':.3,'direction':'clockwise'}})
eps=np.logspace(-4,-1,121);coeff=1e-4/(np.sqrt(2)*eps);response=np.full_like(eps,5e-5)
fig,ax=plt.subplots(figsize=(112/25.4,75/25.4));fig.subplots_adjust(left=.17,right=.97,bottom=.18,top=.95)
ax.loglog(eps,coeff,color=BLUE,label='系数相对变化');ax.loglog(eps,response,color=GREEN,ls='--',label='响应相对扰动');ax.set(xlim=(1e-4,1e-1),ylim=(1e-5,1),xlabel=r'$\widetilde\varepsilon$',ylabel='相对变化');ax.legend();ax.grid(which='major')
save(fig,'coefficient-sensitivity',{'eta':1e-4,'epsilon':eps.tolist(),'coefficient_change':coeff.tolist(),'response_change':response.tolist(),'formula':'|eta|/(sqrt(2)*epsilon); |eta|/2'})
gamma=np.logspace(-3,0,81);epsilon=.02;delta=epsilon**2/(np.hypot(gamma/2,epsilon)+gamma/2);theta=.5*np.degrees(np.arctan2(2*epsilon,gamma))
fig,axs=plt.subplots(1,2,figsize=(169/25.4,70/25.4));fig.subplots_adjust(left=.08,right=.98,bottom=.2,top=.91,wspace=.35)
axs[0].semilogx(gamma,delta,color=BLUE);axs[0].axhline(epsilon,color=MUTED,ls='--');axs[0].set(xlim=(1e-3,1),ylim=(0,.022),xlabel='$\gamma$',ylabel='$\Delta\lambda_{\max}$',yticks=[0,.01,.02])
axs[1].semilogx(gamma,theta,color=GREEN);axs[1].set(xlim=(1e-3,1),ylim=(0,49),xlabel='$\gamma$',ylabel=r'$\theta$（度）',yticks=[0,15,30,45])
for a in axs:a.grid()
save(fig,'gap-direction',{'epsilon':epsilon,'gamma':gamma.tolist(),'max_eigenvalue_increment':delta.tolist(),'angle_degrees':theta.tolist(),'formula':'sqrt((gamma/2)^2+epsilon^2)-gamma/2; theta=atan(2epsilon/gamma)/2'})
(OUT/'data-and-sources.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
