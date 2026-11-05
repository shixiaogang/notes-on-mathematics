"""Analytic teaching figures for the probability and discrete mathematics parts.
Run from any directory. No random experiments and no LaTeX process are used.
All formulas, construction parameters and sampled output data are saved to sources.json.
"""
from pathlib import Path
import sys
import json, math, sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
ROOT=next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0,str(ROOT / 'figures/00-shared/mathematical-generators/matplotlib'))
from plot_style import configure, prepare_figure, style_record
from plot_style import BLUE, RED, YELLOW, MUTED as GRAY, GRID, YELLOW_FILL

configure()
records={}
def panels(n=2,width=169,height=67):
    fig,axs=plt.subplots(1,n,figsize=(width/25.4,height/25.4),layout='constrained')
    axs=np.atleast_1d(axs)
    for ax in axs: ax.set_axisbelow(True);ax.grid(axis='y',color=GRID,lw=.5)
    return fig,axs

def save(fig,name,formula,parameters,data,reference):
    width,height=(np.asarray(fig.get_size_inches())*25.4).tolist()
    prepare_figure(fig)
    for ext in ['pdf','svg','png']:
        fig.savefig(asset_path(HERE, f'{name}.{ext}'),dpi=300)
    plt.close(fig)
    records[name]={'kind':'analytic teaching construction; not experimental data',
        'source':reference,'formula':formula,'parameters':parameters,'data':data,
        'processing':'Direct evaluation; no filtering, stochastic sampling or smoothing.',
        'physical_size_mm':[width,height],'png_dpi':300,'style':style_record(),
        'outputs':[f'{name}.{x}' for x in ['pdf','svg','png']]}

# A density is integrated, whereas the CDF records accumulated probability.
x=np.linspace(-.035,.285,641);dens=np.where((x>=0)&(x<=.25),4.,0.);cdf=np.clip(4*x,0,1)
fig,(a,b)=panels()
a.plot([-.035,0,0,.25,.25,.285],[0,0,4,4,0,0],color=YELLOW)
a.fill_between([.10,.15],0,4,color=YELLOW_FILL)
a.annotate('面积 0.20',(.125,2.1),ha='center',fontsize=8.5)
a.set(xlabel='$x$',ylabel='密度 $f(x)$',title='(a) 高度与区间面积',xlim=(-.035,.285),ylim=(0,4.7))
b.plot(x,cdf,color=YELLOW)
b.vlines([.10,.15],0,[.4,.6],colors=GRAY,ls=':',lw=.6)
b.plot([.10,.15],[.4,.6],'o',color=YELLOW,ms=4)
b.annotate('$F(0.15)-F(0.10)=0.20$',(.14,.51),xytext=(.025,.85),fontsize=8)
b.set(xlabel='$x$',ylabel='分布函数 $F(x)$',title='(b) 累积概率的差',xlim=(-.035,.285),ylim=(0,1.05))
save(fig,'probability-density-cdf','f(x)=4 I(0<=x<=1/4); F(x)=clip(4x,0,1)',
     {'support':[0,.25],'interval':[.1,.15],'probability':.2}, {'x':x.tolist(),'density':dens.tolist(),'cdf':cdf.tolist()},
     '01-probability-theory.tex: uniform density example in probability spaces section')

q=np.array([.5,.4,.1]);p=np.array([.2,.3,.5]);g=np.array([1.,2.,4.]);w=p/q
fig,(a,b)=panels();xx=np.arange(3);bw=.34
for ax,ys1,ys2,l1,l2 in [(a,q,p,'采样分布 $Q$','目标分布 $P$'),(b,q*g,q*w*g,'未加权 $q_jg_j$','加权 $q_jw_jg_j$')]:
    ax.bar(xx-bw/2,ys1,bw,color=BLUE,label=l1);ax.bar(xx+bw/2,ys2,bw,color=RED,label=l2)
    ax.set_xticks(xx,['$a$','$b$','$c$']);ax.set_ylim(bottom=0);ax.legend(loc='upper left')
    for xpos,ys in [(xx-bw/2,ys1),(xx+bw/2,ys2)]:
        for pos,v in zip(xpos,ys):ax.text(pos,v+.025,f'{v:g}',ha='center',va='bottom',fontsize=8)
