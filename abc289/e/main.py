from collections import defaultdict
from collections import deque
import sys
input = sys.stdin.readline
t=int(input())

for i in range(t):
    n,m=map(int,input().split())

    C=list(map(int,input().split()))
    L=[[] for i in range(n)]
    for j in range(m):
        u,v=map(int,input().split())
        u-=1
        v-=1
        L[u].append(v)
        L[v].append(u)

    seen=[[-1]*n for i in range(n)]
    q=deque()
    q.append((0,n-1))
    seen[0][n-1]=0

    flag=1
    while q:
        t,a=q.popleft()

        for nt in L[t]:
            for na in L[a]:
                if C[nt]!=C[na] and seen[nt][na]==-1: 
                    q.append((nt,na))
                    seen[nt][na]=seen[t][a]+1
                    if nt==n-1 and na==0:
                        print(seen[n-1][0])
                        flag=0
                        break
            if flag==0:
                break
    if flag:
        print(-1)
