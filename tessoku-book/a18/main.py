from collections import defaultdict

N, S = map(int, input().split())

A = list(map(int, input().split()))

seen = [False]*100001
seen[0] = True

for i in A:
    for j in range(10000+1)[::-1]:
        if seen[j]:
            seen[i+j] = True

# print(seen[:S])
if seen[S]:
    print("Yes")
else:
    print("No")