a.set(title='(a) 目标质量与抽样频率',ylabel='概率质量',ylim=(0,.90))
b.set(title='(b) 对期望的逐项贡献',ylabel='概率 × 函数值',ylim=(0,2.65))
save(fig,'probability-importance-weights','w=p/q; E_Q[g]=sum(q*g); E_P[g]=E_Q[w*g]',
     {'outcomes':['a','b','c']},{'Q':q.tolist(),'P':p.tolist(),'g':g.tolist(),'weights':w.tolist(),'unweighted_contributions':(q*g).tolist(),'weighted_contributions':(p*g).tolist()},
     '01-probability-theory.tex: finite change-of-measure example')

# Both the transient state distribution and the exact stationary variance are deterministic formulas.
t=np.arange(31);pn=(1-.7**t)/3;periodic=(t%2).astype(float)
n=np.arange(1,101);ratio=np.array([1+2*sum((1-k/j)*.7**k for k in range(1,j)) for j in n])
fig,(a,b)=panels()
a.plot(t,pn,color=BLUE,label='非周期链');a.plot(t,periodic,color=RED,ls='--',marker='.',ms=3,label='二状态周期链')
a.axhline(1/3,color=GRAY,ls=':',lw=.6);a.legend(loc='lower center',bbox_to_anchor=(.5,1.0),ncol=2);a.set(xlabel='步数 $t$',ylabel='$P(Z_t=2)$',ylim=(-.04,1.15))
a.set_title('(a) 从状态 0 出发的分布',pad=22)
b.plot(n,ratio,color=YELLOW);b.axhline(17/3,color=GRAY,ls=':',lw=.6);b.axhline(1,color=GRAY,ls='--',lw=.6)
b.text(44,5.88,'极限 $17/3$',fontsize=8);b.text(55,1.17,'独立基准 1',fontsize=8)
b.set(xlabel='样本量 $n$',ylabel=r'$n\,\mathrm{Var}(\bar Y_n)/\mathrm{Var}(Y_0)$',ylim=(0,6.6))
b.set_title('(b) 相关性对均值方差的放大',pad=22)
save(fig,'stochastic-mixing-variance','P=[[.9,.1],[.2,.8]]; P(Z_t=2|Z_0=0)=(1-.7^t)/3; periodic P=[[0,1],[1,0]]; variance ratio=1+2 sum_{k=1}^{n-1}(1-k/n)*.7^k',
     {'Y_values':[0,2],'stationary_mass':[2/3,1/3],'stationary_autocorrelation':.7,'asymptotic_variance_ratio':17/3},
     {'t':t.tolist(),'nonperiodic_state_probability':pn.tolist(),'periodic_state_probability':periodic.tolist(),'n':n.tolist(),'stationary_variance_ratio':ratio.tolist()},
     '02-stochastic-processes-and-approximation.tex: ex:stoch-two-state-chain, eq:stoch-two-state-autocorrelation, eq:stoch-markov-average-variance')

ang=np.linspace(0,2*np.pi,401);ell1=np.column_stack([np.cos(ang)/2,np.sin(ang)/np.sqrt(2)]);ell2=np.column_stack([np.cos(ang)/np.sqrt(3),np.sin(ang)/np.sqrt(3)])
fig,(a,)=panels(1,112,75)
a.plot(*ell1.T,color=BLUE,label=r'$V=\mathrm{diag}(4,2)$');a.plot(*ell2.T,color=RED,ls='--',label=r'$V=\mathrm{diag}(3,3)$')
a.axhline(0,color=GRAY,lw=.6);a.axvline(0,color=GRAY,lw=.6);a.set_aspect('equal');a.legend(loc='upper right',bbox_to_anchor=(1.0,1.22),ncol=1)
a.set(xlabel='第一坐标误差 $e_1$',ylabel='第二坐标误差 $e_2$',xlim=(-.82,.82),ylim=(-.82,.82))
save(fig,'stochastic-design-ellipsoids','e^T V e<=1; e_i=cos/sin(angle)/sqrt(V_ii)',
     {'V_unbalanced':[[4,0],[0,2]],'V_balanced':[[3,0],[0,3]],'normalized_radius':1,'interpretation':'geometry only; actual confidence radii may differ because determinants differ'},
     {'angle':ang.tolist(),'unbalanced':ell1.tolist(),'balanced':ell2.tolist()},
     '02-stochastic-processes-and-approximation.tex: ex:stoch-two-dimensional-adaptive-design')

