from collections import defaultdict
N, K = map(int, input().split())

A = list(map(int, input().split()))

a = sorted(set(A))

cnt=0
if a[0]!=0:
    print(0)
    exit()
length = len(a)
for i in range(N-1):
    if i + 1 >= len(a):
        print(a[i]+1)
        exit()
    #連続している
    if a[i]+1 == a[i+1]:
        cnt+=1
        if cnt == K:
            print(i+1)
            exit()
    else:
        print(i+1)
        exit()
print(K)