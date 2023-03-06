from collections import defaultdict

D = int(input())
N = int(input())

a = [0]*D
for _ in range(N):
    L, R = map(int, input().split())
    L-=1
    R-=1
    a[L]+=1
    if R==D-1:
        continue
    a[R+1]-=1

print(a[0])
for i in range(1,len(a)):
    a[i]+=a[i-1]
    print(a[i])