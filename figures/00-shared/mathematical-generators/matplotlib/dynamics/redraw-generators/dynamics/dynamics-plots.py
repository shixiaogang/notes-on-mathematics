#!/usr/bin/env python3
"""Reproduce the mathematical teaching figures; no empirical data are used.

Run with Python plus NumPy and Matplotlib installed. The script finds repository
fonts relative to itself and exports PDF, SVG, and PNG at the final book width.
Each JSON records the expressions, grids, parameters, and output checks.
"""
from pathlib import Path
import json
import hashlib
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0, str(ROOT / 'figures/00-shared/academic-drawing'))
from plot_style import configure, prepare_figure, style_record

from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL
configure()
from plot_style import BLUE, RED, GREEN, YELLOW
from plot_style import INK, STROKE, MUTED as GREY, BLUE_FILL as PALE
RECORDS = {}
CHAPTERS = {
    'convolution-boundaries': '03-graphs-and-signals/01-signal-representation-and-processing.tex',
    'aliasing-curves': '03-graphs-and-signals/01-signal-representation-and-processing.tex',
    'euler-stability': '05-dynamical-systems-control-decision-and-games/01-action-and-state.tex',
    'kalman-density-update': '05-dynamical-systems-control-decision-and-games/01-action-and-state.tex',
    'cost-thresholds': '05-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex',
    'cvar-threshold': '05-dynamical-systems-control-decision-and-games/03-policy-value-and-optimization.tex',
    'stability-safety': '05-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex',
    'barrier-projection': '05-dynamical-systems-control-decision-and-games/02-policy-realization-and-control.tex',
    'matching-best-responses': '05-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex',
    'bargaining-disagreement': '05-dynamical-systems-control-decision-and-games/04-multi-agent-response-and-evolution.tex',
}

def canvas(width_mm=112, height_mm=64, ncols=1, nrows=1, **kwargs):
    fig, axs = plt.subplots(nrows, ncols, figsize=(width_mm/25.4,height_mm/25.4),
                            layout='constrained', **kwargs)
    fig.get_layout_engine().set(w_pad=.02, h_pad=.02, wspace=.07, hspace=.06)
    for ax in np.asarray(axs).reshape(-1):
        ax.spines[['right','top']].set_visible(False)
        ax.tick_params(length=3, pad=2)
    return fig, axs

