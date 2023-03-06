from collections import defaultdict
import math

T = int(input())

def lcm(a, b):
        return int(a * b / math.gcd(a, b))

#衝突する回数を計算する必要がある。
for _ in range(T):
    N, D, K = map(int, input().split())
    D = D % N
    min_com=int(N / math.gcd(N, D))
    print(((K-1)*D)%N+(K-1)//min_com)

        
