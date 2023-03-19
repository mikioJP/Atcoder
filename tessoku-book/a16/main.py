from collections import defaultdict

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dist = [-1]*N
dist[0]=0
dist[1]=A[0]

for i in range(2,N):
    dist[i] = min(dist[i-1]+A[i-1], dist[i-2]+B[i-2])
    
print(dist[-1])