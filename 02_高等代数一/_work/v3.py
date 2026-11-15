import sympy as sp
from sympy import symbols, Matrix, factor, simplify, expand
a,b,n,x=symbols('a b n x')

def tri_gen(d,sub,sup,N):
    return Matrix(N,N,lambda i,j: d if i==j else (sup if j==i+1 else (sub if i==j+1 else 0))).det()

print("== 三对角 d=a+b, 上=ab, 下=1 ==")
for N in [1,2,3,4,5,6]:
    got=sp.expand(tri_gen(a+b,1,a*b,N)); form=sp.cancel((a**(N+1)-b**(N+1))/(a-b))
    print(N, sp.simplify(got-form)==0, sp.factor(got))
print("a=b (N=4):", sp.expand(tri_gen(2*a,1,a**2,4) - 5*a**4))

print("== 三对角 13/6 再确认 N=6 ==")
print(tri_gen(13,6,6,6), (9**7-4**7)//5)

print("== (x-1)|f(x) <=> (x^n-1)|f(x^n) 抽查 ==")
for f in [x**2-1, x**3-1, x**2+x+1, x**3-2*x+1, x-1, x**2+1]:
    lhs=sp.rem(f,x-1,x)==0
    g=expand(f.subs(x,x**4))
    rhs=sp.rem(g,x**4-1,x)==0
    print(f, lhs, rhs, lhs==rhs)
