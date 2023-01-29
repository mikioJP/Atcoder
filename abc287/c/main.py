# グラフ探索：s-tパスを求める
# 計算量：O(|V|+|E|)

INF=10**9
# 入力受取        
N, M = map(int, input().split())

# グラフ生成
G = [[] for i in range(N)]

for j in range(M):
    a, b = map(int, input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)

# print(G)

if N != M+1:
    print("No")
    exit()

for i in range(N):
    if(len(G[i])) > 2:
        print("No")
        exit()

from collections import deque

que=deque(G[0])
seen=[False for _ in range(N)]
while que:
    x=que.popleft()
    if (seen[x]):
        continue
    seen[x]=True
    if (G[x]):
        for i in G[x]:
            que.append(i)

if seen.count(1)==N:
    print("Yes")
else:
    print("No")