import random, fractions as F
from fractions import Fraction as Q

def gen(n):
    # 造一个满足条件的整数矩阵：先定负的非对角元，再让对角元足够大且各列和>0
    A=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j: A[i][j]=-random.randint(1,3)
    for j in range(n):
        s=sum(A[i][j] for i in range(n) if i!=j)   # 负数
        A[j][j]=-s+random.randint(1,3)             # 使列和>0
    return A

def det(M):
    M=[[Q(x) for x in row] for row in M]; n=len(M); d=Q(1)
    for c in range(n):
        p=next((r for r in range(c,n) if M[r][c]!=0), None)
        if p is None: return Q(0)
        if p!=c: M[c],M[p]=M[p],M[c]; d=-d
        d*=M[c][c]
        inv=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/inv
            for k in range(c,n): M[r][k]-=f*M[c][k]
    return d

def check(A):
    n=len(A)
    ok_sign=all(A[i][i]>0 for i in range(n)) and all(A[i][j]<0 for i in range(n) for j in range(n) if i!=j)
    ok_col=all(sum(A[i][j] for i in range(n))>0 for j in range(n))
    return ok_sign and ok_col

def schur(A):
    n=len(A); a11=Q(A[0][0])
    B=[[Q(A[i][j]) - Q(A[i][0])*Q(A[0][j])/a11 for j in range(1,n)] for i in range(1,n)]
    return B

random.seed(1)
bad=0
for trial in range(300):
    n=random.randint(2,6)
    A=gen(n)
    if not check(A): continue
    if det(A)<=0: print("  det<=0 ?!",A); bad+=1
    if n>2:
        B=schur(A)
        # 检查 Schur 补是否仍满足三条
        m=n-1
        s1=all(B[i][i]>0 for i in range(m))
        s2=all(B[i][j]<0 for i in range(m) for j in range(m) if i!=j)
        s3=all(sum(B[i][j] for i in range(m))>0 for j in range(m))
        if not(s1 and s2 and s3):
            print("  Schur 失去条件:", "diag",s1,"sign",s2,"colsum",s3); bad+=1
print("trials done, bad =",bad)
