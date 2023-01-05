import sys
input = sys.stdin.readline

s=list(map(str, input().split()))
t=list(map(str, input().split()))
s=list(str(s))
t=list(str(t))

cnt=-1
for i in range(len(t)):
    if t[i]!=s[i]:
        print(cnt)
        break
    cnt+=1

    

