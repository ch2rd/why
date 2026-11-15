import sympy as sp
from sympy import Matrix, symbols, prod, simplify
a=[0,1,2]; b=[2,3,6]
M=Matrix(3,3,lambda i,j: a[i]**j)
print("M =",M.tolist())
D=M.det(); print("D = det =",D)
V=1
for i in range(3):
    for j in range(i+1,3):
        V*= (a[j]-a[i])
print("V_3 = prod(a_j-a_i) =",V)
for j in range(3):
    Mj=M.copy()
    for i in range(3): Mj[i,j]=b[i]
    print(f"D_{j} = {Mj.det()}   c_{j} = D_{j}/D = {sp.Rational(Mj.det(),D)}")
print()
print("齐次方程组（b=0）只有零解？系数矩阵行列式 =",D)
# 验证 f = x^2+2
x=sp.symbols('x')
f=x**2+2
print("f(0),f(1),f(2) =",[f.subs(x,v) for v in a])
# 两点重合的退例
M2=Matrix([[1,0],[1,0]]); print("a=(0,0) 时系数行列式 =",M2.det())
