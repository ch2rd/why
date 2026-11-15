import sympy as sp
from sympy import Matrix, symbols, simplify, cancel
x,y=sp.symbols('x y')
def A(n):  # 参考答案的矩阵：对角 x+y，上次对角 xy，下次对角 1
    return Matrix(n,n,lambda i,j: x+y if i==j else ((x*y) if j==i+1 else (1 if i==j+1 else 0))).det()
def B(n):  # 试卷印的：对角 xy，上次对角 x+y，下次对角 1
    return Matrix(n,n,lambda i,j: x*y if i==j else ((x+y) if j==i+1 else (1 if i==j+1 else 0))).det()
print("参考答案矩阵 A_n 是否 = (x^{n+1}-y^{n+1})/(x-y):")
for n in range(1,7):
    got=sp.factor(sp.expand(A(n)))
    pred=sp.cancel((x**(n+1)-y**(n+1))/(x-y))
    print(f"  n={n}: {got}   ==公式? {sp.simplify(got-pred)==0}")
print()
print("试卷印的矩阵 B_n（对角 xy、上次对角 x+y）:")
for n in range(1,5):
    print(f"  n={n}: {sp.factor(sp.expand(B(n)))}")
