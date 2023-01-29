from collections import defaultdict

N1, N2 = map(int, input().split())

S=[[] for i in range(N1)]

T=[[] for i in range(N2)]

d=defaultdict(int)
for i in range(N1):
    d[str(input())[-3:]]+=1
for i in range(N2):
    T[i]=str(input())
T=list(set(T))

ans=0
for i in range(len(T)):
    ans+=d[T[i]]
print(ans)