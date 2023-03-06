from collections import defaultdict
import math

N = int(input())

A = list(map(int, input().split()))
ans=0
center = len(A)/2.0

for i in range(len(A)):
    if A[i] != A[-i+1]:
        ans += center-i

 