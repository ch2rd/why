import sympy as sp
from sympy import symbols, gcd, Poly, rem, expand
x=sp.symbols('x')
def G(a,b): return sp.gcd(Poly(a,x,domain=sp.QQ),Poly(b,x,domain=sp.QQ)).as_expr()

print("== P4: x^2+x+1 divides x^{2n}+x^n+1 ? ==")
for n in range(1,14):
    r=sp.rem(expand(x**(2*n)+x**n+1),x**2+x+1,x)
    print("  n=%2d  rem=%-3s divisible=%-5s  3|n=%s" % (n,r,r==0,n%3==0))

print("== P5: (x-1)^2 divides n x^{n+1}-(n+1)x^n+1 ? ==")
for n in range(1,9):
    f=n*x**(n+1)-(n+1)*x**n+1
    print("  n=%d rem=%s" % (n, sp.rem(expand(f),(x-1)**2,x)))

print("== P6 ==  u=1, v=-x^2 :")
u=1; v=-x**2
print("   ",sp.expand(u*(x**6-1)+v*(x**4-1)))
print("    general sol check:",sp.expand((u+(x**2+1))*(x**6-1)+(v-(x**4+x**2+1))*(x**4-1)))

print("== P8: gcd(x^15-1,x^10-1,x^6-1) ==")
print("   ",G(G(x**15-1,x**10-1),x**6-1))

print("== P7: lcm check ==")
for m in range(1,7):
  for n in range(1,7):
    d=int(sp.gcd(m,n)); L=int(sp.lcm(m,n))
    lcm_poly=sp.cancel((x**m-1)*(x**n-1)/(x**d-1))
    ok=sp.rem(expand(lcm_poly*(x**d-1)),x**L-1,x)==0 and sp.rem(x**L-1,lcm_poly,x)==0
    # proper: lcm_poly should divide x^L - 1
    ok2=sp.simplify(sp.rem(sp.expand(x**L-1),sp.expand(lcm_poly),x))==0
    # alternative: check divisibility by poly division
    q,r=sp.div(Poly(x**L-1,x),Poly(sp.expand(lcm_poly),x))
    print("  m=%d n=%d  lcm divides x^L-1: %s" % (m,n,r.as_expr()==0))
