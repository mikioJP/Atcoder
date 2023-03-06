from collections import defaultdict

N, Q = map(int, input().split())

A = list(map(int, input().split()))

acuum_A = [0]*len(A)
acuum_A[0] = A[0]
∑ß
for i in range(1,len(A)):
    acuum_A[i]=acuum_A[i-1]+A[i]

for _ in range(Q):
    L, R = map(int, input().split())
    L-=1
    R-=1
    if L ==0:
        print(acuum_A[R])
    else:
        print(acuum_A[R]-acuum_A[L-1])

