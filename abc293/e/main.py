import math
A, X, M = map(int, input().split())

B = A%M
print(pow(B, X, M))

print(B*(1-pow(B, X, M))/(1-B))
