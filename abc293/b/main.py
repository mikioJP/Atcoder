N = int(input())

A = list(map(int, input().split()))

seen = [0]*N
cnt=0

for i in range(N):
    if seen[i]:
        continue
    else:
        seen[A[i]-1]=1

print(N-sum(seen))

is_first=1
for i in range(N):
    if seen[i]==0:
        if is_first:
            print(i+1, end="")
            is_first=0
        else:
            print(" ", end="")
            print(i+1, end="")
print()