n=np.arange(1,201);ci=1.96*2/np.sqrt(n);pi=1.96*2*np.sqrt(1+1/n)
fig,(a,)=panels(1,112,69)
a.plot(n,ci,color=BLUE,label='均值置信区间');a.plot(n,pi,color=RED,ls='--',label='单次观测预测区间');a.legend(loc='upper right')
a.plot([25,25],[ci[24],pi[24]],'o',color=GRAY,ms=3);a.axvline(25,color=GRAY,ls=':',lw=.6)
a.set(xlabel='样本量 $n$',ylabel='区间半宽',xlim=(1,200),ylim=(0,6))
save(fig,'statistics-mean-prediction-width','CI halfwidth=1.96*sigma/sqrt(n); PI halfwidth=1.96*sigma*sqrt(1+1/n)',
     {'known_sigma':2,'normal_quantile':1.96,'coverage':'approximately 95%, using rounded normal quantile'},
     {'n':n.tolist(),'confidence_halfwidth':ci.tolist(),'prediction_halfwidth':pi.tolist()},
     '03-mathematical-statistics.tex: ex:statistics-running-sensor-calibration, confidence/credible/prediction intervals')

r=np.linspace(-3,3,601);delta=1.;sq=.5*r*r;hub=np.where(abs(r)<=delta,sq,delta*abs(r)-.5*delta**2)
fig,(a,b)=panels()
for ax,y1,y2 in [(a,sq,hub),(b,r,np.clip(r,-delta,delta))]:
    ax.plot(r,y1,color=BLUE,label='平方损失');ax.plot(r,y2,color=RED,ls='--',label='Huber损失');ax.set_xlabel('残差 $r$');ax.legend(loc='upper left')
a.legend(loc='upper center');a.set(title='(a) 对大残差的惩罚',ylabel='损失');b.set(title='(b) 单个残差的得分贡献',ylabel=r'损失导数 $\psi(r)$')
save(fig,'statistics-huber-loss','squared loss=r^2/2; Huber=r^2/2 if |r|<=delta else delta*|r|-delta^2/2; psi=clip(r,-delta,delta)',
     {'delta':1,'interpretation':'bounded residual score; influence of complete estimator also depends on design and curvature'},
     {'r':r.tolist(),'squared_loss':sq.tolist(),'Huber_loss':hub.tolist(),'squared_derivative':r.tolist(),'Huber_derivative':np.clip(r,-delta,delta).tolist()},
     '03-mathematical-statistics.tex: robust losses and influence functions')

h=np.linspace(0,4,401);tv=np.array([math.erf(z/(2*np.sqrt(2))) for z in h]);kl=h*h/2
fig,axs=panels(3,169,64)
for ax,y,title,ylab in zip(axs,[kl,tv,h],['(a) KL散度','(b) 总变差','(c) $W_2$距离'],['$h^2/2$',r'$2\Phi(h/2)-1$','$h$']):
    ax.plot(h,y,color=YELLOW);ax.set(title=title,xlabel='均值间距 $h$',ylabel=ylab,xlim=(0,4),ylim=(0,max(y)*1.09))
