from collections import defaultdict
from statistics import mean

N = int(input())
X = sorted(list(map(int, input().split())))

print(mean(X[N:-(N)]))