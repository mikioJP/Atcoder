from collections import defaultdict

T = int(input())

for i in range(T):
    N, K = map(int, input().split())
    # print(N, K)
    S = str(input())
    if(len(S)==1):
        print("Yes")
        continue
    if(K%N==0):
        print("Yes")
        continue
    if(len(S)%2==1):
        for i in range(len(S)//2):
            # print(list(S[0:len(S)//2-i]))
            # print(list(S[len(S)//2+i+1:]))
            if(S[0:len(S)//2-i]==S[len(S)//2+i+1:]):
                if(K%(2*(i+1)))==0:
                    print("Yes")
                    break
            if(i==len(S)//2-1):
                print("No")
                break
    else:
        for i in range(len(S)//2+1):
            # print(list(S[0:len(S)//2-i]))
            # print(list(S[len(S)//2+i:]))
        
            if(S[0:len(S)//2-i]==S[len(S)//2+i:]):
                if(K%(2*i))==0:
                    print("Yes")
                    break
            if(i==len(S)//2):
                print("No")
    # continue