def save(fig, name, expressions, sampling, parameters, question, width_mm, height_mm):
    prepare_figure(fig)
    outputs = {}
    for ext in ['pdf','svg','png']:
        path = asset_path(HERE, f'{name}.{ext}')
        fig.savefig(path, dpi=300, facecolor='white')
        outputs[ext] = {'file':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    meta = {
        'figure': name, 'generator': str(Path(__file__).relative_to(ROOT)), 'construction_origin_date': '2026-10-06',
        'kind': 'analytic teaching construction; not an experiment or observed data',
        'question': question, 'expressions': expressions, 'sampling': sampling,
        'parameters': parameters, 'data_source': 'Expressions and exact examples in the corresponding volume-one chapter; derived in this script.',
        'size_mm': [width_mm,height_mm],
        'fonts': style_record()['fonts'],
        'palette_policy': style_record()['palette'],
        'palette_assignment': 'Semantic roles are explicit in the source; current per-export artist-data/typography and bound manual review establish actual assignments, not the number of series.',
        'style': style_record(),
        'style_helper_sha256': hashlib.sha256((Path(__import__('plot_style').__file__)).read_bytes()).hexdigest(),
        'outputs': outputs,
        'validation': {'analytic_values': 'Checked by assertions and direct evaluation in generator',
                       'visual': 'No automatic visual approval; consult current asset-bound manual review',
                       'book_compilation': 'Drawing replay alone is not book-page approval; see redraw-20261011 review and current build/check-target'},
    }
    chapter = Path('tex/01-mathematical-preliminaries')/CHAPTERS[name]
    meta['source'] = {'file':str(chapter), 'sha256':hashlib.sha256((ROOT/chapter).read_bytes()).hexdigest()}
    RECORDS[name] = meta
    (asset_path(HERE, f'{name}.json')).write_text(json.dumps(meta, ensure_ascii=False, indent=2)+'\n')
    plt.close(fig)

# The zero and periodic boundary rules produce different operators.
x=np.array([1.,2.,1.]); h=np.array([1.,-1.])
linear=np.convolve(x,h)
circular=np.array([sum(x[r]*np.pad(h,(0,1))[(t-r)%3] for r in range(3)) for t in range(3)])
assert np.allclose(linear,[1,1,-1,-1]) and np.allclose(circular,[0,1,-1])
fig, axs=canvas(112,82,nrows=2,sharex=True,sharey=True)
for ax,values,color,marker,label in zip(axs,[linear,circular],[BLUE,GREEN],['o','s'],['零延拓','周期边界（长度 3）']):
    t=np.arange(len(values)); ax.vlines(t,0,values,color=color,lw=1.1)
    ax.scatter(t,values,s=20,color=color,marker=marker,zorder=3)
    ax.axhline(0,color=GREY,lw=.6)
    ax.text(.97,.85,label,transform=ax.transAxes,ha='right')
    ax.set_ylim(-1.35,1.35); ax.set_yticks([-1,0,1]); ax.set_ylabel('输出')
    for ti,yi in zip(t,values): ax.text(ti+.10,yi+(.12 if yi>=0 else -.22),f'{yi:g}',fontsize=8)
axs[-1].set_xlim(-.3,3.5); axs[-1].set_xticks(range(4)); axs[-1].set_xlabel('输出位置 $t$')
save(fig,'convolution-boundaries',{'linear':'y[t]=sum_r x[r]h[t-r] with zero extension','circular':'y[t]=sum_(r=0)^2 x[r]h[(t-r) mod 3]'}, {'positions':[0,1,2,3],'finite_sum':True},{'x':x.tolist(),'h':h.tolist(),'linear':linear.tolist(),'circular':circular.tolist()},'Why does changing the boundary change the first output?',112,82)

# Different continuous frequencies yield identical integer samples.
t=np.linspace(0,5,1201); sample_t=np.arange(6)
f1=np.cos(.8*np.pi*t); f2=np.cos(1.2*np.pi*t)
assert np.allclose(np.cos(.8*np.pi*sample_t),np.cos(1.2*np.pi*sample_t))
fig,ax=canvas(112,64)
ax.plot(t,f1,color=BLUE,label=r'$\cos(0.8\pi t)$')
ax.plot(t,f2,color=GREEN,ls='--',label=r'$\cos(1.2\pi t)$')
ax.scatter(sample_t,np.cos(.8*np.pi*sample_t),color=INK,s=18,zorder=4,label='共同样本')
ax.set(xlim=(-.1,5.1),ylim=(-1.3,1.5),xlabel='连续位置 $t$',ylabel='信号值')
ax.set_xticks(range(6)); ax.set_yticks([-1,0,1]); ax.legend(loc='upper center',ncols=3,columnspacing=.9,handlelength=1.5)
save(fig,'aliasing-curves',{'f1':'cos(0.8*pi*t)','f2':'cos(1.2*pi*t)','sample_identity':'cos(1.2*pi*n)=cos(0.8*pi*n), n integer'}, {'continuous_grid':'1201 evenly spaced points in [0,5]','samples':'integers 0,...,5'}, {'sampling_interval':1},'Which differences disappear when only integer samples are retained?',112,64)

# Continuous stability does not guarantee Euler stability.
fig,axs=canvas(169,64,ncols=2,sharex=True,sharey=True)
for ax,step in zip(axs,[.5,2.2]):
    grid=np.arange(int(np.floor(8.8/step))+1)*step
    numeric=(1-step)**np.arange(len(grid))
    exact_t=np.linspace(0,8.8,701)
    ax.plot(exact_t,np.exp(-exact_t),color=BLUE,label='精确解')
    ax.plot(grid,numeric,color=(GREEN if step<2 else RED),marker='s',ms=3,ls='--',label='Euler 状态')
    ax.axhline(0,color=GREY,lw=.6)
    ax.set(xlim=(-.12,9.0),ylim=(-2.5,2.5),xlabel='时间 $t$')
    ax.set_title(rf'$h={step:g},\quad 1-h={1-step:g}$',fontweight='normal',fontsize=8)
    ax.legend(loc='upper left')
axs[0].set_ylabel('状态 $x$')
save(fig,'euler-stability',{'ode':'dx/dt=-x, x(0)=1','exact':'x(t)=exp(-t)','euler':'x_k=(1-h)^k, t_k=k*h'}, {'exact':'701 evenly spaced points in [0,8.8]','euler':'all grid points k*h<=8.8'}, {'h':[.5,2.2]},'How can a stable differential equation give a growing numerical trajectory?',169,64)

# A Gaussian posterior moves toward a reading while retaining uncertainty.
state=np.linspace(-6,6,1401)
def density(z,mean,var): return np.exp(-(z-mean)**2/(2*var))/np.sqrt(2*np.pi*var)
prior_mean,prior_var,noise_var,reading=0,4,1,2
K=prior_var/(prior_var+noise_var); post_mean=prior_mean+K*(reading-prior_mean); post_var=prior_var*noise_var/(prior_var+noise_var)
assert np.allclose([K,post_mean,post_var],[.8,1.6,.8])
fig,ax=canvas(112,64)
ax.plot(state,density(state,prior_mean,prior_var),color=BLUE,label=r'预测 $\mathcal{N}(0,4)$')
ax.plot(state,density(state,post_mean,post_var),color=GREEN,ls='--',label=r'滤波 $\mathcal{N}(1.6,0.8)$')
ax.axvline(reading,color=GREY,ls=':',lw=.6)
ax.text(reading+.15,.02,'读数 2',fontsize=8)
ax.set(xlim=(-6,6),ylim=(0,.53),xlabel='隐藏状态 $x$',ylabel='条件密度')
ax.legend(loc='upper left')
save(fig,'kalman-density-update',{'density':'exp(-(x-m)^2/(2*p))/sqrt(2*pi*p)','K':'p_minus/(p_minus+r)','m_plus':'m_minus+K*(y-m_minus)','p_plus':'p_minus*r/(p_minus+r)'}, {'grid':'1401 evenly spaced points in [-6,6]','no_truncation_renormalization':True}, {'m_minus':0,'p_minus':4,'r':1,'y':2,'K':K,'m_plus':post_mean,'p_plus':post_var},'How do observation precision and prior precision change a posterior density?',112,64)

# Cost-sensitive decisions compare two risk lines, not the probability alone.
p=np.linspace(0,1,501)
fig,axs=canvas(169,65,ncols=2,sharex=True)
for ax,cfn in zip(axs,[1,9]):
    threshold=1/(1+cfn)
    ax.plot(p,1-p,color=BLUE,label='预测阳性')
    ax.plot(p,cfn*p,color=GREEN,ls='--',label='预测阴性')
    ax.axvline(threshold,color=GREY,ls=':',lw=.6)
    ax.scatter([threshold],[1-threshold],color=INK,s=17,zorder=4)
    ax.set(xlim=(0,1),ylim=(0,cfn*1.04),xlabel='阳性概率 $p$')
    ax.set_title(rf'$c_{{\mathrm{{FP}}}}=1,\quad c_{{\mathrm{{FN}}}}={cfn}$',fontweight='normal',fontsize=8)
    ax.text(threshold+.02,.20 if cfn==1 else cfn*.40,rf'阈值 ${threshold:g}$',fontsize=8)
    ax.legend(loc='upper center')
axs[0].set_ylabel('条件风险')
save(fig,'cost-thresholds',{'positive':'r(1|p)=c_FP*(1-p)','negative':'r(0|p)=c_FN*p','threshold':'c_FP/(c_FP+c_FN)'}, {'p':'501 evenly spaced points in [0,1]','axes':'same probability range; loss ranges shown separately'}, {'c_FP':1,'c_FN':[1,9]},'Why does the same estimated probability lead to different actions under different losses?',169,65)

# The CVaR threshold and tail mean are distinct coordinates.
eta=np.linspace(-.5,11.5,1201); losses=np.array([0,2,10]); probabilities=np.array([.6,.3,.1]); alpha=.75
phi=eta+np.maximum(losses[None,:]-eta[:,None],0)@probabilities/(1-alpha)
assert np.isclose(2+np.maximum(losses-2,0)@probabilities/(1-alpha),5.2)
fig,ax=canvas(112,64)
ax.plot(eta,phi,color=BLUE)
ax.scatter([2],[5.2],color=BLUE,edgecolor=STROKE,lw=.6,s=29,zorder=4)
ax.plot([2,2], [4.4,5.2], color=GREY,ls=':',lw=.6)
ax.plot([-.5,2],[5.2,5.2],color=GREY,ls=':',lw=.6)
ax.text(2.35,4.70,r'最小点 $(2,5.2)$',fontsize=8)
ax.set(xlim=(-.5,11.5),ylim=(4.4,12),xlabel=r'阈值 $\eta$',ylabel=r'目标 $\phi(\eta)$')
ax.set_xticks([0,2,5,10]); ax.set_yticks([5.2,8,10,12])
save(fig,'cvar-threshold',{'phi':'eta + E[(L-eta)_+]/(1-alpha)','distribution':'P(L=0,2,10)=(0.6,0.3,0.1)','tail_mean':'(0.1*10+0.15*2)/0.25=5.2'}, {'eta':'1201 evenly spaced points in [-0.5,11.5]','breakpoints':[0,2,10],'breakpoint_values_in_grid':True}, {'alpha':alpha,'losses':losses.tolist(),'probabilities':probabilities.tolist(),'VaR':2,'CVaR':5.2},'Why can a quantile differ from the average of the worst tail mass?',112,64)

# Both closed loops are stable; one violates a state constraint.
k=np.arange(9); safe=.5**k; unsafe=(-.5)**k
fig,ax=canvas(112,64)
ax.axhspan(-.7,0,color=PALE,zorder=0)
ax.plot(k,safe,color=BLUE,marker='o',ms=3.5,label=r'$u_t=-0.5x_t$')
ax.plot(k,unsafe,color=RED,marker='s',ms=3.5,ls='--',label=r'$u_t=-1.5x_t$')
ax.axhline(0,color=GREY,lw=.6)
ax.text(5.3,-.53,'禁止区域 $x<0$',fontsize=8)
ax.set(xlim=(-.1,8.1),ylim=(-.7,1.17),xlabel='离散时刻 $t$',ylabel='状态 $x_t$')
ax.set_xticks([0,2,4,6,8]); ax.legend(loc='upper right')
save(fig,'stability-safety',{'plant':'x_(t+1)=x_t+u_t, x_0=1','safe':'x_t=(0.5)^t','unsafe':'x_t=(-0.5)^t'}, {'t':'all integers 0,...,8'}, {'safe_set':'[0,infinity)','feedback_gains':[.5,1.5]},'Why is eventual convergence not enough to guarantee safety throughout a trajectory?',112,64)

# A barrier inequality creates a state-dependent half line of actions.
x=np.linspace(0,2,501); nominal=-np.ones_like(x); bound=-x; corrected=np.maximum(nominal,bound)
fig,ax=canvas(112,64)
ax.fill_between(x,bound,.25,color=PALE,zorder=0)
ax.plot(x,bound,color=GREY,ls=':',lw=.6,label='可行边界 $u=-x$')
ax.plot(x,nominal,color=BLUE,label='名义动作 $-1$')
ax.plot(x,corrected,color=GREEN,ls='--',label='安全投影')
ax.annotate('',xy=(.2,-.2),xytext=(.2,-1),arrowprops={'arrowstyle':'->','lw':.6,'color':STROKE})
ax.text(.27,-.50,'$x=0.2$',fontsize=8)
ax.set(xlim=(0,2),ylim=(-2.25,.25),xlabel='当前状态 $x$',ylabel='动作 $u$')
ax.legend(loc='lower left',fontsize=8)
save(fig,'barrier-projection',{'plant':'dx/dt=u','h':'h(x)=x, alpha(h)=h','feasible':'u>=-x','nominal':'u_nom=-1','projection':'u_star=max(-1,-x)'}, {'x':'501 evenly spaced points in [0,2]'}, {'U':'all real numbers','state_for_arrow':.2,'original_action':-1,'corrected_action':-.2},'How does an inequality on the state derivative change the permitted control action?',112,64)

# Best response is a correspondence, not necessarily a continuous function.
fig,ax=canvas(112,75)
for xs,ys in [([0,0],[0,.5]),([1,1],[.5,1]),([0,1],[.5,.5])]: ax.plot(xs,ys,color=BLUE)
for xs,ys in [([0,.5],[1,1]),([.5,1],[0,0]),([.5,.5],[0,1])]: ax.plot(xs,ys,color=GREEN,ls='--')
ax.scatter([.5],[.5],color=INK,s=25,zorder=5)
ax.text(.56,.55,'共同最佳响应',fontsize=8)
ax.set(xlim=(-.08,1.08),ylim=(-.08,1.23),xlabel='行方选正面的概率 $p$',ylabel='列方选正面的概率 $q$',aspect='equal')
ax.set_xticks([0,.5,1]);ax.set_yticks([0,.5,1])
ax.legend(handles=[Line2D([0],[0],color=BLUE,label='行方最佳响应'),Line2D([0],[0],color=GREEN,ls='--',label='列方最佳响应')],loc='upper center',ncols=2,columnspacing=1.2,fontsize=8)
save(fig,'matching-best-responses',{'payoff':'M=[[1,-1],[-1,1]], row maximizes and column minimizes','BR1':'p=0 if q<0.5; p in [0,1] if q=0.5; p=1 if q>0.5','BR2':'q=1 if p<0.5; q in [0,1] if p=0.5; q=0 if p>0.5'}, {'segments':'exact piecewise correspondence; all endpoints included','not_a_trajectory':True}, {'equilibrium':[.5,.5]},'Why must a mixed equilibrium be a mutual best response, including tied actions?',112,75)

# The same feasible sum has different solutions when disagreement changes.
fig,axs=canvas(169,71,ncols=2,sharex=True,sharey=True)
for ax,d,opt in zip(axs,[(1,1),(0,1)],[(3,3),(2.5,3.5)]):
    ax.fill([0,6,0],[0,0,6],color=PALE,zorder=0)
    ax.plot([0,6],[6,0],color=GREY,lw=.6)
    ax.plot([d[0],d[0]],[d[1],6-d[0]],color=GREY,ls=':',lw=.6)
    ax.plot([d[0],6-d[1]],[d[1],d[1]],color=GREY,ls=':',lw=.6)
    ax.scatter([d[0]],[d[1]],color=BLUE,s=28,zorder=4)
    ax.scatter([opt[0]],[opt[1]],color=RED,s=28,zorder=4)
    ax.text(d[0]+.22,d[1]-.35,'分歧点',fontsize=8.2)
    ax.text(opt[0]+.15,opt[1]+.2,rf'$({opt[0]:g},{opt[1]:g})$',fontsize=8.5)
    ax.set(xlim=(-.35,6.35),ylim=(-.35,6.35),xlabel='参与者 1 收益 $u_1$',aspect='equal')
    ax.set_title(rf'$\mathbf{{d}}=({d[0]},{d[1]})$',fontweight='normal',fontsize=9)
    ax.set_xticks([0,2,4,6]);ax.set_yticks([0,2,4,6])
axs[0].set_ylabel('参与者 2 收益 $u_2$')
save(fig,'bargaining-disagreement',{'feasible':'u_1>=0, u_2>=0, u_1+u_2<=6','objective':'maximize (u_1-d_1)*(u_2-d_2) with u_i>=d_i','optimum':'equal gains along u_1+u_2=6'}, {'geometry':'exact vertices and optimal points; no fitted data'}, {'disagreement':[[1,1],[0,1]],'optima':[[3,3],[2.5,3.5]]},'How does changing a disagreement point change bargaining while retaining the same feasible outcomes?',169,71)
manifest={'construction_origin_date':'2026-10-06', 'generator':str(Path(__file__).relative_to(ROOT)),
          'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
          'style':style_record(),
          'style_helper_sha256':hashlib.sha256((Path(__import__('plot_style').__file__)).read_bytes()).hexdigest(),
          'scope':'Ten analytical teaching figures in volume one; no empirical data.',
          'figures':RECORDS}
(asset_path(HERE, 'sources.json')).write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
print('Created ten figures, each with PDF, SVG, PNG, and analytical JSON.')
