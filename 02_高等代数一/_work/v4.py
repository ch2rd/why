import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify, prod, Poly
x,a,b,c,p,q,n=sp.symbols('x a b c p q n')

print("== |i-j| 行列式 ==")
for N in [1,2,3,4,5,6]:
    print(N, Matrix(N,N,lambda i,j: abs(i-j)).det())

print("== 4阶 x a b c / a x c b / b c x a / c b a x ==")
M=Matrix([[x,a,b,c],[a,x,c,b],[b,c,x,a],[c,b,a,x]])
print(sp.factor(M.det()))

print("== 三对角 0/1 ==")
def tr(off,N):
    return Matrix(N,N,lambda i,j: 0 if i==j else (1 if abs(i-j)==1 else 0)).det()
print([tr(1,N) for N in range(1,8)])

print("== |x 1 1;1 x 1;1 1 x| ==")
print(sp.factor(Matrix([[x,1,1],[1,x,1],[1,1,x]]).det()))

print("== 对角x 其余a ==")
for N in [2,3,4,5]:
    M2=Matrix(N,N,lambda i,j: x if i==j else a)
    print(N, sp.simplify(M2.det()-(x-a)**(N-1)*(x+(N-1)*a)))

print("== x^3-3x^2+ax+b 重根条件 ==")
f=x**3-3*x**2+a*x+b
print("res =",sp.factor(sp.resultant(f,sp.diff(f,x),x)))

print("== x^4+a x^2+b 重根 ==")
f2=x**4+a*x**2+b
print("res =",sp.factor(sp.resultant(f2,sp.diff(f2,x),x)))

print("== x^6-1 ==")
print(sp.factor(x**6-1), sp.factor(x**6-1,extension=sp.I))
print("Phi_6:",sp.factor(x**6-1)[0] if 0 else sp.cyclotomic_poly(6,x))

print("== x^4+4 分解(R) ==")
print(sp.factor(x**4+4))
