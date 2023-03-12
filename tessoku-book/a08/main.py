from collections import defaultdict
import itertools

H, W = map(int, input().split())
X =[[0]*W for _ in range(H)]

for i in range(H):
    X[i] = list(itertools.accumulate(list(map(int, input().split()))))

Z = [[ 0 ]*(W+1) for _ in range(H+1)]

for i in range(1,W+1):
    for j in range(1,H+1):
        Z[j][i] = Z[j-1][i] + X[j-1][i-1]
    
# for i in Z:
#     print(i)
Q = int(input())

for _ in range(Q):
    A, B, C, D = map(int, input().split())
    print(Z[C][D]+Z[A-1][B-1]-Z[A-1][D]-Z[C][B-1])
        



