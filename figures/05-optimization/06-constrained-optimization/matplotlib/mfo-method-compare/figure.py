from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from mfo_common import *

# St(5,200), f=tr(X'AX)/2, A=diag(linspace(1,100,200)). Grassmann RTR, RGD, and an augmented Lagrangian with L-BFGS.
import json
n,k=200,5; a=np.linspace(1,100,n)[:,None]; rng=np.random.default_rng(4)
Xs=np.linalg.qr(rng.normal(size=(n,k)))[0]
qf=lambda Y:(lambda Q,R:Q*np.sign(np.diag(R)))(*np.linalg.qr(Y))
fv=lambda X:.5*(a*X*X).sum()
def res(X):
    Xq=qf(X); AX=a*Xq; return np.linalg.norm(AX-Xq@(Xq.T@AX))
feas=lambda X:np.linalg.norm(X.T@X-np.eye(k))
def rtr(tol=1e-7):
    X=Xs.copy(); D=2.; c=0; qr=0; L=[(0,0,res(X),feas(X))]
    for t in range(300):
        AX=a*X; S=X.T@AX; G=AX-X@S; c+=k; ng=np.linalg.norm(G)
        if ng<tol: break
        def Hv(V):
            nonlocal c
            c+=k; W=a*V-V@S; return W-X@(X.T@W)
        V,st,cnt=tcg(G,Hv,D,min(.1,ng),inner=lambda u,v:(u*v).sum())
        pred=-((G*V).sum()+.5*(V*Hv(V)).sum()); c-=k
        Y=qf(X+V); qr+=1; r=(fv(X)-fv(Y))/pred
        if r<.25: D/=4
        elif r>.75 and abs(np.linalg.norm(V)-D)<1e-9: D*=2
        if r>=.25: X=Y
        L.append((c,qr,res(X),feas(X)))
    return L
def rgd(tol=1e-7,T=6000):
    X=Xs.copy(); c=0;qr=0;al=1e-2; L=[(0,0,res(X),feas(X))]
    for t in range(T):
        AX=a*X; S=X.T@AX; G=AX-X@S; c+=k; ng=np.linalg.norm(G); f0=.5*np.trace(S)
        if ng<tol: break
        al*=2
        while True:
            Y=qf(X-al*G); qr+=1; fn=fv(Y)
            if fn<=f0-1e-4*al*ng*ng or al<1e-12: break
            al/=2
        c+=0; X=Y; L.append((c,qr,res(X),feas(X)))
    return L
def al_method(tol=1e-7):
    X=Xs+0; Lam=np.zeros((k,k)); sig=10.; c=0; L=[(0,0,res(X),feas(X))]
    def F(Z):
        nonlocal c
        AZ=a*Z; c+=k; C=Z.T@Z-np.eye(k); C=(C+C.T)/2
        val=.5*(Z*AZ).sum()+(Lam*C).sum()+.5*sig*(C*C).sum()
        return val,AZ+2*Z@(Lam+sig*C)
    for outer in range(40):
        S=[];Y=[]; val,gr=F(X); inner_tol=max(tol*.5,1e-1*0.5**outer*10)
        for it in range(1500):
            ng=np.linalg.norm(gr)
            if ng<inner_tol: break
            qq=gr.copy(); xi=[]
            for s,y in zip(reversed(S),reversed(Y)):
                r=1/(s*y).sum(); e=r*(s*qq).sum(); qq-=e*y; xi.append((r,e,s,y))
            gam=(S[-1]*Y[-1]).sum()/(Y[-1]*Y[-1]).sum() if S else 1/(sig+a.max())
            z=gam*qq
            for r,e,s,y in reversed(xi): z+=(e-r*(y*z).sum())*s
            al=1.; gd=-(gr*z).sum()
            while True:
                Xn=X-al*z; vn,gn=F(Xn)
                if vn<=val+1e-4*al*gd or al<1e-12: break
                al/=2
            s=Xn-X; y=gn-gr
            if (s*y).sum()>1e-12:
                S.append(s);Y.append(y)
                if len(S)>20: S.pop(0);Y.pop(0)
            X,val,gr=Xn,vn,gn
            L.append((c,0,res(X),feas(X)))
        C=X.T@X-np.eye(k); C=(C+C.T)/2; Lam=Lam+sig*C
        if np.linalg.norm(C)>1e-3: sig*=2
        if res(X)<tol and feas(X)<1e-8: break
    return L
R={'RTR':rtr(),'RGD':rgd(),'AL':al_method()}
info={m:dict(feas_max=max(p[3] for p in R[m]),matvec=R[m][-1][0],qr=R[m][-1][1],res=R[m][-1][2],feas=R[m][-1][3],points=len(R[m])) for m in R}
print(json.dumps(info,indent=0))
fig,axs=figure(width_mm=112,height_mm=50,ncols=2)
for m,c,nm,lw in [('AL',YELLOW,'增广 Lagrange',1.5),('RGD',PURPLE,'黎曼梯度下降',1.4),('RTR',GREEN,'黎曼信赖域',1.6)]:
    d=np.array(R[m]); axs[0].loglog(np.maximum(d[:,0],1),d[:,2],color=c,lw=lw,label=nm)
    axs[1].loglog(np.maximum(d[:,0],1),np.maximum(d[:,3],1e-17),color=c,lw=lw,label=nm)
axs[0].set_xlabel('矩阵乘列数\n(a)'); axs[0].set_ylabel('黎曼驻点残差'); axs[0].legend(handlelength=1.6,loc='lower left')
axs[1].set_xlabel('矩阵乘列数\n(b)'); axs[1].set_ylabel('可行误差')
save(fig, Path(__file__).resolve().parent,'figure',{'formula':'St(5,200), spectrum 1..100, seed 4','info':info})
