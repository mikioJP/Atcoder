from collections import defaultdict

N, K = map(int, input().split())

S = list(str(input()))

cnt = 0

for i in S:
    if i =="o" and cnt < K:
        print("o", end="")
        cnt+=1
    else:
        print("x", end="")
print()
