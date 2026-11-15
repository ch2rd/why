import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify, prod
x=sp.symbols('x')
print("== 卷二C1 n=3,5 ==")
for n_ in [3,5]:
    xs=symbols(f'x1:{n_+1}')
    M=Matrix(n_,n_,lambda i,j: xs[j]**(i if i<n_-1 else n_))
    V=prod([xs[j]-xs[i] for i in range(n_) for j in range(i+1,n_)])
    print(n_, sp.simplify(expand(M.det()-expand(V*sum(xs))))==0)
print("== 卷二C1 n=2 说明 ==")
print("n=2 行重复，需 n>=3")

print("== 卷六C4 2x^4-7x^3+4x^2+7x-6 ==")
f=2*x**4-7*x**3+4*x**2+7*x-6
print(sp.factor(f))
P=sp.Poly(f,x); print("gcd(f,f')=",sp.gcd(P,sp.Poly(sp.diff(f,x),x)))

print("== 卷四C4 2x^3-2x^2-x+1 / x^2-1 ==")
f2=2*x**3-2*x**2-x+1; g2=x**2-1
print("gcd=",sp.gcd(sp.Poly(f2,x),sp.Poly(g2,x)))
print("check u=1,v=2-2x:",sp.expand(f2+(2-2*x)*g2))

print("== 卷六C3 x^6-1 在R上 ==")
print(sp.factor(x**6-1), "|", sp.factor(x**6-1,extension=sp.sqrt(3)))
