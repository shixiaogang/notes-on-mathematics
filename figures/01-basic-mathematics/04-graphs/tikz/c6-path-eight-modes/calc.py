# 第6章 6.2—6.5 新增示例的复算脚本（纯 Python，无第三方依赖）：六点路径的 Lf 与能量、八点路径余弦模态、
# 平缓/加跳动函数的谱坐标、两个三角形弱连接时的 lambda_2。运行：python3 本文件。
import math
def mv(A,x): return [sum(a*b for a,b in zip(row,x)) for row in A]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def lap(n,edges):
    L=[[0.0]*n for _ in range(n)]
    for i,j,w in edges:
        L[i][j]-=w;L[j][i]-=w;L[i][i]+=w;L[j][j]+=w
    return L
def jacobi(A,it=200):
    n=len(A);A=[r[:] for r in A];V=[[float(i==j) for j in range(n)] for i in range(n)]
    for _ in range(it):
        p,q,m=0,1,0
        for i in range(n):
            for j in range(i+1,n):
                if abs(A[i][j])>m:m,p,q=abs(A[i][j]),i,j
        if m<1e-14:break
        th=0.5*math.atan2(2*A[p][q],A[q][q]-A[p][p]);c,s=math.cos(th),math.sin(th)
        for k in range(n):
            akp,akq=A[k][p],A[k][q];A[k][p]=c*akp-s*akq;A[k][q]=s*akp+c*akq
        for k in range(n):
            apk,aqk=A[p][k],A[q][k];A[p][k]=c*apk-s*aqk;A[q][k]=s*apk+c*aqk
        for k in range(n):
            vkp,vkq=V[k][p],V[k][q];V[k][p]=c*vkp-s*vkq;V[k][q]=s*vkp+c*vkq
    ev=sorted([(A[i][i],[V[k][i] for k in range(n)]) for i in range(n)])
    return ev
P=lambda n:[(i,i+1,1.0) for i in range(n-1)]
f=[0,1,2,4,3,3.];L=lap(6,P(6));print("Lf",mv(L,f),"E",dot(f,mv(L,f)))
n=8;L=lap(n,P(n))
U=[]
for k in range(n):
    a=math.pi*k/n;u=[math.cos(a*(r-0.5)) for r in range(1,n+1)];nr=math.sqrt(dot(u,u));u=[x/nr for x in u];lam=2-2*math.cos(a)
    ok=max(abs(x-lam*y) for x,y in zip(mv(L,u),u))<1e-12
    sc=sum(1 for i in range(n-1) if u[i]*u[i+1]<0)
    U.append((lam,u));print(k,"%.3f"%lam,["%.3f"%x for x in u],ok,sc)
for name,g in [("ramp",[float(r) for r in range(1,9)]),("smooth",[1,2,3,4,4,3,2,1.]),("noisy",[1+0.5,2-.5,3+.5,4-.5,4+.5,3-.5,2+.5,1-.5]),("noisy2",[x+0.5*(-1)**r for r,x in enumerate([1,2,3,4,4,3,2,1.])])]:
    c=[dot(u,g) for _,u in U];E=dot(g,mv(L,g))
    print(name,g,["%.3f"%x for x in c],"n2",dot(g,g),"%.4f"%sum(x*x for x in c),"E",E,"%.4f"%sum(l*x*x for (l,_),x in zip(U,c)),"RQ %.4f"%(E/dot(g,g)))
for eps in [1,0.1,0.01,0]:
    ed=[(0,1,1),(1,2,1),(0,2,1),(3,4,1),(4,5,1),(3,5,1),(2,3,eps)]
    ev=jacobi(lap(6,ed));print(eps,["%.4f"%l for l,_ in ev],["%.3f"%x for x in ev[1][1]])
