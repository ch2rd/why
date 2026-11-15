import sympy as sp
from sympy import symbols, Matrix, factor, expand, simplify
x,a,b,c,p,q,s=sp.symbols('x a b c p q s')
M=Matrix([[x,a,b,c],[a,x,c,b],[b,c,x,a],[c,b,a,x]])
Ns=M.copy()
for i in range(4): Ns[i,0]=x+a+b+c
for i in range(4): Ns[i,0]=Ns[i,0]/(x+a+b+c)   # 第1列全为1
for i in range(1,4): Ns[i,:]=Ns[i,:]-Ns[0,:]  # Ri <- Ri-R1
M3=Ns[1:4,1:4]
print("M3 =",M3)
d3=sp.factor(expand(M3.det()))
print("det M3 =",d3)
target=sp.expand((x+a-b-c)*(x-a+b-c)*(x-a-b+c))
print("相等?",sp.simplify(expand(M3.det()-target))==0)
sub={x:p+a, c:q+b, a:s+b}
print(" M3(p,q,s) =",sp.simplify(M3.subs(sub)))
print(" det =",sp.factor(sp.expand(d3.subs(sub))))
print(" 目标 =",sp.factor(sp.expand(target.subs(sub))))
