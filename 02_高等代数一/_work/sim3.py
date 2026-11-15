import sympy as sp
from sympy import symbols, Poly, gcd, div
x=sp.symbols('x')
def G(a,b): return sp.gcd(Poly(a,x,domain=sp.QQ),Poly(b,x,domain=sp.QQ)).as_expr()
def v2(n):
    k=0
    while n%2==0: n//=2; k+=1
    return k

print("m  n | direct gcd           | x^e+1 if v2(m)>v2(n) | old (x^g-1)/(x^h-1) | agree")
bad=0
for m in range(1,16):
  for n in range(1,16):
    e=int(sp.gcd(m,n)); g=int(sp.gcd(m,2*n)); h=int(sp.gcd(g,n))
    simple = x**e+1 if v2(m)>v2(n) else 1
    old = sp.cancel((x**g-1)/(x**h-1))
    d = G(x**m-1, x**n+1)
    if sp.simplify(d-simple)!=0 or sp.simplify(d-old)!=0:
        print("  MISMATCH", m, n, d, simple, old); bad+=1
print("mismatches:", bad)
