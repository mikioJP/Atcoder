N=int(input())
A=list(map(int,input().split()))
M=int(input())
B=list(map(int,input().split()))
X=int(input())
dp=[0 for i in range(3*10**5)]
dp[0]=1
for i in B:
  dp[i]=-1
for i in range(10**5):
  if dp[i]==1:
    for a in A:
      dp[i+a]|=dp[i]
if dp[X]==1:
  print("Yes")
else:
  print("No")
  