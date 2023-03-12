from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)
import math

N, X = map(int, input().split())

A = list(map(int, input().split()))
L=0
R=N-1
A = sorted(A)

while(L<=R):
    ans = (R+L)//2
    if A[ans]==X:
        print(ans+1)
        exit() 
    if A[ans] < X:
        L=ans+1
    else:
        R = ans-1