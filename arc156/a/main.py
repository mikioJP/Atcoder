from collections import defaultdict

T = int(input())

for _ in range(T):
    N = int(input())
    S = [int(char) for char in list(str(input()))]
    
    # 和は偶数
    # N==3　のケースは注意必要(中央が1の時は不可)
    # N>= 4で隣との交換が二手または3手でできる
    # 二つしかない時に隣り合っていると手数が増える（N＝4だと2or3, N=5以上だと2）
    cnt=sum(S)
    # print(sum(S))
    if cnt%2 == 0:
        if cnt!=2:
            if (N!=3):
                print(int(cnt/2))
                continue
            else:
                if S[1]==1:
                    print(-1)
                    continue
                else:
                    print(int(cnt/2))
                    continue
        else:
            fisrt_idx=S.index(1)
            if S[fisrt_idx + 1]==1:
                if (N==3 and S[1]==1):
                    print(-1)
                    continue
                if (N==4 and S[1]==1 and S[2]==1):
                    print(3)
                    continue
                # 隣接している
                print(2)
                continue
            else:
                print(1)
    else:
        print(-1)
        continue