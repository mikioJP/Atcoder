import sys
import io

# N桁 Bの倍数 K
_INPUT = """\
7 3
atcoder
"""

sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline
#-------------------------------
import itertools

input = sys.stdin.readline
N,B,K=map(int,input().split())
cs = map(str, input().split())

devider = 10**9+7
ans=0

combi=itertools.product(cs, repeat=N)
# print(list(combi))


num_combi=[]
for n in list(combi):
    str_num =""
    for i in range(K):
        str_num+=n[i]
    num_combi.append(int(str_num))

print(num_combi)

for i in num_combi:
    if i%B==0:
        ans+=1 

print(ans % devider)
