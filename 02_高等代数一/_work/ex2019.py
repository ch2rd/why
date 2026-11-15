import sympy as sp
from sympy import Matrix, symbols, prod, simplify, expand, factor

print("=== 2019 题二: (行 i=n..0, 列 k=0..n) a_i^{n-k} b_i^k ===")
for n in [1,2,3]:
    a=sp.symbols(f'a0:{n+1}'); b=sp.symbols(f'b0:{n+1}')
    idx=list(range(n,-1,-1))
    M=Matrix(n+1,n+1,lambda r,c: a[idx[r]]**(n-c)*b[idx[r]]**c)
    D=sp.factor(sp.expand(M.det()))
    Q=sp.factor(sp.expand(sp.prod([a[j]*b[i]-a[i]*b[j] for i in range(n+1) for j in range(i+1,n+1)])))
    P=sp.factor(sp.expand(sp.prod([a[i]*b[j]-a[j]*b[i] for i in range(n+1) for j in range(i+1,n+1)])))
    print(f" n={n}: D == prod(a_j b_i - a_i b_j) ? {sp.simplify(D-Q)==0} ;  D == prod(a_i b_j - a_j b_i) ? {sp.simplify(D-P)==0}")
    if n<=2: print("   D =",D,"\n   Q =",Q)

print()
print("=== 2019 题五: 三对角 xy / x+y / 1 ===")
x,y=sp.symbols('x y')
def tri(n):
    return Matrix(n,n,lambda i,j: x*y if i==j else ((x+y) if j==i+1 else (1 if i==j+1 else 0))).det()
for n in range(1,7):
    print(f" n={n}:", sp.factor(sp.expand(tri(n))))
import math
def formula(n):
    s=0
    for k in range(n//2+1):
        s+= (-1)**k*math.comb(n-k,k)*(x*y)**(n-2*k)*(x+y)**k
    return s
print(" 公式校验:", [sp.simplify(sp.expand(tri(n)-formula(n)))==0 for n in range(1,8)])
