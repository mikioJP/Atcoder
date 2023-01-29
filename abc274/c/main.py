from collections import defaultdict

N = int(input())

A = list(map(int,input().split(" ")))
A = list(map(lambda x: x-1, A))
# print(A)
par=[0]*(N*2+1)
gen=[0]*(N*2+1)

for i in range(N):
    # par[A[i]*2]=A[i]
    gen[(i+1)*2-1]+=gen[A[i]]+1
    # par[A[i]*2+1]=A[i]
    gen[(i+1)*2]+=gen[A[i]]+1

for i in range(2*N+1):
    print(gen[i])


