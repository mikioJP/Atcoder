S = str(input())
# print(S)

if len(S)%2==0:
    for i in range(len(S)):
        if i%2==0:
            print(S[i+1], end="")
        else:
            print(S[i-1], end="")
    print()
else:
    for i in range(len(S)-1):
        if i%2==0:
            print(S[i+1], end="")
        else:
            print(S[i-1], end="")
    print(S[-1])