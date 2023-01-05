from collections import deque
import sys
import io

# N桁 Bの倍数 K
_INPUT = """\
18 5
kittyonyourlapasdw
"""

sys.stdin = io.StringIO(_INPUT)
input = sys.stdin.readline
# -------------------------------
n, k = map(int, input().split())
s = input()
q = []
word = ""
for i, j in enumerate(s):

    # 追加するものよりも、qの中身の数字の方が大きければ、qの中身を捨てる
    while q and q[-1] > j:
        q.pop()
    q.append(j)

    # ここから最後まで１文字ずつ追加していく
    if i >= n - k:
        word += q.pop(0)

print(word)
