from collections import defaultdict
import sys
sys.setrecursionlimit(10**7)

N = int(input())
S = list(str(input()))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x=0
y=0
# seen=[[0]*(2*N) for i in range(2*N)]
# seen[0][0] = 1
s=set()
s.add((0, 0))

for i in S:
    if (i =="R"):
        x+=dx[0]
        y+=dy[0]
    elif(i == "L"):
        x+=dx[1]
        y+=dy[1]
    elif(i == "U"):
        x+=dx[2]
        y+=dy[2]
    else:  
        x+=dx[3]
        y+=dy[3]

    if (x, y) in s:
        print("Yes")
        exit()
    else:
        s.add((x, y))
print("No")