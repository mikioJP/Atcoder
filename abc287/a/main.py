N=int(input())
S=[ [] for i in range(N)]

for i in range(N):
    S[i]=str(input())
if N/2 < S.count("For"):
    print("Yes")
else:
    print("No")