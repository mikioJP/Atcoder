from collections import defaultdict
import itertools

N = int(input())

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

ans = 0
for i in range(1,N):
    num_AB = 1
    num_CD = 1
    AB = factorization(i)
    CD = factorization(N-i)
    
    for j in AB:
        if j[0]==1:
            continue
        num_AB*=(j[1]+1)
    for k in CD:
        if k[0]==1:
            continue
        num_CD*=(k[1]+1)

    # print(AB, num_AB)

    ans+=num_AB*num_CD

print(ans)


