"""Exact teaching curves for the current linear solvers chapters; no sampled data."""
from pathlib import Path
import sys,json,hashlib
import numpy as np
import matplotlib.pyplot as plt
ROOT=next(p for p in Path(__file__).resolve().parents if (p/'build.sh').exists())
sys.path.insert(0,str(ROOT/'figures/00-shared/academic-drawing'))
from plot_style import configure,prepare_figure,style_record,BLUE,GREEN,YELLOW,RED,MUTED,BLUE_FILL
configure();OUT=Path(__file__).resolve().parent
records=[]
def canvas():
 f,a=plt.subplots(figsize=(112/25.4,61/25.4));f.subplots_adjust(left=.16,right=.97,bottom=.2,top=.95);a.grid(False,which='both');return f,a
def save(f,name,data):
 prepare_figure(f)
 for ext in ['pdf','png','svg']:f.savefig(OUT/(name+'.'+ext),dpi=300)
 records.append(dict(name=name,width_mm=112,height_mm=61,reference_width_mm=112,scale=1,font_pt=8,facts=data,style=style_record(),source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()))
 plt.close(f)
f,a=canvas();t=np.linspace(0,5,501);ls=np.array([(7-np.sqrt(5))/2,(7+np.sqrt(5))/2]);p=(1-t/4)**2;q=1-7*t/11+t*t/11
for v in ls:a.axvline(v,color=MUTED,lw=.6,ls=':')
a.axhline(0,color=MUTED,lw=.6);a.plot(t,p,color=BLUE,label='固定因子');a.plot(t,q,color=GREEN,ls='--',label='谱点为根')
a.scatter(ls,(1-ls/4)**2,color=BLUE,s=15,zorder=4);a.scatter(ls,[0,0],color=GREEN,s=15,zorder=4)
a.set(xlabel='$t$',ylabel='$p_2(t)$',xlim=(0,5),ylim=(-.18,1.05),xticks=[0,*ls,5]);a.set_xticklabels(['0','$\\lambda_2$','$\\lambda_1$','5']);a.legend(loc='upper right')
save(f,'krylov-polynomial-roots',{'A':[[4,1],[1,3]],'eigenvalues':ls.tolist(),'polynomials':['(1-t/4)^2','1-7t/11+t^2/11'],'both_p0':1,'interpretation':'analytic comparison; not an eigenvalue-dependent implementation'})
f,a=canvas();lam=np.logspace(-6,0,401);sig=np.array([1,.05]);truth=np.ones(2);noise=np.array([0,.05]);factors=sig[:,None]**2/(sig[:,None]**2+lam)
bias=(factors-1)*truth[:,None];pert=sig[:,None]/(sig[:,None]**2+lam)*noise[:,None]
a.loglog(lam,np.linalg.norm(bias,axis=0),color=BLUE,label='偏差');a.loglog(lam,np.linalg.norm(pert,axis=0),color=GREEN,ls='--',label='扰动项');a.loglog(lam,np.linalg.norm(bias+pert,axis=0),color=YELLOW,ls='-.',label='总误差');a.set(xlabel='$\\lambda$',ylabel='欧氏范数',xlim=(1e-6,1),ylim=(1e-4,2));f.subplots_adjust(top=.84);a.legend(ncol=3,fontsize=7.5,loc='lower left',bbox_to_anchor=(-.05,1.01),borderaxespad=0)
save(f,'regularization-error-components',{'A':np.diag(sig).tolist(),'true_x':truth.tolist(),'noise':noise.tolist(),'b_observed':[1,.1],'bias':'(sigma^2/(sigma^2+lambda)-1)*true_x','noise_term':'sigma/(sigma^2+lambda)*noise','scope':'one deterministic perturbation; norms of components do not add; no statistical variance claim'})
f,a=canvas();A=np.array([[.7,1],[0,.5]]);Q=np.eye(2);X=np.linalg.solve(np.eye(4)-np.kron(A.T,A.T),Q.flatten(order='F')).reshape((2,2),order='F');xs=[np.array([0.,1.])]
for k in range(12):xs.append(A@xs[-1])
xs=np.array(xs);eu=(xs*xs).sum(axis=1);energy=np.einsum('ni,ij,nj->n',xs,X,xs)
assert np.max(np.abs(X-A.T@X@A-Q))<1e-12
assert np.allclose(energy[:-1]-energy[1:],eu[:-1])
a.semilogy(range(13),eu/eu[0],color=BLUE,marker='o',ms=2.5,label='欧氏二次量');a.semilogy(range(13),energy/energy[0],color=GREEN,ls='--',marker='s',ms=2.5,label='Lyapunov二次量');a.set(xlabel='$k$',ylabel='相对二次量',xticks=[0,3,6,9,12],ylim=(1e-4,2));a.legend(fontsize=7.5)
save(f,'lyapunov-decrease',{'A':A.tolist(),'Q':Q.tolist(),'X':X.tolist(),'x0':xs[0].tolist(),'states':xs.tolist(),'energy':energy.tolist(),'euclidean_squared':eu.tolist(),'identity':'V_k-V_(k+1)=||x_k||_2^2; V_k=x_k^T X x_k','verification':'identity checked at every plotted step; X symmetric positive definite'})
(OUT/'manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2)+'\n')
print('Generated',len(records),'analytic figures')
