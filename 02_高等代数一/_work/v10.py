import sympy as sp
from sympy import Matrix, symbols, factor, expand, simplify, prod, Poly
x=sp.symbols('x')

print("== 北工大 2025 一(1): (x-1)^2 | x^3+Ax^2+B ==")
A,B=sp.symbols('A B')
f=x**3+A*x**2+B
sols=sp.solve([sp.Eq(f.subs(x,1),0), sp.Eq(sp.diff(f,x).subs(x,1),0)],[A,B])
print(sols, " A-B =", sp.simplify(sols[A]-sols[B]))
print("直接除:",sp.div(f,(x-1)**2,x))

print("== 北工大 2025 一(2): |1..16| ==")
M=Matrix(4,4,lambda i,j: 4*i+j+1); print(M.det())

print("== 北工大 2025 三(11): M11+M21-M41 ==")
D=Matrix([[3,-5,2,1],[1,1,0,-5],[-1,3,1,3],[2,4,1,3]])
print("D =",D.det())
M11=D.minor_submatrix(0,0).det(); M21=D.minor_submatrix(1,0).det(); M41=D.minor_submatrix(3,0).det()
print("M11,M21,M41 =",M11,M21,M41," sum =",M11+M21-M41)
# 等价：第1列换成 (1,-1,0,1)
E=D.copy()
for i,c in enumerate([1,-1,0,1]): E[i,0]=c
print("换成(1,-1,0,1)后的行列式 =",E.det())

print("== 北工大 2025 三(9): 余式 ==")
r=sp.symbols('r0:3')
rr=r[0]*x**2+r[1]*x+r[2]
sol=sp.solve([sp.Eq(rr.subs(x,1),3), sp.Eq(rr.subs(x,-1),1), sp.Eq(sp.diff(rr,x).subs(x,1),7)],r)
print(sol, "=> r(x) =",rr.subs(sol))

print("== 北工大 2025 三(10) ==")
g=x**4-x**3-3*x**2+5*x-2
print(sp.factor(g))

print("== 田青春2015 一(2): 三对角 上4 下1 对角5 ==")
def tri(N):
    return Matrix(N,N,lambda i,j: 5 if i==j else (4 if j==i+1 else (1 if i==j+1 else 0))).det()
for N in [1,2,3,4]:
    print(N, tri(N), "公式",(4**(N+1)-1)//3)

print("== Cauchy: D_n = |1/(1-a_i b_j)| ==")
a=sp.symbols('a1:4'); b=sp.symbols('b1:4')
M=Matrix(3,3,lambda i,j: 1/(1-a[i]*b[j]))
num=sp.simplify(M.det())
pred=prod([(a[j]-a[i]) for i in range(3) for j in range(i+1,3)])*prod([(b[j]-b[i]) for i in range(3) for j in range(i+1,3)])/prod([1-a[i]*b[j] for i in range(3) for j in range(3)])
print("差 =",sp.simplify(num-pred))