save(fig,'information-gaussian-distances','For P=N(0,1), Q=N(h,1): KL=h^2/2; TV=2*Phi(h/2)-1; W2=|h|',
     {'sigma':1,'warning':'different objects and units; heights are not rankings of strength'},
     {'h':h.tolist(),'KL':kl.tolist(),'TV':tv.tolist(),'W2':h.tolist()},
     '04-information-theory-and-statistical-geometry.tex: same Gaussian location family comparison')

q=np.linspace(.015,.8,601);p=.2;exact=p*np.log(p/q)+(1-p)*np.log((1-p)/(1-q));quad=(q-p)**2/(2*p*(1-p))
fig,(a,b)=panels()
for ax in [a,b]:
    ax.plot(q,exact,color=BLUE,label='精确 KL');ax.plot(q,quad,color=RED,ls='--',label='Fisher二阶项');ax.axvline(p,color=GRAY,lw=.6,ls=':');ax.set_xlabel('目标参数 $q$')
a.set(title='(a) 全部显示范围',ylabel=r'$D_{\rm KL}(\mathrm{Ber}(0.2)\|\mathrm{Ber}(q))$',xlim=(.015,.8),ylim=(0,1.3));a.legend(loc='upper center')
b.set(title='(b) 局部放大',ylabel='散度',xlim=(.14,.26),ylim=(0,.016));b.legend(loc='upper left')
save(fig,'information-fisher-local','KL(Ber(p)||Ber(q))=p log(p/q)+(1-p) log((1-p)/(1-q)); local=(q-p)^2/[2p(1-p)]',
     {'p':p,'domain':'0<q<1','Fisher_information':1/(p*(1-p))},
     {'q':q.tolist(),'exact_KL':exact.tolist(),'Fisher_quadratic':quad.tolist()},
     '04-information-theory-and-statistical-geometry.tex: thm:information-kl-local-fisher')

r=np.linspace(0,1,201);lower=.6*(1-r);upper=lower+r
fig,(a,b)=panels()
a.bar([0,1],[.44,.2],color=[BLUE,RED],width=.55);a.set_xticks([0,1],['观测均值差','调整后的ATE']);a.set(title='(a) 混杂改变比较人群',ylabel='处理效应',ylim=(0,.6))
for pos,v in enumerate([.44,.2]):a.text(pos,v+.015,f'{v:.2f}',ha='center')
b.fill_between(r,lower,upper,color=YELLOW_FILL);b.plot(r,lower,color=YELLOW);b.plot(r,upper,color=YELLOW);b.vlines(.2,.48,.68,color=GRAY,ls=':',lw=.6)
b.set(title='(b) 未覆盖质量与识别范围',xlabel='未覆盖目标质量 $r$',ylabel='策略价值',xlim=(0,1),ylim=(0,1.05));b.annotate('$r=0.2$：$[0.48,0.68]$',(.2,.58),xytext=(.28,.10),fontsize=8)
save(fig,'causal-confounding-coverage','X equiprobable; e(0)=.2,e(1)=.8; E[Y0|X]=(.1,.5), E[Y1|X]=(.3,.7); raw=.62-.18=.44, adjusted=.2; bounds .6(1-r)+[0,r]',
     {'covariate_mass':[.5,.5],'propensity':[.2,.8],'control_mean':[.1,.5],'treated_mean':[.3,.7],'covered_reward':.6,'reward_range':[0,1]},
     {'observed_difference':.44,'adjusted_ATE':.2,'uncovered_mass':r.tolist(),'policy_lower':lower.tolist(),'policy_upper':upper.tolist()},
     '05-causal-inference.tex: confounding calculation and eq:causal-policy-value-bounds; two separate teaching constructions')

m=np.arange(1,21);allpatterns=2.**m;restricted=1+m*(m+1)/2
fig,(a,)=panels(1,112,70)
a.semilogy(m,allpatterns,color=BLUE,label='任意二值标记 $2^m$');a.semilogy(m,restricted,color=RED,ls='--',label='区间标记 $1+m(m+1)/2$');a.legend(loc='upper left')
a.set(xlabel='互异输入数 $m$',ylabel='可实现模式数（对数轴）',xlim=(1,20));a.set_xticks([1,5,10,15,20])
save(fig,'combinatorics-growth-patterns','unrestricted=2^m; interval classifiers=1+m(m+1)/2; at-most-two-positive class has same count but different patterns',
     {'ordered_inputs':True,'m_max':20}, {'m':m.tolist(),'all_patterns':allpatterns.tolist(),'interval_patterns':restricted.tolist()},
     '02-combinatorics.tex: binary labeling example and Sauer--Shelah lemma')

