n = int(input())

d = [[] for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    d[a].append(b)
    d[b].append(a)

#parent?
#各頂点の親と深さを記録
par = [-1]*n
depth = [0]*n
from collections import deque
st = deque()
st.append((0,0))
while len(st)>0:
    cur, dep = st.pop()
    for nxt in d[cur]:
        if nxt == par[cur]:
            continue
        par[nxt] = cur
        depth[nxt] = dep+1
        st.append((nxt,dep+1))

L = [(i,depth[i]) for i in range(n)]
L.sort(key=lambda x:-x[1])
# print(L)

dp = [[[],[]] for _ in range(n)]
# dpi,k,j​ 頂点 i を根とする部分木に含まれる頂点を V として選ぶかどうかを決める方法であって、
# 連結成分数が j であるようなものの個数。ただし、k=0 ならば頂点 i は選ばれず、k=1 ならば選ばれている。

for cur, _ in L:
    count = 1
    sdp0 = [1]
    sdp1 = [1]
    for nxt in d[cur]:
        if nxt == par[cur]:
            continue
        ndp0 = dp[nxt][0]
        ndp1 = dp[nxt][1]
        count += len(ndp0)
        vndp0 = [0]*count
        vndp1 = [0]*count
        for i in range(len(sdp0)):
            for j in range(len(ndp0)):
                vndp0[i+j] += sdp0[i]*ndp0[j]
                vndp0[i+j] %= 998244353
                vndp1[i+j] += sdp1[i]*(ndp0[j]+ndp1[j])
                vndp1[i+j] %= 998244353
                vndp0[i+j+1] += sdp0[i]*ndp1[j]
                vndp0[i+j+1] %= 998244353
        sdp0 = vndp0
        sdp1 = vndp1
    dp[cur][0] = sdp0
    dp[cur][1] = sdp1


dp0 = dp[0][0] + [0]
dp1 = dp[0][1] + [0]
for i in range(1, n+1):
    print((dp0[i]+dp1[i-1])%998244353)




