import sys
input = sys.stdin.readline

h, w=map(int, input().split())

a = [[] for i in range(h)]
cnt=0
for i in range(h):
    a[i]=list(map(str,input().split()))
    for j in list(str(a[i])):
        if j=="#":
            cnt+=1
print(cnt)