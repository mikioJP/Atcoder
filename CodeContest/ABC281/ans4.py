import sys
import io

_INPUT = """\
3 1 2
1 3 5
"""

sys.stdin = io.StringIO(_INPUT)
# ------------------------------------------------
input = sys.stdin.readline

N,K,D = map(int, input().split())
a_list= list(map(int, input().split()))

max_rest=[0]*D

for i in a_list:
    if i > max_rest[i%D]:
        max_rest[i%D]=i
# print(max_rest)


def part_sum0(a, A):
    # 初期化
    N = len(a)
    dp = [[0 for i in range(A + 1)] for j in range(N + 1)]
    dp[0][0] = 1

    # DP
    for i in range(N):
        for j in range(A + 1):
            if a[i] <= j:  # i+1番目の数字a[i]を足せるかも
                dp[i + 1][j] = dp[i][j - a[i]] or dp[i][j]
            else:  # 入る可能性はない
                dp[i + 1][j] = dp[i][j]
    return dp[N][A]

ret=part_sum0(a_list, 0)
print(ret)