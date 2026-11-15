import sympy as sp
from sympy import Matrix
def tri(n):
    return Matrix(n,n,lambda i,j: 13 if i==j else (6 if abs(i-j)==1 else 0)).det()
print("n | direct | formula (9^(n+1)-4^(n+1))/5 | equal")
for n in range(1,9):
    d=int(tri(n)); f=(9**(n+1)-4**(n+1))//5
    print(n, "|", d, "|", f, "|", d==f)
print()
print("D1..D6 =",[int(tri(k)) for k in range(1,7)])
print("6x6 =",int(tri(6)),"  (9^7-4^7)/5 =",(9**7-4**7)//5)
