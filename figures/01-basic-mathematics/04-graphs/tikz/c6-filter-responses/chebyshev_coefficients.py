import math
g=lambda l:1/(1+3*l)
a,b=0.0,2.0
def solve(A,y):
    n=len(A); M=[r[:]+[v] for r,v in zip(A,y)]
    for i in range(n):
        p=max(range(i,n),key=lambda r:abs(M[r][i])); M[i],M[p]=M[p],M[i]
        for r in range(n):
            if r!=i:
                f=M[r][i]/M[i][i]; M[r]=[x-f*z for x,z in zip(M[r],M[i])]
    return [M[i][n]/M[i][i] for i in range(n)]
for K in (2,4,6):
    nodes=[(a+b)/2+(b-a)/2*math.cos((2*j+1)*math.pi/(2*(K+1))) for j in range(K+1)]
    A=[[x**p for p in range(K+1)] for x in nodes]; c=solve(A,[g(x) for x in nodes])
    err=max(abs(g(a+(b-a)*t/2000)-sum(ci*(a+(b-a)*t/2000)**p for p,ci in enumerate(c))) for t in range(2001))
    print(K,["%.6f"%x for x in c],"maxerr %.4f"%err, "nodes",["%.4f"%x for x in nodes])
