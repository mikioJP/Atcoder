from collections import defaultdict

N, K = map(int, input().split())

A = list(map(int, input().split()))

mod=998244353

seen = [False]*(N+K)

for i in A:
    seen[i]=True

cnt=K
result=1
i=0
cum=0
series_cnt=seen.index(False)
time=0
choice=[0]*(N+K)

while time < K:
    if (False) in seen:
        series_cnt=seen.index(False)
    else:
        series_cnt+=1
    choice[time]=(series_cnt+1) %mod 
    seen[series_cnt]=True
    time+=1

for i in range(K):
    result = result*choice[i] % mod
print(choice)
print(result)