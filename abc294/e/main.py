import sys
sys.setrecursionlimit(10**6)

L, N1, N2 = map(int, input().split())

a = []
b=[]
cnt=0
for _ in range(N1):
    s, l = map(int, input().split())
    a.append((s, l+cnt))
    cnt+=l
# print(a)
cnt=0
for _ in range(N2):
    s, l = map(int, input().split())
    b.append((s, l+cnt))
    cnt+=l
# print(a)
cur_a = 0
cur_b = 0
aidx=0
bidx=0
ans=0
while(aidx < N1 and bidx < N2):
    na, la = a[aidx]
    nb, lb = b[bidx]

    if na==nb:
        ans+= min(la, lb)-max(cur_a, cur_b)
    # print(cur_a, la, cur_b,lb, ans)
    
    
    if la < lb:
        aidx+=1
        cur_a = la
    else:
        bidx+=1
        cur_b=lb

    
print(ans)



