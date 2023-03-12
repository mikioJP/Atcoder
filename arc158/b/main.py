N = int(input())

X = list(map(int, input().split()))

X = sorted(X)
plus=[]
minus= []
for x in X:
    if (x < 0):
        minus.append(x)
    else:
        plus.append(x)
plus.sort()
minus.sort()


def calc(a, b, c):
    return (a+b+c)/(a*b*c)

import itertools
ans_min = 10**6
ans_max = -1*10**6
val=[]

for i in range(len(minus)):
    if i < 3 or i >= len(minus) - 3:
        val.append(minus[i])
 
for i in range(len(plus)):
    if i < 3 or i >= len(plus) - 3:
        val.append(plus[i])

# print(val)
for comb in itertools.combinations(val, 3):
    a, b, c = comb
    ret = calc(a, b, c)
    if ret < ans_min:
        ans_min = ret
    if ret > ans_max:
        ans_max = ret


print(ans_min)
print(ans_max)

