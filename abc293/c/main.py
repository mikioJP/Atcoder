import sys
sys.setrecursionlimit(10**8)
H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
path = set()
ans = 0

def dfs(i,j):
    global ans
    if A[i][j] in path:
        return
    path.add(A[i][j])

    if i == H-1 and j == W-1:
        ans += 1
    
    if j+1 < W:
        dfs(i,j+1)
    
    if i+1 < H:
        dfs(i+1, j)
    
    path.remove(A[i][j])

dfs(0,0)
print(ans)

