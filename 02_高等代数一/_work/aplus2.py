import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify, prod
a=sp.symbols('a')
for n in [2,3,4]:
    xs=sp.symbols(f'x1:{n+1}')
    A=Matrix(n,n,lambda i,j: a + xs[i]**(j+1))
    D=sp.expand(A.det())
    Vd=sp.prod([xs[j]-xs[i] for i in range(n) for j in range(i+1,n)])
    en=sp.prod(xs)
    Q=sp.prod([xi-1 for xi in xs])
    pred=sp.expand(Vd*((1+a)*en - a*Q))
    print(f"n={n}:  |A| == V*( (1+a)∏x_i - a∏(x_i-1) ) ? {sp.simplify(D-pred)==0}")
    print(f"      a=0  :  {sp.simplify(sp.expand(D.subs(a,0)) - Vd*en)==0}")
    print(f"      a=-1 :  {sp.simplify(sp.expand(D.subs(a,-1)) - Vd*Q)==0}")
    # 线性于 a 的验证
    print(f"      线性: {sp.simplify(sp.expand(D - (D.subs(a,0) - a*(D.subs(a,-1)-D.subs(a,0)))))==0}")
    print()
