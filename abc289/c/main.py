from collections import defaultdict

N, M =map(int, input().split())

C=[0]*M
A=[[] for i in range(M)]
for i in range(M):
    C[i]=int(input())
    A[i]=set(list(map(int, input().split())))


from itertools import product

ans=0
for bits in product([0, 1], repeat=M):
    # print("bits: ", bits)
    a = [x for bit, x in zip(bits, A) if bit == 1]
    if not a: continue

    # print("選んだもの: ", a)
    sample=set()
    for i in a:
        sample|=i
    if sample == set(list(range(1,N+1))):
        ans+=1
print(ans)