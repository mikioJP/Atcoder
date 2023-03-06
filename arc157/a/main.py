from collections import defaultdict

N, A, B, C, D = map(int, input().split())

#A or Dから始まるとき
#AからA
#AからBorC
#AからD
if (B==0):
    if (C==0):
        if(A > 0 and D > 0):
            print("No")
            exit()
    elif(C== 1):
        print("Yes")
        exit()
    else:
        print("No")
        exit()
        
if (C==0):
    if (B==0):
        if(A > 0 and D > 0):
            print("No")
            exit()
        else:
            print("Yes")
            exit()
    elif(B == 1):
        print("Yes")
        exit()
    else:
        print("No")
        exit()

if (A > 0 and ((B == C) or ((B - C)==1))):
    print("Yes")
    exit()
#DからD
#DからBorC
#DからA
if (D > 0 and ((B == C) or ((C - B)==1))):
    print("Yes")
    exit()

# BorC から始まる時
#BからAやDを使いながらCへ
if (B != 0 and C!=0 and ((B-C) == 0 or (B-C) == 1)):
    print("Yes")
    exit()
if (B != 0 and C!=0 and ((C-B) == 0 or (C-B) == 1)):
    print("Yes")
    exit() 

#BorCからAやDへ
if (C == 0 and A==0 and B==1 and D > 0):
    print("Yes")
    exit()
if (B == 0 and D==0 and C==1 and A > 0):
    print("Yes")
    exit()

print("No")