fig,(a,)=panels(1,112,63);gains=np.array([2,1,0]);a.bar([0,1,2],gains,color=YELLOW,width=.5)
a.set_xticks([0,1,2],[r'$S=\varnothing$',r'$S=\{2\}$',r'$S=\{2,4\}$']);a.set(ylabel='新增候选 3 的覆盖增量',ylim=(0,2.5))
for j,v in enumerate(gains):a.text(j,v+.06,str(v),ha='center')
save(fig,'combinatorics-coverage-marginals','Q2={b,c,d}, Q3={c,e}, Q4={d,e}; marginal of adding 3 = |Q3 minus union_{i in S}Qi|',
     {'nested_contexts':[[],[2],[2,4]],'added_element':3}, {'marginal_gains':gains.tolist()},
     '02-combinatorics.tex: eq:comb-running-coverage and eq:comb-diminishing-returns')

A=np.array([[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]],dtype=float);L=np.diag(A.sum(1))-A;eig,U=np.linalg.eigh(L);eig[np.abs(eig)<1e-12]=0;initial=np.array([1.,0,0,0]);time=1.;smooth=U@(np.exp(-time*eig)*(U.T@initial))
t=np.linspace(0,2,201)
fig,(a,b)=panels();xx=np.arange(4);bw=.34
a.bar(xx-bw/2,initial,bw,color=BLUE,label='$t=0$');a.bar(xx+bw/2,smooth,bw,color=RED,label='$t=1$');a.axhline(.25,color=GRAY,ls=':',lw=.6)
a.set_xticks(xx,['1','2','3','4']);a.set(title='(a) 同一图上的信号平滑',xlabel='顶点',ylabel='信号值',ylim=(0,1.25));a.legend(loc='upper right')
for lam,color,ls in [(0,BLUE,'-'),(2,RED,'--'),(4,YELLOW,':')]:b.plot(t,np.exp(-lam*t),color=color,ls=ls,label=fr'$\lambda={lam}$')
b.set(title='(b) 各频率的保留比例',xlabel='扩散时间 $t$',ylabel=r'$e^{-t\lambda}$',ylim=(0,1.15));b.legend(loc='upper right')
save(fig,'graph-diffusion-spectrum','L=diag(A1)-A; f(t)=U diag(exp(-t*lambda)) U^T f(0); initial=(1,0,0,0)',
     {'adjacency':A.tolist(),'initial':initial.tolist(),'snapshot_time':time,'limit':[.25]*4,'roundoff_rule':'Eigenvalues with absolute value below 1e-12 are represented as zero.'},
     {'eigenvalues':eig.tolist(),'snapshot':smooth.tolist(),'t':t.tolist(),'frequency_gains':{str(j):np.exp(-j*t).tolist() for j in [0,2,4]}},
     '01-graph-theory.tex: eq:graph-theory-running-edges and graph heat equation')

(asset_path(HERE, 'sources.json')).write_text(json.dumps({'description':'Reproducible analytical teaching figures, October 2026. All values follow displayed formulas or explicit finite constructions in these chapters.','fonts':{'Chinese':'fonts/LXGWWenKai-Regular.ttf','Latin':'fonts/SourceSans3-Regular.otf','math':'Matplotlib STIX'},'palette':{'one_series':YELLOW,'two_series':[BLUE,RED],'three_series':[BLUE,RED,YELLOW]},'style':style_record(),'figures':records},ensure_ascii=False,indent=2)+'\n')
print(f'Generated {len(records)} figures with PDF/SVG/PNG and formula/data provenance.')
