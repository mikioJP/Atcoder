from collections import defaultdict

N, Q = map(int, input().split())

a = [0]*N

for _ in range(Q):
    query, number = map(int, input().split(" "))
    if query==1:
        a[number-1]+=1
    elif query==2:
        a[number-1]+=2
    elif query==3:
        if a[number-1] >=2:
            print("Yes")
        else:
            print("No")
