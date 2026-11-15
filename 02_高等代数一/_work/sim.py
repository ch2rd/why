import sympy as sp
from sympy import symbols, gcd, Poly, div, rem, expand, factor
x=sp.symbols('x')

def G(a,b):
    return sp.gcd(Poly(a,x,domain=sp.QQ),Poly(b,x,domain=sp.QQ)).as_expr()

print("== 题2: gcd(x^m+1, x^n+1)  ==")
for m in range(1,9):
  for n in range(1,9):
    g=int(sp.gcd(m,n)); pred = x**g+1 if (m//g)%2==1 and (n//g)%2==1 else 1
    got=G(x**m+1,x**n+1)
    if sp.simplify(got-pred)!=0: print("  MISMATCH",m,n,got,pred)
print("  全部通过")

print("== 题3: gcd(x^m-1, x^n+1)  ==")
bad=0
for m in range(1,11):
  for n in range(1,11):
    g=int(sp.gcd(m,2*n)); h=int(sp.gcd(g,n))
    pred=sp.cancel((x**g-1)/(x**h-1))
    got=G(x**m-1,x**n+1)
    if sp.simplify(got-pred)!=0: print("  MISMATCH",m,n,got,pred); bad+=1
print("  不匹配数:",bad)

print("== 题4: x^2+x+1 | x^{2n}+x^n+1 ? ==")
for n in range(1,13):
    r=sp.rem(expand(x**(2*n)+x**n+1),x**2+x+1,x)
    print("  n=",n," 余式=",r," 结论:", "可整除" if r==0 else "不可整除", "| 3∤n:",n%3!=0)

print("== 题5: (x-1)^2 | n x^{n+1}-(n+1)x^n+1 ==")
for n in range(1,8):
    f=n*x**(n+1)-(n+1)*x**n+1
    print("  n=",n," 余式=",sp.rem(expand(f),(x-1)**2,x))

print("== 题6: u(x^6-1)+v(x^4-1)=x^2-1 ==")
u=1; v=-x**2
print("  ",sp.expand(u*(x**6-1)+v*(x**4-1)))
print("   通解检查:",sp.expand((u+(x**2+1))*(x**6-1)+(v-(x**4+x**2+1))*(x**4-1)))

print("== 题8: gcd(x^15-1,x^10-1,x^6-1) ==")
g=G(G(x**15-1,x**10-1),x**6-1); print("  ",g,"  gcd(15,10,6)=",sp.gcd(15,sp.gcd(10,6)))
