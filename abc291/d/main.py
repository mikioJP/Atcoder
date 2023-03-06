from collections import defaultdict

N = int(input())

dp=[[0]*2 for _ in range(N)]
A_pre, B_pre  = map(int, input().split())

dp[0][0]=1
dp[0][1]=1

mod=998244353

for i in range(1,N):
    A_cur, B_cur = map(int, input().split())
    
    if A_cur!= A_pre and A_cur!= B_pre:
        dp[i][0] = (dp[i-1][0] + dp[i-1][1])%mod
    elif A_cur!= A_pre:
        dp[i][0] = dp[i-1][0]
    elif A_cur!= B_pre:
        dp[i][0] = dp[i-1][1]
    
    if B_cur!= A_pre and B_cur!= B_pre:
        dp[i][1] = (dp[i-1][0] + dp[i-1][1])%mod
    elif B_cur!= A_pre:
        dp[i][1] = dp[i-1][0]
    elif B_cur!= B_pre:
        dp[i][1] = dp[i-1][1]
    A_pre=A_cur
    B_pre=B_cur

print((dp[N-1][0]+dp[N-1][1])%mod)

    


