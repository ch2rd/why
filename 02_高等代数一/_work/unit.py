import sympy as sp
from sympy import symbols, Poly
x=sp.symbols('x')
def G(a,b): return sp.gcd(Poly(a,x,domain=sp.QQ),Poly(b,x,domain=sp.QQ)).as_expr()
def v2(n):
    k=0
    while n%2==0: n//=2; k+=1
    return k

print("=== table: 4 combinations ===")
bad=[]
for m in range(1,13):
  for n in range(1,13):
    d=int(sp.gcd(m,n))
    pred={
      'mm': x**d-1,
      'mp': x**d+1 if v2(m)>v2(n) else 1,
      'pm': x**d+1 if v2(n)>v2(m) else 1,
      'pp': x**d+1 if v2(m)==v2(n) else 1,
    }
    got={'mm':G(x**m-1,x**n-1),'mp':G(x**m-1,x**n+1),'pm':G(x**m+1,x**n-1),'pp':G(x**m+1,x**n+1)}
    for k in pred:
        if sp.simplify(got[k]-pred[k])!=0:
            bad.append((m,n,k,got[k],pred[k]))
print("mismatches:", len(bad))
for b in bad[:10]: print("  ",b)

print("=== P1: x^n+1 | x^m-1  <=>  m/n is positive even ===")
bad2=0
for m in range(1,15):
  for n in range(1,15):
    div = sp.rem(x**m-1, x**n+1, x)==0
    cond = (m % n == 0) and ((m//n) % 2 == 0)
    if div!=cond: print("  MISMATCH",m,n,div,cond); bad2+=1
print("mismatches:", bad2)

print("=== P6: quotients coprime ===")
for m in range(2,11):
  for n in range(2,11):
    d=int(sp.gcd(m,n))
    A=sp.cancel((x**m-1)/(x**d-1)); B=sp.cancel((x**n-1)/(x**d-1))
    if sp.simplify(G(A,B)-1)!=0: print("  MISMATCH",m,n,A,B)
print("done")
