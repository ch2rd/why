import sympy as sp
from sympy import symbols, Matrix, factor, gcd, Poly, expand, simplify, cancel, det, Rational

x,a,b,n=sp.symbols('x a b n')

print("== 1. gcd+Bezout 卷一 ==")
f=sp.Poly(x**4+x**3-x-1,x); g=sp.Poly(x**3-x**2+x-1,x)
G=sp.gcd(f,g); print("gcd:",G)
u=sp.Rational(-1,2)*(x+1); v=sp.Rational(1,2)*(x**2+3*x+3)
print("uf+vg =",sp.expand(u*f.as_expr()+v*g.as_expr()))

print("== 2. 三对角 13/6 ==")
def tri(d,e,N):
    return sp.Matrix(N,N,lambda i,j: d if i==j else (e if abs(i-j)==1 else 0)).det()
for N in [1,2,3,4,5]:
    print(N, sp.factor(tri(13,6,N)), "formula",(9**(N+1)-4**(N+1))//5 if N<6 else '')

print("== 3. 加边 a_i ==")
a1,a2,a3,a4=symbols('a1 a2 a3 a4')
for N,aa in [(2,[a1,a2]),(3,[a1,a2,a3]),(4,[a1,a2,a3,a4])]:
    M=Matrix(N,N,lambda i,j: aa[i]+1 if i==j else 1)
    form=sp.prod(aa)*(1+sum(1/aa[i] for i in range(N)))
    print(N, sp.simplify(M.det()-sp.expand(form)))

print("== 4. 有理根分解 ==")
print(sp.factor(x**4-x**3-7*x**2+x+6))

print("== 5. Vandermonde变形 末行 x^n ==")
xs=symbols('x1:5')
M=Matrix(4,4,lambda i,j: xs[j]**i if i<3 else xs[j]**4)
V=sp.prod([xs[j]-xs[i] for i in range(4) for j in range(i+1,4)])
print(sp.simplify(sp.expand(M.det()-sp.expand(V*sum(xs)))))
