import sympy as sp
from sympy import Matrix, symbols, simplify, expand, prod, eye, zeros
a=sp.symbols('a')

print("=== 加边恒等式 det[[V,1],[-a*1^T,1]] == det(V + a*ones) ===")
for n in [2,3]:
    xs=sp.symbols(f'x1:{n+1}')
    V=Matrix(n,n,lambda i,j: xs[i]**(j+1))
    A=V + a*sp.ones(n,n)
    M=zeros(n+1,n+1)
    for i in range(n):
        for j in range(n): M[i,j]=V[i,j]
        M[i,n]=1
    for j in range(n): M[n,j]=-a
    M[n,n]=1
    print(f" n={n}: equal? {sp.simplify(expand(M.det()-A.det()))==0}")

print()
print("=== P1: det(diag(a_i)+11^T) ===")
for n in [2,3,4]:
    aa=sp.symbols(f'am1:{n+1}')
    D=(sp.diag(*aa)+sp.ones(n,n)).det()
    pred=prod(aa)*(1+sum(1/x for x in aa))
    print(f" n={n}: ok? {sp.simplify(expand(D-pred))==0}   D={sp.factor(expand(D))}")

print()
print("=== P2: det(I + a b^T) ===")
for n in [2,3,4]:
    aa=sp.symbols(f'c1:{n+1}'); bb=sp.symbols(f'e1:{n+1}')
    D=(sp.eye(n)+Matrix(aa)*Matrix(bb).T).det()
    pred=1+sum(aa[i]*bb[i] for i in range(n))
    print(f" n={n}: ok? {sp.simplify(expand(D-pred))==0}")

print()
print("=== P3: 箭形 ===")
for n in [2,3]:
    a0=sp.symbols('a0')
    aa=sp.symbols(f'q1:{n+1}'); bb=sp.symbols(f'r1:{n+1}'); cc=sp.symbols(f's1:{n+1}')
    M=zeros(n+1,n+1)
    M[0,0]=a0
    for i in range(n):
        M[0,i+1]=bb[i]; M[i+1,0]=cc[i]; M[i+1,i+1]=aa[i]
    D=M.det()
    pred=prod(aa)*(a0-sum(bb[i]*cc[i]/aa[i] for i in range(n)))
    print(f" n={n}: ok? {sp.simplify(expand(D-pred))==0}")
