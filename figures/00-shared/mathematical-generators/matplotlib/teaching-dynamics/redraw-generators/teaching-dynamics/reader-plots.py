"""Three reproducible teaching diagrams, with analytic or explicitly simulated inputs.

Run with Python, NumPy and Matplotlib. No TeX dependency is used. Output paths,
fonts and the shared book style resolve relative to this source file.
"""
from pathlib import Path
import sys
import hashlib,json,sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
HERE=Path(__file__).resolve().parent
ROOT=next(p for p in Path(__file__).resolve().parents if (p / 'build.sh').is_file() and (p / 'tex/book.tex').is_file())
sys.path.insert(0, str(ROOT / 'figures/00-shared'))
from resource_paths import asset_path
sys.path.insert(0,str(ROOT / 'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record
from plot_style import BLUE,RED,GREEN, YELLOW,STROKE,MUTED,GRID,BLUE_FILL,RED_FILL,YELLOW_FILL
from plot_style import BLUE, GREEN, YELLOW, RED, PURPLE, BLUE_FILL, GREEN_FILL, YELLOW_FILL, RED_FILL, PURPLE_FILL, note
configure()
CHAPTER='tex/01-mathematical-preliminaries/'

def save(fig,name,size,chapter,purpose,formula,parameters,data=None):
    prepare_figure(fig)
    outputs={}
    for ext in ('pdf','svg','png'):
        path=asset_path(HERE, f'{name}.{ext}')
        fig.savefig(path,dpi=300,facecolor='white')
        outputs[ext]={'file':str(path.relative_to(ROOT)),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
    record={'figure':name,'construction_origin_date':'2026-10-06','purpose':purpose,
      'generator':str(Path(__file__).relative_to(ROOT)),
      'generator_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'source':{'chapter':CHAPTER+chapter,'sha256':hashlib.sha256((ROOT/CHAPTER/chapter).read_bytes()).hexdigest()},
      'kind':'teaching construction, not empirical data','formula':formula,'parameters':parameters,
      'data_file':data,'size_mm':size,'style':style_record(),
      'style_helper_sha256':hashlib.sha256((Path(__import__('plot_style').__file__)).read_bytes()).hexdigest(),
      'software':{'Matplotlib':matplotlib.__version__,'NumPy':np.__version__},'outputs':outputs,
      'checks':{'analytic_scope':'Construction and assertions executed by this generator',
        'visual':'No automatic visual approval; consult current asset-bound manual review',
        'boundary':'This export record does not establish book compilation, target consistency or actual book-page acceptance; those checks are recorded separately'}}
    (asset_path(HERE, f'{name}.json')).write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    plt.close(fig)

def overlap():
    size=[169,70]
    fig,axes=plt.subplots(1,3,figsize=np.array(size)/25.4)
    fig.subplots_adjust(left=.065,right=.987,bottom=.25,top=.84,wspace=.36)
    for ax,t in zip(axes[:2],[.5,1.5]):
        a,b=max(0,t-1),min(1,t)
        assert b-a==.5
        ax.add_patch(Rectangle((0,.56),1,.19,facecolor=BLUE_FILL,edgecolor=BLUE,lw=1.1))
        ax.add_patch(Rectangle((t-1,.22),1,.19,facecolor=GREEN_FILL,edgecolor=GREEN,lw=1.1))
        ax.add_patch(Rectangle((a,.10),b-a,.77,facecolor=PURPLE_FILL,edgecolor='none',zorder=-1))
        ax.plot([a,b],[.92,.92],color=PURPLE,lw=1.1)
        ax.text(.5,.66,r'$f(\tau)$',ha='center',va='center')
        ax.text(t-.5,.32,r'$g(t-\tau)$',ha='center',va='center')
        ax.set(xlim=(-.65,1.65),ylim=(0,1.09),xticks=[-.5,0,.5,1,1.5],yticks=[],xlabel=r'积分位置 $\tau$',title=f'固定输出位置 t = {t}')
        ax.spines['left'].set_visible(False)
        note(ax.text((a+b)/2,1.0,'重叠长度 0.5',ha='center',color=MUTED))
    ax=axes[2]
    t=np.linspace(-.3,2.3,401)
    y=np.maximum(0,np.minimum(1,t)-np.maximum(0,t-1))
    assert np.isclose(np.interp(1,t,y),1,atol=.004)
    ax.plot(t,y,color=PURPLE)
    ax.scatter([.5,1.5],[.5,.5],color=PURPLE,s=18,zorder=3)
    ax.set(xlim=(-.3,2.3),ylim=(-.03,1.17),xticks=[0,1,2],yticks=[0,.5,1],xlabel=r'输出位置 $t$',ylabel='重叠长度',title='全部位置的卷积输出')
    ax.grid(axis='y')
    save(fig,'continuous-convolution-overlap',size,'03-graphs-and-signals/01-signal-representation-and-processing.tex',
      'Separate the integration variable from the output location and interpret convolution as overlap area.',
      'f=g=1_[0,1]; g(t-tau) supported on [t-1,t]; (f*g)(t)=max(0,min(1,t)-max(0,t-1))',
      {'output_positions':[.5,1.5],'curve_points':401,'curve_interval':[-.3,2.3]})

def lasalle():
    size=[112,87]
    fig,ax=plt.subplots(figsize=np.array(size)/25.4)
    fig.subplots_adjust(left=.17,right=.97,bottom=.18,top=.94)
    w=np.sqrt(3)/2
    t=np.linspace(0,12,1601)
    q=np.exp(-t/2)*(np.cos(w*t)+np.sin(w*t)/(2*w))
    p=-np.exp(-t/2)*np.sin(w*t)/w
    # Closed form satisfies q'=p, p'=-q-p and initial state (1,0).
    assert np.isclose(q[0],1) and np.isclose(p[0],0)
    assert np.max(np.diff((q*q+p*p)/2))<1e-12
    th=np.linspace(0,2*np.pi,361)
    for radius in [.25,.5,.75,1]:
        ax.plot(radius*np.cos(th),radius*np.sin(th),color=GRID,lw=.5,zorder=0)
    ax.axhline(0,color=MUTED,lw=.6,ls='--',zorder=1)
    ax.plot(q,p,color=BLUE,lw=1.1,zorder=2)
    ax.scatter([1,0],[0,0],s=[17,14],color=[BLUE,STROKE],zorder=3)
    for a,b in [(30,58),(220,248),(520,548)]:
        ax.annotate('',xy=(q[b],p[b]),xytext=(q[a],p[a]),arrowprops={'arrowstyle':'->','color':BLUE,'lw':1.1,'mutation_scale':8})
    ax.annotate('起点 (1, 0)',xy=(1,0),xytext=(.50,.16),arrowprops={'arrowstyle':'-','color':MUTED,'lw':.6})
    ax.text(-1.05,.12,r'零导数集合 $p=0$',color=MUTED,fontsize=8)
    ax.annotate('最大不变集：原点',xy=(0,0),xytext=(-.88,.62),arrowprops={'arrowstyle':'-','color':MUTED,'lw':.6})
    ax.set(xlim=(-1.1,1.1),ylim=(-1.08,.82),xticks=[-1,-.5,0,.5,1],yticks=[-1,-.5,0,.5],xlabel=r'位置 $q$',ylabel=r'速度 $p$')
    ax.set_aspect('equal',adjustable='box')
    save(fig,'lasalle-zero-set',size,'05-dynamical-systems-control-decision-and-games/01-action-and-state.tex',
      'Zero instantaneous energy derivative is not an invariant trajectory.',
      'q=e^(-t/2)(cos(wt)+sin(wt)/(2w)); p=-e^(-t/2)sin(wt)/w; w=sqrt(3)/2; V=(q^2+p^2)/2; Vdot=-p^2',
      {'initial_state':[1,0],'damping':1,'time_interval':[0,12],'points':1601,'reference_energy_radii':[.25,.5,.75,1]})

def quadratic_variation():
    size=[169,75];n=4096;dt=1/n;seed=20261006
    retained=ROOT/"figures/00-shared/mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/matplotlib/teaching-dynamics/brownian-increments.csv"
    table=np.genfromtxt(retained,delimiter=",",names=True)
    increments=table["increment"]
    path=np.r_[0,table["cumulative_path"]];t=np.r_[0,table["time"]]
    assert len(increments)==n and np.allclose(path[1:],np.cumsum(increments),rtol=0,atol=1e-12)
    values=[]
    fig,axes=plt.subplots(1,2,figsize=np.array(size)/25.4)
    fig.subplots_adjust(left=.075,right=.975,bottom=.23,top=.86,wspace=.28)
    axes[0].plot(t,path,color=BLUE,lw=1.1)
    axes[0].set(xlabel=r'时间 $t$',ylabel='累计高斯增量',title='同一组细网格增量的路径折线',xlim=(0,1))
    for mesh,color in [(64,BLUE),(1024,GREEN)]:
        stride=n//mesh
        d=np.diff(path[::stride]);times=t[::stride];qv=np.r_[0,np.cumsum(d*d)]
        assert len(times)==mesh+1
        axes[1].step(times,qv,where='post',color=color,lw=1.1,label=f'{mesh} 个区间')
        values.append((mesh,float(qv[-1])))
    axes[1].plot([0,1],[0,1],color=MUTED,lw=.6,ls='--',label='理论极限 t')
    axes[1].set(xlabel=r'时间 $t$',ylabel='平方增量累计和',title='改变分割，不重新生成路径',xlim=(0,1),ylim=(0,1.28))
    axes[1].legend(loc='upper left',handlelength=1.7)
    for ax in axes:ax.grid(axis='y')
    save(fig,'brownian-quadratic-variation',size,'04-random-variables-distributions-and-causality/01-random-variables.tex',
      'Quadratic variation is accumulated along time on the same coupled sample, distinct from endpoint variance across samples.',
      'delta W_i=sqrt(1/4096)*epsilon_i with seeded independent N(0,1); coarse increments sum the same fine increments; Q_m(t)=sum completed coarse increments squared; E Q_m(1)=1 and Var Q_m(1)=2/m',
      {'seed':seed,'fine_intervals':n,'coarse_intervals':[64,1024],'endpoint_sums':values,
       'scope':'A finite Gaussian-grid teaching construction; a single polygon is not a proof of Brownian convergence or a differentiable Brownian path.'},
      str(retained.relative_to(ROOT)))

if __name__=='__main__':
    overlap();lasalle();quadratic_variation()
