S = input()
T = input()

mae = [False]*(len(T)+1)
ushiro = [False]*(len(T)+1)
mae[0] = True
ushiro[0] = True
for i in range(len(T)):
    x = S[i]
    y = T[i]
    if   x == "?" or y == "?" or x == y :
        mae[i+1]=True
    else:
        break

S= list(reversed(S))
T = list(reversed(T))

for i in range(len(T)):
    x = S[i]
    y = T[i]
    if x == "?" or y == "?" or x == y :
        ushiro[i+1]=True
    else:
        break
#累積をとる。
from itertools import accumulate

mae=list(accumulate(mae))
ushiro=list(accumulate(ushiro))

for i in range(len(T)+1):
    if mae[i]!=i+1:
        mae[i]=False
    else:
        mae[i]=True
    if ushiro[i]!=i+1:
        ushiro[i]=False
    else:
        ushiro[i]=True

for i in range(len(T)+1):
    if mae[i] and ushiro[len(T)- i]:
        print("Yes")
    else:
        print("No")

