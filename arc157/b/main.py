from collections import defaultdict, Counter
from itertools import groupby

N , K = map(int, input().split())
S = str(input())

X_cnt = S.count("X")
if K > X_cnt:
    target = "Y"
    target2 = "X"
    K = N - K
else:
    target = "X"
    target2= "Y"

#はしを切り落とす
first_t_idx=list(S).index(target2)
last_t_idx=abs( N -1 - list(reversed(S)).index(target2))
# print(first_t_idx, last_t_idx)
S=S[first_t_idx:last_t_idx+1]

droped=first_t_idx+1+(N-1-last_t_idx)

grouped = groupby(S)

res = []
for k, v in grouped:
    if (k ==target):
        res.append(int(len(list(v))))

res=sorted(res)
# print(res)

ans=0
while(K>0):
    if (K >= res[0]):
        cnt = res.pop(0)
        K-=cnt
        ans = ans + cnt + 1
    else:
        ans += K
        K=0
print(ans)