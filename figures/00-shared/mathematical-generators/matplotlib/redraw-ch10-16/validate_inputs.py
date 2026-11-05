from pathlib import Path
import json,hashlib,math
import numpy as np
root=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
base=Path(__file__).resolve().parent
rows=json.loads((base/'baseline-source-map.json').read_text())
bykey={r['key']:r for r in rows};results={}
def datum(key):return json.loads((root/Path(bykey['v1-'+key]['path']).parent/'data.json').read_text())['axes']
def check(key,claim,actual,expected,atol=1e-12):
 a=np.asarray(actual,dtype=float);e=np.asarray(expected,dtype=float)
 assert a.shape==e.shape and np.allclose(a,e,rtol=1e-12,atol=atol,equal_nan=True),(key,claim,a.shape,e.shape)
 err=np.abs(a-e);finite=err[np.isfinite(err)]
 results.setdefault(key,[]).append({'claim':claim,'shape':list(a.shape),'maximum_absolute_difference':float(finite.max()) if len(finite) else 0,'result':'pass'})
def line(key,ai,li,formula,claim):
 d=datum(key)[ai]['lines'][li];x=np.array(d['x']);check(key,claim,d['y'],formula(x))
def bars(key,ai,expected,claim):check(key,claim,[x['height'] for x in datum(key)[ai]['patches']],expected)
# Each identity checks artists exported by the current canonical generators.
line('probability-density-cdf',1,0,lambda x:np.clip(4*x,0,1),'CDF is clipped integral of density 4 on [0,1/4]')
check('probability-density-cdf','mass of displayed [.1,.15] interval',4*(.15-.1),.2)
a=datum('rv-paths')[0]['lines'];check('rv-paths','all 30 fixed teaching values',[x['y'] for x in a[:3]],[[14,16,12,23,20,26,23,31,27,34],[14,10,15,10,14,8,11,7,13,9],[14,20,24,19,27,32,30,24,34,37]])
check('rv-paths','fixed-time section',[x['y'][5] for x in a[:3]],[26,8,32])
q=np.array([.5,.4,.1]);p=np.array([.2,.3,.5]);g=np.array([1.,2.,4.])
bars('probability-importance-weights',0,np.r_[q,p],'all target/proposal masses');bars('probability-importance-weights',1,np.r_[q*g,p*g],'weighted and unweighted expectation contributions')
a=datum('rv-poisson-compensation')[0]['lines'];check('rv-poisson-compensation','count values',a[0]['y'],[0,1,2,3,3])
for j,i in enumerate([1,2,4,6]):check('rv-poisson-compensation',f'compensated segment {j}',a[i]['y'],j-np.array(a[i]['x']))
csv=root/'figures/00-shared/mathematical-preliminaries-lower/01-random-variables-distributions-and-causality/matplotlib/teaching-dynamics/brownian-increments.csv';b=np.genfromtxt(csv,delimiter=',',names=True)
path=np.r_[0,b['cumulative_path']];check('reader-brownian-quadratic-variation','frozen CSV path',datum('reader-brownian-quadratic-variation')[0]['lines'][0]['y'],path)
check('reader-brownian-quadratic-variation','cumulative increments',np.cumsum(b['increment']),b['cumulative_path'])
for li,mesh in enumerate([64,1024]):check('reader-brownian-quadratic-variation',f'coupled {mesh}-interval quadratic sum',datum('reader-brownian-quadratic-variation')[1]['lines'][li]['y'],np.r_[0,np.cumsum(np.diff(path[::4096//mesh])**2)])
line('statistics-huber-loss',0,0,lambda x:x*x/2,'squared loss');line('statistics-huber-loss',0,1,lambda x:np.where(abs(x)<=1,x*x/2,abs(x)-.5),'Huber delta1 loss');line('statistics-huber-loss',1,1,lambda x:np.clip(x,-1,1),'Huber score')
line('statistics-local-boundary-fit',0,0,lambda x:np.full_like(x,10.25),'weighted mean');line('statistics-local-boundary-fit',0,1,lambda x:9.2+1.4*x,'weighted linear function')
line('statistics-mean-prediction-width',0,0,lambda x:3.92/np.sqrt(x),'known-sigma mean width');line('statistics-mean-prediction-width',0,1,lambda x:3.92*np.sqrt(1+1/x),'known-sigma prediction width')
for li,V in enumerate([[4,2],[3,3]]):
 d=datum('stochastic-design-ellipsoids')[0]['lines'][li];check('stochastic-design-ellipsoids',f'eTVe=1 for V={V}',V[0]*np.array(d['x'])**2+V[1]*np.array(d['y'])**2,np.ones(401))
line('probability-vanishing-spikes',1,0,lambda x:1/x,'tail probability');line('probability-vanishing-spikes',1,1,lambda x:np.ones_like(x),'mean1 despite shrinking mass')
line('stochastic-mixing-variance',0,0,lambda x:(1-.7**x)/3,'aperiodic chain distribution');line('stochastic-mixing-variance',0,1,lambda x:x%2,'periodic chain distribution')
line('stochastic-mixing-variance',1,0,lambda x:np.array([1+2*sum((1-k/n)*.7**k for k in range(1,int(n))) for n in x]),'exact stationary variance ratio')
bars('information-kernel-distinguishability',1,[0,np.sqrt(1.5+.5*np.exp(-2)-2*np.exp(-.5))],'population MMD under linear/Gaussian kernels')
line('information-gaussian-distances',0,0,lambda x:x*x/2,'equal-variance Gaussian KL');line('information-gaussian-distances',1,0,lambda x:np.array([math.erf(h/(2*np.sqrt(2))) for h in x]),'equal-variance Gaussian TV');line('information-gaussian-distances',2,0,lambda x:abs(x),'equal-variance Gaussian W2')
a=datum('information-binary-channel-information')[0]['lines'];check('information-binary-channel-information','input entropy splits as Hcond+I',np.array(a[0]['y'])+a[1]['y'],np.full(501,np.log(2)))
for ai in [0,1]:
 line('information-fisher-local',ai,0,lambda x:.2*np.log(.2/x)+.8*np.log(.8/(1-x)),'Bernoulli exact KL');line('information-fisher-local',ai,1,lambda x:(x-.2)**2/.32,'local Fisher quadratic')
bars('causal-confounding-coverage',0,[.44,.2],'observed difference versus adjustedATE');line('causal-confounding-coverage',1,0,lambda x:.6*(1-x),'lower identification bound');line('causal-confounding-coverage',1,1,lambda x:.6*(1-x)+x,'upper identification bound')
inputs=root/'figures/02-mathematical-preliminaries-lower/02-dynamical-systems-control-decision-and-games/matplotlib/redraw-generators/state-and-control/inputs';temp=np.genfromtxt(inputs/'dynamics/temperature.tsv',delimiter='\t',names=True);ou=np.genfromtxt(inputs/'dynamics/ou.tsv',delimiter='\t',names=True);control=np.genfromtxt(inputs/'control/temperature.tsv',delimiter='\t',names=True)
for i,name in enumerate(['deterministic','state','observation']):check('action-state-temperature-layers',f'frozen temperature {name}',datum('action-state-temperature-layers')[0]['lines'][i]['y'],temp[name])
check('action-state-temperature-layers','noiseless recurrence',temp['deterministic'][1:],.8*temp['deterministic'][:-1]+.4)
for i,name in enumerate(['path2','path3','path4','path1','mean']):check('action-state-ou-paths',f'frozen OU {name}',datum('action-state-ou-paths')[0]['lines'][i]['y'],ou[name])
for i,t in enumerate([.5,2]):line('action-state-ou-paths',1,i,lambda x:np.exp(-(x-np.exp(-t))**2/(.36*(1-np.exp(-2*t))))/np.sqrt(np.pi*.36*(1-np.exp(-2*t))),'exact OU density')
for i,h in enumerate([.5,2.2]):line('dynamical-euler-stability',i,0,lambda x:np.exp(-x),'exact ODE exp(-t)');line('dynamical-euler-stability',i,1,lambda x:(1-h)**np.rint(x/h).astype(int),f'Euler grid h={h}')
t=np.linspace(0,12,1601);w=np.sqrt(3)/2;qq=np.exp(-t/2)*(np.cos(w*t)+np.sin(w*t)/(2*w));pp=-np.exp(-t/2)*np.sin(w*t)/w
check('reader-lasalle-zero-set','closed-form q',datum('reader-lasalle-zero-set')[0]['lines'][5]['x'],qq);check('reader-lasalle-zero-set','closed-form p',datum('reader-lasalle-zero-set')[0]['lines'][5]['y'],pp)
line('stochastic-stepsize-bias-variance',0,0,lambda x:1-.8**x,'fixed-step mean');line('stochastic-stepsize-bias-variance',1,0,lambda x:(1-.8**(2*x))/9,'fixed-step variance');line('stochastic-stepsize-bias-variance',1,1,lambda x:1/x,'decreasing-step variance')
for i,K in enumerate([0,4]):line('dynamical-transient-growth',0,i,lambda x:np.hypot(K*x*2.**(1-x),2.**(-x)),f'power trajectory norm K={K}')
for i,m,v in [(0,0,4),(1,1.6,.8)]:line('dynamical-kalman-density-update',0,i,lambda x:np.exp(-(x-m)**2/(2*v))/np.sqrt(2*np.pi*v),'Gaussian density with exact posteriorparameters')
for ai,method in [(0,'pred'),(2,'filter'),(4,'smooth')]:check('action-state-temperature-inference',f'frozen {method} mean',datum('action-state-temperature-inference')[ai]['lines'][2]['y'],temp[method])
for col,suf in enumerate(['fixed','moving']):
 check('control-temperature-regulation-tracking',f'{suf} exact tracking error',control['x_'+suf]-control['r_'+suf],-2*.5**control['t']);check('control-temperature-regulation-tracking',f'{suf} state recurrence',control['x_'+suf][1:],.8*control['x_'+suf][:-1]+control['u_'+suf][:-1])
 for ai,name in [(col,'r_'),(col,'x_'),(col+2,'ur_'),(col+2,'u_')]:
  li=0 if name in ['r_','ur_'] else 1;check('control-temperature-regulation-tracking',f'artist {name+suf}',datum('control-temperature-regulation-tracking')[ai]['lines'][li]['y'],control[name+suf])
line('control-stability-safety',0,0,lambda x:.5**x,'stable safe loop');line('control-stability-safety',0,1,lambda x:(-.5)**x,'stable constraint-violating loop')
line('control-barrier-projection',0,2,lambda x:np.maximum(-1,-x),'projection max(-1,-x)')
line('decision-cvar-threshold',0,0,lambda x:x+np.maximum(np.array([0,2,10])[None,:]-x[:,None],0)@np.array([.6,.3,.1])/.25,'CVaR variational objective')
bars('decision-cvar-reweighting',0,[.6,.3,.1,0,.6,.4],'risk-envelope mass');check('decision-cvar-reweighting','tail expected loss',np.array([0,2,10])@np.array([0,.6,.4]),5.2)
check('policy-temperature-comparison','fixed state trajectory',datum('policy-temperature-comparison')[0]['lines'][1]['y'],[0,.4,.72]);check('policy-temperature-comparison','feedback trajectory',datum('policy-temperature-comparison')[0]['lines'][2]['y'],[0,1,1.5]);bars('policy-temperature-comparison',1,[5.25,1.49,6.74,8.1984,.32,8.5184],'state, action and total costs')
for ai,cfn in enumerate([1,9]):line('decision-cost-thresholds',ai,0,lambda x:1-x,'positive conditional risk');line('decision-cost-thresholds',ai,1,lambda x:cfn*x,'negative conditional risk')
a=datum('game-matching-best-responses')[0]['lines'];check('game-matching-best-responses','exact best response graph segments',[[z['x'],z['y']] for z in a],[[[0,0],[0,.5]],[[1,1],[.5,1]],[[0,1],[.5,.5]],[[0,.5],[1,1]],[[.5,1],[0,0]],[[.5,.5],[0,1]]])
line('game-update-trajectories',0,0,lambda k:(2/3)*(1-(-.5)**k),'same-state heating bestresponse recurrence');a=datum('game-update-trajectories')[1]['lines'][0];check('game-update-trajectories','continuous gradient orbit radius',np.hypot(np.array(a['x'])-.5,np.array(a['y'])-.5),np.full(181,.3))
assert len(results)==33,len(results)
inputfiles=[csv,inputs/'dynamics/temperature.tsv',inputs/'dynamics/ou.tsv',inputs/'control/temperature.tsv'];manifest=[{'path':str(p.relative_to(root)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in inputfiles]
out={'scope':'33 current Matplotlib exports. Exact artist identities validated; this is numerical preflight, not visual approval. No source/resource mutations or stochastic draws.','checks':results,'retained_input_files':manifest,'all_checks_passed':True}
(base/'quantitative-current-validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print('PASS:',len(results),'figures,',sum(len(v) for v in results.values()),'numeric checks. Four retained random/deterministic tables hash-bound.')
