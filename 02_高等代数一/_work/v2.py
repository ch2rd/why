import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify, prod

x,a,b,n=sp.symbols('x a b n')

print("== det(a_i+b_j) ==")
a1,a2,a3=symbols('a1 a2 a3'); b1,b2,b3=symbols('b1 b2 b3')
for N,(aa,bb) in [(2,([a1,a2],[b1,b2])),(3,([a1,a2,a3],[b1,b2,b3]))]:
    M=Matrix(N,N,lambda i,j: aa[i]+bb[j])
    print(N, sp.factor(M.det()))

print("== 箭形 ==")
a0,a1,a2,a3,c1,c2,c3,b1,b2,b3=symbols('a0 a1 a2 a3 c1 c2 c3 b1 b2 b3')
M=Matrix(4,4,lambda i,j: a0 if (i,j)==(0,0) else (([b1,b2,b3][j-1]) if i==0 else (([c1,c2,c3][i-1]) if j==0 else ((a1,a2,a3)[i-1] if i==j else 0))))
form=sp.prod([a1,a2,a3])*(a0-(b1*c1/a1+b2*c2/a2+b3*c3/a3))
print(N, sp.simplify(M.det()-sp.expand(form)))

print("== x^3+ax+b 重根 ==")
# condition det: res(f,f')
f=x**3+a*x+b
print("res(f,f') =", sp.factor(sp.resultant(f,sp.diff(f,x),x)))
print("solve a in terms of alpha:")
al=sp.symbols('alpha')
print(sp.solve([sp.Eq(3*al**2+a,0), sp.Eq(al**3+a*al+b,0)],[a,b]))

print("== (x-1)^3(x+1)^2 展开 ==")
print(sp.expand((x-1)**3*(x+1)**2))
f5=sp.Poly(x**5-x**4-2*x**3+2*x**2+x-1,x)
print("gcd(f,f')=",sp.gcd(f5,sp.Poly(sp.diff(f5.as_expr(),x),x)))

print("== 三对角 (a+b, ab) ==")
def tri(d,e,N):
    return sp.Matrix(N,N,lambda i,j: d if i==j else (e if abs(i-j)==1 else 0)).det()
for N in [1,2,3,4,5]:
    got=sp.simplify(tri(a+b,a*b,N))
    form=sp.simplify((a**(N+1)-b**(N+1))/(a-b))
    print(N, sp.simplify(got-form))
print("a=b case:", [sp.simplify(tri(2*a,a*a,N)-(N+1)*a**N) for N in [1,2,3,4]])

print("== Vandermonde 1..n rows x^1..x^n ==")
import math
for N in [2,3,4,5]:
    M=Matrix(N,N,lambda i,j: (j+1)**(i+1))
    pred=math.factorial(N)*prod(math.factorial(k) for k in range(1,N))
    print(N, M.det(), pred, M.det()==pred)

print("== Cramer 4元 ==")
A=Matrix([[2,1,-5,1],[1,-3,0,-6],[0,2,-1,2],[1,4,-7,6]])
print("detA =",A.det())
print("A*sol =",A*Matrix([1,-1,2,0]))

print("== det(xI+B) ==")
B=Matrix([[1,2,3],[1,2,3],[1,2,3]])
xl=sp.symbols('x')
print(sp.factor((xl*sp.eye(3)+B).det()))

print("== x^4+1 分解/不可约 ==")
print(sp.factor(x**4+1), sp.factor(x**4+1,extension=sp.I))
print("shift:",sp.expand((x+1)**4+1))

print("== x^4+4 ==")
print(sp.factor(x**4+4))
