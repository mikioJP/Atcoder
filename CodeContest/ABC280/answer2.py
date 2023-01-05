import sys
input = sys.stdin.readline

h=int(input())
Sn=list(map(int, input().split()))

an = []
an_sum=[]
an.append(Sn[0])
an_sum.append(Sn[0])


for i in range(len(Sn)-1):
    an.append(Sn[i+1]-an_sum[i])
    an_sum.append(an_sum[i]+an[i+1])

for s in an:
    print(s, end=" ")


    

