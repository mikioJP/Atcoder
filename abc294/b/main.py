H, W = map(int, input().split())

A =[list(map(int, input().split())) for _ in range(H)]

# for i in range(H):
#     A[i] = list(map(int, input().split()))
# print(A)
for h in range(H):
    for w in range(W):
        if A[h][w] == 0:
            A[h][w]='.'
        else:
            A[h][w]=chr(A[h][w]+64)
    print("".join(A[h]))