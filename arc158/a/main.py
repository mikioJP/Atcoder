import sys
sys.setrecursionlimit(10**6)

T = int(input())

for _ in range(T):
    a =list(map(int,input().split()))
    
    cnt = 0
    a = sorted(a)

    if a[0]%2==0:
        if a[1]%2!=0 or a[2]%2!=0 or sum(a)%3!=0:
            print(-1)
            continue
    else:
        if a[1]%2!=1 or a[2]%2!=1 or sum(a)%3!=0:
            print(-1)
            continue

    s = sum(a)/3
    d = abs(a[0]-s) + abs(a[1]-s) + abs(a[2]-s)
    print(d//4)




        
    

