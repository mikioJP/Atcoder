import sys
input = sys.stdin.readline



# input
n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

a.append(l)
# length ary
dif = [a[0]]
for i in range(n):
    dif.append(a[i+1]-a[i])


def is_ok(x):
    length = 0
    cnt = 0
    for i in dif:
        length += i
        if length >= x:
            length = 0
            cnt += 1
    return cnt


def judge(ng, ok):
    while ng-ok > 1:
        mid = (ng+ok) // 2
        if is_ok(mid) >= k+1:
            ok = mid
        else:
            ng = mid
    return ok


print(judge(l+1, -1))
