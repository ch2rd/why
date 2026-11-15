import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify, prod
a=sp.symbols('a')
for n in [2,3]:
    xs=sp.symbols(f'x1:{n+1}')
    A=Matrix(n,n,lambda i,j: a + xs[i]**(j+1))
    D=sp.factor(expand(A.det()))
    print(f"n={n}:  |A| = {D}")
    # 提出范德蒙德因子
    Vand=sp.prod([xs[j]-xs[i] for i in range(n) for j in range(i+1,n)])
    print("   除以范德蒙德:", sp.simplify(sp.cancel(expand(A.det())/Vand)))
    # 再看 a=0 时
    print("   a=0 时:", sp.factor(expand(A.det().subs(a,0))))
    print()
