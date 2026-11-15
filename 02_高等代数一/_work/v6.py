import sympy as sp, random
from sympy import Poly, symbols, Matrix, factor, expand, simplify, gcd
x,a,b,c,lam=sp.symbols('x a b c lambda')

def bez(p,q):
    old_r,r=Poly(p,x,domain=sp.QQ),Poly(q,x,domain=sp.QQ)
    os_,s=Poly(1,x,domain=sp.QQ),Poly(0,x,domain=sp.QQ)
    ot,t=Poly(0,x,domain=sp.QQ),Poly(1,x,domain=sp.QQ)
    while r.as_expr()!=0:
        quo,remd=sp.div(old_r,r,domain=sp.QQ)
        old_r,r=r,Poly(remd,x,domain=sp.QQ)
        os_,s=s,os_-quo*s
        ot,t=t,ot-quo*t
    return old_r,os_,ot

print("== 搜索整数 Bezout 例 ==")
random.seed(11); out=[]
for _ in range(200000):
    f=Poly([random.randint(-4,4) for _ in range(random.choice([3,4]))]+[1],x)
    g=Poly([random.randint(-4,4) for _ in range(random.choice([2,3]))]+[1],x)
    d=gcd(f,g)
    if d.degree()!=1: continue
    G,s,t=bez(f,g)
    # normalize so that u*f+v*g = d
    k=sp.simplify(d.as_expr()/G.as_expr())
    u=(s.as_expr()*k); v=(t.as_expr()*k)
    u=sp.expand(u); v=sp.expand(v)
    if u.is_polynomial(x) and v.is_polynomial(x):
        if all(q.is_integer for q in Poly(u,x).all_coeffs()) and all(q.is_integer for q in Poly(v,x).all_coeffs()):
            if u.free_symbols<={x} and abs(sp.Poly(u,x).max_norm())<12 and abs(Poly(v,x).max_norm())<12:
                if sp.expand(u*f.as_expr()+v*g.as_expr()-d.as_expr())==0:
                    out.append((f.as_expr(),g.as_expr(),d.as_expr(),u,v))
    if len(out)>=8: break
seen=set()
for f,g,d,u,v in out:
    if (f,g) in seen: continue
    seen.add((f,g))
    print("f=",f); print("  g=",g); print("  gcd=",d,"  u=",u,"  v=",v)
    if len(seen)>=5: break

print()
print("== 4阶反对称 ==")
a12,a13,a14,a23,a24,a34=sp.symbols('a12 a13 a14 a23 a24 a34')
A=Matrix([[0,a12,a13,a14],[-a12,0,a23,a24],[-a13,-a23,0,a34],[-a14,-a24,-a34,0]])
pf=a12*a34-a13*a24+a14*a23
print("diff:",sp.simplify(A.det()-pf**2))

print("== 卷四 C1 |i-j| 公式 ==")
for N in range(2,8):
    got=Matrix(N,N,lambda i,j: abs(i-j)).det()
    pred=(-1)**(N-1)*(N-1)*2**(N-2)
    print(N,got,pred,got==pred)

print("== 卷五 C1 ==")
print(sp.factor(Matrix([[x+1,2,3],[1,x+2,3],[1,2,x+3]]).det()))

print("== 卷五 C2 |i+j-1| n>=3 ==")
for N in [2,3,4,5]:
    print(N, Matrix(N,N,lambda i,j: i+j+1).det())

print("== 卷五 C3 det ==")
A3=Matrix([[1,2,3],[3,-1,1],[1,-3,2]])
print("det=",A3.det()," A*[2,-1,3]=",A3*Matrix([2,-1,3]))

print("== 卷四 C3 x^4-4x+lam 重根 ==")
print("res=",sp.factor(sp.resultant(x**4-4*x+lam,4*x**3-4,x)))

print("== x^6-1 重根? (f,f') ==")
f6=Poly(x**6-1,x); print(sp.gcd(f6,Poly(sp.diff(f6.as_expr(),x),x)))

print("== 卷五 C4 x^4+a x^2+b ==")
print(sp.factor(sp.resultant(x**4+a*x**2+b,sp.diff(x**4+a*x**2+b,x),x)))
