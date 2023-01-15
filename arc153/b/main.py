H ,W = map(int, input().split())
A = [input() for i in range(H)]
Q=int(input())
a=[]
b=[]
for i in range(Q):
    tmp1, tmp2 = map(int, input().split())
    a.append(tmp1-1)
    b.append(tmp2-1)

tmp=[[""] * W for i in range(H)]

for n in range(Q):
    an = a[n]
    bn= b[n]
    if n ==0:
        for i in range(H):
            for j in range(W):
                #block1
                if ((i <= an) and (j <= bn)):
                    tmp[i][j] = A[an-i][bn-j]
                #block2
                if ((i <= an) and (j > bn)):
                    tmp[i][j] = A[an-i][W+bn-j]
                #block3ß
                if ((i > an) and (j > bn)):
                    tmp[i][j] = A[H+an-i][W+bn-j]            
                #block4
                if ((i > an) and (j <= bn)):
                    tmp[i][j] = A[H+an-i][bn-j]
        result = tmp
    else:
        tmp=[[""] * W for i in range(H)]
        for i in range(H):
            for j in range(W):
                #block1
                if ((i <= an) and (j <= bn)):
                    tmp[i][j] = result[an-i][bn-j]
                #block2
                if ((i <= an) and (j > bn)):
                    tmp[i][j] = result[an-i][W+bn-j]
                #block3ß
                if ((i > an) and (j > bn)):
                    tmp[i][j] = result[H+an-i][W+bn-j]            
                #block4
                if ((i > an) and (j <= bn)):
                    tmp[i][j] = result[H+an-i][bn-j]
        result = tmp
        

for i in range(H):
    for j in range(W):
        print(result[i][j], end="")
    print()