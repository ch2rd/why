import sympy as sp
from sympy import Poly, symbols, Matrix, factor, expand, simplify, gcd, rem
x=sp.symbols('x')

print("== 找 gcd+Bezout 例子 ==")
import itertools, random
random.seed(7)
def bezout(p,q):
    # p,q Poly over QQ
    old_r,r=sp.Poly(p,x,domain=sp.QQ),sp.Poly(q,x,domain=sp.QQ)
    old_s,s=sp.Poly(1,x,domain=sp.QQ),sp.Poly(0,x,domain=sp.QQ)
    old_t,t=sp.Poly(0,x,domain=sp.QQ),sp.Poly(1,x,domain=sp.QQ)
    while r.degree()>0 or r.as_expr()!=0:
        if r.as_expr()==0: break
        quo,remd=sp.div(old_r,r,domain=sp.QQ)
        old_r,r=r,sp.Poly(remd,x,domain=sp.QQ)
        old_s,s=s,old_s-quo*s
        old_t,t=t,old_t-quo*t
    return old_r,old_s,old_t

cands=[]
for _ in range(40000):
    f=Poly([random.randint(-3,3) for _ in range(4)]+[1],x)
    g=Poly([random.randint(-3,3) for _ in range(2)]+[1],x)
    d=gcd(f,g)
    if d.degree()==1 and d.as_expr()!=x:
        G,s,t=bezout(f,g)
        if all(c.q in (1,2) for c in list(s.all_coeffs())+list(t.all_coeffs())):
            cands.append((f.as_expr(),g.as_expr(),d.as_expr(),s.as_expr(),t.as_expr()))
    if len(cands)>=6: break
for c in cands[:6]:
    print("f=",c[0],"  g=",c[1],"  gcd=",c[2])
    print("   u=",sp.nsimplify(c[3]),"  v=",sp.nsimplify(c[4]))
