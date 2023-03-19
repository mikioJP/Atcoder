from collections import defaultdict

N , W = map(int, input().split())

ans=0
dp=[[-1]*(W+1) for _ in range(N+1)]
dp[0][0] = 0
for i in range(1,N+1):
    w, v = map(int, input().split())
    for j in range(W+1):
        if dp[i-1][j]!=-1:
            if j + w <= W:
                dp[i][j+w] = max(dp[i-1][j]+v,dp[i][j+w])
            dp[i][j] = max(dp[i-1][j],dp[i][j])

# print(dp)
print(max(dp[N]))

