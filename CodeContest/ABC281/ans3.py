import sys
import io

_INPUT = """\
3 281
94 94 94
"""

sys.stdin = io.StringIO(_INPUT)
# ------------------------------------------------
input = sys.stdin.readline

N, T= map(int,input().split())
len_ary=list(map(int,input().split()))

accumulated_len=[]
accumulated_len.append(0)
for i in range(N):
    accumulated_len.append(accumulated_len[i]+len_ary[i])
accumulated_len = accumulated_len[1:]
# print(accumulated_len)

max_len = accumulated_len[-1]
time = T%max_len

for i in range(N):
    if(accumulated_len[i] > time):
        if(i==0):
            print(1, time)
        else:
            print(i+1, time-accumulated_len[i-1])
        exit()
