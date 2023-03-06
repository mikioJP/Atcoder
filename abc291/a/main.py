from collections import defaultdict
S =list(str(input()))

for i in range(len(S)):
    if S[i].isupper():
        print(i+1)
        exit()