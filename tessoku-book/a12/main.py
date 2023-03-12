from collections import defaultdict

N, K = map(int, input().split())

A = list(map(int, input().split()))

A = sorted(A)

ans_max = 10**9
ans_min = 1

def check(N, K, A, ans):
    cum=0
    for i in range(N):
        cum+=ans//A[i]
    return cum
        

while (ans_min < ans_max):
    ans = (ans_max+ans_min)//2
    ret = check(N, K, A, ans)

    if ret < K:
        ans_min=ans+1
    elif ret >= K:
        ans_max=ans
print(ans_min)