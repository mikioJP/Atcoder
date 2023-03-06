from collections import defaultdict, deque

N, M = map(int, input().split())

a = list(map(int, input().split()))

q=[]
ans=[]

for i in range(N):
    if i+1 in a:
        q.append(i+1)
    else:
        if q:
            q.append(i+1)
            ans= ans + q[::-1]
            q=[]
        else:
            ans.append(i+1)
for i in range(len(ans)):
    if i == len(ans)-1: 
        print(ans[i], end="")
    else:
        print(ans[i], end=" ")
print()
        