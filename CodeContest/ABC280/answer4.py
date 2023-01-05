import sys
import io

_INPUT ="""\
    121
"""

sys.stdin=io.StringIO(_INPUT)
input = sys.stdin.readline
#------------------------------------------------
import math

input = sys.stdin.readline
k = int(input())

def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


a = prime_factorize(k)
ans=0
n=0
for i in list(set(a)):
    cnt=a.count(i)
    while(cnt>0):
        n+=i
        x=n
        while(x%i==0):
            x/=i
            cnt-=1
    ans = max(ans, n)

print(int(ans))


