from fractions import Fraction
def C(x, depth=30):
    # Cantor function
    x=float(x); val=0.0; scale=0.5
    for _ in range(depth):
        if x<1/3: x*=3
        elif x>2/3: val+=scale; x=3*x-2
        else: return val+scale
        scale/=2
    return val
N=243
pts1=[];pts2=[]
for i in range(N+1):
    x=i/N
    F=x/2+C(x)/4+(0.25 if x>=0.5 else 0)
    (pts1 if x<0.5 else pts2).append((x,F))
# add left limit at 1/2
x=0.5; pts1.append((x, x/2+C(x)/4)); pts2.insert(0,(0.5,0.5/2+C(0.5)/4+0.25))
f=lambda P:" ".join(f"({a:.4f},{b:.4f})" for a,b in P)
print("L:",f(pts1)); print("R:",f(pts2))
