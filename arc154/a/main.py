from collections import defaultdict

N=int(input())
A=str(input())
B=str(input())

min=100000000000000

for i in range(N):
    tmpA=A
    tmpB=B
    for j in range(i,N):
        rev=tmpA[i]
        tmpA[i] = tmpB[j]
        tmpB[j]=rev
        if (min > int(tmpA)*int(tmpB)):
            A=tmpA
            B=tmpB
print(A*B)