from collections import defaultdict

N, M = map(int, input().split())

adj=[set() for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    u-=1
    v-=1
    
    adj[u].add(v)
print(adj)

ans = 0

for i in range(len(adj)):
    set_i =adj[i]
    for j in set_i:
        if not set_i> adj[j]:
            set_subst = set_i - adj[j]
            ans += len(set_subst)
            adj[i]|=set_subst

for i in range(len(adj)):
    set_i =adj[i]
    for j in set_i:
        if not set_i> adj[j]:
            set_subst = set_i - adj[j]
            ans += len(set_subst)
            adj[i]|=set_subst
print(ans)
            