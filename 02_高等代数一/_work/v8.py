import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify
x=sp.symbols('x')
print("== x^4+4 其实可约，x^4+1 不可约 ==")
print("x^4+4 =",sp.factor(x**4+4))
print("x^4+1 =",sp.factor(x**4+1), " 在R:",sp.factor(x**4+1,extension=sp.sqrt(2)))

print()
print("== 卷六 Q1: 3x3 约化 ==")
a,b,c=sp.symbols('a b c')
p,q,s=sp.symbols('p q s')
M3=Matrix([[p,q,-q],[q,p,s],[-q,s,p]])
print("3x3 det =",sp.factor(expand(M3.det())))
# 期望等于 (x-a-b-c? ) 用 p,q,s 表示三个因子
# x+a-b-c = p+? ; 直接检验与原式一致性
M=Matrix([[x,a,b,c],[a,x,c,b],[b,c,x,a],[c,b,a,x]])
D=M.det()
print("原式 =",sp.factor(D))
M2=M.copy()
# 数值校验：C1求和, 提因子, Ri-R1
import random
random.seed(3)
for _ in range(3):
    sub={x:random.randint(-3,3),a:random.randint(-3,3),b:random.randint(-3,3),c:random.randint(-3,3)}
    Mv=M.subs(sub)
    N=Mv.copy()
    for i in range(4): N[i,0]=sum(Mv[i,j] for j in range(4))
    f=N[0,0]
    N=N/f
    for i in range(1,4): N[i,:]=N[i,:]-N[0,:]
    sub3=N[1:4,1:4]
    print(" check:",sp.simplify(sub3.det()-(D.subs(sub)/f)))

print()
print("== 卷六 Q8: 4阶反对称 ==")
A12,A13,A14,A23,A24,A34=sp.symbols('a12 a13 a14 a23 a24 a34')
A=Matrix([[0,A12,A13,A14],[-A12,0,A23,A24],[-A13,-A23,0,A34],[-A14,-A24,-A34,0]])
for (i,j) in [(0,1),(0,2),(0,3)]:
    Mij=A.minor_submatrix(i,j)
    print(f"M1{j+1} =",sp.factor(expand(Mij.det())))
print("det =",sp.factor(expand(A.det())))
