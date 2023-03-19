N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 動的計画法
dp = [ None ] * (N+1)
dp[1] = 0
dp[2] = A[0]
for i in range(3, N+1):
	dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

# 最短経路計算
# print(dp)
path = []
cur = N

while(1):
    path.append(cur)
    if cur == 1:
        break
    if dp[cur] == dp[cur-1] + A[cur-2]:
        cur-=1
    else:
        cur-=2
    # path.reverse()
    

print(len(path))
path.reverse()
for i in range(len(path)):
    path[i] = str(path[i])

print(" ".join(path))